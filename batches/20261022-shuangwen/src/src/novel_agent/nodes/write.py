"""正文生成：场景级 best-of-2 → 拼章 → 标题 → 摘要。

**并发策略**：章节串行推进，2 路并发用在「同一场景生成 2 个候选」上。

为什么不并行写章：`--max-num-seqs 2` 下吞吐本来就上不去，而短篇只有 8~12 章，
串行跑完二十来分钟。真正的瓶颈是**通过率**（book-01 实测从 69% 衰减到 6.5%），
不是吞吐。best-of-2 两个请求并发执行，墙钟约等于单发，却直接压住质量衰减。
附带好处是章节串行时每章都能拿到完整的前文摘要链 —— 短篇里衔接质量比吞吐重要。

**不要用 `add_node(defer=True)` 做场景级 fan-in**：`defer` 的语义是「推迟到 run
即将结束时执行」（graph/state.py:397），用在自环里会直接废掉循环。
2 个 Send 在同一个 super-step 跑完，下一步的汇总节点只会被调度一次 —— 标准
super-step 语义就够了。
"""

from __future__ import annotations

from langgraph.types import Overwrite, Send

from .. import config as C
from .. import llm
from ..config import Diction, load_profile
from ..context import (
    render_anchor,
    render_bans,
    render_chapter_context,
    render_scene_context,
    tail_window,
)
from ..quality.checks import score_text
from ..quality.rules import (
    normalize_prose,
    strip_echoed_blocks,
    strip_echoed_prefix,
    to_cn,
)
from ..store import RunStore

# 跨题材通用的正文要求。每一句都对着一个实测出来的失败模式：
#   「不要大段写心里怎么想」←  book-01 实测心理活动 11.5%（参照书 1.9%）
#   「用朴素的 X说」        ←  attr_adv_pct 实测 20%，硬线是 15%
#   「每隔几轮插一段动作/环境」← 首次真跑 narration_para_pct 掉到 0~7%、
#                              dialogue_run_mean 冲到 14~17（目标上限 10），
#                              模型被前两条推成了纯对话乒乓
#   「中文弯引号」          ←  模型时而输出半角 `"`，会让对话类指标全部读成 0
# 题材专属的要求走 profile 的 prose_system_extra，不要往这里加。
#
# 注意这段是**对话体小说**的基座：弯引号、对话归属、插叙打断节奏三条都预设了对白。
# 非虚构档位（aiyuce）用 `profile.prose_system` 整段替换它 —— 追加压不掉反向指令。
PROSE_SYSTEM_BASE = (
    "你是中文小说作者。只输出小说正文，不要标题、不要编号、不要解释、不要总结。"
    "不要大段写人物心里怎么想，把想法写成他做的事和说的话。"
    "对话归属用朴素的「X说」「X问」，不要堆「冷冷地说」「无奈地叹了口气」"
    "这类情绪副词。"
    "不要写成从头到尾一问一答的对白 —— 每三到五轮对话就插一段动作或环境的叙述"
    "把节奏断开。"
    "对话一律用中文弯引号“”，不要用半角引号。")


def title_system(d: Diction) -> str:
    return (f"你给{d.piece}{d.section}起标题。"
            "只输出标题本身，不超过 12 个字，不要引号、不要编号。")


def summary_system(d: Diction) -> str:
    return (f"你给{d.piece}{d.section}写摘要。"
            "只输出一句话，30-50 字，写发生了什么事，不要评论。")


def _beat(state: dict, n: int) -> dict:
    for b in state.get("outline") or []:
        if b["no"] == n:
            return b
    return {"no": n, "title": "", "beat": "", "target_chars": 2200, "scale": "normal"}


def _specs(state: dict, n: int) -> list[dict]:
    return (state.get("scene_specs") or {}).get(str(n)) or []


