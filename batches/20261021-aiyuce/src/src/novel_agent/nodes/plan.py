"""计划阶段：立意 → 人物卡 → 大纲 → 分场细纲。

这一阶段是本项目质量投入的重心。理由是硬约束：24000 上下文装不下 3 万字，
所以**全局一致性只能在计划层保证，不能靠「读完全文再改」**。
两个人工卡点都放在这里，正文阶段只做局部闸门与廉价修复。

**本模块不含任何题材假设。** schema 的字段描述、prompt 的具体要求、lint 的阈值，
全部来自 `profile.lang`（`config.SceneLang`）。最初版本把论辩体的「争」写死在这里，
结果所有题材都被掰成辩论，而且 `outline_lint` 硬查「每章 ≥2 人开口」会让单人视角、
书信体、独白体每章都报错。

**也不含文体假设。** 「小说」「人物」这两个词来自 `profile.diction`
（`config.Diction`）—— 非虚构档位把它们换成「文章」「当事方」。

实测教训（2026-10-18 真跑）：
  - 模型在大纲上的失败模式不是 JSON 格式，而是内容套路 —— schema 守得住，
    产出却是「困境初现／挣扎与抉择／转折与希望」+ 主角叫李明。
    解药是先逼出具体物，再让情节在具体物上长。
  - 8B **不照办负向禁止清单**。给分场 prompt 塞 12 条「这些论题已经争过，不准再争」
    完全无效，它照旧产出一字不差的同一个问题。改成正向局部约束（每章的驱动力锁死
    在它自己的 `must_object` 上，别章的物件列为禁区）之后，跨章重复 12 处 → 0 处。
"""

from __future__ import annotations

from .. import config as C
from .. import llm
from ..config import Profile, load_profile, plan_rhythm
from ..context import render_anchor
from ..quality.checks import load_blacklist
from ..quality.rules import sim_ratio, title_blacklist_reasons, to_cn


def _system(p: Profile) -> str:
    """结构化调用的 system。身份词按文体变（`profile.diction.editor`），其余通用。

    「具体可指认」「禁止抽象标签」两条跨文体都成立 —— 文章里的「前景广阔」
    和小说里的「命运」是同一个病：用标签代替可核查的东西。
    """
    return (f"你是{p.diction.editor}。只输出要求的结构化结果，不要解释、不要寒暄。"
            "一切设定必须具体可指认：具体的地方、具体的物件、具体的数目。"
            "禁止使用「命运」「觉醒」「新世界」「试炼」这类抽象标签。")


def _premise_schema(p: Profile) -> dict:
    return {
        "type": "object",
        "properties": {
            "logline": {"type": "string",
                        "description": "一句话故事，必须含具体的人、地方和处境"},
            "setting": {"type": "string",
                        "description": "年代、地点、环境，要具体到房间/街道/科室"},
            "conflict_axis": {"type": "string", "description": p.lang.axis_desc},
            "concrete_objects": {"type": "array", "items": {"type": "string"},
                                 "description": "贯穿全篇的 3-5 个具体物件"},
            "ending_direction": {"type": "string", "description": "结局朝哪个方向落"},
        },
        "required": ["logline", "setting", "conflict_axis", "concrete_objects",
                     "ending_direction"],
    }


def _cast_schema(p: Profile) -> dict:
    return {
        "type": "object",
        "properties": {
            "characters": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "key": {"type": "string",
                                "enum": ["A", "B", "C", "ORG", "LOC"]},
                        "name": {"type": "string",
                                 "description": "中文姓名，不要叫李明/张伟/王芳"},
                        "role": {"type": "string"},
                        "stance": {"type": "string",
                                   "description": p.lang.stance_desc},
                        "concrete": {"type": "string",
                                     "description": "他手上有什么、管什么、藏什么"},
                    },
                    "required": ["key", "name", "role", "stance", "concrete"],
                },
            }
        },
        "required": ["characters"],
    }


def _outline_schema(p: Profile) -> dict:
    return {
        "type": "object",
        "properties": {
            "chapters": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "no": {"type": "integer"},
                        "title": {"type": "string",
                                  "description": "具体物或具体动作，不要抽象词"},
                        "beat": {"type": "string", "description": "本章推进的那一件事"},
                        "must_object": {"type": "string",
                                        "description": "本章必须出现的物件"},
                        "speakers": {
                            "type": "array", "items": {"type": "string"},
                            "description": (f"本章必须出场的人，至少 "
                                            f"{max(1, p.lang.min_speakers)} 个")},
                    },
                    "required": ["no", "title", "beat", "must_object", "speakers"],
                },
            }
        },
        "required": ["chapters"],
    }


