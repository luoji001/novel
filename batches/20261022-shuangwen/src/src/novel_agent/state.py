"""State schema 与 reducer。

两条贯穿全文件的设计约束：

**① 已定稿的正文不进 state，只留索引 + 磁盘路径。**
24000 token 装不下 3 万字。如果正文在 state 里，迟早有某个节点把它拼进 prompt，
而且不会报错 —— 只会静默退化。正文不在 state 里，这个错误在物理上不可能发生；
能看全文的只有纯 python 闸门（从磁盘读）。附带好处是 checkpoint 不会膨胀：
`durability="sync"` 下每个 super-step 都要写一份快照。
代价：回退重写某章时，磁盘文件必须跟着回退（见 store.ChapterStore.rewind）。
**正在写的那一章**例外 —— 它只有 ~2500 字，放在 `scenes_draft` 里，推进时清空。

**② 自环节点只写 LastValue 通道，不写 `operator.add` 通道。**
`write_scene → pick_best_scene → write_scene` 是自环。如果自环路径上的节点往
add 通道写，重采的那一场会被追加两次 —— 不报错，只是正文里多一段。所以
`scenes_draft` 是 LastValue（整表覆盖），`candidates` 虽然是 add 通道但由
`pick_best_scene` 在读完的同一步用 `Overwrite([])` 清空。
"""

from __future__ import annotations

import operator
from typing import Annotated, Any, Literal, TypedDict

from pydantic import BaseModel, Field

Scale = Literal["short", "normal", "long"]

# ---------- 人工卡点的决策对象 ----------
# 用 interrupt(value, response_schema=...) 直接拿回已校验的对象，
# 省掉在节点里手写一遍解析和校验。


class Approval(BaseModel):
    """大纲 / 细纲 / 终稿卡点的统一决策对象。"""
    action: Literal["accept", "revise", "edit"] = Field(
        description="accept=照此继续；revise=带意见打回重做；edit=我直接给了改好的内容")
    notes: str = Field(default="", description="revise 时写给模型的具体意见")
    patch: dict[str, Any] | None = Field(
        default=None, description="edit 时的替换内容")


# ---------- 创作计划 ----------

class CharacterCard(BaseModel):
    key: str = Field(description="占位符键，如 A / B / ORG / LOC")
    name: str
    role: str = Field(default="", description="在本篇里承担什么")
    stance: str = Field(
        default="", description="他在核心张力里的位置。具体说法由 profile 决定："
                                "论辩=站哪一边，悬疑=知道什么/隐瞒什么")
    concrete: str = Field(default="", description="具体物：他手上有什么、管什么、藏什么")


class Premise(BaseModel):
    """立意。必须落到具体物上 —— 实测模型一放开就给「困境初现/挣扎与抉择/转折与希望」
    这种纯模板，主角叫李明。具体物是唯一的解药。"""
    logline: str = Field(description="一句话故事")
    setting: str = Field(description="时间地点与环境，要具体")
    conflict_axis: str = Field(
        description="本篇的核心张力。叫法与语义由 profile 决定："
                    "论辩=核心分歧，悬疑=核心谜题，言情=关系张力，科幻=设定的代价")
    concrete_objects: list[str] = Field(
        default_factory=list, description="贯穿全篇的具体物件（账本/单子/钥匙…）")
    ending_direction: str = Field(default="", description="结局朝哪个方向落")


class ChapterBeat(BaseModel):
    no: int
    title: str
    beat: str = Field(description="本章要推进的那一件事")
    target_chars: int
    scale: Scale = "normal"
    must_object: str = Field(
        default="", description="本章必须出现的物件。实测：被强制成字段的要求 100% 落地，"
                               "只写在散文描述里的会掉")
    speakers: list[str] = Field(
        default_factory=list,
        description="本章必须出场的人。下限由 profile 的 min_speakers 决定 —— "
                    "独白体/书信体可以设 1 或 0")


