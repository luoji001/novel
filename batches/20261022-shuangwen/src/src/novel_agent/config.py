"""全部可调参数集中在这里，不散落在各模块的 os.environ.get 里。

常量里凡是带数字的，都标了它的校准依据。没有依据的数字不该出现在这种文件里 ——
上游 `MIN_CHAPTER_LEN=200` 的教训就是：下限设得比实际产出还低，等于没有下限。
"""

from __future__ import annotations

import os
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

from .quality.rules import Gates

PKG_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = PKG_ROOT.parents[1]
PROFILES_DIR = PROJECT_ROOT / "profiles"


def _env(key: str, default: str) -> str:
    return os.environ.get(key, default)


# ---------- 服务接入 ----------
# 默认全指本地 vLLM。三类调用可以**分别**指向不同端点（见下面的 Endpoint）：
#   struct 计划层（立意/人物/大纲/分场）—— 约 14k 入 token/部，换第三方换质量最划算
#   aux    标题/摘要/书名/审校          —— 约 39k 入 token/部，不配就继承 struct
#   prose  正文（场景生成）             —— 占 85% 算力，留本地用 novel-sft3 LoRA
BASE_URL = _env("VLLM_BASE_URL", "http://127.0.0.1:8000/v1")
API_KEY = _env("VLLM_API_KEY", "sk-local")
STRUCT_MODEL = _env("NOVEL_STRUCT_MODEL", "qwen3-8b")      # AWQ 基座
PROSE_MODEL = _env("NOVEL_PROSE_MODEL", "novel-sft3")      # 中文小说 LoRA

PROMPT_BUDGET_TOKENS = 9000

# 并发上限。本地必须 <= vLLM 的 --max-num-seqs（当前 2）。
# 设 2 = best-of-2 吃满两路，用户的对话通道会被挤；白天建议 1。
CONCURRENCY = int(_env("NOVEL_CONCURRENCY", "2"))


@dataclass(frozen=True)
class Dialect:
    """供应商方言 —— 同一个 OpenAI 兼容接口，能接受的参数差别很大。

    `sampling` 三档，这是接第三方时最容易静默踩的地方：

      "full"      vLLM：标准参数 + extra_body 里的 top_k / repetition_penalty
      "standard"  DeepSeek / OpenAI 兼容网关：只有标准参数。
                  **top_k 和 repetition_penalty 会被拒收或静默忽略** ——
                  而 repetition_penalty=1.1 是本项目对抗复读塌缩的主力之一，
                  静默忽略比报错更糟（产出悄悄退化，指标上看不出来）。
      "none"      Claude 当代模型（Opus 5 / Sonnet 5 / Opus 4.7·4.8 / Fable 5）：
                  temperature / top_p / top_k **一律 400 拒收**，
                  改用 output_config.effort 控制深度。
                  （Opus 4.6 / Sonnet 4.6 / Haiku 4.5 仍接受采样参数。）

    后果：本项目「每个节点独立设温度」的核心设计在 Claude 当代模型上不成立。
    正文的温度阶梯（0.85→1.25）和 best-of-2 的 variant 扰动更是完全没有对应物。
    所以 Claude 只适合接**结构化调用**——那些本来就是低温确定性的。
    """
    kind: str                 # "openai" | "anthropic"（决定用哪个 client 类）
    sampling: str             # "full" | "standard" | "none"
    context: int              # 上下文窗口
    note: str = ""

    # 非空则每次调用下发 `reasoning_effort`。给**推理模型**用 ——
    # 实测（2026-10-22，opencode-go 上的 deepseek-v4.1-flash，max_tokens=900）：
    #   不送        → 400 "Thinking mode does not support this tool_choice"
    #   none        → 推理 0 tok，tool_call 稳定
    #   low         → **不稳**：premise 只花 8 tok，cast 花 758 tok 然后撞满 1200
    #                 空产出。「low」不是思考预算的硬上限，只是倾向。
    #   medium/high → 推理吃掉 896 / 900，撞满预算，空产出
    # 本项目全部结构化调用都是「温度 + 强制 tool_choice」，而 max_tokens 是按
    # 不带思考的产出标定的 —— 所以只能取 none：让预算全部留给 JSON 本身。
    reasoning_effort: str = ""
    # max_tokens 的倍率。`struct_sampling` 的预算（premise 900 / cast 1200 /
    # outline 2600）是按**本地 8B 的产出长度**标定的，换一个更啰嗦的模型就会在
    # JSON 中途截断 —— 而截断表现为「解析失败」，极难归因到预算上
    #（上游的头号规划失败源：第四章 30 轮里 24 次是它）。
    # 实测同一组 prompt 在 deepseek-v4.1-flash 上的占用：
    #   premise 900/900（撞顶）｜ cast 1154/1200｜ plan:ch2 1286/1340｜ outline 1201/2600
    # 放大 max_tokens 不花钱（出 token 按实际生成计费），截断才花钱。
    max_tokens_scale: float = 1.0
    # 非空 = 每个请求必须带这个会话头，值用 run 的 slug（一部书 = 一次会话，
    # 既满足网关的路由要求，也让同一本书的固定前缀命中它那边的 prompt 缓存）。
    session_header: str = ""
    # 网关要求客户端用自己的 UA 标识，而不是 SDK / HTTP 库的默认值。
    user_agent: str = ""


