"""图装配。

两个导出：
  `graph`       —— 不带 checkpointer，给 `langgraph dev` 用（dev server 自己注入持久化）
  `build_app()` —— 带 SqliteSaver，给 CLI 用

**这两套持久化不是同一个**：在 Studio 里审核通过的 thread，CLI 看不到，反之亦然。
这是刻意接受的（dev 只用来看拓扑和调单章），但必须知道，否则会以为 thread 丢了。
"""

from __future__ import annotations

import sqlite3

from langgraph.graph import END, START, StateGraph
from langgraph.types import RetryPolicy

from . import config as C
from .config import load_profile
from .nodes import approve, check, finish, plan, repair, write
from .state import NovelState
from .store import RunStore

# 只管传输故障。质量重试一律走显式条件边自环 —— retry_policy 用同样的输入重跑，
# 看不见质量，也无法改采样参数或回传拒因，而这两件事才是重试的全部意义。
TRANSPORT_RETRY = RetryPolicy(max_attempts=3, initial_interval=1.0,
                              backoff_factor=2.0, max_interval=20.0)


def init(state: NovelState) -> dict:
    cfg = dict(state["config"])
    prof = load_profile(cfg.get("profile", "default"))
    cfg.setdefault("chapters", prof.chapters)
    cfg.setdefault("target_total_chars", prof.target_total_chars)
    cfg.setdefault("scenes_per_chapter", prof.scenes_per_chapter)
    cfg.setdefault("prose_model", C.PROSE_MODEL)
    cfg.setdefault("gate_mode", "observe")
    cfg["concurrency"] = C.CONCURRENCY
    RunStore(cfg["slug"]).ensure()
    return {"config": cfg, "cursor": 1, "scene_idx": 1, "attempts": 0,
            "scenes_draft": [], "revision": 0,
            "bans": {"titles": [], "sentences": [], "templates": []}}


def write_chapter_start(state: NovelState) -> dict:
    """开始写当前章。只重置本章的暂存，不碰已定稿的东西。"""
    return {"scene_idx": 1, "attempts": 0, "scenes_draft": [],
            "draft_body": "", "draft_title": "", "draft_summary": "",
            "verdict": None}


def scene_router(state: NovelState):
    """场景循环的唯一路由：要么扇出下一场的候选，要么收工拼章。

    返回 `list[Send]` 或节点名。被三处共用：章节开始、选优之后、重写某场之后。
    """
    n = state["cursor"]
    total = len((state.get("scene_specs") or {}).get(str(n)) or [])
    if total and state.get("scene_idx", 1) > total:
        return "assemble"
    return write.fan_out_scene(state)


def chapter_router(state: NovelState) -> str:
    """推进到下一章，或收工。

    顺带做全局熔断：顶的是**调用数**而不是失败数 —— 失败数衡量不了「反复成功但
    每章都要 4 轮」这种慢性失控，而 book-01 的末段正是「每 3 轮成功一次、总共烧
    157 轮」。撞到顶就带着已写好的章去收尾，不要让 run 以 traceback 结束。
    """
    prof = load_profile(state["config"]["profile"])
    if state.get("calls_used", 0) >= prof.budget.run_max_calls:
        return "halt"
    total = state["config"]["chapters"]
    return "next_chapter" if state["cursor"] < total else "compile_book"


