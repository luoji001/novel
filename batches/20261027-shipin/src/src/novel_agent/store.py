"""章节正文的磁盘真相源。

state 里只有索引（`ChapterRecord`），正文在这里。两边必须一起回退 —— 这是本设计
最容易写出 bug 的地方：如果 state 说「第 5 章要重写」而磁盘上还是旧正文，
跨章去重就会拿旧章当历史比，于是新写的第 5 章永远「与历史重复」。
"""

from __future__ import annotations

import json
import threading
import time
from pathlib import Path

from . import config as C

# jsonl 追加的全局锁。Send 扇出的候选任务跑在不同线程上，两个线程同时写
# calls.jsonl 会交错出半行。单行 append 在 Linux 上通常是原子的，但「通常」
# 不够 —— 日志坏掉的时候恰恰是你最需要它的时候。
_APPEND_LOCK = threading.Lock()


class RunStore:
    def __init__(self, slug: str, root: Path | None = None) -> None:
        self.slug = slug
        self.root = (root or C.DATA_ROOT) / "runs" / slug
        self.chapters_dir = self.root / "chapters"
        self.logs_dir = self.root / "logs"

    def ensure(self) -> None:
        for d in (self.chapters_dir, self.logs_dir):
            d.mkdir(parents=True, exist_ok=True)

    # ---------- 章节正文 ----------
    def chapter_path(self, n: int) -> Path:
        return self.chapters_dir / f"ch{n:02d}.md"

    def write_chapter(self, n: int, body: str) -> str:
        self.ensure()
        p = self.chapter_path(n)
        p.write_text(body.rstrip() + "\n", encoding="utf-8")
        return str(p)

    def read_chapter(self, n: int) -> str:
        p = self.chapter_path(n)
        return p.read_text(encoding="utf-8") if p.exists() else ""

    def read_chapters(self, upto: int | None = None) -> dict[int, str]:
        """读已定稿章节。闸门要拿它们做跨章去重 —— 这是正文唯一被完整读取的地方，
        而且只在纯 python 里用，不进 prompt。"""
        out: dict[int, str] = {}
        if not self.chapters_dir.exists():
            return out
        for p in sorted(self.chapters_dir.glob("ch*.md")):
            try:
                n = int(p.stem[2:])
            except ValueError:
                continue
            if upto is None or n <= upto:
                out[n] = p.read_text(encoding="utf-8")
        return out

    def rewind(self, k: int) -> list[str]:
        """把第 k 章及之后的正文移进 .trash（不删）。配合 state 的 Overwrite 一起用。"""
        moved = []
        trash = self.chapters_dir / ".trash" / time.strftime("%Y%m%d-%H%M%S")
        for p in sorted(self.chapters_dir.glob("ch*.md")):
            try:
                n = int(p.stem[2:])
            except ValueError:
                continue
            if n >= k:
                trash.mkdir(parents=True, exist_ok=True)
                p.rename(trash / p.name)
                moved.append(p.name)
        return moved

    # ---------- 其他产物 ----------
    def write_json(self, name: str, data) -> str:
        self.ensure()
        p = self.root / name
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2),
                     encoding="utf-8")
        return str(p)

    def write_text(self, name: str, text: str) -> str:
        self.ensure()
        p = self.root / name
        p.write_text(text, encoding="utf-8")
        return str(p)

    def append_jsonl(self, name: str, record: dict) -> None:
        """字段与生产线的 logs/*.jsonl 对齐，这样 train/distill_insights.py
        将来不用改一行就能吃这份数据。线程安全（见 _APPEND_LOCK）。"""
        self.ensure()
        line = json.dumps(record, ensure_ascii=False) + "\n"
        with _APPEND_LOCK, (self.logs_dir / name).open("a", encoding="utf-8") as f:
            f.write(line)

    def read_jsonl(self, name: str) -> list[dict]:
        """读回一份 jsonl。坏行跳过而不是抛 —— 日志是用来排查问题的，
        它自己不该成为新的故障点。"""
        p = self.logs_dir / name
        if not p.exists():
            return []
        out = []
        for ln in p.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if not ln:
                continue
            try:
                out.append(json.loads(ln))
            except json.JSONDecodeError:
                continue
        return out
