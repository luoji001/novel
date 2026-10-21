"""上下文装配 —— 全项目唯一允许拼 prompt 的地方。

把它集中成一个模块是刻意的：24000 的上下文顶，只要有一处节点自己拼 prompt 并把
正文塞进去，就会静默超限。集中之后预算是可审计的。

分层预算（汉字数）：

| 层 | 内容 | 上限 |
|---|---|---|
| 全局（固定前缀，命中 prefix-caching） | 立意 + 人物卡 + 分歧轴 | 1200 |
| 章级 | 本章细纲 + 前 3 章摘要 | 900 |
| 场景级 | 本场 spec + 上一场末尾原文 | 700 |
| 禁止清单 | bans 回传 | 400 |

合计 ~3200 字 ≈ 5500 token，加上最大 max_tokens 4096 仍远低于 24000。
"""

from __future__ import annotations

from .quality.rules import CHAPTER_RE, to_cn

ANCHOR_MAX = 1200
CHAPTER_MAX = 900
SCENE_MAX = 700
BANS_MAX = 400


def tail_window(text: str, chars: int) -> str:
    """取正文尾部若干字，**剥掉章标题行**。

    必须剥：上游的教训是窗口里带标题 → 模型照抄标题，同一个标题被原封不动提了 7 次。
    """
    lines = [ln for ln in (text or "").splitlines()
             if not CHAPTER_RE.match(ln)]
    body = "\n".join(lines).strip()
    return body[-chars:] if len(body) > chars else body


def render_anchor(premise: dict | None, characters: list[dict] | None,
                  cast: dict[str, str] | None = None, *,
                  axis_name: str = "核心张力") -> str:
    """全局锚点。放在 prompt 最前面，内容固定 → 命中 vLLM 的 --enable-prefix-caching。

    `axis_name` 由 profile 决定：论辩体叫「核心分歧」，悬疑叫「核心谜题」，
    言情叫「关系张力」。叫法不对会把模型往错的方向推。
    """
    if not premise:
        return ""
    parts = [
        "【本篇设定】",
        f"故事：{premise.get('logline', '')}",
        f"背景：{premise.get('setting', '')}",
        f"{axis_name}：{premise.get('conflict_axis', '')}",
    ]
    objs = premise.get("concrete_objects") or []
    if objs:
        parts.append(f"贯穿物件：{'、'.join(objs[:6])}")

    # 人与机构/场所必须分开渲染。cast schema 的 key 枚举里 ORG 是机构、LOC 是
    # 场景（见 plan.py 的 cast prompt：「ORG 填机构/组织名，LOC 填主要场景名」），
    # 所以「教务处」「高三（2）班教室」出现在 cast 里是**对的**。
    # 错的是把它们和人排在同一个「· 名字｜角色｜主张：…｜手上有：…」列表里 ——
    # 那等于告诉模型教务处有主张、手上还拿着东西。
    # 实测后果：2701 个大纲章里 166 个（6.1%）把 ORG/LOC 列进了
    # 「本章必须开口的人」（如 speakers=['教务处','苏文远']）。
    # 顺带修掉一个截断 bug：原来统一取前 5 个，4 个人 + ORG + LOC 时
    # 会把一个**人**挤掉，而挤掉的是人、留下的是场所。
    people = [c for c in (characters or []) if c.get("key") not in ("ORG", "LOC")]
    places = [c for c in (characters or []) if c.get("key") in ("ORG", "LOC")]
    for c in people[:5]:
        bits = [c.get("name", "")]
        if c.get("role"):
            bits.append(c["role"])
        if c.get("stance"):
            bits.append(f"主张：{c['stance']}")
        if c.get("concrete"):
            bits.append(f"手上有：{c['concrete']}")
        parts.append("· " + "｜".join(b for b in bits if b))
    if places:
        parts.append("机构与场所（不是人，不会说话）："
                     + "、".join(c.get("name", "") for c in places[:3]
                                 if c.get("name")))
    out = "\n".join(parts)
    return out[:ANCHOR_MAX]