# 加一家供应商 = 加一条配置，不改代码。
DIALECTS: dict[str, Dialect] = {
    "vllm": Dialect("openai", "full", 24000,
                    "本地 vLLM，--max-model-len 24000"),
    "deepseek": Dialect("openai", "standard", 128000,
                        "不支持 top_k / repetition_penalty"),
    "anthropic": Dialect("anthropic", "none", 200000,
                         "当代模型拒收采样参数，用 effort 代替"),
    # OpenCode Zen（按量）/ OpenCode Go（订阅）。同一套 OpenAI 兼容面 + Bearer，
    # 两者只差 base_url 与可用模型，所以共用这一条方言。
    #
    # 为什么是 standard 而不是 full：它是**代理到上游**的网关（OpenAI / Anthropic /
    # Google / DeepSeek / Kimi / GLM …），top_k 与 repetition_penalty 是 vLLM 扩展，
    # 在那些上游要么不存在要么被网关吃掉 —— 而静默忽略比报错更糟（见 Dialect 的注释）。
    # 真确认了你的 base_url 会透传，再改成 "openai-compatible"。
    #
    # ⚠ base_url 必须从你自己的 console 抄，不要照搬文档截图：Zen 与 Go 的路径不同，
    # 第三方资料里至少流传着三种写法。绑完先 `novel-agent endpoints --probe`。
    "opencode": Dialect("openai", "standard", 128000,
                        "OpenCode Zen/Go 网关；base_url 从 console 抄，窗口按模型变",
                        reasoning_effort="none",
                        session_header="x-opencode-session",
                        user_agent="novel-agent/0.1",
                        max_tokens_scale=2.0),
    # 兜底：自建网关 / OpenRouter / 硅基流动之类，通常会透传 extra_body
    "openai-compatible": Dialect("openai", "full", 128000,
                                 "假定透传 extra_body；不透传就改成 standard"),
}


@dataclass(frozen=True)
class Endpoint:
    """一类调用的落点。"""
    role: str                 # "struct" | "prose"
    base_url: str
    api_key: str
    model: str
    provider: str
    # 仅 anthropic 用：user 级 key（sk-ant-usr-…）没绑 workspace，
    # 不带 `anthropic-workspace-id` 头会 400。workspace 级 key 不用填。
    workspace: str = ""

    @property
    def dialect(self) -> Dialect:
        d = DIALECTS.get(self.provider)
        if d is None:
            raise ValueError(
                f"不认识的 provider {self.provider!r}。"
                f"可用：{', '.join(sorted(DIALECTS))}（或在 DIALECTS 里加一条）")
        return d


def _endpoint(role: str, default_model: str) -> Endpoint:
    """按角色读环境变量，缺的回落到全局（也就是本地 vLLM）。"""
    up = role.upper()
    return Endpoint(
        role=role,
        base_url=_env(f"NOVEL_{up}_BASE_URL", "") or BASE_URL,
        api_key=_env(f"NOVEL_{up}_API_KEY", "") or API_KEY,
        model=_env(f"NOVEL_{up}_MODEL", default_model),
        provider=_env(f"NOVEL_{up}_PROVIDER", "vllm"),
        workspace=_env(f"NOVEL_{up}_WORKSPACE_ID", ""),
    )


AUX_KEYS = ("PROVIDER", "BASE_URL", "API_KEY", "MODEL")