def build_graph() -> StateGraph:
    g = StateGraph(NovelState)

    # ── 计划阶段 ────────────────────────────────────────────
    g.add_node("init", init)
    g.add_node("premise", plan.premise, retry_policy=TRANSPORT_RETRY)
    g.add_node("cast", plan.cast, retry_policy=TRANSPORT_RETRY)
    g.add_node("outline", plan.outline, retry_policy=TRANSPORT_RETRY)
    g.add_node("outline_lint", plan.outline_lint)
    g.add_node("approve_outline", approve.approve_outline)
    g.add_node("plan_scenes", plan.plan_scenes, retry_policy=TRANSPORT_RETRY)
    g.add_node("plans_lint", plan.plans_lint)
    g.add_node("approve_scenes", approve.approve_scenes)

    # ── 正文阶段 ────────────────────────────────────────────
    g.add_node("write_chapter_start", write_chapter_start)
    # 不设 add_node(timeout=)：LangGraph 只对 **async** 节点支持节点级超时
    # （sync 的 Python 执行没法在进程内安全取消，compile 时会直接报错）。
    # 单次请求的上限由 llm.py 里 ChatOpenAI 的 timeout=600 兜住。
    g.add_node("write_scene_candidate", write.write_scene_candidate,
               retry_policy=TRANSPORT_RETRY)
    g.add_node("pick_best_scene", write.pick_best_scene)
    g.add_node("assemble", write.assemble, retry_policy=TRANSPORT_RETRY)
    g.add_node("validate", check.validate)
    g.add_node("retitle", repair.retitle, retry_policy=TRANSPORT_RETRY)
    g.add_node("revise_scene", repair.revise_scene)
    g.add_node("degraded_accept", repair.degraded_accept)
    g.add_node("commit_chapter", write.commit_chapter)
    g.add_node("next_chapter", write.next_chapter)

    # ── 收尾 ────────────────────────────────────────────────
    g.add_node("compile_book", finish.compile_book)
    g.add_node("consistency_pass", finish.consistency_pass,
               retry_policy=TRANSPORT_RETRY)
    g.add_node("book_report", finish.book_report)
    g.add_node("approve_final", approve.approve_final)
    g.add_node("export", finish.export)
    g.add_node("halt", finish.halt)

    # ── 边 ──────────────────────────────────────────────────
    g.add_edge(START, "init")
    g.add_edge("init", "premise")
    g.add_edge("premise", "cast")
    g.add_edge("cast", "outline")
    g.add_edge("outline", "outline_lint")
    g.add_edge("outline_lint", "approve_outline")
    g.add_conditional_edges("approve_outline", approve.route_after_outline,
                            {"outline": "outline", "plan_scenes": "plan_scenes",
                             "halt": "halt"})
    g.add_edge("plan_scenes", "plans_lint")
    g.add_edge("plans_lint", "approve_scenes")
    g.add_conditional_edges("approve_scenes", approve.route_after_scenes,
                            {"plan_scenes": "plan_scenes",
                             "write_chapter_start": "write_chapter_start"})

    # 场景循环。三个入口共用 scene_router。
    for src in ("write_chapter_start", "pick_best_scene", "revise_scene",
                "next_chapter"):
        g.add_conditional_edges(src, scene_router,
                                ["write_scene_candidate", "assemble"])
    g.add_edge("write_scene_candidate", "pick_best_scene")

    g.add_edge("assemble", "validate")
    g.add_conditional_edges("validate", check.route_after_validate,
                            {"commit_chapter": "commit_chapter",
                             "retitle": "retitle",
                             "revise_scene": "revise_scene",
                             "degraded_accept": "degraded_accept"})
    g.add_edge("retitle", "validate")
    g.add_edge("degraded_accept", "commit_chapter")
    g.add_conditional_edges("commit_chapter", chapter_router,
                            {"next_chapter": "next_chapter",
                             "compile_book": "compile_book",
                             "halt": "halt"})

    g.add_edge("compile_book", "consistency_pass")
    g.add_edge("consistency_pass", "book_report")
    g.add_edge("book_report", "approve_final")
    g.add_edge("approve_final", "export")
    g.add_edge("export", END)
    g.add_edge("halt", "book_report")
    return g


# 给 langgraph dev：不带 checkpointer
graph = build_graph().compile()


def build_app(db_path: str | None = None):
    """给 CLI：带 SqliteSaver 的持久化版本。

    不用 `SqliteSaver.from_conn_string` —— 它是 contextmanager，CLI 要长期持有连接。
    `check_same_thread=False` 是必须的：Send 扇出的候选任务跑在不同线程上。
    """
    from langgraph.checkpoint.sqlite import SqliteSaver

    path = db_path or str(C.DATA_ROOT / "state" / "checkpoints.sqlite")
    (C.DATA_ROOT / "state").mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path, check_same_thread=False)
    saver = SqliteSaver(conn)
    saver.setup()
    return build_graph().compile(checkpointer=saver)
