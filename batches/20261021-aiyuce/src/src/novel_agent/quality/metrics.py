#!/usr/bin/env python3
"""小说结构指标 —— 生成侧与评测侧共用的唯一定义。

为什么要单独一个模块：循环里「拦」和 compare_to_baseline.py 里「量」如果各写一套
正则，两边的数就会悄悄对不上，于是「校验通过」和「指标达标」变成两件事。
所有结构指标只在这里定义一次。

基线来自《天幕红尘》(豆豆) 51 章 / 277,410 字的实测，
推导过程见 train/data/books/tianmu-hongchen/PATTERNS.md。
"""

import re
import statistics as st

# ---------- 文本切分 ----------
# 章标题行：### 第N章：标题 / 第N章 标题
CHAPTER_LINE = re.compile(r"^#{0,3}\s*第\s*[0-9零一二三四五六七八九十百千两]+\s*章")
# 对话跨度。兼容全角双引号与直角引号（两本书分别在用）
QUOTE_RAW = re.compile(r"[“「][^”」]*[”」]")
QUOTE_INNER = re.compile(r"[“「]([^”」]*)[”」]")
SENT_END = re.compile(r"[。！？…]+")

# 归属句：「X说：“…」/「”X说」。只统计动词，人名交给调用方的 cast
SAY_VERBS = "说道问答讲叫喊笑补充解释反问追问插话接话打断"
ATTR_ANY = re.compile(rf"[一-龥]{{2,4}}[{SAY_VERBS}][：:，,]?\s*[“「]")
ATTR_AFTER = re.compile(rf"[”」]\s*[一-龥]{{2,4}}[{SAY_VERBS}]")
# 「说」要同时数引号前与引号后两种形式。只数引号前的话分子缺一半，
# 而分母 ATTR_ANY+ATTR_AFTER 是两种都数的 —— 这个不对称会把占比压到实际的六成。
ATTR_SAY = re.compile(r"[一-龥]{2,4}说[：:，,]?\s*[“「]")
ATTR_SAY_AFTER = re.compile(r"[”」]\s*[一-龥]{2,4}说")
# 情绪副词归属：「冷冷地说」「无奈地问」
ATTR_ADV = re.compile(r"[一-龥]{1,4}地(说|问|道)")

# 心理活动标记。这批词是判定「段落在写想法而不是写事」的依据
INNER = re.compile(r"(想|觉得|心里|心中|明白|意识到|琢磨|纳闷|纠结|仿佛|似乎|回想)")

# 场景切换：时间或地点标记。与 PATTERNS.md 第 4 节同一套
TIME_MARK = re.compile(
    r"(第二天|次日|当天|当晚|这天|那天|几天后|一周后|不久|随后|过了?[一两三几]+"
    r"[天周月年小时分钟]|上午|下午|中午|傍晚|晚上|深夜|凌晨|天亮|清晨)")
PLACE_MARK = re.compile(
    r"(到了?|来到|走进|进了?|回到|坐在|站在|离开|出了?)[一-龥]{0,10}?"
    r"(房间|屋里|客厅|办公室|车间|厂区|会议室|食堂|仓库|饭店|餐厅|咖啡|宾馆|酒店|"
    r"机场|家里|楼下|门口|车里|工位|产线|库房|门卫|医院|病房)")

# ---------- 《天幕红尘》实测基线 ----------
BASELINE = {
    "chapter_chars_mean": 5439,
    "chapter_chars_median": 5172,
    "chapter_chars_cv": 0.52,
    "paragraphs_mean": 101.1,
    "dialogue_chars_pct": 51.8,
    "dialogue_para_pct": 77.4,
    "interiority_para_pct": 1.9,
    "narration_para_pct": 20.7,
    "turn_len_median": 16,
    "turn_under20_pct": 56.6,
    "turn_over200_pct": 2.0,
    "attr_say_pct": 79.0,
    "attr_adv_pct": 3.6,
    "scenes_per_chapter": 5.2,
    "dialogue_run_mean": 6.6,
}

