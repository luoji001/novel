"""本地 vLLM 接入层 —— 全项目唯一的 LLM 出口。

所有节点都必须走 `call()` / `call_structured()`，这样算力账本（telemetry）才是全的。

三条硬约束，每条都有实测依据：

**① 不传 `reasoning_effort`，不传 `chat_template_kwargs`。**
vLLM 会把 `reasoning_effort` 转成 `enable_thinking=true`，优先级高于
`--default-chat-template-kwargs`。nothink 已经在服务端的 `--chat-template`
里无条件固化（模板层预填空 `<think></think>`），客户端再传只会打架。

**② 每次调用都显式传全部采样参数。**
`--override-generation-config` 只改**默认值**（conf 里 2026-10-06 的实测更正）。
不显式传就会静默继承 temp 0.8 / top_p 0.95 / top_k 40 / rp 1.1 ——
于是「大纲节点低温严谨」这个设计根本没生效，而且不会有任何报错。

**③ `max_retries=0`。**
传输重试交给 LangGraph 的 `retry_policy`。两层叠加后一次「失败」实际是 3×3=9 次
请求，预算账全错，而且重试不可见。
"""

from __future__ import annotations

import json
import re
import threading
import time
from dataclasses import asdict, dataclass
from functools import lru_cache
from typing import Any, Literal

from langchain_openai import ChatOpenAI

from . import config as C

# 第二道并发闸。图层的 max_concurrency 限的是任务数；如果哪天某个节点内部自己起了
# 并行调用，图层就管不住了。默认与 --max-num-seqs 对齐。
_SLOTS = threading.BoundedSemaphore(C.CONCURRENCY)


def est_tokens(s: str) -> int:
    """中文 token 估算，取上界（Qwen3 对中文约 1 字 ≈ 0.6~1 token，这里按 1.7 保守估）。"""
    return int(len(s or "") * 1.7) + 8


class ContextOverflow(RuntimeError):
    """prompt 超预算。宁可报错也不让服务端静默截断 —— 被截断的是末尾的
    「写法要求」，模型会直接回到塌缩分布，而且没有任何报错。"""


def _log_call(run: str | None, record: dict) -> None:
    """把一次调用的完整现场落到 runs/<slug>/logs/calls.jsonl。

    为什么直写磁盘、不走 state：
      ① 113 次调用 × 约 6000 token 的 prompt 进 checkpoint 会把快照撑爆，
         而 `durability="sync"` 下每个 super-step 都要写一份快照。
      ② 直写意味着 **run 崩了日志还在** —— 那恰恰是你最想看它的时候。
         走 state 的话，异常抛出时这一轮的 state 更新根本没提交。

    这份日志填的是原有遥测的那个缺口：`report.md` 能告诉你「第 3 章烧了 5 轮」，
    但看不到**是哪个 prompt 产出了那段烂正文**。
    """
    if not run or not C.LOG_CALLS:
        return
    try:
        from .store import RunStore
        RunStore(run).append_jsonl("calls.jsonl", record)
    except Exception:          # noqa: BLE001
        # 记日志失败绝不能把主流程带下去 —— 观测是手段，不是目的。
        pass


@dataclass(frozen=True)
class Sampling:
    temperature: float
    top_p: float = 0.95
    top_k: int = 40
    repetition_penalty: float = 1.1
    presence_penalty: float = 0.0
    frequency_penalty: float = 0.0
    max_tokens: int = 1024

    # Claude 当代模型拒收采样参数，只能用 effort 表达「想多深」。
    # 这不是温度的等价物（effort 控思考深度，不控随机性），所以不做
    # temperature→effort 的换算，而是由调用方按**任务类型**直接给。
    effort: str = "high"

    def bind_kwargs(self, sampling: str = "full") -> dict[str, Any]:
        """按方言产出可以安全下发的参数。

        三档的差别见 `config.Dialect.sampling` 的注释。要紧的是 `standard`：
        它**丢掉** top_k 和 repetition_penalty —— 那两个是 vLLM 扩展，
        第三方会拒收或静默忽略。丢在这里是显式的，比让服务端静默忽略好。
        """
        if sampling == "none":
            # Claude 当代模型：一个采样参数都不能带，否则 400。
            # `output_config` 必须平铺下发 —— 它是 ChatAnthropic 的一等字段，
            # 也是 Messages.create 直收的参数。裹进 `model_kwargs` 会被原样
            # 转发成 API 字段，报 `unexpected keyword argument 'model_kwargs'`
            # （model_kwargs 是构造参数，不是 bind 参数）。
            return {"max_tokens": self.max_tokens,
                    "output_config": {"effort": self.effort}}

        out: dict[str, Any] = {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "presence_penalty": self.presence_penalty,
            "frequency_penalty": self.frequency_penalty,
            "max_tokens": self.max_tokens,
        }
        if sampling == "full":
            out["extra_body"] = {"top_k": self.top_k,
                                 "repetition_penalty": self.repetition_penalty}
        return out


