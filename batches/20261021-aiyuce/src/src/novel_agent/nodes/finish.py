"""收尾：合稿 → 一致性检查 → 报告 → 导出。

`consistency_pass` 只看**摘要 + 人物卡**，不看全文 —— 不是偷懒，是硬约束：
24000 上下文装不下 3 万字，GPU 也满了（起不了第二实例、跑不了 embedding 做 RAG）。
而且 8B 做一致性审校本来就不太靠得住，所以它**只报不改**，判断权交给终稿卡点的人。
"""

from __future__ import annotations

import time

from .. import llm
from ..config import Diction, load_profile
from ..quality import metrics as NM
from ..quality.rules import CHAPTER_RE, chapter_title, to_cn
from ..store import RunStore


def _critic_system(d: Diction) -> str:
    return (f"你是{d.critic}。只挑出**事实层面**的前后矛盾："
            "人名/称呼不一致、时间线错乱、前面埋的物件后面没交代、"
            f"{d.cast_noun}立场无理由翻转。只列问题，不要改写，不要夸。")


def compile_book(state: dict) -> dict:
    """按章号排序合稿，并按 profile 的 `[form]` 渲染交付形态。

    内部**始终**按章走——闸门机器依赖「第N章」标题（`chapter_blocks` 靠它切块
    做跨章去重、`title_checks` 靠它查标题撞车）。形态只在这里体现，
    所以换形态不用动图拓扑、也不用动质量层。

    `single_arc`：一个经典推理短篇是一条连续弧，不该有章号。
    实测依据见 `profiles-sft/xuanyi/BASELINE.md`（福尔摩斯 58 篇，p50 13,579 字）。

    `sectioned`：文章有小标题，但没有「第N章」。整行删掉（single_arc 的做法）
    对文章丢得太多 —— 小标题是文章结构的一部分，读者靠它扫全文的论证链。
    """
    cfg = state["config"]
    store = RunStore(cfg["slug"])
    prof = load_profile(cfg.get("profile", "default"))
    bodies = store.read_chapters()
    if not bodies:
        return {"report": {"error": "没有任何已定稿章节"}}

    title, tele = _book_title(state, prof)
    if prof.form.kind == "single_arc":
        sep = f"\n\n{prof.form.section_sep}\n\n"
        segs = [_strip_chapter_heading(bodies[n]) for n in sorted(bodies)]
        text = f"# {title}\n\n" + sep.join(s for s in segs if s) + "\n"
    elif prof.form.kind == "sectioned":
        segs = [_demote_chapter_heading(bodies[n]) for n in sorted(bodies)]
        text = f"# {title}\n\n" + "\n\n".join(s for s in segs if s) + "\n"
    else:
        parts = [f"# {title}\n"] + [bodies[n].strip() for n in sorted(bodies)]
        text = "\n\n".join(parts) + "\n"
    store.write_text("book.md", text)
    out: dict = {"book_title": title}
    if tele:
        out["telemetry"] = [tele]
        out["calls_used"] = 1
    return out


def _book_title_system(d: Diction) -> str:
    return (f"你给中文{d.work}起书名。只输出书名本身，不超过 8 个字，"
            "不要引号、不要书名号、不要副标题。")


