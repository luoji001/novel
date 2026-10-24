"""规则式校验与打分 —— 纯函数，不调 LLM、不读环境变量、不碰磁盘。

移植自 /mnt/c/code/scripts/novel/openclaw-novel-loop（见 VENDOR.md）。
相对上游的三处改造：

1. **阈值全部参数化**：上游在模块加载时读 NOVEL_LOOP_* 环境变量，这里改成由
   `Gates` 从 profiles/*.toml 注入。目的是让同一套规则能服务不同题材 —— 上游
   把《天幕红尘》的论辩口径写死在模块级，换题材就得改代码。
2. **`_CAST` 从模块全局变成参数**：占位符回代（‹A›→陆放）是每部作品不同的，
   不该是进程级状态。
3. **`validate_chapter` 拆成三组**：`hard_checks` / `title_checks` / `soft_checks`。
   上游把标题问题和结构问题混在同一个 reasons 列表里，调用方只能整章作废；
   book-01 的复盘显示标题类拦截占全部拒因的 36.7%（300 次）却「实际救回 0 章」。
   拆开之后，只有标题出问题的章可以走廉价的 retitle 路径，正文原样保留。
"""

from __future__ import annotations

import difflib
import math
import re
from collections import Counter
from dataclasses import dataclass, field

# ---------- 章节标题 ----------
# 同时认 Markdown 与纯文本标题
CHAPTER_RE = re.compile(r"^\s*[#>*\-\s]*第\s*([0-9零一二三四五六七八九十百千两]+)\s*章")
CHAPTER_NUM_RE = re.compile(r"第\s*([0-9零一二三四五六七八九十百千两]+)\s*章")

# 套话收尾 / 自我指涉式坍缩句（上游 2026-10-04 收紧版，原样搬运）
TEMPLATE_RE = re.compile(
    r"(?:他们的?|他的|她的|它的)(?:故事|旅程|冒险|传说|征程)[，,]?\s*"
    r"(?:才|仍|依然|还|永远|正|将|正在)?\s*在?\s*(?:刚刚|只|不过|才)?\s*(?:是)?\s*"
    r"(?:开始|继续|继续书写|延续|未完)"
    r"|(?:故事|旅程|冒险|传说|征程)[，,]?\s*(?:才|仍|依然|还|永远|将)\s*在?\s*(?:刚刚)?\s*(?:开始|继续|延续)"
    r"|将继续书写下去|依然继续|仍在继续|还在继续|依然在继续"
    r"|(?:(?<![他她它我你])这|这一切)[，,]?\s*(?:才|只|不过)?\s*(?:是)?\s*(?:一个|刚刚)?\s*开始"
    r"|至此结束|新的轮回|命运的重演|未完待续")