# ---------- 两个互不兼容的采样工厂 ----------
# 这个分离是刻意的，用类型把一个具体的 bug 变成不可能。
#
# 上游 2026-10-07 修过两个 bug，它们一起把第四章烧掉 30 轮：
#   ① plan_scenes 的 max_tokens 写死 1600，长档 9 个场景的 JSON 放不下 → 截断
#      → 解析失败（24 次失败全是这个）
#   ② 它 `dict(sampling)` 继承了正文的逐轮升温，temp 被推到 1.30、presence 1.20
#      → 越失败越升温、越升温越产不出合法 JSON → 死循环
#
# 所以 `struct_sampling` 的签名里**根本没有 attempt 参数**：结构化调用不可能升温。

StructKind = Literal["premise", "cast", "outline", "plan", "title", "summary", "critic"]

_STRUCT: dict[StructKind, Sampling] = {
    # 要 JSON 合法 + 设定自洽；高温在这里只会换出新毛病
    "premise": Sampling(temperature=0.45, top_p=0.90, top_k=20,
                        repetition_penalty=1.05, max_tokens=900,
                        effort="high"),      # 要点子，值得想深
    "cast":    Sampling(temperature=0.40, top_p=0.90, top_k=20,
                        repetition_penalty=1.05, max_tokens=1200,
                        effort="medium"),
    # 唯一需要「点子」的结构化调用；presence 0.2 压 beats 之间雷同
    "outline": Sampling(temperature=0.55, top_p=0.92, top_k=40,
                        repetition_penalty=1.05, presence_penalty=0.20,
                        max_tokens=2600, effort="high"),   # 唯一要「点子」的结构化调用
    "plan":    Sampling(temperature=0.35, top_p=0.90, top_k=20,
                        repetition_penalty=1.02, max_tokens=2000,
                        effort="medium"),
    # 标题要多样。用基座而不是 LoRA：LoRA 的标题分布来自已被判定「去近似后
    # 369 章只剩 162 个实质不同标题」的旧语料，用它等于主动采样进那个同质簇。
    "title":   Sampling(temperature=0.85, top_p=0.95, top_k=40,
                        repetition_penalty=1.10, presence_penalty=0.40,
                        max_tokens=48, effort="low"),      # 一行字，不值得想
    # 摘要要准。温度高会编造正文里没有的事 —— 而摘要是长期记忆的唯一载体，
    # 摘要错了等于记忆错了。
    "summary": Sampling(temperature=0.30, top_p=0.90, top_k=20,
                        repetition_penalty=1.05, max_tokens=240,
                        effort="low"),
    # 挑错要近确定性，否则同一稿两次给两套意见
    "critic":  Sampling(temperature=0.20, top_p=0.80, top_k=20,
                        repetition_penalty=1.00, max_tokens=1200,
                        effort="high"),      # 挑错要仔细
}


def struct_sampling(kind: StructKind, *, want: int = 0) -> Sampling:
    """结构化调用的采样档位。**没有 attempt 参数，不参与任何扰动。**

    `want` 用于按场景数算 max_tokens —— 上游把它写死 1600，长档 9 场的 JSON
    放不下就截断，而截断表现为「解析失败」，很难归因到预算上。
    """
    s = _STRUCT[kind]
    if kind == "plan" and want:
        return Sampling(**{**asdict(s),
                           "max_tokens": min(6000, 420 + want * 230)})
    return s


def prose_sampling(attempt: int, target_chars: int, *, variant: int = 0) -> Sampling:
    """正文采样。扰动必须加在**采样**上，不能只改 prompt 文本。

    上游的教训：v1 的自救只改 prompt，同一个标题被原封不动提了 7 次 ——
    分布没动，重试等于从同一个已塌缩的分布里再独立采一次样。

    `variant` 用于 best-of-2：同一场同时发两个候选，一个稳一个野。
    `attempt` 是本章重写轮数，逐轮升温。
    """
    step = min(attempt, 2)
    base = 0.85 + 0.15 * variant          # variant 0 → 0.85, variant 1 → 1.00
    return Sampling(
        temperature=min(base + 0.08 * step, 1.25),
        top_p=0.95,
        top_k=40,
        repetition_penalty=1.10 + 0.05 * variant,
        presence_penalty=min(0.30 + 0.15 * step, 1.20),
        frequency_penalty=min(0.2 * step, 0.6) if step >= 2 else 0.0,
        max_tokens=max(700, min(4096, int(target_chars * 2.4))),
    )


# ---------- 客户端 ----------

