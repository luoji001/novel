"""章级校验与路由 —— 纯 python，不调 LLM。

闸门有两个模式（`config.gate_mode`）：

- `observe`：全部降级为软警告，只记录分布，不拦任何东西。**第一次跑必须用这个。**
- `enforce`：按 profile 的硬线拦截。

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

    observe = cfg.get("gate_mode", "observe") == "observe"
    hard, title = (([], []) if observe else (v.hard, v.title))
    soft = v.soft + ([f"[observe] {r}" for r in v.hard + v.title] if observe else [])

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
                    "observe": observe},
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
    if state.get("attempts", 0) >= prof.gates.chapter_max_attempts:
        return "degraded_accept"
    if v.get("title") and not v.get("hard"):
        return "retitle"            # 只重写一行字
    return "revise_scene"           # 只重写最差的那一场
