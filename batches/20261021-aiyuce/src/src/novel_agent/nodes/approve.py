"""人工卡点。

**这些节点绝对不能有副作用。** `interrupt()` 恢复时节点会从头重跑整个函数 ——
在这里写文件、追加 jsonl、或者计一次调用，每次 resume 都会重复执行一遍。
表现是「日志里多了一份重复记录」，很难归因。落盘一律放在后面独立的 persist 节点。

卡点放在大纲和细纲、而不是正文上，是由硬约束决定的：24000 上下文装不下 3 万字，
全局一致性只能在计划层保证。「写到第 6 章忘了第 2 章埋的伏笔」这类问题，
人工审核计划是唯一的真防线。
"""

from __future__ import annotations

from langgraph.types import Overwrite, interrupt

from ..config import load_profile
from ..state import Approval


def approve_outline(state: dict) -> dict:
    lint = (state.get("approvals") or {}).get("outline_lint", {}).get("issues") or []
    decision: Approval = interrupt(
        {
            "stage": "大纲确认",
            "premise": state.get("premise"),
            "characters": state.get("characters"),
            "outline": state.get("outline"),
            "lint": lint,
            "hint": "accept 照此写 / revise 带意见打回 / edit 直接给改好的 outline",
        },
        response_schema=Approval,
    )
    out: dict = {"approvals": {"outline": decision.model_dump()}}
    if decision.action == "revise":
        out["revision"] = state.get("revision", 0) + 1
    elif decision.action == "edit" and decision.patch:
        if "outline" in decision.patch:
            out["outline"] = decision.patch["outline"]
        if "premise" in decision.patch:
            out["premise"] = decision.patch["premise"]
    return out


def route_after_outline(state: dict) -> str:
    """revise 打回重做，但有上限 —— 不能无限打回。"""
    d = (state.get("approvals") or {}).get("outline") or {}
    prof = load_profile(state["config"]["profile"])
    if d.get("action") == "revise":
        if state.get("revision", 0) >= prof.budget.outline_max_revisions:
            return "halt"
        return "outline"
    return "plan_scenes"


def approve_scenes(state: dict) -> dict:
    lint = (state.get("approvals") or {}).get("plans_lint", {}).get("issues") or []
    decision: Approval = interrupt(
        {
            "stage": "分场细纲确认",
            "scene_specs": state.get("scene_specs"),
            "lint": lint,
            "hint": "accept 开始写正文 / revise 带意见重拆 / edit 直接给改好的 scene_specs",
        },
        response_schema=Approval,
    )
    out: dict = {"approvals": {"scenes": decision.model_dump()}}
    if decision.action == "edit" and decision.patch:
        if "scene_specs" in decision.patch:
            # scene_specs 是合并通道，人工删掉某一场时必须整表覆盖
            out["scene_specs"] = Overwrite(decision.patch["scene_specs"])
    return out


def route_after_scenes(state: dict) -> str:
    d = (state.get("approvals") or {}).get("scenes") or {}
    return "plan_scenes" if d.get("action") == "revise" else "write_chapter_start"


def approve_final(state: dict) -> dict:
    decision: Approval = interrupt(
        {
            "stage": "终稿确认",
            "report": state.get("report"),
            "hint": "accept 导出 / revise 说明要改哪章（之后用 novel-agent redo）",
        },
        response_schema=Approval,
    )
    return {"approvals": {"final": decision.model_dump()}}