def _plan_schema(p: Profile) -> dict:
    return {
        "type": "object",
        "properties": {
            "scenes": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "idx": {"type": "integer"},
                        "place": {"type": "string"},
                        "present": {"type": "array", "items": {"type": "string"}},
                        "driver": {"type": "string",
                                   "description": p.lang.driver_desc},
                        "entry_state": {"type": "string"},
                        "outcome": {"type": "string",
                                    "description": "出场时发生了什么变化"},
                    },
                    "required": ["idx", "place", "present", "driver", "outcome"],
                },
            }
        },
        "required": ["scenes"],
    }


def _spend(tele: dict) -> dict:
    return {"telemetry": [tele], "calls_used": 1}


def _prof(state: dict) -> Profile:
    return load_profile(state["config"].get("profile", "default"))


def premise(state: dict) -> dict:
    cfg = state["config"]
    p = _prof(state)
    prompt = (
        f"为一篇{cfg['target_total_chars']}字的中文{p.diction.work}立意。\n"
        f"题材：{cfg['genre']}\n"
        + (f"拟定标题：{cfg['title']}\n" if cfg.get("title") else "")
        + "\n要求：\n"
        + (p.lang.premise_rule or
           "1. 立意必须从具体处境长出来，不准搬用现成的思想标签。\n")
        + "· 具体物件要能被人拿在手上、写在纸上、算进账里。\n"
          "调用 submit_premise 提交。")
    data, tele = llm.call_structured(
        prompt, llm.struct_sampling("premise"), _premise_schema(p),
        "submit_premise", system=_system(p), tag="premise",
        run=cfg["slug"])
    return {"premise": data, **_spend(tele)}


def cast(state: dict) -> dict:
    p = _prof(state)
    prompt = (
        f"{render_anchor(state['premise'], [], axis_name=p.lang.axis_name)}\n\n"
        f"为这篇{p.diction.piece}设计 2-4 个{p.diction.cast_noun}。\n要求：\n"
        + (p.lang.cast_rule or "1. A 和 B 必须构成本篇的主要张力。\n")
        + "· 每个人都要有「手上有什么」—— 他管的事、他签的字、他藏的东西。"
          "没有具体权责的人物在故事里没有分量。\n"
          "· 姓名要像真人，不要用李明、张伟、王芳这类占位名。\n"
          "· ORG 填机构/组织名，LOC 填主要场景名。\n"
          "调用 submit_cast 提交。")
    data, tele = llm.call_structured(
        prompt, llm.struct_sampling("cast"), _cast_schema(p),
        "submit_cast", system=_system(p), tag="cast",
        run=state["config"]["slug"])
    chars = data.get("characters") or []
    cast_map = {c["key"]: c["name"] for c in chars
                if c.get("key") and c.get("name")}
    return {"characters": chars, "cast": cast_map, **_spend(tele)}


def outline(state: dict) -> dict:
    """产出章级 beat 表。

    `scale` 和 `target_chars` **不交给模型**（实测它会把所有章都标成 normal），
    由 config.plan_rhythm 在代码里分配：首章冷开场、末章收束走 short 档位，
    这样 metrics.structural_reasons 会豁免它们的密度硬线。
    """
    cfg = state["config"]
    p = _prof(state)
    n = cfg["chapters"]
    notes = (state.get("approvals", {}).get("outline", {}) or {}).get("notes", "")

    prompt = (
        f"{render_anchor(state['premise'], state.get('characters'), axis_name=p.lang.axis_name)}\n\n"
        f"把这个故事拆成 {n} 章，总共约 {cfg['target_total_chars']} 字。\n要求：\n"
        "· 每章推进**一件具体的事**。\n"
        "· 章与章之间要有因果：上一章的结果造成下一章的处境。\n"
        "· 标题用具体物或具体动作命名（「三月的货款」而不是「艰难的抉择」）。\n"
        "· 禁止出现「困境初现」「挣扎与抉择」「转折与希望」这类套路章名。\n"
        "· must_object 必须是前面设定里的具体物件之一。\n"
        + (p.lang.outline_rule or "")
        + (f"\n【上一轮的修改意见，必须照改】\n{notes}\n" if notes else "")
        + "调用 submit_outline 提交。")

    data, tele = llm.call_structured(
        prompt, llm.struct_sampling("outline"), _outline_schema(p),
        "submit_outline", system=_system(p), tag="outline",
        run=cfg["slug"])

    rhythm = plan_rhythm(p, n, cfg["target_total_chars"])
    beats = []
    for i, raw in enumerate((data.get("chapters") or [])[:n]):
        scale, target = rhythm[i] if i < len(rhythm) else ("normal", 2200)
        beats.append({
            "no": i + 1,
            "title": (raw.get("title") or f"第{to_cn(i + 1)}章").strip(),
            "beat": raw.get("beat") or "",
            "target_chars": target,
            "scale": scale,
            "must_object": raw.get("must_object") or "",
            "speakers": raw.get("speakers") or [],
        })
    return {"outline": beats, **_spend(tele)}