# ---------- book-03 的目标区间 ----------
# 格式：(软下限, 软上限, 硬拦线)。软区间只打印警告，硬线才拦截重采。
#
# ⚠ 硬线的标定基准（2026-10-07 修正，这里踩过一次坑）：
# 第一版把**全书聚合值**直接当成单章阈值（心理活动 >5% 拦、副词归属 >6% 拦、
# 对话 run <4 拦），结果拿《天幕红尘》自己的第 5 章去测，三条全被拦了 ——
# 参照书的真章过不了以它为蓝本定的闸门，闸门就是错的，只会白烧算力。
# 原因是单章方差远大于全书聚合。实测 51 章的单章分布：
#   interiority_para_pct  p50 1.4  p90 6.7  p95 8.7  max 27.3
#   attr_adv_pct          p50 3.3  p90 8.3  p95 11.6 max 13.1
#   dialogue_run_mean     p5 2.5   p10 3.7  p50 6.7  max 21
#   dialogue_chars_pct    p5 25.8  p10 34.4 p50 53.3
# 所以硬线改成按**单章分布的 p3 左右**定：比参照书最差的 3% 还差才算塌缩。
# 审美目标（想要的样子）一律放软区间 —— 它该经常响，但不该卡死生成。
TARGETS = {
    "dialogue_chars_pct": (38.0, 58.0, 20.0),
    "interiority_para_pct": (0.0, 6.0, 15.0),
    "narration_para_pct": (10.0, 40.0, None),
    "turn_under20_pct": (45.0, 72.0, None),
    "attr_say_pct": (70.0, 100.0, None),
    "attr_adv_pct": (0.0, 8.0, 15.0),
    "dialogue_run_mean": (3.5, 10.0, 1.8),
}


def strip_title(text):
    """去掉章标题行，返回正文段落列表。"""
    lines = [ln for ln in text.splitlines() if not CHAPTER_LINE.match(ln.strip())]
    return [ln.strip() for ln in lines if ln.strip()]


def classify_para(p):
    """段落类型：dialogue_pure / dialogue_tagged / interiority / narration。

    判定顺序要紧：先看有没有对话。一段话只要带了引号就算对话段，
    哪怕它同时含「觉得」—— 否则对话段会被误计成心理段。
    """
    q = sum(len(m) for m in QUOTE_RAW.findall(p))
    if q == 0:
        return "interiority" if INNER.search(p) else "narration"
    return "dialogue_pure" if q / len(p) > 0.85 else "dialogue_tagged"


def count_scenes(paras):
    """按时空标记切场景，返回 (场景数, 各场段数)。"""
    if not paras:
        return 0, []
    breaks = [0] + [i for i, p in enumerate(paras)
                    if i and (TIME_MARK.search(p[:25]) or PLACE_MARK.search(p[:40]))]
    breaks.append(len(paras))
    lens = [breaks[i + 1] - breaks[i] for i in range(len(breaks) - 1)]
    lens = [x for x in lens if x > 0]
    return len(lens), lens


def dialogue_runs(paras):
    """连续对话段的 run 长度列表。衡量论辩是否接得上，还是一问一答就断。"""
    runs, run = [], 0
    for p in paras:
        if classify_para(p).startswith("dialogue"):
            run += 1
        else:
            if run:
                runs.append(run)
            run = 0
    if run:
        runs.append(run)
    return runs


def chapter_metrics(text):
    """单章全部结构指标。text 可含标题行。"""
    paras = strip_title(text)
    body = "\n".join(paras)
    n = len(body.replace("\n", ""))
    m = {"chars": n, "paragraphs": len(paras)}
    if not paras or not n:
        return m

    types = [classify_para(p) for p in paras]
    tp = len(types)
    dq = sum(len(q) for q in QUOTE_RAW.findall(body))
    m["dialogue_chars_pct"] = round(100 * dq / n, 1)
    m["dialogue_para_pct"] = round(
        100 * sum(1 for t in types if t.startswith("dialogue")) / tp, 1)
    m["interiority_para_pct"] = round(
        100 * sum(1 for t in types if t == "interiority") / tp, 1)
    m["narration_para_pct"] = round(
        100 * sum(1 for t in types if t == "narration") / tp, 1)

    turns = [len(q) for q in QUOTE_INNER.findall(body)]
    m["turns"] = len(turns)
    if turns:
        m["turn_len_median"] = round(st.median(turns))
        m["turn_len_mean"] = round(st.mean(turns), 1)
        m["turn_len_max"] = max(turns)
        m["turn_under20_pct"] = round(100 * sum(1 for t in turns if t < 20) / len(turns), 1)
        m["turn_over200_pct"] = round(100 * sum(1 for t in turns if t > 200) / len(turns), 1)

    attr = len(ATTR_ANY.findall(body)) + len(ATTR_AFTER.findall(body))
    m["attributions"] = attr
    if attr:
        say = len(ATTR_SAY.findall(body)) + len(ATTR_SAY_AFTER.findall(body))
        m["attr_say_pct"] = round(100 * say / attr, 1)
        m["attr_adv_pct"] = round(100 * len(ATTR_ADV.findall(body)) / attr, 1)

    sc, sl = count_scenes(paras)
    m["scenes"] = sc
    m["scene_len_mean"] = round(st.mean(sl), 1) if sl else 0

    runs = dialogue_runs(paras)
    m["dialogue_run_mean"] = round(st.mean(runs), 1) if runs else 0.0
    m["dialogue_run_max"] = max(runs) if runs else 0

    sents = [s for s in SENT_END.split(body) if len(s.strip()) > 1]
    if sents:
        lens = [len(s) for s in sents]
        m["sent_len_mean"] = round(st.mean(lens), 1)
        m["sentences"] = len(sents)
    return m


