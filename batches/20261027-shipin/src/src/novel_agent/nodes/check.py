"""章级校验与路由 —— 纯 python，不调 LLM。

闸门有三个模式（`config.gate_mode`）：

- `observe`：全部降级为软警告，只记录分布，不拦任何东西。**第一次跑必须用这个。**
- `defect` ：只拦**缺陷类**（逐字复读 / 整章相似 / 章节过短 / 标题问题），
             密度硬线仍然只记录。标定期的推荐档。
- `enforce`：按 profile 的全部硬线拦截。

**为什么要有中间那一档**（2026-10-23 加）：`observe` 的语义是「不拦任何东西」，
而这件事在 2026-10-21 那批 271 篇上的实测后果是 —— 1626 章里 889 章（54.7%）
被 `HARD_SCORE_CAP` 压了分，其中 674 次是章内自我复读，**而 1626 章的
`attempts` 全部为 0**：修复路径一次都没进，有缺陷的正文原样落盘。
`retitle` / `revise_scene` 这两条廉价路径就白建了。

但直接切 `enforce` 是另一个错误：密度硬线全部未标定，那正是
`metrics.py:68-78` 警告的「拿一个分布当所有分布的闸门」。所以把两类分开 ——
分界线是**判定依赖什么**，不是严重程度，见 `quality.checks.split_hard`。

⚠ 一个已知的局限：`defect` 档拦住之后走的是重采，而重采对**prompt 造成的**
缺陷无效。aiyuce 那 674 次复读抄的是 `driver_rule` 里要求的那句
「这条推论会被什么推翻」—— 同一个 prompt 重采三次还是同一句，最后 `degraded_accept`
放行，只多烧了算力。那一类得改 prompt（把固定句改成结构字段），不是靠闸门。
标题撞车相反：`retitle` 48 token、禁用清单是个小闭集，是 `defect` 档真正能救的。

为什么第一次必须 observe：现有阈值全部标定在**长篇**分布上（51 / 210 / 369 章），
而本项目要用到**短篇**（8~12 章、围着一个分歧轴）。至少三条明确会错：

- `plot_sim_max=0.55`（摘要相似度）：短篇所有章都在争同一件事，摘要天然相似
- `theme_max=0.58`（与最近 3 章的 bigram 余弦）：短篇「最近 3 章」就是全篇的 1/3
- `TARGETS` 来自论辩体；题材一换，对话占比 38~58% 的目标就没有依据

这正是 metrics.py:68-78 记录过的那个错误的翻版 —— 拿一个分布当所有分布的闸门。
正确做法是先用 observe 跑 2~3 部，收集**单章分布的 p3**，再据此定硬线。
实测已经证明这套流程有效：本项目的 `tests/test_quality.py` 就是这么锁定的。
"""

from __future__ import annotations

from ..config import load_profile
from ..quality.checks import split_hard
from ..quality.checks import validate as run_validate
from ..quality.rules import extract_title
from ..store import RunStore


def validate(state: dict) -> dict:
    cfg = state["config"]
    prof = load_profile(cfg["profile"])
    n = state["cursor"]
    beat = next((b for b in state.get("outline") or [] if b["no"] == n), {})

    # 正文从磁盘读 —— 这是全文唯一被完整读取的地方，而且只在纯 python 里用。
    prior = RunStore(cfg["slug"]).read_chapters(upto=n - 1)

    v = run_validate(
        state["draft_body"], n, prior, prof.gates,
        target_chars=beat.get("target_chars"),
        scale=beat.get("scale", "normal"),
        targets=prof.targets,
        cast=state.get("cast") or {},
        summary=state.get("draft_summary", ""),
        prior_summaries=[s for k, s in (state.get("summaries") or {}).items()
                         if k != str(n)],
        attempts=state.get("attempts", 0),
    )

    # 三档闸门。`defect` 是 2026-10-23 加的中间档，理由见模块注释。
    mode = cfg.get("gate_mode", "observe")
    defect, dist = split_hard(v.hard, prof.targets)
    if mode == "enforce":
        hard, title, recorded = v.hard, v.title, []
    elif mode == "defect":
        hard, title, recorded = defect, v.title, dist
    else:                                    # observe
        hard, title, recorded = [], [], v.hard + v.title
    # `[observe]` 是「只记录、没拦」的标记，不是模式名 —— 三档共用同一个前缀，
    # 这样既有的日志查询（以及 quality.jsonl 里已经积累的 1626 条）口径不变。
    soft = v.soft + [f"[observe] {r}" for r in recorded]

    # 拒因回传：把具体的拦截项变成下一轮 prompt 里的禁止清单。
    # 上游自述这是 v1 的「最大设计缺陷」—— 算出了拦截原因却只 print 到日志，
    # 于是每次重试都是从同一个已塌缩的分布里再独立采一次样。
    bans: dict[str, list[str]] = {"titles": [], "sentences": [], "templates": []}
    if v.title:
        t = extract_title(state["draft_body"])
        if t:
            bans["titles"].append(t)
    for r in v.hard + v.soft:
        if "套路句式" in r:
            bans["templates"].extend(_quoted(r))
        elif "重复" in r or "复读" in r:
            bans["sentences"].extend(_quoted(r))

    return {
        "verdict": {"hard": hard, "title": title, "soft": soft,
                    "metrics": v.metrics, "score": v.score,
                    "degraded": state.get("attempts", 0) >= prof.gates.degrade_after,
                    # 保留 `observe` 这个布尔是为了向后兼容（旧 thread 的
                    # checkpoint 里有它）；`gate_mode` 才是三档的真相源。
                    "observe": mode == "observe", "gate_mode": mode},
        "bans": bans,
    }


def _quoted(reason: str) -> list[str]:
    """从中文拦截原因里抠出「」括起来的具体片段，用于禁止清单。"""
    out, buf, inside = [], [], False
    for ch in reason:
        if ch == "「":
            inside, buf = True, []
        elif ch == "」":
            if inside and buf:
                s = "".join(buf).rstrip("…").split("×")[0].strip()
                if len(s) >= 3:
                    out.append(s)
            inside = False
        elif inside:
            buf.append(ch)
    return out[:4]


def route_after_validate(state: dict) -> str:
    """校验后的分级修复路由。

    分级的全部意义是**别作废整章**：book-01 的 300 次标题重复拦截占全部拒因的
    36.7%，被标注为「廉价可修」，但实际救回 0 章 —— 每一次都是整章重写。
    """
    v = state.get("verdict") or {}
    prof = load_profile(state["config"]["profile"])

    if not v.get("hard") and not v.get("title"):
        return "commit_chapter"
    # `budget.chapter_max_attempts`，**不是** `gates.chapter_max_attempts` ——
    # 后者不存在（轮数上限在 Budget 上，Gates 只有 degrade_after）。
    # 这一行原来写错了，而且是 2026-10-23 加 `defect` 档时才被测出来：
    # observe 模式下 hard/title 永远为空、上面那个 return 提前退出，
    # 于是这整条分级修复路由从来没有被执行过（三批真跑 1626 章 + 2701 章，
    # attempts 全为 0）。一旦开 defect 或 enforce，第一次标题撞车就 AttributeError。
    if state.get("attempts", 0) >= prof.budget.chapter_max_attempts:
        return "degraded_accept"
    if v.get("title") and not v.get("hard"):
        return "retitle"            # 只重写一行字
    return "revise_scene"           # 只重写最差的那一场