def outline_lint(state: dict) -> dict:
    """大纲体检 —— 纯 python，在人工卡点**之前**跑。

    在大纲阶段就查标题套路，不要等正文写完才拦：book-01 的 300 次标题重复拦截
    发生在正文阶段，每次都伴随一章的 GPU 开销。标题在大纲阶段是免费的。

    「每章至少几人出场」由 profile 决定 —— 纯文学/独白体可以设 0 或 1。
    """
    p = _prof(state)
    beats = state.get("outline") or []
    bl = load_blacklist(",".join(f"{k}={v}" for k, v in
                                 sorted((state.get("cast") or {}).items())))
    issues: list[str] = []

    titles = [b["title"] for b in beats]
    for i, t in enumerate(titles):
        issues.extend(f"第{i + 1}章{r}" for r in title_blacklist_reasons(t, bl))
    for i in range(len(titles)):
        for j in range(i + 1, len(titles)):
            r = sim_ratio(titles[i], titles[j])
            if r >= 0.6:
                issues.append(
                    f"第{i + 1}章《{titles[i]}》与第{j + 1}章《{titles[j]}》"
                    f"标题近似 {r:.2f}")
    # ORG/LOC 是机构与场所，不是人（见 context.render_anchor 的注释）。
    # 它们混进 speakers 会有两个后果：① 模型被要求让教务处开口；
    # ② min_speakers 被虚高的计数蒙过去 —— speakers=['教务处'] 在
    # min_speakers=1 下算合格，而实际上一个人都没开口。所以先剔再数。
    nonppl = {c.get("name") for c in (state.get("characters") or [])
              if c.get("key") in ("ORG", "LOC") and c.get("name")}
    for b in beats:
        if p.lang.require_object and not b.get("must_object"):
            issues.append(f"第{b['no']}章没有指定必须出现的物件")
        speakers = b.get("speakers") or []
        misplaced = [s for s in speakers if s in nonppl]
        if misplaced:
            issues.append(f"第{b['no']}章把机构/场所列成了必须开口的人："
                          f"{'、'.join(misplaced)}")
        if len(speakers) - len(misplaced) < p.lang.min_speakers:
            issues.append(f"第{b['no']}章出场人物不足 {p.lang.min_speakers} 个")
        if not b.get("beat"):
            issues.append(f"第{b['no']}章没写要推进什么")

    beat_texts = [b.get("beat", "") for b in beats]
    for i in range(len(beat_texts)):
        for j in range(i + 1, len(beat_texts)):
            if sim_ratio(beat_texts[i], beat_texts[j]) >= 0.65:
                issues.append(f"第{i + 1}章与第{j + 1}章要做的事几乎是同一件")

    return {"approvals": {"outline_lint": {"issues": issues}}}