def struct_endpoint() -> Endpoint:
    return _endpoint("struct", STRUCT_MODEL)


def prose_endpoint() -> Endpoint:
    return _endpoint("prose", PROSE_MODEL)


def aux_endpoint() -> Endpoint:
    """标题 / 摘要 / 书名 / 一致性审校的落点。

    为什么要把它从 struct 里拆出来：按 tag 聚合本机 703 部 run 的 calls.jsonl
    （抽样 40 部）得到的实测分布是 ——

      summary 23,820 + title 14,246 + book_title 944 ≈ 39k 入 token/部
      premise + cast + outline + plan                 ≈ 13.9k 入 token/部

    也就是说**标题与摘要占结构化侧 token 的 73%**，而它俩的 prompt 之所以大是因为
    带正文节选（`body[:3000]` / `body[:1200]`），计划层的 prompt 全被 context.py
    的分层预算封在 1200 字锚点以内。所以「把计划层交给第三方」和「把标题摘要也交
    出去」是两件成本差四倍的事 —— 在订阅额度制（OpenCode Go 那种每 5h / 每周
    限流）下更是差在硬墙上，不是差在钱上。

    **不配任何 `NOVEL_AUX_*` 就继承结构化端点**，默认行为与拆分之前逐字一致。
    """
    if not any(os.environ.get(f"NOVEL_AUX_{k}") for k in AUX_KEYS):
        return struct_endpoint()
    return _endpoint("aux", STRUCT_MODEL)


# 上下文硬顶。取三个端点里**最小的那个** —— context.py 的分层预算是全局的，
# 按大的算会在小的那一端静默超限（而超限时服务端截断掉的恰恰是末尾的写法要求）。
def model_context() -> int:
    return min(struct_endpoint().dialect.context,
               prose_endpoint().dialect.context,
               aux_endpoint().dialect.context)


# 向后兼容：仍有代码直接读 C.MODEL_CONTEXT
MODEL_CONTEXT = model_context()

DATA_ROOT = Path(_env("NOVEL_DATA_ROOT", str(Path.home() / "novel-agent")))

# 是否把每次 LLM 调用的完整现场（prompt / completion / 采样参数）落到
# runs/<slug>/logs/calls.jsonl。默认开 —— 它填的是「看不到是哪个 prompt 产出了
# 那段烂正文」这个缺口，一部小说约 1~2 MB，代价可以忽略。
# 设 0 关闭（比如只想跑产出、不想留现场）。
LOG_CALLS = _env("NOVEL_LOG_CALLS", "1") not in ("0", "false", "False", "")

# ---------- 生成侧常量 ----------
# 产出率：模型实际写出的字数 / 指令要求的字数。上游实测 0.82。
# 用途是**前馈补偿** —— 要 600 字就得让它写 600/0.82 ≈ 732 字，否则系统性偏短，
# 而偏短会直接撞上章长硬下限，白烧一轮。
LENGTH_YIELD = float(_env("NOVEL_LENGTH_YIELD", "0.82"))

# 单场目标字数。上游长篇用 750；短篇 2200 字/章 ÷ 4 场 = 550，
# 恰好落在 novel-sft3 的风格先验（567 字/章）附近 —— 场景级生成和这个 LoRA 是对齐的。
SCENE_CHARS = int(_env("NOVEL_SCENE_CHARS", "560"))


@dataclass(frozen=True)
class Budget:
    """三层预算 + 全局熔断。

    为什么全局顶是**调用数**而不是失败数：失败数衡量不了「反复成功但每章都要 4 轮」
    这种慢性失控。book-01 的末段是「每 3 轮成功一次、总共烧 157 轮」—— 连续失败
    计数器拦不住它。
    """
    scene_max_attempts: int = 2      # 每场最多重采 2 次（best-of-2 已经是 2 个样本）
    chapter_max_attempts: int = 3    # 每章最多重写 3 轮 → 之后 degraded 接受
    outline_max_revisions: int = 3   # 大纲最多打回 3 次 → 之后交人工
    # 10 章短篇的预期调用数：立意1 + 人物1 + 大纲1 + 分场10 + 正文(10章×4场×2候选=80)
    # + 标题10 + 摘要10 ≈ 113。留 2× 冗余。撞到这个顶说明闸门标定有问题，该人看。
    run_max_calls: int = 260
    run_deadline_sec: int = 9000


