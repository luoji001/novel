"""Langfuse 追踪 —— 可选，默认关闭。

设计上的三条硬规矩：

**① 没配 = 关闭，绝不回落到云端。**
Langfuse SDK 解析 host 的顺序是
`base_url 参数 → LANGFUSE_BASE_URL → host 参数 → LANGFUSE_HOST → "https://cloud.langfuse.com"`
（`langfuse._client.client.Langfuse.__init__` 的源码，2026-10-19 核对）。
也就是说**什么都不配就会把数据发到 SaaS**。自托管的全部意义就是别这么干，
所以这里要求必须显式给出 base_url，缺了就直接判定为关闭。

**② 非本地地址默认拒绝。**
解析出来的 host 不在 loopback 上就报错退出，除非显式设
`NOVEL_LANGFUSE_ALLOW_REMOTE=1`。一个打错的变量名不该导致小说草稿外发。

**③ 任何失败都不影响生成。**
Langfuse 没装、没起、认证失败、网络不通 —— 一律降级为「不追踪」并打一行提示。
观测是手段，不是目的。

追踪结构：一部小说 = 一个 Langfuse **session**（`session_id = slug`），
与 LangGraph 的 `thread_id = slug` 对齐，这样 Langfuse 里的分组和 checkpoint
的分组是同一套。
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import urlparse

_LOCAL_HOSTS = {"localhost", "127.0.0.1", "::1", "0.0.0.0", "host.docker.internal"}


class TracingConfigError(RuntimeError):
    """配置本身有问题（比如指向了外网）。这个要抛，不要静默降级 ——
    静默降级会让「以为在本地追踪、其实在往外发」成为可能。"""


@dataclass
class Tracing:
    """追踪句柄。`enabled=False` 时所有方法都是空操作。"""
    enabled: bool = False
    session_id: str = ""
    base_url: str = ""
    handler: Any = None
    client: Any = None
    reason: str = ""          # 关闭的原因，给 CLI 打印
    _scored: set = field(default_factory=set, repr=False)

    # ---------- 给 LangGraph 的 config ----------
    def config_patch(self, *, profile: str = "", gate_mode: str = "") -> dict:
        """要合并进 invoke config 的部分。未启用时返回空 dict。

        `callbacks` 放进 config 之后，LangChain 的 `ensure_config()` 会通过
        `var_child_runnable_config` 这个 ContextVar 把它透传到节点内部手工
        构造的 `.invoke()` —— 所以 `llm.py` 不需要为追踪改任何代码。
        """
        if not self.enabled:
            return {}
        return {
            "callbacks": [self.handler],
            "metadata": {
                "langfuse_session_id": self.session_id,
                "langfuse_tags": [t for t in ("novel-agent", profile, gate_mode) if t],
            },
        }

    # ---------- 分数 ----------
    def score_chapter(self, record: dict) -> None:
        """把一章的规则分数推成 Langfuse score。

        逐个指标各推一条，而不是只推一个总分 —— 这样才能在 Langfuse 里按
        「dialogue_chars_pct < 20」筛，而这正是 observe→定硬线 要做的事。
        """
        if not self.enabled:
            return
        no = record.get("no")
        key = ("chapter", no)
        if key in self._scored:        # 节点重跑（interrupt 恢复）时别推重复的
            return
        self._scored.add(key)

        comment = "；".join((record.get("issues") or [])[:6]) or None
        meta = {"chapter": no, "title": record.get("title"),
                "scale": record.get("scale"), "chars": record.get("chars"),
                "attempts": record.get("attempts"),
                "degraded": record.get("degraded")}
        self._score("chapter_score", record.get("score"), comment, meta)
        for name, value in (record.get("metrics") or {}).items():
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                self._score(f"m.{name}", value, None, meta)
        # 质量债条数是个好筛选维度：>0 意味着这章是带病放行的
        self._score("debt_count", len(record.get("issues") or []), comment, meta)

    def score_scene(self, rec: dict) -> None:
        """场景选优的记录。记下 best-of-2 里**被选中**那个的分数与采样档位。"""
        if not self.enabled or rec.get("kind") != "scene":
            return
        key = ("scene", rec.get("chapter"), rec.get("scene"))
        if key in self._scored:
            return
        self._scored.add(key)
        self._score("scene_score", rec.get("score"), f"picked={rec.get('picked')}",
                    {"chapter": rec.get("chapter"), "scene": rec.get("scene"),
                     "picked": rec.get("picked"),
                     "candidates": rec.get("candidates")})

    def _score(self, name: str, value, comment, metadata) -> None:
        if value is None:
            return
        try:
            self.client.create_score(
                name=name, value=float(value), session_id=self.session_id,
                data_type="NUMERIC", comment=comment, metadata=metadata)
        except Exception as e:                                    # noqa: BLE001
            print(f"  ⚠ Langfuse 打分失败（已忽略）：{type(e).__name__}: {e}")

    def flush(self) -> None:
        if not self.enabled:
            return
        try:
            self.client.flush()
        except Exception:                                         # noqa: BLE001
            pass


def _resolve_base_url() -> str:
    """按优先级取 base_url。**刻意不提供默认值** —— 没配就是没开。"""
    for key in ("NOVEL_LANGFUSE_BASE_URL", "LANGFUSE_BASE_URL", "LANGFUSE_HOST"):
        v = (os.environ.get(key) or "").strip()
        if v:
            return v
    return ""


def _assert_local(base_url: str) -> None:
    host = (urlparse(base_url).hostname or "").lower()
    if host in _LOCAL_HOSTS or host.endswith(".local"):
        return
    if os.environ.get("NOVEL_LANGFUSE_ALLOW_REMOTE") == "1":
        print(f"  ⚠ Langfuse 指向非本地地址 {host}，已被 "
              f"NOVEL_LANGFUSE_ALLOW_REMOTE=1 放行")
        return
    raise TracingConfigError(
        f"Langfuse 的 base_url 指向 {host!r}，不是本机。\n"
        f"  小说 prompt 会被发到那里。确认这是你要的，就设 "
        f"NOVEL_LANGFUSE_ALLOW_REMOTE=1；\n"
        f"  本地自托管应该是 http://localhost:3000"
        f"（见 observability/keys.env）。")


def setup(slug: str, *, verbose: bool = True) -> Tracing:
    """为一次 run 准备追踪。任何问题都降级为「不追踪」（配置指向外网除外）。"""
    if os.environ.get("NOVEL_TRACING") == "0":
        return Tracing(reason="NOVEL_TRACING=0")

    base_url = _resolve_base_url()
    pk = (os.environ.get("LANGFUSE_PUBLIC_KEY") or "").strip()
    sk = (os.environ.get("LANGFUSE_SECRET_KEY") or "").strip()
    if not (base_url and pk and sk):
        missing = [n for n, v in (("base_url", base_url),
                                  ("LANGFUSE_PUBLIC_KEY", pk),
                                  ("LANGFUSE_SECRET_KEY", sk)) if not v]
        return Tracing(reason=f"未配置（缺 {', '.join(missing)}）")

    _assert_local(base_url)        # 这个要抛，不降级

    try:
        from langfuse import Langfuse
        from langfuse.langchain import CallbackHandler
    except ImportError:
        return Tracing(reason="没装 langfuse（uv sync --extra observability）")

    try:
        client = Langfuse(public_key=pk, secret_key=sk, base_url=base_url,
                          environment="local", tracing_enabled=True,
                          flush_at=20, flush_interval=5.0, timeout=10)
        if not client.auth_check():
            return Tracing(reason=f"认证失败（密钥对不上 {base_url}）")
        handler = CallbackHandler()
    except Exception as e:                                        # noqa: BLE001
        return Tracing(reason=f"初始化失败 {type(e).__name__}: {e}")

    if verbose:
        print(f"  ◉ Langfuse 追踪已开：{base_url}  session={slug}")
    return Tracing(enabled=True, session_id=slug, base_url=base_url,
                   handler=handler, client=client)