CN_DIGITS = {"零": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4,
             "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
CN_UNITS = {"十": 10, "百": 100, "千": 1000}
CN_NUM = "零一二三四五六七八九"

SENT_SPLIT = re.compile(r"[。！？!?；;\n]+")
QUOTE_SPAN = re.compile(r"[「『“]([^」』”]*)[」』”]")
PUNCT = set("，。！？；：、…—～·《》〈〉（）【】[]「」『』“”‘’ \t\n\r")

DUP_SPLIT = re.compile(r"[。！？!?…\n]+")
DUP_DIALOG = re.compile(r"[「『“]([^」』”]+)[」』”]")
DUP_STRIP = "「」『』“”‘’，,：:；;、 \t\r"

# 归属脚手架：人名 + 说话动词。用于主题重合的归一化（上游 2026-10-07 加）。
# 起因：把 attr_say_pct 推到 81%（《天幕红尘》的目标形式）之后，每章重复出现上百次
# 相同的归属 bigram，于是 bigram 余弦把「被强制统一的形式」算成了「主题重合」。
# 实测形式贡献了 0.11 的虚高。主题重合要测情节有没有推进，人名和说话动词不含这个信息。
ATTR_SCAFFOLD = re.compile(r"[一-龥]{2,4}(?:说|问|道|答|笑|喊|叫)[：:，,]?")

# 裸归属句形态（”X说 / X问道）。这类骨架必须从模板黑名单里剔除 —— 上游 2026-10-07
# 的教训：book-03 第一章被「”陆放说 ×31」判套路密度超限拦掉，而《天幕红尘》有 2127 次
# 裸「说」归属（占 79%，约 42 次/章）。两条规则对着拉，模型的解法是干脆不归属，
# 写成无归属的对话乒乓。裸归属是标点性脚手架，不是文风套路。
# 只豁免**裸**形式：「冷冷地说」这类带情绪副词的仍然要拦。
BARE_ATTR_RE = re.compile(r"^[”」]?[‹›A-Za-z一-龥]{1,4}(说|问|道|答|说道|问道)$")


@dataclass(frozen=True)
class Gates:
    """校验阈值。由 profiles/*.toml 的 [gates] 节注入。"""
    min_ratio: float = 0.55
    sim_threshold: float = 0.90
    theme_max: float = 0.58
    title_sim_max: float = 0.60
    plot_sim_max: float = 0.55
    tpl_per_kilo: float = 16.0
    tpl_single_max: int = 2
    sent_dup_min_len: int = 10
    sent_dup_max: int = 2
    sent_self_dup_max: int = 0
    degrade_after: int = 3


@dataclass
class Verdict:
    """一次校验的结果。

    `title_only` 是驱动廉价修复路径的关键：正文全部合格、只有标题出问题时，
    调用方应该只重新生成标题行，而不是把整章丢掉重写。
    """
    hard: list[str] = field(default_factory=list)      # 正文级硬拦
    title: list[str] = field(default_factory=list)     # 标题级问题（廉价可修）
    soft: list[str] = field(default_factory=list)      # 只记录不拦
    metrics: dict = field(default_factory=dict)
    score: float | None = None

    @property
    def ok(self) -> bool:
        return not self.hard and not self.title

    @property
    def title_only(self) -> bool:
        return bool(self.title) and not self.hard


# ---------- 中文数字 ----------
def cn2int(s: str | None) -> int | None:
    """中文数字 / 阿拉伯数字 → int；无法解析返回 None。"""
    s = (s or "").strip()
    if not s:
        return None
    if s.isdigit():
        return int(s)
    total, num = 0, 0
    for ch in s:
        if ch in CN_DIGITS:
            num = CN_DIGITS[ch]
        elif ch in CN_UNITS:
            total += (num or 1) * CN_UNITS[ch]
            num = 0
        else:
            return None
    return total + num


def to_cn(n: int | None) -> str:
    """int → 中文数字（1~9999）。"""
    if n is None or n <= 0:
        return str(n)
    if n < 10:
        return CN_NUM[n]
    if n < 20:
        return "十" + (CN_NUM[n % 10] if n % 10 else "")
    if n < 100:
        return CN_NUM[n // 10] + "十" + (CN_NUM[n % 10] if n % 10 else "")
    if n < 1000:
        s = CN_NUM[n // 100] + "百"
        r = n % 100
        if r == 0:
            return s
        return s + ("零" + CN_NUM[r] if r < 10 else to_cn(r))
    if n < 10000:
        s = CN_NUM[n // 1000] + "千"
        r = n % 1000
        if r == 0:
            return s
        return s + ("零" + to_cn(r) if r < 100 else to_cn(r))
    return str(n)


# ---------- 文本切分 ----------
def chapter_blocks(text: str) -> list[tuple[int, str]]:
    """返回 [(章号, 章块全文), ...]；块长度 > 30 才计入，跳过空标题。"""
    lines = (text or "").splitlines()
    marks = []
    for i, ln in enumerate(lines):
        m = CHAPTER_RE.match(ln)
        if m:
            marks.append((i, cn2int(m.group(1))))
    out = []
    for k, (i, num) in enumerate(marks):
        end = marks[k + 1][0] if k + 1 < len(marks) else len(lines)
        blk = "\n".join(lines[i:end]).strip()
        if num is not None and len(blk) > 30:
            out.append((num, blk))
    return out


def chapter_title(ln: str) -> str | None:
    """从标题行取「第N章」之后的标题文本；无标题返回 None。"""
    m = CHAPTER_RE.match(ln)
    if not m:
        return None
    return ln[m.end():].strip().lstrip("：:，,、.。 \t").strip()


def extract_title(chapter: str) -> str | None:
    """取章节正文里第一个标题行的标题文本。"""
    for ln in (chapter or "").splitlines():
        t = chapter_title(ln)
        if t:
            return t
    return None


def retitle(chapter: str, new_title: str, n: int) -> str:
    """替换标题行（没有标题行则补上），保留正文。

    用于标题层面的廉价修复：标题撞车、缺标题、章号写错 —— 这三类都只是一行字，
    正文往往是好的。实测基座约 1/3 的输出不给标题直接写正文，这时必须补标题
    而不是丢掉整章。
    """
    lines = (chapter or "").splitlines()
    for i, ln in enumerate(lines):
        if CHAPTER_RE.match(ln):
            prefix = "### " if ln.lstrip().startswith("#") else ""
            lines[i] = f"{prefix}第{to_cn(n)}章：{new_title}"
            return "\n".join(lines)
    return f"### 第{to_cn(n)}章：{new_title}\n" + (chapter or "").lstrip()


def normalize_prose(text: str) -> str:
    """把半角引号归一化成中文弯引号，顺带收拾省略号与破折号。

    **这不是锦上添花，是闸门能不能用的前提。** metrics.py 的 `QUOTE_RAW` /
    `QUOTE_SPAN` 只匹配 `[「『“]…[」』”]`，半角 `"` 一个都认不出来。

    实测（2026-10-18 首次真跑 4 章）：模型**时而用半角、时而用中文弯引号**。
    第 1 章全用半角，于是 `dialogue_chars_pct` 读成 0.0、`attributions` 读成 0 ——
    肉眼看那一章 60% 是对话。在 enforce 模式下它会被判「对话归零 / 结构塌缩」
    硬拦，而且每一章都可能这样，闸门的误拦率会接近 100%。
    第 2~4 章用的是中文引号，读数正常（58.2% / 63.6%）。
    间歇性比一贯性更难查，所以必须在入闸之前归一化。

    归一化同时也改善产出本身 —— 中文小说的行文规范就是用「」或“”。
    """
    t = text or ""
    # 成对切换：奇数次出现 → 开引号，偶数次 → 闭引号。按段落重置，
    # 这样某一段引号数为奇数时不会把后面所有段落的开闭关系全带偏。
    out_paras = []
    for para in t.split("\n"):
        buf, open_now = [], True
        for ch in para:
            if ch == '"':
                buf.append("“" if open_now else "”")
                open_now = not open_now
            else:
                # 单引号不动：它在中文里少见，而且可能是英文缩写的撇号，
                # 一律替换反而会改坏正文。
                buf.append(ch)
        out_paras.append("".join(buf))
    t = "\n".join(out_paras)
    t = t.replace("...", "……").replace("--", "——")
    return t


def sim_ratio(a: str, b: str) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in SENT_SPLIT.split(text or "") if len(s.strip()) >= 4]


def _bigrams(text: str) -> list[str]:
    chars = [c for c in (text or "") if c not in PUNCT]
    return [chars[i] + chars[i + 1] for i in range(len(chars) - 1)]


def _content_only(text: str, cast: dict[str, str] | None = None) -> str:
    """剔掉归属脚手架与本书人名，只留内容词，供主题重合比较用。

    不动 `_bigrams` 本身 —— 它还被 bigram_ttr（词汇多样性）使用，
    那个指标要的恰恰是包含全部用词的原始分布。
    """
    t = ATTR_SCAFFOLD.sub("", text or "")
    for v in (cast or {}).values():
        if v:
            t = t.replace(v, "")
    return t


def cos_sim(a: str, b: str, cast: dict[str, str] | None = None) -> float:
    """bigram 频率向量的余弦相似度：抓「措辞不同但主题/用词池相同」的主题重合。"""
    ca = Counter(_bigrams(_content_only(a, cast)))
    cb = Counter(_bigrams(_content_only(b, cast)))
    common = set(ca) & set(cb)
    if not common:
        return 0.0
    num = sum(ca[c] * cb[c] for c in common)
    da = math.sqrt(sum(v * v for v in ca.values()))
    db = math.sqrt(sum(v * v for v in cb.values()))
    return num / (da * db) if da and db else 0.0


# ---------- 句级重复 ----------
def _dup_units(text: str, min_len: int) -> tuple[list[str], list[str]]:
    """句级单元 → (句子列表, 对话列表)。两个列表分别独立比对，避免同一句台词被双重计数。

    对话单独成列表是为了抓住「同一句台词换个引语动词再说一遍」。
    """
    sents = []
    for s in DUP_SPLIT.split(text or ""):
        s = s.strip().strip(DUP_STRIP)
        if len(s) >= min_len:
            sents.append(s)
    dialogs = []
    for d in DUP_DIALOG.findall(text or ""):
        d = d.strip().strip(DUP_STRIP + "。")
        if len(d) >= min_len:
            dialogs.append(d)
    return sents, dialogs


def strip_echoed_prefix(text: str, prior: list[str]) -> tuple[str, int]:
    """剥掉开头那些已在 `prior` 里逐字出现过的段落。返回 (剩余正文, 被剥字数)。

    **为什么必须在代码里剥，而不是在 prompt 里要求。** 场景 prompt 给了
    「上一场的结尾」之后跟着一句「（不要重复这段）」—— 那是**负向禁止指令**，
    而本项目已经实测过 8B 不照办负向清单（见 nodes/plan.py 的模块注释：
    12 条「不准再争的论题」完全无效）。

    真跑证据（xiaoyuan-20261020-15 第 1 章第 2 场）：temp 0.85 与 1.00
    两路候选**都**以第 1 场全部 7 段的逐字副本开头，v1 的整个输出（383 字）
    就是那份副本、新内容 0 字。best-of-2 在这里不设防，因为两路同时抄。
    全语料 2701 章里 738 章带逐字重复段，xiaoyuan 占 39%。

    只剥**前缀**，不做全局去重：中段的逐字重复可能是刻意的回环（同一句台词
    在结尾再说一遍是正常写法），而开头的逐字复制只可能是 echo。
    """
    paras = [p for p in (text or "").split("\n\n")]
    seen = {q.strip() for t in (prior or []) for q in t.split("\n\n") if q.strip()}
    if not seen:
        return (text or "").strip(), 0

    def is_echo(s: str) -> bool:
        # 逐字整段命中，或是某个前段的**后缀** —— 后者是因为衔接窗口取的是
        # 「末尾若干字」，可能从段落中间切起，模型从那个切口开始抄。
        return s in seen or any(len(s) >= 12 and q.endswith(s) for q in seen)

    # 扫前缀。短段（<15 字）**跨过去而不停下** —— 实测 fixcheck-01 第 6 章：
    # 模型先吐了一句「到了。」（3 字）才开始抄，严格前缀扫描在那一句上停死，
    # 于是 6 段 164 字的逐字副本整块留了下来。
    # 只有在后面真的跟着 echo 时才会把短段一起剥掉（下面回退到 last_echo），
    # 所以不会误伤「以一句短句开场」这种正常写法。
    cut = last_echo = 0
    for i, p in enumerate(paras):
        s = p.strip()
        if not s:
            cut = i + 1
            continue
        if is_echo(s):
            cut = last_echo = i + 1
        elif len(s) < 15:
            cut = i + 1          # 暂且跨过，但不认它是 echo
        else:
            break
    # 回退到最后一个真 echo：中间跨过的短段只有在 echo 之前才跟着剥，
    # echo 之后的短段是新内容，必须留下。
    cut = last_echo
    if not cut:
        return (text or "").strip(), 0
    echoed = sum(len(p.strip()) for p in paras[:cut])
    return "\n\n".join(paras[cut:]).strip(), echoed


def strip_echoed_blocks(text: str, prior: list[str], min_run: int = 2
                        ) -> tuple[str, int]:
    """挖掉**夹在正文中间**的 echo 段块。返回 (剩余正文, 被挖字数)。

    `strip_echoed_prefix` 只管开头，但实测还有一种形态它按设计不该管：
    模型先写一段真的新开头，**再**整块抄上一场，然后接着往下写。
    fixcheck-02 第 6 章第 3 场就是这个样子 —— 第 0 段是 90 字的新内容，
    第 1~3 段是上一场的逐字副本，第 4 段起又是新的。前缀扫描在第 0 段
    正确地停下，于是那 132 字留在了成品里。

    **为什么敢挖中间：连续 ≥2 段逐字重复不可能是刻意的。** 单段重复可能是
    回环（同一句台词在结尾再说一遍是正常写法），所以 `min_run` 默认 2 ——
    这条线把「写法」和「复读」分开，不靠猜。

    全语料回放（17782 个候选）：前缀剥除拿掉 554,743 字之后，这条规则还能
    再拿掉 149,838 字（多 27%），命中 588 个候选（3.31%）。
    """
    seen = {q.strip() for t in (prior or []) for q in t.split("\n\n") if q.strip()}
    if not seen:
        return (text or "").strip(), 0
    paras = [p.strip() for p in (text or "").split("\n\n") if p.strip()]
    keep: list[str] = []
    echoed = 0
    i, n = 0, len(paras)
    while i < n:
        if paras[i] in seen:
            j = i
            while j < n and paras[j] in seen:
                j += 1
            if j - i >= min_run:
                echoed += sum(len(p) for p in paras[i:j])
            else:
                keep.extend(paras[i:j])          # 单段：留着，可能是回环
            i = j
        else:
            keep.append(paras[i])
            i += 1
    return "\n\n".join(keep).strip(), echoed


def sentence_duplicate_reasons(chapter: str, existing_text: str, g: Gates) -> list[str]:
    """句级重复检查。整句逐字复制是复读坍缩的早期信号 —— 整章相似度 0.90 太粗，
    只抄 2~3 句时抓不住，需要句级兜底。"""
    reasons: list[str] = []
    cs, cd = _dup_units(chapter, g.sent_dup_min_len)
    if not cs and not cd:
        return reasons
    # ① 章内自我复读：同一章里整句说两遍
    self_dup, example = 0, ""
    for units in (cs, cd):
        for u, k in Counter(units).items():
            if k >= 2:
                self_dup += 1
                if len(u) > len(example):
                    example = u
    if self_dup > g.sent_self_dup_max:
        reasons.append(f"章内自我复读 {self_dup} 句（如「{example[:24]}…」）")
    # ② 与历史章节逐字重复（句子、对话两个口径分别比对）
    es, ed = _dup_units(existing_text, g.sent_dup_min_len)
    dup, example2 = 0, ""
    for units, hist in ((cs, set(es)), (cd, set(ed))):
        for u in set(units):
            if u in hist:
                dup += 1
                if len(u) > len(example2):
                    example2 = u
    if dup > g.sent_dup_max:
        reasons.append(f"与历史章节逐字重复 {dup} 句（如「{example2[:24]}…」）")
    return reasons


# ---------- 句式骨架模板 ----------
def expand_blacklist(raw: dict, cast: dict[str, str] | None = None) -> dict:
    """把黑名单里的 ‹A›/‹B›/‹ORG›/‹LOC› 回代成本书人名，并过滤不可用骨架。

    为什么需要密度上限而不是一刀切禁止：「点了点头」「深吸一口气」是正常中文表达，
    全禁会让模型没法写字；只有扎堆出现才是模板化。
    """
    cast = cast or {}

    def expand(p: str) -> str:
        for k, v in cast.items():
            p = p.replace(f"‹{k}›", v)
        return p

    def usable(p: str, min_len: int) -> bool:
        # 太短会误伤；仍含未解析占位符的匹配不上正文；裸归属句见 BARE_ATTR_RE。
        return (len(p) >= min_len and "‹" not in p and "›" not in p
                and not BARE_ATTR_RE.match(p))

    tpl = []
    for key in ("sentence_templates", "opening_templates"):
        for it in raw.get(key) or []:
            p = expand(it.get("pattern") or "")
            if usable(p, 4):
                tpl.append({"pattern": p, "df": it.get("df", 0)})
    dlg = []
    for it in raw.get("dialogue_templates") or []:
        p = expand(it.get("pattern") or "")
        if usable(p, 3):
            dlg.append({"pattern": p, "df": it.get("df", 0)})
    # 同一骨架可能在两个来源里都有，按 df 降序去重
    seen, uniq = set(), []
    for it in sorted(tpl, key=lambda x: -x["df"]):
        if it["pattern"] not in seen:
            seen.add(it["pattern"])
            uniq.append(it)
    return {
        "templates": uniq,
        "dialogues": dlg,
        "title_words": [it.get("word") for it in (raw.get("title_words") or [])
                        if it.get("word")],
    }


def template_hits(text: str, blacklist: dict) -> list[tuple[str, int]]:
    """返回 [(骨架, 命中次数), ...]，按次数降序。

    用「不重叠的最长匹配」计数：黑名单里天然存在嵌套片段（「这个世界的」⊃「这个世界」
    ⊃「个世界的」），逐条 count 会把同一处文本计 3 次，密度虚高 2~3 倍。
    """
    body = re.sub(r"[，,、：:；;\s]", "", text or "")
    consumed = bytearray(len(body))
    hits: list[tuple[str, int]] = []
    for it in sorted(blacklist.get("templates") or [],
                     key=lambda x: -len(x["pattern"])):
        p = it["pattern"]
        c, start = 0, 0
        while True:
            i = body.find(p, start)
            if i < 0:
                break
            if not any(consumed[i:i + len(p)]):
                for k in range(i, i + len(p)):
                    consumed[k] = 1
                c += 1
            start = i + 1
        if c:
            hits.append((p, c))
    # 对白按原文匹配（含标点），与骨架各自独立计数
    for it in blacklist.get("dialogues") or []:
        c = (text or "").count(it["pattern"])
        if c:
            hits.append((it["pattern"], c))
    hits.sort(key=lambda x: -x[1])
    return hits


def template_reasons(text: str, blacklist: dict, g: Gates
                     ) -> tuple[list[str], list[tuple[str, int]]]:
    """模板骨架密度检查：返回 (原因列表, 命中明细)。"""
    hits = template_hits(text, blacklist)
    if not hits:
        return [], hits
    reasons = []
    total = sum(c for _, c in hits)
    per_kilo = total / max(1, len(text or "")) * 1000
    if per_kilo > g.tpl_per_kilo:
        top = "、".join(f"「{p}」×{c}" for p, c in hits[:3])
        reasons.append(f"套路句式密度 {per_kilo:.1f}/千字 > {g.tpl_per_kilo}（{top}）")
    heavy = [(p, c) for p, c in hits if c > g.tpl_single_max]
    if heavy:
        top = "、".join(f"「{p}」×{c}" for p, c in heavy[:3])
        reasons.append(f"单条套路句式超限：{top}")
    return reasons, hits


def title_blacklist_reasons(title: str, blacklist: dict) -> list[str]:
    """标题里的套路词。在**大纲阶段**就该跑这个，不要等正文写完才拦。"""
    bad = [w for w in (blacklist.get("title_words") or []) if w and w in (title or "")]
    return [f"标题含套路词：{'、'.join(f'「{w}」' for w in bad)}"] if bad else []