#《天幕红尘》里只讲叙述不讲对话的「结构标点」章：ch1 冷开场、ch17/28/45/50/51
# 转折与收束。这些章对话占比低到 1.6%、心理活动高到 27.3%，是刻意的，不是塌缩。
# 所以 short 档位豁免对话密度类硬线 —— 闸门必须能表达「这章本来就不是论辩场」，
# 否则它会精确地拦掉参照书写得最好的那几章。
DENSITY_KEYS = ("dialogue_chars_pct", "dialogue_run_mean", "interiority_para_pct")


def structural_reasons(m, target_chars=None, targets=None, min_ratio=0.55,
                       scale=None):
    """按目标区间产出 (硬拦原因, 软警告)。

    硬拦只用于「结构性塌缩」——写得太短、几乎没有对话、通篇心理活动。
    偏离区间但没触硬线的，一律降为软警告：区间是审美目标，不该卡死生成。

    scale  本章档位。"short" 时对话密度类指标只警告不拦（见 DENSITY_KEYS）。

    min_ratio 默认 0.55 而不是 0.7：参照书单章字数围绕任一目标值散得很宽，
    卡 0.7 会把「目标 5200、实写 3600」这种完全正常的章拦掉。
    0.55 仍然能抓住 book-02 那种 567 字（目标的 11%）的真塌缩。
    """
    T = targets or TARGETS
    hard, soft = [], []

    # 章长：按本章 scale 的目标字数判，不用全局下限。
    # 全局 MIN_CHAPTER_LEN=200 的教训是——下限设得比实际产出还低，等于没有下限。
    if target_chars:
        floor = int(target_chars * min_ratio)
        if m.get("chars", 0) < floor:
            hard.append(f"章节过短 {m.get('chars',0)} < {floor}"
                        f"（本章目标 {target_chars} 字的 {min_ratio:.0%}）")

    for key, (lo, hi, hard_line) in T.items():
        v = m.get(key)
        if v is None:
            continue
        # short 档位是结构标点章，允许整章没有对话 —— 密度类指标降为软警告
        if scale == "short" and key in DENSITY_KEYS:
            hard_line = None
        # 硬线方向：对话占比和 run 是「低于则拦」，心理活动和副词是「高于则拦」
        if hard_line is not None:
            if key in ("dialogue_chars_pct", "dialogue_run_mean"):
                if v < hard_line:
                    hard.append(f"{key} {v} < {hard_line}（结构塌缩）")
                    continue
            elif v > hard_line:
                hard.append(f"{key} {v} > {hard_line}（结构塌缩）")
                continue
        if v < lo:
            soft.append(f"{key} {v} 低于目标 {lo}")
        elif v > hi:
            soft.append(f"{key} {v} 高于目标 {hi}")
    return hard, soft


def book_metrics(chapters):
    """整书汇总。chapters = [章正文, ...]。用于 compare_to_baseline。"""
    per = [chapter_metrics(c) for c in chapters]
    lens = [p["chars"] for p in per if p.get("chars")]
    agg = {"chapters": len(per), "total_chars": sum(lens)}
    if lens:
        agg["chapter_chars_mean"] = round(st.mean(lens))
        agg["chapter_chars_median"] = round(st.median(lens))
        agg["chapter_chars_cv"] = round(st.stdev(lens) / st.mean(lens), 2) if len(lens) > 1 else 0.0
    agg["paragraphs_mean"] = round(st.mean([p["paragraphs"] for p in per]), 1) if per else 0

    # 占比类指标按全书重算，而不是对各章的百分比取平均 ——
    # 章长差 6 倍时，平均百分比会把短章的权重放大。
    def wavg(key, weight="chars"):
        num = sum(p.get(key, 0) * p.get(weight, 0) for p in per if key in p)
        den = sum(p.get(weight, 0) for p in per if key in p)
        return round(num / den, 1) if den else 0.0

    for k in ("dialogue_chars_pct", "dialogue_para_pct", "interiority_para_pct",
              "narration_para_pct", "turn_under20_pct", "turn_over200_pct",
              "attr_say_pct", "attr_adv_pct"):
        agg[k] = wavg(k)
    for k in ("scenes", "dialogue_run_mean"):
        vals = [p[k] for p in per if p.get(k)]
        agg["scenes_per_chapter" if k == "scenes" else k] = (
            round(st.mean(vals), 1) if vals else 0.0)
    med = [p["turn_len_median"] for p in per if p.get("turn_len_median")]
    agg["turn_len_median"] = round(st.median(med)) if med else 0
    return agg, per