@dataclass(frozen=True)
class SceneLang:
    """题材对「场景驱动力」的定义 —— 本项目支持多题材的全部关键。

    一场戏到底在推进什么，各题材的答案根本不同：
      论辩体：这一场**争**的是哪件事
      悬疑：  这一场**揭示还是隐瞒**哪条信息
      科幻：  这一场**触碰**到设定的哪条规则、代价是什么
      言情：  这一场把两人的关系**挪动**了哪一格
      纯文学：这一场让人物对自己处境的**认知**变了哪一点

    最初版本把「争」写死在 schema 的字段描述和 prompt 里，结果所有题材都会被掰成
    辩论，而且 `outline_lint` 硬查「每章 ≥2 人开口」会让单人视角、书信体、独白体
    每章都报错。所以把这套说法整体外置到 profile。

    注意只外置**说法**，不外置结构：字段仍叫 `driver`，lint 仍然查重合度，
    图拓扑一行不动。这样加题材的成本是写一个 toml，不是改代码。
    """
    driver_name: str = "论题"            # 报告与 lint 里怎么称呼它
    driver_desc: str = "这一场要争的那件事"   # 进 JSON schema 的 description
    driver_rule: str = ""                # 进 prompt 的具体要求，可用 {obj} / {want}
    axis_name: str = "核心分歧"
    axis_desc: str = "核心分歧：两种主张各是什么，都要能站得住"
    stance_desc: str = "在核心分歧上站哪一边"
    premise_rule: str = ""
    cast_rule: str = ""
    outline_rule: str = ""
    dedup_threshold: float = 0.55        # plans_lint 判「同一件事」的阈值
    min_speakers: int = 2                # outline_lint 要求每章至少几人开口
    require_object: bool = True           # 是否要求每章有 must_object


@dataclass(frozen=True)
class Form:
    """交付形态 —— 成品长什么样，与内部的生成单元解耦。

    为什么需要这一层：实测（2026-10-19，福尔摩斯 58 篇独立短篇）一个经典推理
    短篇是 **13,579 字（p50）的一条连续弧**，不是十章连载。而最初的 xuanyi 档位
    照抄了长篇骨架（20,000 字 / 10 章），形式上根本不对。

    但闸门机器依赖「第N章」标题 —— `chapter_blocks` 靠它切块做跨章去重、
    `title_checks` 靠它查标题撞车。所以内部**始终**按章走，
    只在 `compile_book` 落地成品时按这里的 `kind` 渲染。
    这样既不动图拓扑、也不动质量层，交付形态却能按题材变。

    三种 kind：
      chaptered    分章连载，保留「### 第N章：标题」
      single_arc   单篇连续弧，章标题整行去掉，段间用 section_sep 分隔
      sectioned    去掉章号、保留小标题（「## 标题」）—— 文章有小标题但没有章号
    """
    kind: str = "chaptered"        # chaptered | single_arc | sectioned
    unit_label: str = "章"          # 内部分段的叫法，进报告与卡点展示
    section_sep: str = "※"          # single_arc 的段间分隔符


@dataclass(frozen=True)
class Diction:
    """文体称呼 —— 整条链路上写死「小说」的那几个词。

    为什么需要这一层：`SceneLang` 外置了「一场戏在推进什么」的说法，但**文体**
    仍然写死在 prompt 里 —— 结构化调用的身份是「中文小说的结构编辑」、正文
    system 是「你是中文小说作者…对话一律用中文弯引号」、标题/摘要/书名/审校
    四处都写着「小说」。于是非虚构档位（推演、评论）一进来就被这套口径掰成
    小说，而 8B 面对自相矛盾的 system prompt 产出最不稳（它会同时试着满足
    「写文章」和「写对白」，结果两边都不像）。

    **所有默认值与改造前逐字相同**，六个小说档位渲染出的 prompt 一个字节都没变
    （`tests/test_profiles.py::test_diction_defaults_keep_the_novel_prompts_verbatim`
    是这条的回归）。

    `unit` 与 `Form.unit_label` 刻意分开：后者只进成品与报告，前者进 prompt。
    xuanyi 的成品按「幕」渲染，但 prompt 里仍叫「章」—— 那个档位正在 observe
    模式下标定分布，改它的 prompt 会让正在收集的分布漂移。
    """
    work: str = "短篇小说"            # 成品：「为一篇 N 字的中文{work}立意」
    piece: str = "小说"               # 文内指称：「为这篇{piece}设计…」
    unit: str = "章"                  # prompt 里一段的叫法（落盘标题仍是「第N章」）
    section: str = "章节"             # 「你给{piece}{section}起标题」
    editor: str = "中文小说的结构编辑"   # 结构化调用（立意/人物/大纲/分场）的身份
    critic: str = "中文小说的责任编辑"   # 一致性审校的身份
    cast_noun: str = "人物"            # cast 的称呼：人物 / 当事方
    # 章级上下文里那一行。小说要的是「必须**开口**的人」（和 min_speakers 是一对）；
    # 文章里的当事方是用来让机制落地的，让他开口就变成编对话了。
    speaker_label: str = "必须开口的人"