def _book_title(state: dict, prof) -> tuple[str, dict | None]:
    """定书名。

    为什么要专门生成：批量跑的时候没人给 `--title`，而原来的兜底是用 slug ——
    20 篇全叫 `xuanyi-20261019-NN`，归类就失去意义了。
    一次调用 48 token，占一部小说 67 次调用的 1.5%，换每篇一个真名字。

    兜底链：命令行给的 → 模型起的 → 第一幕的标题 → slug。
    最后两级保证这个节点在模型不可用时也不会失败。
    """
    cfg = state["config"]
    if cfg.get("title"):
        return cfg["title"], None

    beats = state.get("outline") or []
    fallback = (beats[0].get("title") if beats else "") or cfg["slug"]
    chapters = state.get("chapters") or {}
    summaries = [chapters[k].get("summary", "")
                 for k in sorted(chapters, key=lambda x: int(x))]
    if not summaries:
        return fallback, None

    p = state.get("premise") or {}
    prompt = (
        f"这是一篇{prof.name}{prof.diction.work}。\n"
        f"故事：{p.get('logline', '')}\n"
        f"{prof.lang.axis_name}：{p.get('conflict_axis', '')}\n\n"
        "逐段摘要：\n" + "\n".join(f"- {s}" for s in summaries if s) + "\n\n"
        "起一个书名。用故事里的**具体物件或具体动作**命名"
        "（像《当票》《铜铃》这样），不要用「迷雾」「真相」「谜案」"
        "这类抽象词，不要带「之谜」「事件」这类后缀。\n"
        f"以下是各段的小标题，书名不要和它们重复："
        f"{'、'.join(b.get('title', '') for b in beats)}")
    try:
        text, tele = llm.call(prompt, llm.struct_sampling("title"),
                              system=_book_title_system(prof.diction),
                              tag="book_title", run=cfg["slug"])
    except Exception:                                          # noqa: BLE001
        return fallback, None
    t = (text or "").strip().strip("《》\"'“” ").split("\n")[0][:12]
    return (t or fallback), tele


def _strip_chapter_heading(body: str) -> str:
    """去掉「### 第N章：标题」那一行，保留正文。

    单篇连续弧的交付形态里不该出现章号。章标题在内部是闸门用的脚手架，
    不是成品的一部分。
    """
    lines = (body or "").splitlines()
    out = [ln for ln in lines if not CHAPTER_RE.match(ln)]
    return "\n".join(out).strip()


def _demote_chapter_heading(body: str) -> str:
    """「### 第N章：标题」→「## 标题」。只去章号，留小标题。

    `sectioned` 形态用。空标题的那行直接丢掉（不留一个光秃秃的「##」）。
    """
    out = []
    for ln in (body or "").splitlines():
        t = chapter_title(ln)
        if t is None:                     # 不是章标题行
            out.append(ln)
            continue
        if t:
            out.append(f"## {t}")
    return "\n".join(out).strip()


def consistency_pass(state: dict) -> dict:
    """只拿摘要 + 人物卡做一致性检查。只报不改。"""
    chapters = state.get("chapters") or {}
    if not chapters:
        return {}
    d = load_profile(state["config"].get("profile", "default")).diction
    lines = []
    for k in sorted(chapters, key=lambda x: int(x)):
        r = chapters[k]
        lines.append(f"第{to_cn(r['no'])}{d.unit}《{r.get('title','')}》："
                     f"{r.get('summary','')}")
    cast_lines = [f"{c.get('name')}（{c.get('role','')}，主张：{c.get('stance','')}）"
                  for c in state.get("characters") or []]

    prompt = (f"【{d.cast_noun}】\n" + "\n".join(cast_lines) +
              f"\n\n【逐{d.unit}摘要】\n" + "\n".join(lines) +
              "\n\n找出其中的事实矛盾。没有就回复「未发现」。")
    text, tele = llm.call(prompt, llm.struct_sampling("critic"),
                          system=_critic_system(d), tag="consistency",
                          run=state["config"]["slug"])
    return {"report": {**(state.get("report") or {}),
                       "consistency": (text or "").strip()},
            "telemetry": [tele], "calls_used": 1}


