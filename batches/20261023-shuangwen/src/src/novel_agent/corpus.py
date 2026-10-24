"""参考语料 → 可复算的基线。

**语料只当尺子，不进 prompt。** 它用来算分布、定硬线、抽结构模板；
文风由 `novel-sft3` 和 prompt 决定。这条界线是刻意的：
`profiles-sft/xuanyi/福尔摩斯探案全集.epub` 是 19 世纪英文作品的**中译本**，
把它的句法直接喂进生成会把译文腔学进产出（实测对照见 `baseline.json` 的
`notes`，以及下面 NATIVE_KEYS 的注释）。

方法论照抄生产线：拿参照书算**单篇分布**，硬线定在 p3。
依据是 `quality/metrics.py:68-78` 记录的那次教训 ——
用全书聚合值当单章阈值，结果参照书自己的章过不了以它为蓝本定的闸门。

一切都是可复算的：换语料重跑 `novel-agent baseline <profile>` 就行。
"""

from __future__ import annotations

import hashlib
import html as H
import json
import re
import statistics as stat
import time
import zipfile
from dataclasses import dataclass
from pathlib import Path

from .quality import metrics as NM
from .quality.rules import chapter_blocks, normalize_prose

# 非正文篇目。epub 里的前言/序/附录会污染分布：
# 福尔摩斯那本的《前言》2936 字、对话占比 2.1%，混进去会把 p3 拉低。
_FRONT_MATTER = re.compile(
    r"^\s*(前言|序[言章]?|自序|译序|译者序|代序|后记|跋|附录|目录|版权|"
    r"出版说明|导读|作者简介|内容简介|编者按)")

# 进 baseline 的指标。顺序就是报告里的顺序。
KEYS = (
    "chars", "paragraphs",
    "dialogue_chars_pct", "dialogue_para_pct",
    "interiority_para_pct", "narration_para_pct",
    "turn_under20_pct", "turn_len_median",
    "attr_say_pct", "attr_adv_pct",
    "dialogue_run_mean", "dialogue_run_max",
    "scenes", "scene_len_mean", "sent_len_mean",
)

# 「题材/结构」维度 —— 这些可以放心跟参照书学，它们刻画的是形式而不是语感。
GENRE_KEYS = ("chars", "dialogue_chars_pct", "dialogue_para_pct",
              "narration_para_pct", "dialogue_run_mean", "scenes",
              "scene_len_mean", "interiority_para_pct")

# 「中文原生文风」维度 —— **不要**跟译本学这几项。
# 实测三方对照（2026-10-19，单篇 p50）：
#     指标               天幕红尘(原创)  福尔摩斯(中译)  三体(原创)
#     attr_adv_pct            3.3          22.2         11.8
#     sent_len_mean          31.4          25.1         35.6
# 译本的情绪副词归属是三体的两倍、天幕的七倍，句子也明显更短。
# 这两项要用**原创中文语料**定基线。
NATIVE_KEYS = ("attr_adv_pct", "attr_say_pct", "sent_len_mean",
               "turn_len_median", "turn_under20_pct")

# 本模块自己的产出。扫语料时必须跳过，否则会自污染。
_ARTIFACTS = {"baseline.json", "BASELINE.md"}

# 章标题行：用来区分「长篇的分章」与「独立短篇」。
# 福尔摩斯全集里两种都有（41 个分章 + 58 个独立短篇），
# 而标定一个**短篇**生成器，该用的是后者。
_CHAPTER_TITLE = re.compile(r"^(第)?[一二三四五六七八九十百零〇\d]+\s*[章节回]")


@dataclass
class Piece:
    """语料里的一个独立单元：一个短篇，或长篇的一章。"""
    source: str
    title: str
    text: str
    chaptered: bool          # True = 长篇的分章；False = 独立成篇

    @property
    def chars(self) -> int:
        return len(self.text)


# ---------- 抽取 ----------