def fan_out_scene(state: dict) -> list[Send]:
    """为当前场景扇出 2 个候选。条件边的目标。

    两个候选的差别在采样（variant 0 稳 / variant 1 野），不在 prompt ——
    上游的教训是只改 prompt 文本等于从同一个分布里再采一次样，分布没动。
    """
    n = state["cursor"]
    idx = state.get("scene_idx", 1)
    specs = _specs(state, n)
    spec = next((s for s in specs if s["idx"] == idx), specs[-1] if specs else {})
    lanes = min(C.CONCURRENCY, 2) or 1
    return [Send("write_scene_candidate",
                 {"_variant": v, "_spec": spec, "_n": n, "_idx": idx,
                  "_total": len(specs), "_state": _slim(state)})
            for v in range(lanes)]


def _slim(state: dict) -> dict:
    """只把场景生成真正需要的东西传给 Send 任务。

    刻意不传 `chapters`（索引里有磁盘路径，正文根本不在 state 里）——
    Send 的 payload 会进 checkpoint，带上没用的东西会让快照变大。
    """
    return {
        "premise": state.get("premise"),
        "characters": state.get("characters"),
        "summaries": state.get("summaries") or {},
        "scenes_draft": state.get("scenes_draft") or [],
        "bans": state.get("bans") or {},
        "attempts": state.get("attempts", 0),
        "outline": state.get("outline") or [],
        "config": state.get("config") or {},
    }