def render_chapter_context(beat: dict, summaries: dict[str, str], n: int, *,
                           unit: str = "章",
                           speaker_label: str = "必须开口的人") -> str:
    """章级上下文：本章要做的事 + 前 3 章摘要。

    **正文不进这里**，只有摘要。摘要是长期记忆的唯一载体 —— 上游的诊断是
    「摘要没信息量就等于没有长期记忆，这是打转的结构性成因」。

    `unit` 由 `profile.diction.unit` 决定：小说叫「章」，非虚构文章叫「节」。
    落盘的章标题仍是「第N章」（闸门机器依赖它），只有 prompt 里的叫法跟着文体变。

    `speaker_label` 同理。小说要的是「必须**开口**的人」—— 这条和 min_speakers
    是一对。非虚构档位换成「必须出场的当事方」：文章里的当事方是用来让机制落地的，
    让他开口就变成编对话了。
    """
    parts = [
        f"【第{to_cn(n)}{unit}任务】",
        f"要推进的事：{beat.get('beat', '')}",
        f"目标字数：{beat.get('target_chars', 0)} 字",
    ]
    if beat.get("must_object"):
        parts.append(f"本{unit}必须出现的物件：{beat['must_object']}")
    if beat.get("speakers"):
        parts.append(f"本{unit}{speaker_label}：{'、'.join(beat['speakers'][:4])}")

    prior = []
    for k in range(max(1, n - 3), n):
        s = summaries.get(str(k))
        if s:
            prior.append(f"第{to_cn(k)}{unit}：{s}")
    if prior:
        parts.append("【前情（只给摘要，不给原文）】\n" + "\n".join(prior))
    out = "\n".join(parts)
    return out[:CHAPTER_MAX]


def render_scene_context(spec: dict, prev_tail: str, total: int, *,
                         driver_name: str = "这一场要推进的事") -> str:
    """场景级上下文：本场契约 + 上一场末尾原文（衔接用）。

    `driver_name` 由 profile 决定（论题 / 线索 / 规则 / 关系变化 / 认知变化）。
    `driver` 字段兼容旧名 `question` —— 可插拔改造之前的 thread 用的是后者。
    """
    parts = [
        f"【本场（第 {spec.get('idx', 1)}/{total} 场）】",
        f"地点：{spec.get('place', '')}",
        f"在场：{'、'.join(spec.get('present') or [])}",
        f"{driver_name}：{spec.get('driver') or spec.get('question', '')}",
        f"出场时的变化：{spec.get('outcome', '')}",
        f"本场目标字数：{spec.get('target_chars', 600)} 字",
    ]
    if spec.get("entry_state"):
        parts.append(f"入场状态：{spec['entry_state']}")
    if prev_tail:
        parts.append(f"【上一场的结尾，接着往下写（不要重复这段）】\n{prev_tail}")
    out = "\n".join(parts)
    return out[:SCENE_MAX]


def render_bans(bans: dict | None) -> str:
    """拒因回传。

    这是上游自述的「v1 最大的设计缺陷」的修正：validate 算出了「重复的是哪句」
    「撞车的是哪个标题」，但只 print 到日志，从未进入下一轮 prompt。于是每次重试
    都是从同一个已塌缩的分布里再独立采一次样 —— 实测同一个标题被提了 7 次。
    """
    bans = bans or {}
    lines = []
    if bans.get("titles"):
        lines.append(f"· 这些标题不准再用：{'、'.join(bans['titles'][-8:])}")
    if bans.get("sentences"):
        quoted = "、".join(f"「{s[:20]}」" for s in bans["sentences"][-6:])
        lines.append(f"· 这些句子严禁再出现：{quoted}")
    if bans.get("templates"):
        quoted = "、".join(f"「{s}」" for s in bans["templates"][-8:])
        lines.append(f"· 这些套路句式本轮禁用：{quoted}")
    if not lines:
        return ""
    out = "【本轮禁止清单】（违反即判废重写）\n" + "\n".join(lines)
    return out[:BANS_MAX]