def _strip_html(raw: str) -> str:
    b = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", raw, flags=re.S)
    b = re.sub(r"<br[^>]*>", "\n", b)
    b = re.sub(r"</(p|div|h[1-6])>", "\n\n", b)
    b = H.unescape(re.sub(r"<[^>]+>", "", b))
    b = re.sub(r"[ \t\xa0　]+", " ", b)
    return re.sub(r"\n{3,}", "\n\n", b).strip()


def extract_epub(path: Path, min_chars: int = 1500) -> list[Piece]:
    """按 OPF 的 spine 顺序抽正文。

    **必须按 spine 而不是按文件名排序** —— 实测福尔摩斯那本的文件名是
    chapter99…chapter1 的倒序，按名字排会把全书顺序弄反，
    而顺序错了「与前文重复」这类比较就全错。
    """
    z = zipfile.ZipFile(path)
    names = z.namelist()
    opf_name = next((n for n in names if n.endswith(".opf")), None)
    if not opf_name:
        raise ValueError(f"{path.name} 里没有 .opf，不是有效 epub")
    opf = z.read(opf_name).decode("utf-8", "ignore")
    spine = re.findall(r"<itemref[^>]*idref=\"([^\"]+)\"", opf)
    href = dict(re.findall(r"<item[^>]*id=\"([^\"]+)\"[^>]*href=\"([^\"]+)\"", opf))

    out: list[Piece] = []
    for ref in spine:
        h = href.get(ref)
        if not h:
            continue
        leaf = h.split("/")[-1]
        member = next((n for n in names if n.endswith(leaf)), None)
        if not member:
            continue
        raw = z.read(member).decode("utf-8", "ignore")
        m = re.search(r"<h[1-6][^>]*>(.*?)</h[1-6]>", raw, re.S)
        title = H.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else ""
        body = _normalize(_strip_html(raw))
        if len(body) < min_chars or _FRONT_MATTER.match(title):
            continue
        out.append(Piece(source=path.name, title=title, text=body,
                         chaptered=bool(_CHAPTER_TITLE.match(title))))
    return out


def _normalize(text: str) -> str:
    """语料也要过引号归一化 —— 否则基线本身就是错的。

    实测（2026-10-19，福尔摩斯那本 epub）：同一本书里引号风格混用，
    甚至同一篇里混用。
        《希腊译员》  中文弯引号 0 个、ASCII " 313 个 → 对话占比读成 0.0%
        《显贵的主顾》 中文 24 个、ASCII 379 个       → 同样读成 0.0%
        《红发会》    中文 196 个、ASCII 93 个        → 75%，但**被低估**
    `metrics.py` 的 QUOTE_RAW 只认 `[「『“]…[」』”]`，不归一化的话整个基线的
    对话类指标都是偏低的下界，据此定的硬线会系统性偏松。

    这是生成端那个坑（见 rules.normalize_prose）的同一个 bug，换了个入口。
    """
    return normalize_prose(text)


def extract_txt(path: Path, min_chars: int = 1500) -> list[Piece]:
    """纯文本语料。有「第N章」标题就按章切，否则整篇算一个单元。"""
    text = path.read_text(encoding="utf-8", errors="ignore")
    blocks = chapter_blocks(text)
    if blocks:
        return [Piece(source=path.name, title=f"第{n}章", text=b, chaptered=True)
                for n, b in blocks if len(b) >= min_chars]
    if len(text) < min_chars:
        return []
    return [Piece(source=path.name, title=path.stem, text=_normalize(text),
                  chaptered=False)]


def extract(path: Path, min_chars: int = 1500) -> list[Piece]:
    if path.suffix.lower() == ".epub":
        return extract_epub(path, min_chars)
    if path.suffix.lower() in (".txt", ".md"):
        return [p for p in extract_txt(path, min_chars)
                if not _FRONT_MATTER.match(p.title)]
    raise ValueError(f"不支持的语料格式：{path.suffix}")