def write_scene_candidate(payload: dict) -> dict:
    """写一个场景候选。Send 的目标节点。"""
    st = payload["_state"]
    spec, n, idx = payload["_spec"], payload["_n"], payload["_idx"]
    variant, total = payload["_variant"], payload["_total"]
    cfg = st["config"]
    prof = load_profile(cfg.get("profile", "default"))
    beat = next((b for b in st["outline"] if b["no"] == n), {})
    drafted = st["scenes_draft"]

    need = spec.get("target_chars", C.SCENE_CHARS)
    # 前馈补偿：模型产出率实测 0.82，要 600 字就得让它写 600/0.82 ≈ 732 字。
    # 不补偿会系统性偏短，而偏短直接撞章长硬下限，白烧一轮。
    ask = int(need / C.LENGTH_YIELD)

    # 衔接：上一场的末尾原文。tail_window 会剥掉章标题行 —— 不剥的话模型会照抄标题。
    #
    # **窗口必须按场长收。** 写死 400 字在 xiaoyuan 的 540 字场上几乎是整场原文，
    # 模型会直接抄下来当开头（见 rules.strip_echoed_prefix 的实测记录）。
    # 全语料按场景目标字数分桶，只有 tail/scene 比值在变：
    #   400~599 字（tail/scene≈1.00）→ 32% 的章带逐字重复，平均重复占比 5.01%
    #   600~799 字（tail/scene≈0.67）→  8% 的章，1.45%
    # 封在三分之一，既够接得上，又不足以让模型把它当成要续写的正文本体。
    prev_tail = (tail_window(drafted[-1], max(120, min(400, need // 3)))
                 if drafted else "")

    prompt = "\n\n".join(x for x in [
        render_anchor(st["premise"], st["characters"],
                      axis_name=prof.lang.axis_name),
        render_chapter_context(beat, st["summaries"], n,
                               unit=prof.diction.unit,
                               speaker_label=prof.diction.speaker_label),
        render_scene_context(spec, prev_tail, total,
                             driver_name=prof.lang.driver_name),
        render_bans(st["bans"]),
        f"写这一场，约 {ask} 字。直接写正文，不要写标题。",
    ] if x)

    # prose_system 非空 = 非虚构档位整段换掉对话体基座；否则基座 + 题材追加
    system = (prof.prose_system or PROSE_SYSTEM_BASE) + (prof.prose_system_extra or "")
    s = llm.prose_sampling(st["attempts"], need, variant=variant)
    text, tele = llm.call(prompt, s, model=cfg.get("prose_model", C.PROSE_MODEL),
                          system=system,
                          tag=f"scene:ch{n}.s{idx}.v{variant}", role="prose",
                          run=cfg["slug"])
    # 入闸之前归一化引号 —— 模型时而输出半角 `"`，而 metrics 的正则只认中文弯引号，
    # 不归一化会把一章 60% 的对话读成 0%（见 rules.normalize_prose 的实测记录）。
    text = normalize_prose(text).strip()
    # 再剥掉抄上一场的部分：先剥开头，再挖中间的 echo 段块（模型会先写一段
    # 真的新开头、再整块抄，前缀扫描按设计管不到那种）。
    # 两件事都必须在打分之前做：echo 会把 dup_sentence_ratio 推高、把章长撑满，
    # 于是一个没写出新内容的候选看起来又长又合格。
    text, echoed = strip_echoed_prefix(text, drafted)
    text, echoed_blk = strip_echoed_blocks(text, drafted)
    echoed += echoed_blk
    score, detail = score_text(text, drafted, targets=prof.targets)
    if echoed:
        detail["echoed_chars"] = echoed
        # 罚分按 echo 占**原始输出**的比例。全语料回放 8891 个场次，检出 1368 个
        # echo 场次，其中 70% 只有一路抄 —— 罚分之后 pick_best_scene 会自动选中
        # 干净的那一路，不花任何额外算力。两路都抄且剥完过短、真需要重写的只剩
        # 1.37%，那种情况由章长硬下限转去 revise_scene，走的是已有的路径。
        if score is not None:
            raw = echoed + len(text)
            score = round(score * (1.0 - echoed / raw), 1) if raw else None
    return {
        "candidates": [{"idx": idx, "text": text, "sampling": f"v{variant}",
                        "score": score, "detail": detail, "echoed": echoed}],
        "telemetry": [tele],
        "calls_used": 1,
    }


def pick_best_scene(state: dict) -> dict:
    """从候选里选优，定稿本场。

    `candidates` 是 operator.add 通道，必须用 `Overwrite([])` 清空 —— 自环下不清
    会把上一场的候选混进这一场的挑选里。
    """
    cands = state.get("candidates") or []
    if not cands:
        return {"candidates": Overwrite([])}
    # 选分最高的；分数为 None（文本太短算不出指标）的排最后
    best = max(cands, key=lambda c: (c["score"] is not None,
                                     c["score"] or 0, len(c["text"])))
    drafted = list(state.get("scenes_draft") or []) + [best["text"]]
    return {
        "scenes_draft": drafted,           # LastValue：整表覆盖，自环安全
        "candidates": Overwrite([]),
        "scene_idx": state.get("scene_idx", 1) + 1,
        "quality_log": [{"kind": "scene", "chapter": state["cursor"],
                         "scene": best["idx"], "picked": best["sampling"],
                         "score": best["score"],
                         # echoed 必须落进流水：它是判断「衔接窗口收得够不够」
                         # 的唯一依据，而这件事只有跑一批才看得出来。
                         "echoed": best.get("echoed") or 0,
                         "candidates": [{"sampling": c["sampling"],
                                         "score": c["score"],
                                         "chars": len(c["text"]),
                                         "echoed": c.get("echoed") or 0}
                                        for c in cands]}],
    }


def assemble(state: dict) -> dict:
    """拼章 + 起标题 + 写摘要。"""
    n = state["cursor"]
    beat = _beat(state, n)
    body = "\n\n".join(state.get("scenes_draft") or [])
    d = load_profile(state["config"].get("profile", "default")).diction

    banned = [b["title"] for b in state.get("outline") or []]
    banned += list((state.get("bans") or {}).get("titles") or [])
    banned += [r.get("title", "") for r in (state.get("chapters") or {}).values()]

    title_prompt = (
        f"下面是{d.piece}第{to_cn(n)}{d.unit}的正文节选：\n\n{body[:1200]}\n\n"
        f"给这一{d.unit}起一个标题。要求用本{d.unit}出现的**具体物件或具体动作**命名，"
        f"不要用「抉择」「命运」「觉醒」这类抽象词。\n"
        f"以下标题已被占用，不准用也不准只改一个字：{'、'.join(t for t in banned if t)}")
    title, t_tele = llm.call(title_prompt, llm.struct_sampling("title"),
                             system=title_system(d), tag=f"title:ch{n}",
                             role="aux", run=state["config"]["slug"])
    title = (title or beat.get("title") or "").strip().strip("《》\"'“”").split("\n")[0][:16]

    sum_prompt = (f"下面是{d.piece}第{to_cn(n)}{d.unit}的正文：\n\n{body[:3000]}\n\n"
                  f"用一句话（30-50 字）写这一{d.unit}发生了什么事。只写事，不要评论。")
    summary, s_tele = llm.call(sum_prompt, llm.struct_sampling("summary"),
                               system=summary_system(d), tag=f"summary:ch{n}",
                               role="aux", run=state["config"]["slug"])
    summary = (summary or "").strip().split("\n")[0][:80]
    if not summary:
        # 兜底：各场 outcome 串联。摘要是长期记忆的唯一载体，宁可粗糙也不能空 ——
        # 上游的诊断是「摘要没信息量就等于没有长期记忆，这是打转的结构性成因」。
        summary = "；".join(s.get("outcome", "") for s in _specs(state, n))[:80]

    full = f"### 第{to_cn(n)}章：{title}\n\n{body}"
    return {
        "draft_body": full, "draft_title": title, "draft_summary": summary,
        "telemetry": [t_tele, s_tele], "calls_used": 2,
    }


def advance_or_finish(state: dict) -> str:
    """章内场景是否写完。条件边用。"""
    n = state["cursor"]
    total = len(_specs(state, n))
    return "assemble" if state.get("scene_idx", 1) > total else "fan_out_scene"


def next_chapter(state: dict) -> dict:
    """推进到下一章。清空本章的所有暂存与 bans。"""
    return {
        "cursor": state["cursor"] + 1,
        "scene_idx": 1,
        "attempts": 0,
        "scenes_draft": [],
        "draft_body": "", "draft_title": "", "draft_summary": "",
        "verdict": None,
        "candidates": Overwrite([]),
        "bans": Overwrite({"titles": [], "sentences": [], "templates": []}),
    }


def commit_chapter(state: dict) -> dict:
    """定稿落盘。

    **落盘只在这里做**。写作与校验节点都不能有副作用 —— interrupt 恢复时节点会
    从头重跑，有副作用就会重复执行（表现为日志里多一份重复记录，很难归因）。
    """
    cfg = state["config"]
    n = state["cursor"]
    beat = _beat(state, n)
    store = RunStore(cfg["slug"])
    path = store.write_chapter(n, state["draft_body"])
    v = state.get("verdict") or {}
    prof = load_profile(cfg["profile"])

    record = {
        "no": n, "title": state.get("draft_title", ""),
        "summary": state.get("draft_summary", ""),
        "chars": len(state["draft_body"]), "path": path,
        "scale": beat.get("scale", "normal"),
        "metrics": v.get("metrics", {}), "score": v.get("score"),
        "issues": v.get("soft", []),
        "degraded": bool(v.get("degraded")),
        "attempts": state.get("attempts", 0),
    }
    store.append_jsonl("quality.jsonl", {
        "ts": __import__("time").strftime("%Y-%m-%dT%H:%M:%S"),
        "book": cfg["slug"], "chapter": n, "unit": "chapter",
        "judge": "本地规则", "profile": prof.name,
        "score": v.get("score"), "metrics": v.get("metrics", {}),
        "hard": v.get("hard", []), "soft": v.get("soft", []),
        "attempts": state.get("attempts", 0),
    })
    return {
        "chapters": {str(n): record},
        "summaries": {str(n): record["summary"]},
    }