def book_report(state: dict) -> dict:
    """整书报告：指标、质量债、算力账单。

    算力账单里的「墙钟 vs LLM 累计耗时」是判断 best-of-2 值不值的唯一依据 ——
    `--max-num-seqs 2` 下两路并发的真实加速可能远低于 2×（prefix-caching 命中率
    下降、显存带宽瓶颈），跑完第一部就能看出来。
    """
    cfg = state["config"]
    store = RunStore(cfg["slug"])
    prof = load_profile(cfg["profile"])
    chapters = state.get("chapters") or {}
    bodies = store.read_chapters()

    tele = state.get("telemetry") or []
    llm_sec = sum(t.get("sec", 0) for t in tele)
    debts = {k: r.get("issues") or [] for k, r in chapters.items()
             if r.get("issues")}

    # book_metrics 返回 (整书聚合, 逐章明细) 两元组，这里只要聚合那份
    book = (NM.book_metrics([bodies[n] for n in sorted(bodies)])[0]
            if bodies else {})
    report = {
        **(state.get("report") or {}),
        "slug": cfg["slug"], "profile": prof.name,
        "title": state.get("book_title") or cfg.get("title") or "",
        "gate_mode": cfg.get("gate_mode"),
        "chapters": len(bodies),
        "total_chars": sum(len(b) for b in bodies.values()),
        "book_metrics": book,
        "per_chapter": [
            {"no": chapters[k]["no"], "title": chapters[k].get("title"),
             "chars": chapters[k].get("chars"), "score": chapters[k].get("score"),
             "scale": chapters[k].get("scale"),
             "attempts": chapters[k].get("attempts"),
             "degraded": chapters[k].get("degraded"),
             "debt_count": len(chapters[k].get("issues") or [])}
            for k in sorted(chapters, key=lambda x: int(x))],
        "quality_debt": debts,
        "cost": {
            "llm_calls": len(tele),
            "calls_counted": state.get("calls_used", 0),
            "llm_seconds": round(llm_sec, 1),
            "concurrency": cfg.get("concurrency"),
        },
        "halted": state.get("halted", ""),
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    store.write_json("report.json", report)
    store.write_text("report.md", _render_report(report))
    return {"report": report}


def export(state: dict) -> dict:
    cfg = state["config"]
    store = RunStore(cfg["slug"])
    store.write_json("outline.json", state.get("outline") or [])
    store.write_json("scene_specs.json", state.get("scene_specs") or {})
    store.write_json("premise.json", {"premise": state.get("premise"),
                                      "characters": state.get("characters")})
    for rec in state.get("quality_log") or []:
        store.append_jsonl("rounds.jsonl", rec)
    return {}


def halt(state: dict) -> dict:
    """熔断出口。不让 run 以 traceback 结束 —— 已经写好的章必须留下来。"""
    reason = state.get("halted") or "大纲被打回次数超限，需要人工接手"
    return {"halted": reason}


def _render_report(r: dict) -> str:
    lines = [f"# {r.get('title') or r['slug']} 生成报告", "",
             f"slug：`{r['slug']}`",
             f"档位：{r['profile']}　闸门模式：{r['gate_mode']}",
             f"章数：{r['chapters']}　总字数：{r['total_chars']}",
             f"LLM 调用：{r['cost']['llm_calls']} 次，累计 {r['cost']['llm_seconds']} 秒",
             ""]
    if r.get("halted"):
        lines += [f"> ⚠ 熔断：{r['halted']}", ""]
    lines += ["## 逐章", "",
              "| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |",
              "|---|---|---|---|---|---|---|---|"]
    for c in r.get("per_chapter") or []:
        lines.append(
            f"| {c['no']} | {c.get('title','')} | {c.get('chars',0)} | "
            f"{c.get('scale','')} | {c.get('score')} | {c.get('attempts',0)} | "
            f"{'是' if c.get('degraded') else ''} | {c.get('debt_count',0)} |")
    if r.get("consistency"):
        lines += ["", "## 一致性检查（8B 产出，只作参考）", "", r["consistency"]]
    if r.get("quality_debt"):
        lines += ["", "## 质量债（放行但未达标的项）", ""]
        for k in sorted(r["quality_debt"], key=lambda x: int(x)):
            lines.append(f"- 第 {k} 章：")
            lines += [f"  - {x}" for x in r["quality_debt"][k]]
    if r.get("book_metrics"):
        lines += ["", "## 整书结构指标", "", "```",
                  "\n".join(f"{k}: {v}" for k, v in r["book_metrics"].items()),
                  "```"]
    return "\n".join(lines) + "\n"
