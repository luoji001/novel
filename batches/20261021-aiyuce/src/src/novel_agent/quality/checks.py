"""组合校验与打分 —— 把 rules.py 的原语和 metrics.py 的结构指标组装成策略。

和计划里写的「全部放 rules.py」略有偏离：原语（正则、相似度、模板匹配）与
策略（哪些算硬拦、哪些算软警告、怎么合成总分）分开更好读，也方便单独测。

对上游 `validate_chapter` 的关键改造是**把标题问题单独成组**。上游把标题与正文
问题混在一个 reasons 列表里，调用方只能整章作废；book-01 的复盘显示标题类拦截
占全部拒因 36.7%（300 次），标注为「廉价可修」，但**实际救回 0 章**。
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from . import metrics as NM
from .rules import (
    CHAPTER_NUM_RE,
    TEMPLATE_RE,
    Gates,
    Verdict,
    chapter_blocks,
    chapter_title,
    cn2int,
    cos_sim,
    expand_blacklist,
    extract_title,
    sentence_duplicate_reasons,
    sim_ratio,
    template_reasons,
    title_blacklist_reasons,
    to_cn,
    _bigrams,
    _sentences,
)

_BLACKLIST_FILE = Path(__file__).with_name("blacklist.json")


@lru_cache(maxsize=8)
def load_blacklist(cast_key: str = "") -> dict:
    """读模板黑名单并按 cast 回代。文件缺失 = 功能静默关闭（不影响主流程）。

    cast_key 形如 "A=陆放,B=纪宛"，用字符串而非 dict 是为了能 lru_cache。
    """
    try:
        raw = json.loads(_BLACKLIST_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"templates": [], "dialogues": [], "title_words": []}
    cast = {}
    for part in (cast_key or "").split(","):
        if "=" in part:
            k, v = part.split("=", 1)
            if k.strip() and v.strip():
                cast[k.strip()] = v.strip()
    return expand_blacklist(raw, cast)


def hard_checks(chapter: str, n: int, prior_blocks: list[tuple[int, str]],
                g: Gates, *, target_chars: int | None = None,
                scale: str | None = None, targets: dict | None = None,
                cast: dict[str, str] | None = None) -> list[str]:
    """正文级硬拦 —— 只拦「结构性塌缩」和「复读」，这两类重写标题救不回来。

    章号检查放在这里而不是 title_checks：章号错是廉价可修的（retitle 会重写整行），
    但如果模型写的是**另一章的内容**，那是内容问题。保守起见归到硬拦，
    由调用方在 degraded 模式下决定是否放行。
    """
    reasons: list[str] = []

    # ① 章长。按本章 scale 的目标字数判，不用全局下限 ——
    #    上游 MIN_CHAPTER_LEN=200 的教训是：下限设得比实际产出还低，等于没有下限。
    #    这一条由 metrics.structural_reasons 内部处理（它拿 target_chars * min_ratio）。

    # ② 整章复读。degraded 模式下也必须拦，否则会把复读章写进小说。
    if prior_blocks:
        worst = max(sim_ratio(chapter, b) for _, b in prior_blocks)
        if worst >= g.sim_threshold:
            reasons.append(f"与历史章节相似度 {worst:.2f} ≥ {g.sim_threshold}（复读）")

    # ③ 句级重复（跨章逐字抄 / 章内自我复读）
    existing = "\n\n".join(b for _, b in prior_blocks)
    reasons.extend(sentence_duplicate_reasons(chapter, existing, g))

    # ④ 结构指标塌缩（对话归零 / 通篇心理活动 / 过短）。
    #    这是唯一的**肯定性**约束 —— 其余全是否定性的（别重复/别套话/别打转）。
    #    上游的教训：只有否定性约束时，模型会找到一个完美的局部最优 ——
    #    写短、写散、用叙述和心理活动填充，全部合法通过，但离目标形式很远。
    m = NM.chapter_metrics(chapter)
    s_hard, _ = NM.structural_reasons(m, target_chars=target_chars,
                                      targets=targets, min_ratio=g.min_ratio,
                                      scale=scale)
    reasons.extend(s_hard)
    return reasons


def title_checks(chapter: str, n: int, prior_titles: set[str], g: Gates,
                 blacklist: dict) -> list[str]:
    """标题级问题 —— 全部可以只重写一行字修掉。"""
    reasons: list[str] = []

    m = CHAPTER_NUM_RE.search(chapter or "")
    if m is None:
        reasons.append("缺少「第N章」标题")
    else:
        got = cn2int(m.group(1))
        if got != n:
            reasons.append(f"章号错误：应为第{to_cn(n)}章，实际第{to_cn(got)}章")

    title = extract_title(chapter)
    if not title:
        if m is not None:
            reasons.append("有章号但没有标题文本")
        return reasons

    if title in prior_titles:
        reasons.append(f"标题重复：「{title}」已存在")
    elif g.title_sim_max:
        # 近似重复。上游只判字面全等，漏得很厉害：book-02 写了 369 章，去近似后
        # 只剩 162 个实质不同的标题，最大的一簇占 46 章，全靠不全等溜过去。
        worst, ref = 0.0, ""
        for t in prior_titles:
            r = sim_ratio(title, t)
            if r > worst:
                worst, ref = r, t
        if worst >= g.title_sim_max:
            reasons.append(
                f"标题与《{ref}》近似 {worst:.2f} ≥ {g.title_sim_max}"
                f"（换个角度，别只换一个词）")

    reasons.extend(title_blacklist_reasons(title, blacklist))
    return reasons


def soft_checks(chapter: str, n: int, prior_blocks: list[tuple[int, str]],
                g: Gates, blacklist: dict, *, target_chars: int | None = None,
                scale: str | None = None, targets: dict | None = None,
                summary: str = "", prior_summaries: list[str] | None = None,
                cast: dict[str, str] | None = None) -> list[str]:
    """只记录不拦 —— 区间是审美目标，不该卡死生成。

    这些会写进 quality.jsonl 作为下一代调优依据，也会回传给模型当下一轮的禁止清单。
    """
    soft: list[str] = []

    if TEMPLATE_RE.search(chapter or ""):
        soft.append("命中套话收尾句")

    if blacklist:
        tpl, _ = template_reasons(chapter, blacklist, g)
        soft.extend(tpl)

    # 主题重合（原地打转）：与最近 3 章比 bigram 余弦。
    # 短篇没有「情节点 span」的概念（长篇里同一 beat 的几章本来就该同主题，
    # 上游为此加了 beat 感知的排除，否则 73% 的被拒轮次都是这个误伤），
    # 所以这里直接拿前 3 章比。
    if g.theme_max and prior_blocks:
        recent = [b for _, b in prior_blocks][-3:]
        ov = max(cos_sim(chapter, b, cast) for b in recent)
        if ov > g.theme_max:
            soft.append(f"主题与最近 3 章重合 {ov:.2f} > {g.theme_max}（原地打转）")

    # 情节重复：用摘要比。摘要就是情节的指纹，而且比拿正文两两算余弦便宜得多；
    # 上面那条只看最近 3 章，跨远距离的同质簇测不到。
    if summary and prior_summaries and g.plot_sim_max:
        worst, ref = 0.0, ""
        for s in prior_summaries:
            r = sim_ratio(summary, s)
            if r > worst:
                worst, ref = r, s
        if worst >= g.plot_sim_max:
            soft.append(f"情节与已写章节重复 {worst:.2f} ≥ {g.plot_sim_max}"
                        f"（撞上「{ref[:28]}…」）")

    m = NM.chapter_metrics(chapter)
    _, s_soft = NM.structural_reasons(m, target_chars=target_chars,
                                      targets=targets, min_ratio=g.min_ratio,
                                      scale=scale)
    soft.extend(s_soft)
    return soft


# 密度类维度。与 metrics.DENSITY_KEYS 对应 —— 闸门在 scale="short" 时豁免它们的硬线，
# 打分器必须用同一套口径豁免，否则就是上游踩过的那个坑的翻版：
# 「当时只给闸门加了排除、漏了打分器，结果第十章被闸门正确放行，却被打分器判成 23 分。
#  而 quality.jsonl 的分数是筛训练数据的依据，虚低分会把合格样本筛掉。」
# 实测（2026-10-18，参照书 51 章）：不豁免时 ch1 / ch45 的 interiority_score 为 0、
# ch51 的 run_score 为 42.9，而这三章正是刻意写成的结构标点章。
_DENSITY_DIMS = ("dialogue_score", "interiority_score", "run_score")

# 参与「短板门限」的维度。theme_score 刻意不在其中。
# 理由（实测）：参照书 51 章里有 7 章的 theme_score 落在 35~50，因为论辩体长篇全书
# 咬同一个论题，相邻章的 bigram 余弦天然 0.5+。把它纳入短板门限会把这 7 章判成
# 不及格 —— 而短篇只有 8~12 章、围着一个分歧轴，这个效应只会更强。
# 主题重合仍然在 soft_checks 里报警、在明细里记录，只是不单独决定综合分。
_SHORTFALL_DIMS = ("dup_score", "diversity_score", "rhythm_score",
                   "dialogue_score", "interiority_score", "run_score")
_AVERAGE_DIMS = _SHORTFALL_DIMS + ("theme_score",)

# 有硬发现时综合分的上限。
#
# **为什么需要这条。** 打分器和硬闸门是两套独立计算，口径差了约 80 倍：
# `dup_score = (1-dup_ratio)*100`，短板门限 60 —— 要重复率**超过 40%** 才会
# 触发；而硬闸门的 `sent_self_dup_max = 0`，一句逐字重复就判废。
# 实测后果（xiaoyuan-20261020-15，那一批**均分最高**的一本，90.6）：
#   第 1 章 dup_sentence_ratio=0.25（四分之一的句子是逐字重复）
#            → dup_score 75.0 → 没触发门限 → 综合分取均值 **92.3**
#   第 9 章 0.2462 → 90.0；第 4 章 0.1863 → 88.1
# 这不只是报告好看难看的问题：README 写了 quality.jsonl 的字段
# 「train/distill_insights.py 可直接吃」，拿这个分数筛 SFT 数据，
# 会把 echo 最严重的章当成最好的样本挑出来，等于主动训练复读。
#
# 只按 `hard` 加顶，不按 `title` —— 标题撞车是一行字的事，正文可能是好的，
# 那条路径由 retitle 负责（见 title_checks 的注释）。
HARD_SCORE_CAP = 40.0


def _band_score(v: float, lo: float, hi: float, hard: float | None) -> float:
    """按 profile 的软区间给一个指标打分。

    区间内满分；区间外朝**同一侧的硬线**线性衰减。那一侧没有硬线就把惩罚
    封在 60 分 —— 软区间是审美目标、硬线才是塌缩，「偏离审美」不该把综合分打死。

    这替掉了原来硬编码的归一化公式。那套公式的锚点来自《天幕红尘》的论辩体标定，
    用在别的题材上会系统性误判：实测 xuanyi 的一篇，心理活动 22.9%
    （该档位硬线 32%，闸门正确放行）被旧公式 `100-max(0,inner-4)*9` 算成 0 分。
    闸门说合格、打分器说 0 分 —— 和 scale 豁免那个坑是同一类错误，换了个维度。
    """
    if lo <= v <= hi:
        return 100.0
    if v < lo:
        floor = hard if (hard is not None and hard < lo) else None
        if floor is None:
            return max(60.0, 100.0 - (lo - v) / max(lo, 1e-9) * 40.0)
        if lo <= floor:
            return 100.0
        return max(0.0, min(100.0, (v - floor) / (lo - floor) * 100.0))
    ceil = hard if (hard is not None and hard > hi) else None
    if ceil is None:
        return max(60.0, 100.0 - (v - hi) / max(hi, 1e-9) * 40.0)
    if ceil <= hi:
        return 100.0
    return max(0.0, min(100.0, (ceil - v) / (ceil - hi) * 100.0))


def score_text(text: str, prior_texts: list[str], *,
               cast: dict[str, str] | None = None,
               scale: str | None = None,
               targets: dict | None = None) -> tuple[float | None, dict]:
    """规则式文学质量打分。返回 (综合分 0~100, 明细)。只评估、不拦截。

    综合分用**短板门限**而不是均值：dup_score 和 diversity_score 在短文本上
    结构性地恒接近 100，用均值会稀释任何新加的维度 —— 上游实测 theme_score 54.5
    被 dup 99.6 / diversity 99.9 拉到 85.8，于是「原地打转」一直在被放行。
    所以任一维度低于 60 就以它为准。

    `scale="short"` 时密度类维度退出短板门限（仍计入均值）—— 结构标点章
    （冷开场、转折、收束）本来就不是论辩场，拿密度打它的分是在跟体裁打架。
    """
    d: dict = {}

    # ① 句级重复率：同一句话反复出现 = 啰嗦 / 复读
    sents = _sentences(text)
    if sents:
        dup = 1.0 - len(set(sents)) / len(sents)
        d["dup_sentence_ratio"] = round(dup, 4)
        d["dup_score"] = round((1.0 - dup) * 100, 1)

    # ② 词汇多样性：bigram 型例比
    bg = _bigrams(text)
    if bg:
        ttr = len(set(bg)) / len(bg)
        d["bigram_ttr"] = round(ttr, 4)
        d["diversity_score"] = round(min(1.0, ttr / 0.7) * 100, 1)

    # ③ 句长节奏：变异系数，越高越不单调
    lens = [len(s) for s in sents]
    if len(lens) >= 3:
        mean = sum(lens) / len(lens)
        sd = (sum((x - mean) ** 2 for x in lens) / len(lens)) ** 0.5
        cv = sd / mean if mean else 0.0
        d["sentlen_cv"] = round(cv, 4)
        d["rhythm_score"] = round(min(1.0, cv / 0.6) * 100, 1)

    # ④ 结构指标（对话占比、心理活动、对话 run）走 metrics.py，
    #    归一化锚点按参照书**单章**分布定，不用全书聚合（见 metrics.py:68-78）。
    m = NM.chapter_metrics(text)
    d.update({k: v for k, v in m.items() if k in
              ("dialogue_chars_pct", "interiority_para_pct", "dialogue_run_mean",
               "attr_adv_pct", "chars", "scenes")})

    # 三个密度维度按 **profile 的软区间** 归一化。
    # 给了 targets 就用它；没给就退回论辩体的老锚点（保持向后兼容）。
    T = targets or {}
    for metric, score_key, legacy in (
        ("dialogue_chars_pct", "dialogue_score",
         lambda v: next((sc for lo, sc in ((15, 25.0), (25, 50.0), (38, 75.0))
                         if v < lo),
                        100.0 if v <= 58 else 80.0 if v <= 70 else 55.0)),
        ("interiority_para_pct", "interiority_score",
         # 单章 p50 1.4 / p90 6.7：4% 以内满分，15% 归零
         lambda v: max(0.0, min(100.0, 100 - max(0, v - 4) * 9))),
        ("dialogue_run_mean", "run_score",
         # 单章 p10 3.7 / p50 6.7：4.5 段以上满分，1 段归零
         lambda v: max(0.0, min(100.0, (v - 1.0) / 3.5 * 100))),
    ):
        v = m.get(metric)
        if v is None or (metric == "dialogue_run_mean" and not v):
            continue
        band = T.get(metric)
        d[score_key] = round(_band_score(v, *band) if band else legacy(v), 1)

    # ⑤ 主题重合度
    recent = (prior_texts or [])[-3:]
    if recent:
        worst = max(cos_sim(text, b, cast) for b in recent)
        d["theme_overlap"] = round(worst, 4)
        d["theme_score"] = round((1.0 - worst) * 100, 1)

    shortfall_keys = tuple(k for k in _SHORTFALL_DIMS
                           if not (scale == "short" and k in _DENSITY_DIMS))
    avg = [d[k] for k in _AVERAGE_DIMS if k in d]
    if not avg:
        return None, d
    sub = [d[k] for k in shortfall_keys if k in d]
    mean = sum(avg) / len(avg)
    if sub:
        worst = min(sub)
        composite = round(worst if worst < 60 else mean, 1)
        d["worst_dim"] = next((k for k in shortfall_keys if d.get(k) == worst), None)
    else:
        composite = round(mean, 1)
    return composite, d


def validate(chapter: str, n: int, prior_chapters: dict[int, str], g: Gates,
             *, target_chars: int | None = None, scale: str | None = None,
             targets: dict | None = None, cast: dict[str, str] | None = None,
             summary: str = "", prior_summaries: list[str] | None = None,
             attempts: int = 0) -> Verdict:
    """完整校验。`attempts >= g.degrade_after` 时进 degraded 模式。

    degraded 的意思是止损：只保留「结构性塌缩」和「整章复读」两类硬错，其余降级为
    警告。book-01 曾为 11 章产出烧掉 157 轮被丢弃的生成，不能再这样。
    """
    prior_blocks = sorted(((k, v) for k, v in (prior_chapters or {}).items()
                           if k != n), key=lambda x: x[0])
    prior_titles = {t for _, b in prior_blocks
                    for ln in b.splitlines()[:1]
                    if (t := chapter_title(ln))}
    cast_key = ",".join(f"{k}={v}" for k, v in sorted((cast or {}).items()))
    blacklist = load_blacklist(cast_key)

    hard = hard_checks(chapter, n, prior_blocks, g, target_chars=target_chars,
                       scale=scale, targets=targets, cast=cast)
    title = title_checks(chapter, n, prior_titles, g, blacklist)
    soft = soft_checks(chapter, n, prior_blocks, g, blacklist,
                       target_chars=target_chars, scale=scale, targets=targets,
                       summary=summary, prior_summaries=prior_summaries, cast=cast)

    degraded = attempts >= g.degrade_after
    if degraded:
        # 止损：复读与结构塌缩仍拦，其余（含全部标题问题）降级
        soft = soft + [f"[degraded] {r}" for r in title]
        title = []

    score, detail = score_text(chapter, [b for _, b in prior_blocks],
                               cast=cast, scale=scale, targets=targets)
    # 硬发现给综合分加顶（见 HARD_SCORE_CAP）。**与闸门模式无关** ——
    # observe 只决定要不要拦，不该让分数撒谎：分数是筛训练数据的依据，
    # 而 observe 模式恰恰是批量产数据的那个模式。原始分留在明细里，
    # 标定时要看的分布是它。
    if hard and score is not None:
        detail["score_raw"] = score
        detail["hard_capped"] = True
        # 压到上限之下，但**保留次序**。直接 min() 会把所有带硬发现的章压成
        # 同一个 40.0，而这个分数的首要用途是筛训练数据 —— 那需要的是排序，
        # 不是一个标记位（标记位已经有 hard_capped 了）。
        # 实测 fixcheck-01：ch3（自我复读 1 句，raw 93.7）与 ch6（复读 9 句
        # ＋标题撞车，raw 89.7）在 min() 下都变成 40.0，轻重分不出来。
        score = round(HARD_SCORE_CAP * score / 100.0, 1)
    return Verdict(hard=hard, title=title, soft=soft, metrics=detail, score=score)