class SceneSpec(BaseModel):
    idx: int
    place: str
    present: list[str] = Field(default_factory=list)
    driver: str = Field(
        description="这一场的驱动力：它到底在推进什么。各场必须互不相同。"
                    "具体语义由 profile 的 SceneLang 决定 —— 论辩=争哪件事，"
                    "悬疑=揭示还是隐瞒哪条信息，科幻=触碰哪条规则，"
                    "言情=关系挪了哪一格，纯文学=认知变了哪一点")
    entry_state: str = Field(default="", description="入场时的既有状态")
    outcome: str = Field(description="出场时发生了什么变化 —— 下一场的入场契约")
    target_chars: int = 600


class SceneCandidate(TypedDict):
    idx: int
    text: str
    sampling: str          # 哪个采样档位产的
    score: float | None
    detail: dict


class ChapterRecord(TypedDict, total=False):
    """章节索引。正文在 `path` 指的文件里，不在 state 里。"""
    no: int
    title: str
    summary: str
    chars: int
    path: str
    scale: str
    metrics: dict
    score: float | None
    issues: list[str]      # 放行时残留的软警告 = 质量债，报告里要可见
    degraded: bool
    attempts: int


class RunConfig(TypedDict, total=False):
    slug: str
    profile: str
    title: str
    genre: str
    chapters: int
    target_total_chars: int
    scenes_per_chapter: int
    prose_model: str
    gate_mode: str         # observe / enforce
    data_root: str


# ---------- reducer ----------

def merge_by_key(old: dict | None, new: dict | None) -> dict:
    """按键合并，后写覆盖。

    用 dict 而不是 list + operator.add：重跑第 5 章必须**替换**那一条，不是追加
    第二份。add 通道会让「重写」变成「重复」。
    """
    out = dict(old or {})
    out.update(new or {})
    return out


_BAN_CAPS = {"titles": 12, "sentences": 10, "templates": 10}


def merge_bans(old: dict | None, new: dict | None) -> dict:
    """拒因回传的载体，带封顶。

    为什么必须封顶：不封顶 prompt 会被禁止清单挤爆，而 24000 的上下文一旦超了，
    服务端静默截断掉的恰恰是末尾的「写法要求」—— 于是模型又回到塌缩分布去了。
    """
    out = {k: list((old or {}).get(k, [])) for k in _BAN_CAPS}
    for k, cap in _BAN_CAPS.items():
        for x in (new or {}).get(k) or []:
            if x and x not in out[k]:
                out[k].append(x)
        out[k] = out[k][-cap:]
    return out


EMPTY_BANS: dict[str, list[str]] = {k: [] for k in _BAN_CAPS}


def take_max(a: int | None, b: int | None) -> int:
    return max(a or 0, b or 0)


class NovelState(TypedDict, total=False):
    # ── 不变量 ──────────────────────────────────────────────
    run_id: str
    config: RunConfig

    # ── 计划阶段产物（单作者，LastValue 就够）──────────────
    premise: dict | None
    characters: list[dict]
    cast: dict[str, str]                 # 占位符 → 人名，喂给黑名单回代
    outline: list[dict] | None
    scene_specs: dict[str, list[dict]]   # 章号(str) → 场景表。JSON 键只能是 str
    approvals: Annotated[dict[str, dict], merge_by_key]
    revision: Annotated[int, take_max]   # 大纲被打回次数，防无限打回

    # ── 正文推进（串行；自环路径上只有 LastValue）──────────
    cursor: int                          # 当前章号
    scene_idx: int                       # 当前场号
    attempts: int                        # 本章已重写轮数
    candidates: Annotated[list[SceneCandidate], operator.add]
    scenes_draft: list[str]              # 本章已定稿场景正文（推进时整表覆盖）
    draft_body: str                      # assemble 产物
    draft_title: str
    draft_summary: str
    verdict: dict | None

    # ── 成品索引（正文在磁盘上）────────────────────────────
    chapters: Annotated[dict[str, ChapterRecord], merge_by_key]
    summaries: Annotated[dict[str, str], merge_by_key]

    # ── 控制面与账本 ───────────────────────────────────────
    bans: Annotated[dict, merge_bans]
    telemetry: Annotated[list[dict], operator.add]
    quality_log: Annotated[list[dict], operator.add]
    calls_used: Annotated[int, operator.add]
    halted: str                          # 非空 = 熔断原因，条件边直奔收尾
    book_title: str                      # 成品书名（compile_book 定）
    report: dict