@lru_cache(maxsize=8)
def _client_for(kind: str, base_url: str, api_key: str, model: str,
                workspace: str = ""):
    """按端点建 client（复用连接池）。采样参数一律 per-call bind ——
    为每种采样档位新建 client 会让 client 数量随温度阶梯爆炸。

    `kind="anthropic"` 走 ChatAnthropic：Claude 不是 OpenAI 兼容接口，
    拿 ChatOpenAI 套 base_url 是接不上的。
    """
    if kind == "anthropic":
        try:
            from langchain_anthropic import ChatAnthropic
        except ImportError as e:  # pragma: no cover - 取决于是否装了可选依赖
            raise ImportError(
                "provider=anthropic 需要 langchain-anthropic："
                "uv sync --extra anthropic") from e
        # user 级 key（sk-ant-usr-…）不绑 workspace，必须显式带头，否则
        # 每个请求 400。workspace 级 key（sk-ant-api…）留空即可。
        headers = {"anthropic-workspace-id": workspace} if workspace else None
        return ChatAnthropic(model=model, api_key=api_key,
                             default_headers=headers,
                             max_retries=0, timeout=600.0)
    return ChatOpenAI(model=model, base_url=base_url, api_key=api_key,
                      max_retries=0,   # 见模块 docstring 约束 ③
                      timeout=600.0)


def _resolve(role: str, model: str | None):
    """给定角色（struct / prose）拿到 (client, 实际模型名, 方言)。

    `model` 显式给了就覆盖端点的默认模型 —— `--prose-model` 这类开关靠它。
    """
    ep = C.prose_endpoint() if role == "prose" else C.struct_endpoint()
    name = model or ep.model
    d = ep.dialect
    return (_client_for(d.kind, ep.base_url, ep.api_key, name, ep.workspace),
            name, d)


def call(prompt: str, s: Sampling, *, model: str | None = None,
         system: str | None = None, tag: str = "",
         run: str | None = None, role: str = "struct") -> tuple[str, dict]:
    """纯文本调用。返回 (文本, 遥测)。

    `run` 是 slug；给了就把完整现场（prompt / completion / 采样参数）落到
    calls.jsonl。不给就只返回遥测 —— 测试和探针不需要写盘。
    """
    client, model, dia = _resolve(role, model)
    in_est = est_tokens(prompt)
    budget = in_est + s.max_tokens
    if budget > dia.context:
        _log_call(run, _record(run, tag, model, s, system, prompt, "",
                               in_est, 0.0, error="context_overflow"))
        raise ContextOverflow(
            f"[{tag}] prompt {in_est} tok + max_tokens {s.max_tokens} "
            f"= {budget} > 上下文 {dia.context}")
    msgs: list[tuple[str, str]] = []
    if system:
        msgs.append(("system", system))
    msgs.append(("human", prompt))

    t0 = time.monotonic()
    try:
        with _SLOTS:
            msg = client.bind(**s.bind_kwargs(dia.sampling)).invoke(msgs)
    except Exception as e:                                        # noqa: BLE001
        # 失败也要落盘。重试是靠采样扰动起作用的，没有失败现场就看不出
        # 「升了温到底有没有换出不同的样本」。
        _log_call(run, _record(run, tag, model, s, system, prompt, "", in_est,
                               round(time.monotonic() - t0, 2),
                               error=f"{type(e).__name__}: {e}"))
        raise
    sec = round(time.monotonic() - t0, 2)
    text = msg.content if isinstance(msg.content, str) else ""
    usage = (msg.response_metadata or {}).get("token_usage")
    _log_call(run, _record(run, tag, model, s, system, prompt, text, in_est,
                           sec, usage=usage))
    return text, {"tag": tag, "model": model, "temperature": s.temperature,
                  "in_est": in_est, "out_chars": len(text),
                  "usage": usage, "sec": sec}


def _record(run: str | None, tag: str, model: str, s: Sampling,
            system: str | None, prompt: str, completion: str, in_est: int,
            sec: float, *, usage: dict | None = None,
            error: str | None = None, structured: dict | None = None) -> dict:
    """calls.jsonl 的一行。

    刻意把采样参数整组记下来，而不只记 temperature：排查「为什么这一场写塌了」
    时要看的是整组参数（presence/frequency/repetition 在逐轮升温里都在变）。
    """
    rec = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "run": run, "tag": tag, "model": model,
        "sampling": asdict(s),
        "system": system or "",
        "prompt": prompt,
        "completion": completion,
        "in_est": in_est, "out_chars": len(completion),
        "usage": usage, "sec": sec,
        "ok": error is None,
    }
    if error:
        rec["error"] = error
    if structured is not None:
        rec["structured"] = structured
    # 从 tag 里把 (章, 场, 候选) 拆出来，方便和 rounds.jsonl 的分数做 join
    rec.update(parse_tag(tag))
    return rec


