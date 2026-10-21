"""分级修复 —— 按问题的真实成本选修法，而不是一律重写整章。

三档，成本差一到两个数量级：

| 问题 | 修法 | 成本 |
|---|---|---|
| 标题撞车 / 缺标题 / 章号错 | `retitle` 重生成一行字 | 48 token |
| 结构塌缩 / 局部复读 | `revise_scene` 只重写最差的那一场 | 1 场 ≈ 600 字 |
| 轮数超限 | `degraded_accept` 带着质量债放行 | 0 |

book-01 的复盘是这套设计的直接依据：标题类拦截 300 次（占全部拒因 36.7%），
标注「廉价可修」，实际救回 0 章 —— 每次都整章重写。
"""

from __future__ import annotations

from .. import llm
from ..config import load_profile
from ..quality.checks import score_text
from ..quality.rules import retitle as retitle_text
from ..quality.rules import to_cn
# 复用 write 的那一份 —— 原来这里有一份逐字相同的 TITLE_SYSTEM 副本，
# 改文体口径时很容易只改一边，而两边产出的标题要进同一个撞车检查。
from .write import title_system


def retitle(state: dict) -> dict:
    """只重写标题行，正文原样保留。"""
    n = state["cursor"]
    body = state["draft_body"]
    d = load_profile(state["config"].get("profile", "default")).diction
    banned = list((state.get("bans") or {}).get("titles") or [])
    banned += [b["title"] for b in state.get("outline") or []]
    banned += [r.get("title", "") for r in (state.get("chapters") or {}).values()]
    reasons = "；".join((state.get("verdict") or {}).get("title") or [])

    prompt = (
        f"下面是{d.piece}第{to_cn(n)}{d.unit}的正文节选：\n\n{body[:1000]}\n\n"
        f"原标题有问题：{reasons}\n"
        f"重新起一个标题，用本{d.unit}出现的**具体物件或具体动作**命名。\n"
        f"以下标题已被占用，不准用、也不准只改一个字："
        f"{'、'.join(t for t in banned if t)}")
    title, tele = llm.call(prompt, llm.struct_sampling("title"),
                           system=title_system(d), tag=f"retitle:ch{n}",
                           run=state["config"]["slug"])
    title = (title or "").strip().strip("《》\"'“”").split("\n")[0][:16]
    if not title:
        return {"attempts": state.get("attempts", 0) + 1,
                "telemetry": [tele], "calls_used": 1}
    return {
        "draft_body": retitle_text(body, title, n),
        "draft_title": title,
        "attempts": state.get("attempts", 0) + 1,
        "telemetry": [tele], "calls_used": 1,
    }


def revise_scene(state: dict) -> dict:
    """定位到最差的一场，把场号退回去重写那一场。

    只写 LastValue 通道（`scene_idx` / `attempts` / `scenes_draft`）——
    自环路径上往 `operator.add` 通道写会让重采的那一场被追加两次，
    不报错，只是正文里多一段。
    """
    prof = load_profile(state["config"].get("profile", "default"))
    drafted = list(state.get("scenes_draft") or [])
    if not drafted:
        return {"attempts": state.get("attempts", 0) + 1}

    # 挑分最低的一场。prior 取它之前的场景，保持与生成时同样的比较口径。
    worst_i, worst_score = 0, None
    for i, text in enumerate(drafted):
        sc, _ = score_text(text, drafted[:i], targets=prof.targets)
        if worst_score is None or (sc is not None and sc < worst_score):
            worst_i, worst_score = i, sc

    return {
        "scenes_draft": drafted[:worst_i],   # 截断到该场之前，从这里重写
        "scene_idx": worst_i + 1,
        "attempts": state.get("attempts", 0) + 1,
        "draft_body": "", "draft_title": "", "draft_summary": "",
        "quality_log": [{"kind": "revise", "chapter": state["cursor"],
                         "scene": worst_i + 1, "score": worst_score,
                         "reasons": (state.get("verdict") or {}).get("hard", [])}],
    }


def degraded_accept(state: dict) -> dict:
    """轮数超限，带着质量债放行。

    没有这个闸，任何严格的闸门最终都会变成算力黑洞 ——
    book-01 为末段 11 章产出烧掉了 157 轮被丢弃的生成。
    质量债写进 `verdict.soft`，`commit_chapter` 会把它落到 quality.jsonl，
    报告里可见。
    """
    v = dict(state.get("verdict") or {})
    debts = [f"[degraded] {r}" for r in (v.get("hard") or []) + (v.get("title") or [])]
    v["soft"] = (v.get("soft") or []) + debts
    v["hard"], v["title"], v["degraded"] = [], [], True
    return {"verdict": v,
            "quality_log": [{"kind": "degraded", "chapter": state["cursor"],
                             "attempts": state.get("attempts", 0),
                             "debts": debts}]}