# ---------- 分布 ----------

def percentiles(values: list[float]) -> dict:
    """单侧分位。硬线取 p3 —— 比参照语料最差的 3% 还差才算塌缩。"""
    vs = sorted(v for v in values if v is not None)
    if not vs:
        return {}
    def q(p: float) -> float:
        return round(vs[min(len(vs) - 1, int(len(vs) * p))], 2)
    return {"n": len(vs), "min": round(vs[0], 2), "p3": q(.03), "p10": q(.10),
            "p25": q(.25), "p50": q(.50), "p75": q(.75), "p90": q(.90),
            "max": round(vs[-1], 2),
            "mean": round(stat.mean(vs), 2)}


def distribution(pieces: list[Piece], keys=KEYS) -> dict:
    mets = [NM.chapter_metrics(p.text) for p in pieces]
    return {k: d for k in keys
            if (d := percentiles([m.get(k) for m in mets]))}


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def build_baseline(corpus_dir: Path, *, min_chars: int = 1500) -> dict:
    """把一个档位的语料目录算成 baseline。

    独立短篇与长篇分章**分开统计**。标定一个短篇生成器该看前者 ——
    福尔摩斯全集里 58 个独立短篇的单篇 p50 是 13,593 字 / 7 个场景，
    而那 41 个长篇分章的分布完全是另一回事。
    """
    # 排除本函数自己的产出 —— 否则每次重跑都会把上一次的报告当语料吃进去。
    # 实测踩过：BASELINE.md 被算成 1 篇 2525 字的「独立短篇」，污染分布。
    files = sorted(f for f in corpus_dir.iterdir()
                   if f.suffix.lower() in (".epub", ".txt", ".md")
                   and f.name not in _ARTIFACTS)
    if not files:
        raise FileNotFoundError(f"{corpus_dir} 里没有 .epub/.txt 语料")

    sources, pieces = [], []
    for f in files:
        ps = extract(f, min_chars)
        pieces.extend(ps)
        sources.append({"file": f.name, "bytes": f.stat().st_size,
                        "sha256": _sha256(f), "pieces": len(ps),
                        "chars": sum(p.chars for p in ps)})

    standalone = [p for p in pieces if not p.chaptered]
    chaptered = [p for p in pieces if p.chaptered]

    out = {
        "profile": corpus_dir.name,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "min_chars": min_chars,
        "sources": sources,
        "counts": {"standalone": len(standalone), "chaptered": len(chaptered)},
        "standalone": distribution(standalone),
        "chaptered": distribution(chaptered),
        "pieces": [{"title": p.title, "chars": p.chars, "chaptered": p.chaptered,
                    "source": p.source} for p in pieces],
        "notes": [
            "硬线取 p3：比参照语料最差的 3% 还差才算结构塌缩。"
            "依据见 quality/metrics.py:68-78 —— 用聚合值当单篇阈值会拦住参照书自己。",
            "standalone 与 chaptered 分开统计：标定短篇生成器该看 standalone。",
            "译本语料不要用来定 attr_adv_pct / sent_len_mean 这类文风维度"
            "（见 corpus.NATIVE_KEYS 的实测对照）。",
        ],
    }
    return out