@dataclass(frozen=True)
class Profile:
    """题材档位：闸门阈值 + 结构目标 + 章长编排 + 题材语言。"""
    name: str
    gates: Gates
    targets: dict[str, tuple[float, float, float | None]]
    rhythm: dict[str, int]
    lang: SceneLang = field(default_factory=SceneLang)
    form: Form = field(default_factory=Form)
    diction: Diction = field(default_factory=Diction)
    open_scale: str = "short"
    close_scale: str = "short"
    chapters: int = 10
    target_total_chars: int = 20000
    scenes_per_chapter: int = 4
    prose_model_hint: str = ""
    prose_system_extra: str = ""          # 追加到正文 system prompt 的题材要求
    # 非空则**整段替换** write.PROSE_SYSTEM_BASE。给非虚构档位用 ——
    # 那段基座的每一句都是对话体小说的要求（弯引号、对话归属、插叙打断节奏），
    # 对文章是反向指令，而 prose_system_extra 只能追加、压不掉它。
    prose_system: str = ""
    budget: Budget = field(default_factory=Budget)


def load_profile(name: str = "default") -> Profile:
    path = PROFILES_DIR / f"{name}.toml"
    if not path.exists():
        avail = ", ".join(sorted(p.stem for p in PROFILES_DIR.glob("*.toml")))
        raise FileNotFoundError(f"没有档位 {name!r}。可用：{avail}")
    raw = tomllib.loads(path.read_text(encoding="utf-8"))
    meta = raw.get("meta", {})
    rhythm = dict(raw.get("rhythm", {}))
    return Profile(
        name=raw.get("name", name),
        gates=Gates(**raw.get("gates", {})),
        targets={k: (v["lo"], v["hi"], v.get("hard"))
                 for k, v in (raw.get("targets") or {}).items()},
        rhythm={k: int(v) for k, v in rhythm.items() if isinstance(v, int)},
        lang=SceneLang(**(raw.get("scene") or {})),
        form=Form(**(raw.get("form") or {})),
        diction=Diction(**(raw.get("diction") or {})),
        open_scale=str(rhythm.get("open_scale", "short")),
        close_scale=str(rhythm.get("close_scale", "short")),
        chapters=int(meta.get("chapters", 10)),
        target_total_chars=int(meta.get("target_total_chars", 20000)),
        scenes_per_chapter=int(meta.get("scenes_per_chapter", 4)),
        prose_model_hint=raw.get("prose_model_hint", ""),
        prose_system_extra=raw.get("prose_system_extra", ""),
        prose_system=raw.get("prose_system", ""),
    )


def list_profiles() -> list[str]:
    return sorted(p.stem for p in PROFILES_DIR.glob("*.toml"))


def plan_rhythm(profile: Profile, chapters: int, total_chars: int
                ) -> list[tuple[str, int]]:
    """按档位给每章分配 (scale, target_chars)。

    **scale 不交给模型分配** —— 实测它会把所有章都标成 "normal"。
    首章冷开场、末章收束走 short 档位，这样 metrics.structural_reasons 会豁免
    密度类硬线（见 metrics.py:187-191：参照书的这类章对话占比低到 1.6%，
    是刻意的，不是塌缩）。
    """
    scales = ["normal"] * chapters
    if chapters >= 3:
        scales[0] = profile.open_scale
        scales[-1] = profile.close_scale
    weights = [profile.rhythm.get(s, profile.rhythm.get("normal", 2200))
               for s in scales]
    unit = total_chars / max(1, sum(weights))
    return [(s, max(600, int(w * unit))) for s, w in zip(scales, weights)]