def plan_scenes(state: dict) -> dict:
    """为每章拆分场次。串行跑完所有章 —— 短篇只有 10 章，一次一个调用。

    采样用 struct_sampling("plan")，它的签名里没有 attempt 参数：
    结构化调用绝不升温（上游在这里踩过死循环，见 llm.py 的注释）。
    """
    cfg = state["config"]
    p = _prof(state)
    beats = state.get("outline") or []
    anchor = render_anchor(state["premise"], state.get("characters"),
                           axis_name=p.lang.axis_name)
    specs: dict[str, list[dict]] = {}
    teles: list[dict] = []

    # 其他章各自的物件 —— 当前章不准去碰它们。
    # 这比「别重复前面的问题」那种负向清单有效：实测 8B 根本不照办负向清单
    # （2026-10-18 真跑，给了 12 条已用论题，它照旧产出一字不差的同一个问题），
    # 而生产线的结论是「被强制成字段的要求 100% 落地」。所以改成正向的局部约束：
    # 把每章的驱动力锁死在**它自己的物件**上。
    others = {b["no"]: [x["must_object"] for x in beats
                        if x["no"] != b["no"] and x.get("must_object")]
              for b in beats}
    schema = _plan_schema(p)

    for b in beats:
        want = max(2, min(8, round(b["target_chars"] / C.SCENE_CHARS)))
        obj = b.get("must_object") or ""
        off_limits = [o for o in others[b["no"]] if o and o != obj]
        rule = (p.lang.driver_rule or
                "· 每一场的 driver 都必须是关于「{obj}」的，"
                "而且是 {want} 个互不相同的侧面。").format(obj=obj, want=want)
        prompt = (
            f"{anchor}\n\n"
            f"【第{to_cn(b['no'])}章】{b['title']}\n"
            f"本章唯一的载体：{obj}\n"
            f"要推进的事：{b['beat']}\n"
            f"本章出场的人：{'、'.join(b.get('speakers') or [])}\n"
            f"本章目标 {b['target_chars']} 字，拆成 {want} 场。\n\n"
            f"每一场的 driver 指的是：{p.lang.driver_desc}\n\n"
            "要求：\n" + rule + "\n"
            + (f"· 以下物件属于**别的章**，本章一场都不准碰："
               f"{'、'.join(off_limits)}\n" if off_limits else "")
            + "· 每场的 outcome 要是真实的变化，不能是「气氛更紧张了」这类空转。\n"
              "· 上一场的 outcome 就是下一场的 entry_state，必须接得上。\n"
              "· 每场在场的人控制在 1-3 个。\n"
              "调用 submit_scenes 提交。")
        data, tele = llm.call_structured(
            prompt, llm.struct_sampling("plan", want=want), schema,
            "submit_scenes", system=_system(p), tag=f"plan:ch{b['no']}",
            run=cfg["slug"])
        raw = (data.get("scenes") or [])[:want] or [{}]
        per = max(300, int(b["target_chars"] / len(raw)))
        specs[str(b["no"])] = [{
            "idx": i + 1,
            "place": s.get("place") or "",
            "present": s.get("present") or [],
            # 兼容早于「可插拔驱动力」改造的 thread（那时字段叫 question）
            "driver": s.get("driver") or s.get("question") or "",
            "entry_state": s.get("entry_state") or "",
            "outcome": s.get("outcome") or "",
            "target_chars": per,
        } for i, s in enumerate(raw)]
        teles.append(tele)

    return {"scene_specs": specs, "telemetry": teles, "calls_used": len(teles)}


def plans_lint(state: dict) -> dict:
    """细纲体检 —— 纯 python，在人工卡点**之前**跑。

    重点查**跨章驱动力重复**：这是实测发现的主要失败模式（见 plan_scenes 的注释）。
    只报不拦 —— 判断「这两件事是不是同一件」最终得由人来做，闸门只负责把可疑的
    挑出来摆在眼前。

    阈值与称呼都来自 profile：悬疑的「线索」天然比论辩的「论题」更容易措辞相近，
    一刀切的阈值会在某些题材上刷屏。
    """
    p = _prof(state)
    label = p.lang.driver_name
    thr = p.lang.dedup_threshold
    specs = state.get("scene_specs") or {}
    flat: list[tuple[int, int, str]] = []
    for k in sorted(specs, key=lambda x: int(x)):
        for s in specs[k]:
            d = s.get("driver") or s.get("question") or ""
            if d:
                flat.append((int(k), s["idx"], d))

    issues: list[str] = []
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            c1, s1, q1 = flat[i]
            c2, s2, q2 = flat[j]
            r = sim_ratio(q1, q2)
            if r >= thr:
                issues.append(
                    f"第{c1}章第{s1}场「{q1}」与第{c2}章第{s2}场「{q2}」"
                    f"{label}重合 {r:.2f}" + ("（同一章内）" if c1 == c2 else ""))

    for k in sorted(specs, key=lambda x: int(x)):
        for s in specs[k]:
            if not s.get("outcome"):
                issues.append(f"第{k}章第{s['idx']}场没写出场时的变化")
            elif len(s["outcome"]) < 6:
                issues.append(f"第{k}章第{s['idx']}场的变化太空：「{s['outcome']}」")
            if len(s.get("present") or []) < max(1, p.lang.min_speakers - 1):
                issues.append(f"第{k}章第{s['idx']}场在场的人太少")

    return {"approvals": {"plans_lint": {"issues": issues[:30]}}}