def suggest_targets(baseline: dict, *, section: str = "standalone") -> dict:
    """从分布推出 profile 的 `[targets]` 建议值。

    只是**建议**，不自动写进 toml —— 阈值是要人看过才算数的，
    而且题材/文风两类维度该取自不同语料（见 GENRE_KEYS / NATIVE_KEYS）。
    软区间取 p10~p90，硬线取 p3（下限型）或 p90 外推（上限型）。
    """
    d = baseline.get(section) or {}
    # 「低于则拦」的指标。与 metrics.structural_reasons:227 的约定一致。
    LOWER = {"dialogue_chars_pct", "dialogue_run_mean"}
    SKIP = {"chars", "paragraphs", "scene_len_mean", "dialogue_run_max", "scenes"}
    out = {}
    for k, v in d.items():
        if k in SKIP:
            continue
        pct = k.endswith("_pct")       # 百分比指标，上限不能超过 100
        rec: dict = {"lo": v["p10"], "hi": v["p90"],
                     "native": k in NATIVE_KEYS}
        if k in LOWER:
            rec["hard"] = v["p3"]
            # p3 退化成 0 时硬线等于不存在。实测起因是语料里混用引号导致
            # 个别篇目的对话被读成 0%（见 _normalize 的注释）——归一化之后
            # 还退化的话，就是语料里真有不含对话的篇目，该由人决定怎么办。
            if rec["hard"] <= 0 < v["p10"]:
                rec["hard"] = round(v["p10"] * 0.3, 1)
                rec["warn"] = (f"p3={v['p3']} 退化（语料里有该指标为 0 的篇目），"
                               f"已改用 p10×0.3 作为硬线建议，请人工确认")
        else:
            # 上限型：硬线放到 p90 之外，只抓真塌缩
            hard = max(v["p90"] * 1.5, v["max"] * 0.9)
            if pct:
                # 百分比不能建议出 >100 的硬线 —— 那等于不拦。
                # 实测踩过：dialogue_para_pct 的 p90×1.5 算出 115.5。
                if hard >= 100:
                    hard = min(99.0, max(v["p90"] + 10, v["max"]))
                    rec["warn"] = (f"p90×1.5 超过 100%，已收到 {hard}；"
                                   f"百分比指标的上限硬线本来就意义不大，"
                                   f"可以考虑不设")
            rec["hard"] = round(hard, 1)
        out[k] = rec
    return out


def render_report(b: dict) -> str:
    lines = [f"# {b['profile']} 参考语料基线", "",
             f"生成于 {b['generated_at']}　最小单元 {b['min_chars']} 字", "",
             "## 语料", "", "| 文件 | 大小 | 单元数 | 字数 | sha256 |",
             "|---|---|---|---|---|"]
    for s in b["sources"]:
        lines.append(f"| {s['file']} | {s['bytes']:,} | {s['pieces']} | "
                     f"{s['chars']:,} | `{s['sha256'][:12]}…` |")
    lines += ["", f"独立短篇 **{b['counts']['standalone']}** 篇 ｜ "
                  f"长篇分章 **{b['counts']['chaptered']}** 篇", ""]
    for sec, label in (("standalone", "独立短篇"), ("chaptered", "长篇分章")):
        d = b.get(sec)
        if not d:
            continue
        lines += [f"## {label} 的单篇分布", "",
                  "| 指标 | n | p3 | p10 | p50 | p90 | max | 维度 |",
                  "|---|---|---|---|---|---|---|---|"]
        for k in KEYS:
            v = d.get(k)
            if not v:
                continue
            tag = "文风⚠" if k in NATIVE_KEYS else ("结构" if k in GENRE_KEYS else "")
            lines.append(f"| `{k}` | {v['n']} | {v['p3']} | {v['p10']} | "
                         f"{v['p50']} | {v['p90']} | {v['max']} | {tag} |")
        lines.append("")
    lines += ["## 说明", ""] + [f"- {n}" for n in b["notes"]]
    lines.append("")
    lines.append("标「文风⚠」的维度：若本语料是译本，**不要**用它定这几项的阈值。")
    return "\n".join(lines) + "\n"


def write_baseline(corpus_dir: Path, *, min_chars: int = 1500) -> tuple[Path, Path]:
    b = build_baseline(corpus_dir, min_chars=min_chars)
    bj = corpus_dir / "baseline.json"
    bm = corpus_dir / "BASELINE.md"
    bj.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    bm.write_text(render_report(b), encoding="utf-8")
    return bj, bm