_TAG_RE = re.compile(r"^(?P<kind>[a-z_]+)(?::ch(?P<ch>\d+)"
                     r"(?:\.s(?P<scene>\d+))?(?:\.v(?P<variant>\d+))?)?$")


def parse_tag(tag: str) -> dict:
    """`scene:ch2.s1.v0` → {kind:scene, chapter:2, scene:1, variant:0}。

    让 calls.jsonl 能和 rounds.jsonl 的 `quality_log` 记录对上 ——
    后者有「这一场选了哪个候选、分多少」，前者有「那个候选是什么 prompt 产的」。
    两边一 join 就能回答「给我看所有低分场景的 prompt」。
    """
    m = _TAG_RE.match(tag or "")
    if not m:
        return {"kind": (tag or "").split(":")[0] or "unknown"}
    out: dict = {"kind": m.group("kind")}
    for k, field in (("ch", "chapter"), ("scene", "scene"),
                     ("variant", "variant")):
        v = m.group(k)
        if v is not None:
            out[field] = int(v)
    return out


def call_structured(prompt: str, s: Sampling, schema: dict, fn_name: str, *,
                    model: str | None = None, system: str | None = None,
                    tag: str = "", run: str | None = None,
                    role: str = "struct") -> tuple[dict, dict]:
    """结构化调用。用**强制指定函数**的 tool_choice，不依赖模型自主选择。

    已实测（2026-10-18，qwen3-8b + hermes parser）：嵌套 array-of-objects 的
    schema 和 enum 约束都守得住，JSON 一次解析成功。
    仍然保留宽容解析兜底 —— 把流程的正确性全押在服务端的 tool-call parser 上
    风险收益不划算。
    """
    client, model, dia = _resolve(role, model)
    tool = {"type": "function",
            "function": {"name": fn_name, "description": f"提交{fn_name}",
                         "parameters": schema}}
    msgs: list[tuple[str, str]] = []
    if system:
        msgs.append(("system", system))
    msgs.append(("human", prompt))
    bound = client.bind(
        **s.bind_kwargs(dia.sampling), tools=[tool],
        tool_choice={"type": "function", "function": {"name": fn_name}})
    in_est = est_tokens(prompt)
    t0 = time.monotonic()
    try:
        with _SLOTS:
            msg = bound.invoke(msgs)
    except Exception as e:                                        # noqa: BLE001
        _log_call(run, _record(run, tag, model, s, system, prompt, "", in_est,
                               round(time.monotonic() - t0, 2),
                               error=f"{type(e).__name__}: {e}"))
        raise
    sec = round(time.monotonic() - t0, 2)
    usage = (msg.response_metadata or {}).get("token_usage")
    tele = {"tag": tag, "model": model, "role": role,
            "sampling_mode": dia.sampling, "temperature": s.temperature,
            "in_est": in_est, "sec": sec, "usage": usage}

    raw = msg.content if isinstance(msg.content, str) else ""
    calls = getattr(msg, "tool_calls", None) or []
    if calls:
        data = dict(calls[0].get("args") or {})
        _log_call(run, _record(run, tag, model, s, system, prompt, raw, in_est,
                               sec, usage=usage, structured=data))
        return data, tele

    data = _json_loose(raw)
    if data is None:
        # JSON 截断是上游的头号规划失败源（第四章 30 轮里 24 次是这个）。
        # 把原始输出完整留下来，才能判断到底是 max_tokens 不够还是模型跑偏。
        _log_call(run, _record(run, tag, model, s, system, prompt, raw, in_est,
                               sec, usage=usage, error="no_structured_output"))
        raise ValueError(f"[{tag}] 没拿到结构化输出，原始内容前 200 字："
                         f"{raw[:200]}")
    tele["fallback"] = "json_loose"
    _log_call(run, _record(run, tag, model, s, system, prompt, raw, in_est,
                           sec, usage=usage, structured=data))
    return data, tele


def _json_loose(text: str) -> dict | None:
    """宽容 JSON 解析：剥 ```json 围栏、取第一个 {...} 平衡段。"""
    t = (text or "").strip()
    if t.startswith("```"):
        t = t.split("\n", 1)[-1]
        if t.rstrip().endswith("```"):
            t = t.rstrip()[:-3]
    try:
        out = json.loads(t)
        return out if isinstance(out, dict) else None
    except json.JSONDecodeError:
        pass
    start = t.find("{")
    if start < 0:
        return None
    depth = 0
    for i, ch in enumerate(t[start:], start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                try:
                    out = json.loads(t[start:i + 1])
                    return out if isinstance(out, dict) else None
                except json.JSONDecodeError:
                    return None
    return None
