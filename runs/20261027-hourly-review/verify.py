#!/usr/bin/env python3
"""每小时复盘的验证脚本：按 batch.jsonl 的 code_hash 分组，算 LOG.md「待验证」里的各项。

用法（只读，不改任何产出）：
  UV_PROJECT_ENVIRONMENT=/home/liang/.venvs/novel-agent \
    uv run --project /mnt/c/code/novel-agent python verify.py <批次目录> [<批次目录> ...]
例：verify.py ~/novel-agent/batches/20261027-shipin ~/novel-agent/batches/20261028-shipin

同一份代码在不同种子轮次之间均分会晃 66~71（见 LOG 第 3 轮），所以比较时
**要拿同一组种子的整轮**，不要拿几部的均值下结论。
"""
from __future__ import annotations

import collections
import json
import os
import re
import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, "/mnt/c/code/novel-agent/src")
from novel_agent.quality.rules import _dup_units, cos_sim, sim_ratio  # noqa: E402

RUNS = Path.home() / "novel-agent" / "runs"
PREFIX = re.compile(r"^([^，,：:]{1,14})[，,]([^：:]{1,16})[：:]")


def frag(s: str) -> list[str]:
    return [x for x in re.split(r"[，,。；;]", s or "") if len(x) >= 6]


def q(v: list[float], p: float) -> float:
    v = sorted(v)
    return v[int(p * (len(v) - 1))] if v else float("nan")


def selfdup(text: str) -> bool:
    s, d = _dup_units(text, 10)
    return any(k >= 2 for k in collections.Counter(s).values()) or \
        any(k >= 2 for k in collections.Counter(d).values())


def run_stats(slug: str, acc: dict) -> None:
    d = RUNS / slug
    try:
        quality = [json.loads(l) for l in open(d / "logs/quality.jsonl")]
        rounds = [json.loads(l) for l in open(d / "logs/rounds.jsonl")]
        outline = json.load(open(d / "outline.json"))
        premise = json.load(open(d / "premise.json"))
    except FileNotFoundError:
        return
    outline = outline if isinstance(outline, list) else outline.get("chapters", outline)
    acc["runs"] += 1
    for r in quality:
        m = r["metrics"]
        caps = m.get("capped_by") or []
        acc["ch"] += 1
        acc["scores"].append(r["score"])
        acc["short"] += any("章节过短" in c for c in caps)
        acc["selfdup_cap"] += any("自我复读" in c for c in caps)
        acc["attr_cap"] += any(c.startswith("attr_adv_pct") for c in caps)
        if r["chapter"] == 1:
            acc["ch1_ratio"].append(m.get("chars", 0) / max(1, outline[0].get("target_chars", 1)))
        for k in ("interiority_para_pct", "dialogue_chars_pct"):
            if k in m:
                acc[k].append(m[k])
    for r in rounds:
        if r.get("kind") == "scene" and r.get("scene", 1) > 1:
            acc["scenes2"] += 1
            acc["picked_copied"] += bool(r.get("copied"))      # 改动 2 之后才有这个字段
            acc["has_copied_field"] += "copied" in r
    chars = [c for c in premise.get("characters", []) if c.get("key") in ("A", "B", "C", "D")]
    st_frags = [f for c in chars for f in frag(c.get("stance", ""))]
    beats = [b.get("beat", "") for b in outline]
    for b in outline:
        acc["solo_ch"] += len(b.get("speakers") or []) <= 1
    ending = (premise.get("premise") or {}).get("ending_direction", "")
    if ending and len(outline) > 1:
        cast = {c["key"]: c["name"] for c in premise.get("characters", []) if c.get("name")}
        sims = [cos_sim(ending, b.get("beat", ""), cast) for b in outline]
        acc["end_runs"] += 1
        acc["end_last_closest"] += sims[-1] >= max(sims[:-1])
    for r in quality:
        acc["tpl_single"] += any("单条套路句式" in x for x in r.get("soft", []))
    for b in beats:
        acc["beats"] += 1
        acc["beat_stance"] += any(f in PREFIX.sub("", b) for f in st_frags)
    acc["lint_dup_runs"] += any(sim_ratio(beats[i], beats[j]) >= 0.65
                                for i in range(len(beats)) for j in range(i + 1, len(beats)))
    for ch in sorted((d / "chapters").glob("ch*.md")):
        t = ch.read_text()
        acc["prose_ch"] += 1
        acc["prose_stance"] += any(f in t for f in st_frags)


def main(batch_dirs: list[str]) -> None:
    groups: dict[str, dict] = {}
    for bd in batch_dirs:
        for line in open(Path(bd).expanduser() / "batch.jsonl"):
            r = json.loads(line)
            key = f"{Path(bd).name}@{r.get('code_hash')}"
            acc = groups.setdefault(key, collections.defaultdict(lambda: 0))
            for k in ("scores", "ch1_ratio", "interiority_para_pct", "dialogue_chars_pct"):
                if not isinstance(acc[k], list):
                    acc[k] = []
            acc["stories"] += 1
            acc["failed"] += r.get("status") != "ok"
            if r.get("status") == "ok":
                run_stats(r["slug"], acc)
    for key, a in groups.items():
        ch = max(1, a["ch"])
        print(f"\n== {key}　{a['stories']} 部（失败 {a['failed']}），{a['ch']} 章")
        print(f"  章均分 {st.mean(a['scores']):.1f}　中位 {st.median(a['scores']):.1f}")
        print(f"  [改动1] 章节过短 {a['short']}/{ch} = {100*a['short']/ch:.1f}%"
              f"　首章 实际/目标 中位 {q(a['ch1_ratio'], .5):.2f}")
        print(f"  [改动2] 章内自我复读封顶 {a['selfdup_cap']}/{ch} = {100*a['selfdup_cap']/ch:.1f}%"
              f"　第2场起选中候选带副本 {a['picked_copied']}/{a['scenes2']}"
              f"（有 copied 字段的场次 {a['has_copied_field']}）")
        print(f"  [改动3] beat 含 stance 片段 {a['beat_stance']}/{a['beats']} = "
              f"{100*a['beat_stance']/max(1,a['beats']):.1f}%"
              f"　大纲有近重复章 {a['lint_dup_runs']}/{a['runs']} = "
              f"{100*a['lint_dup_runs']/max(1,a['runs']):.1f}%"
              f"　正文逐字复述 stance {a['prose_stance']}/{a['prose_ch']}")
        print(f"  [改动4] attr_adv 封顶 {a['attr_cap']}/{ch}")
        print(f"  [改动5] 挂「单条套路句式」软警告的章 {a['tpl_single']}/{ch}")
        print(f"  [改动6] 大纲单人章（speakers ≤ 1）{a['solo_ch']}/{a['beats']} = "
              f"{100*a['solo_ch']/max(1,a['beats']):.1f}%")
        print(f"  [改动8] 末章 beat 是全书最像结局的一章 {a['end_last_closest']}/{a['end_runs']} = "
              f"{100*a['end_last_closest']/max(1,a['end_runs']):.1f}%")
        print(f"  [回滚监测] interiority p50/p97 {q(a['interiority_para_pct'], .5):.1f}/"
              f"{q(a['interiority_para_pct'], .97):.1f}　dialogue_chars_pct < 5 的章 "
              f"{sum(1 for v in a['dialogue_chars_pct'] if v < 5)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
