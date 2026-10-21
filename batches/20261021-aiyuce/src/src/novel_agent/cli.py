"""CLI。

一部短篇 = 一个 thread（`thread_id = slug`）。两个 interrupt 卡点、断点续跑、
定点重写，全都要求历史在同一个 thread 里 —— 换 thread 等于丢掉人工审核过的大纲。
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from langgraph.types import Command, Overwrite

from . import config as C
from .state import Approval
from .store import RunStore


# 退出码。批处理脚本靠它判断该不该继续放行 —— 这样「自动批准」的策略留在
# 脚本里，而不是烧进 agent。人工卡点是计划层质量的主防线，
# 默认行为必须是「停下来等人」。
EXIT_DONE = 0        # 跑完了，没有待处理的卡点
EXIT_PARKED = 10     # 停在某个人工卡点上


def _cfg(slug: str) -> dict:
    return {"configurable": {"thread_id": slug},
            "max_concurrency": C.CONCURRENCY,
            "recursion_limit": 300}


def _run(app, slug: str, payload) -> int:
    """跑到下一个 interrupt 或结束。`durability="sync"` —— 一个 super-step 等于
    几十秒 GPU，每步多一次 fsync（毫秒级）换「崩溃最多丢一场」，这笔账没有悬念。

    追踪与打分都在这一层做：规则分数从 stream 出来的 state 更新里取，
    所以**节点不需要知道 Langfuse 存在**。
    """
    from . import observability

    st0 = app.get_state(_cfg(slug)).values or {}
    pcfg = (payload or {}).get("config") if isinstance(payload, dict) else None
    pcfg = pcfg or st0.get("config") or {}

    tracing = observability.setup(slug)
    if not tracing.enabled and tracing.reason and os.environ.get("NOVEL_TRACING_VERBOSE"):
        print(f"  ○ 未追踪：{tracing.reason}")

    cfg = {**_cfg(slug),
           **tracing.config_patch(profile=pcfg.get("profile", ""),
                                  gate_mode=pcfg.get("gate_mode", ""))}
    try:
        for chunk in app.stream(payload, cfg, durability="sync",
                                stream_mode="updates"):
            for node, upd in (chunk or {}).items():
                if node == "__interrupt__":
                    continue
                bits = []
                if isinstance(upd, dict):
                    if upd.get("calls_used"):
                        bits.append(f"+{upd['calls_used']} 调用")
                    if "scenes_draft" in upd and upd["scenes_draft"] is not None:
                        bits.append(f"{len(upd['scenes_draft'])} 场定稿")
                    if upd.get("chapters"):
                        bits.append(f"落盘 {list(upd['chapters'])}")
                    if upd.get("halted"):
                        bits.append(f"熔断：{upd['halted']}")
                    for rec in (upd.get("chapters") or {}).values():
                        tracing.score_chapter(rec)
                    for rec in upd.get("quality_log") or []:
                        tracing.score_scene(rec)
                print(f"  · {node}" + (f"  [{'，'.join(bits)}]" if bits else ""),
                      flush=True)
    finally:
        tracing.flush()
    parked = _show_pending(app, slug)
    if tracing.enabled:
        print(f"  ◉ 追踪：{tracing.base_url}/project/novel-agent/sessions/{slug}")
    return EXIT_PARKED if parked else EXIT_DONE


def _show_pending(app, slug: str) -> bool:
    """打印待处理的卡点。返回 True = 停在卡点，False = 已跑完。"""
    st = app.get_state(_cfg(slug))
    if not st.interrupts:
        print(f"\n✓ 跑完了。产出在 {RunStore(slug).root}")
        return False
    for itr in st.interrupts:
        v = itr.value if isinstance(itr.value, dict) else {}
        print(f"\n⏸ 停在卡点：{v.get('stage', '?')}")
        if v.get("lint"):
            print("  体检发现：")
            for x in v["lint"][:12]:
                print(f"    - {x}")
        if v.get("outline"):
            print("  大纲：")
            for b in v["outline"]:
                print(f"    {b['no']:>2}. {b['title']}（{b['scale']}，"
                      f"{b['target_chars']}字）{b['beat'][:40]}")
        if v.get("scene_specs"):
            for k in sorted(v["scene_specs"], key=lambda x: int(x)):
                scenes = v["scene_specs"][k]
                # `driver` 是可插拔改造后的字段名；`question` 是改造之前的旧名，
                # 老 thread resume 回来时读的还是后者。两个都要认。
                print(f"    第{k}章 {len(scenes)} 场："
                      + " | ".join((s.get("driver") or s.get("question") or "?")[:16]
                                   for s in scenes))
        if v.get("report"):
            print(f"  报告：{RunStore(slug).root / 'report.md'}")
        print(f"\n  继续：novel-agent approve {slug} --accept")
        print(f"  打回：novel-agent approve {slug} --revise \"你的意见\"")
    return True


def cmd_new(a) -> int:
    from .graph import build_app
    app = build_app()
    # chapters / target 只在命令行**显式给了**才进 config。
    # 它们的默认值必须留给 profile 的 [meta] —— 否则 argparse 的默认值会盖掉
    # 档位里按实测定好的形态，Phase 1 的结构修改就成了空操作（踩过）。
    cfg = {"slug": a.slug, "profile": a.profile, "title": a.title or "",
           "genre": a.genre, "gate_mode": a.gate,
           "prose_model": a.prose_model or C.PROSE_MODEL}
    if a.chapters is not None:
        cfg["chapters"] = a.chapters
    if a.target is not None:
        cfg["target_total_chars"] = a.target
    payload = {"config": cfg}

    from .config import load_profile
    prof = load_profile(a.profile)
    n = a.chapters if a.chapters is not None else prof.chapters
    total = a.target if a.target is not None else prof.target_total_chars
    unit = prof.form.unit_label
    form = {"single_arc": "单篇连续弧", "sectioned": "分节文章"}.get(
        prof.form.kind, "分章连载")
    print(f"开始：{a.slug}（档位 {prof.name}／{form}，{n} {unit} / {total} 字，"
          f"闸门 {a.gate}，并发 {C.CONCURRENCY}）")
    return _run(app, a.slug, payload)


def cmd_resume(a) -> int:
    from .graph import build_app
    return _run(build_app(), a.slug, None)


def cmd_approve(a) -> int:
    from .graph import build_app
    app = build_app()
    if a.revise:
        d = Approval(action="revise", notes=a.revise)
    elif a.edit:
        d = Approval(action="edit", patch=json.loads(Path(a.edit).read_text("utf-8")))
    else:
        d = Approval(action="accept")
    return _run(app, a.slug, Command(resume=d))


def cmd_status(a) -> None:
    from .graph import build_app
    app = build_app()
    st = app.get_state(_cfg(a.slug))
    v = st.values or {}
    if not v:
        print(f"没有 thread {a.slug!r}")
        return
    cfg = v.get("config") or {}
    print(f"{a.slug}：第 {v.get('cursor', '?')}/{cfg.get('chapters', '?')} 章，"
          f"已定稿 {len(v.get('chapters') or {})} 章，"
          f"调用 {v.get('calls_used', 0)} 次")
    if v.get("halted"):
        print(f"熔断：{v['halted']}")
    print(f"下一步节点：{list(st.next) or '（已结束）'}")
    for k in sorted((v.get("chapters") or {}), key=lambda x: int(x)):
        r = v["chapters"][k]
        print(f"  {r['no']:>2}. {r.get('title','')}　{r.get('chars',0)}字　"
              f"分 {r.get('score')}　轮 {r.get('attempts',0)}"
              + ("　[降级]" if r.get("degraded") else ""))
    _show_pending(app, a.slug)


def cmd_calls(a) -> None:
    """查看调用现场。

    这个命令的存在理由：`report.md` 能告诉你「第 3 章烧了 5 轮」，但看不到
    **是哪个 prompt 产出了那段烂正文**。calls.jsonl 补上了现场，但 2MB 的
    jsonl 没有读取工具等于没有。

    `--bad` 是真正的用法：按场景分数排序，直接看最差那几场的 prompt。
    这条路径服务于 observe→标定 流程 —— 你要先知道低分是 prompt 的问题
    还是闸门标错了，才谈得上定硬线。
    """
    store = RunStore(a.slug)
    calls = store.read_jsonl("calls.jsonl")
    if not calls:
        print(f"{a.slug} 没有 calls.jsonl。"
              f"（NOVEL_LOG_CALLS=0 会关掉它；langgraph dev 不经过 CLI 也不会写）")
        return

    # 和 rounds.jsonl 的 quality_log 做 join：后者有「这一场选了哪个候选、分多少」，
    # 前者有「那个候选是什么 prompt 产的」。键是 (章, 场, 候选编号)。
    scores: dict[tuple, float] = {}
    for r in store.read_jsonl("rounds.jsonl"):
        if r.get("kind") != "scene":
            continue
        for c in r.get("candidates") or []:
            v = str(c.get("sampling", "")).lstrip("v")
            if v.isdigit() and c.get("score") is not None:
                scores[(r["chapter"], r["scene"], int(v))] = c["score"]

    def score_of(c: dict):
        return scores.get((c.get("chapter"), c.get("scene"), c.get("variant")))

    rows = [c for c in calls if not a.tag or c.get("tag", "").startswith(a.tag)]
    if a.failed:
        rows = [c for c in rows if not c.get("ok", True)]
    if a.bad:
        rows = [c for c in rows if score_of(c) is not None]
        rows.sort(key=lambda c: score_of(c))
        rows = rows[:a.bad]

    if a.show is not None:
        if not (0 <= a.show < len(rows)):
            print(f"序号超范围：0..{len(rows) - 1}")
            return
        c = rows[a.show]
        sc = score_of(c)
        print(f"=== #{a.show}  {c['tag']}  {c['model']}  {c['sec']}s"
              + (f"  分={sc}" if sc is not None else "")
              + ("" if c.get("ok", True) else f"  ✗ {c.get('error')}") + " ===")
        print(f"--- 采样 ---\n{json.dumps(c['sampling'], ensure_ascii=False)}")
        if c.get("system"):
            print(f"\n--- system ---\n{c['system']}")
        print(f"\n--- prompt（{c['in_est']} tok 估算）---\n{c['prompt']}")
        print(f"\n--- completion（{c['out_chars']} 字）---\n{c['completion']}")
        if c.get("structured"):
            print(f"\n--- 解析出的结构 ---\n"
                  f"{json.dumps(c['structured'], ensure_ascii=False, indent=2)}")
        return

    total_sec = sum(c.get("sec", 0) for c in calls)
    bad_count = sum(1 for c in calls if not c.get("ok", True))
    print(f"{a.slug}：{len(calls)} 次调用，累计 {total_sec:.1f} 秒"
          + (f"，{bad_count} 次失败" if bad_count else ""))
    print(f"\n{'#':>4} {'tag':<22}{'model':<12}{'温度':>5}{'入tok':>7}{'出字':>7}"
          f"{'秒':>7}{'分':>7}    （出字带 * = 结构化载荷）")
    for i, c in enumerate(rows):
        sc = score_of(c)
        flag = "" if c.get("ok", True) else " ✗"
        # 结构化调用走 tool_calls，content 是空的，载荷在 structured 里 ——
        # 直接显示 out_chars=0 会让人以为模型什么都没返回。
        out = c.get("out_chars", 0)
        if not out and c.get("structured") is not None:
            out = f"{len(json.dumps(c['structured'], ensure_ascii=False))}*"
        print(f"{i:>4} {c.get('tag',''):<22}{c.get('model',''):<12}"
              f"{c['sampling'].get('temperature', 0):>5.2f}{c.get('in_est',0):>7}"
              f"{str(out):>7}{c.get('sec',0):>7.1f}"
              f"{(f'{sc:.1f}' if sc is not None else '-'):>7}{flag}")
    print(f"\n看某一条的全文：novel-agent calls {a.slug} --show <#>")
    if not a.bad:
        print(f"看最差的几场：  novel-agent calls {a.slug} --bad 5")


def cmd_baseline(a) -> None:
    """把参考语料算成可复算的基线。语料只当尺子，不进 prompt。"""
    from .config import PROJECT_ROOT
    from .corpus import GENRE_KEYS, NATIVE_KEYS, suggest_targets, write_baseline

    d = PROJECT_ROOT / "profiles-sft" / a.profile
    if not d.is_dir():
        print(f"没有语料目录 {d}。把 epub/txt 放进去再跑。")
        return
    bj, bm = write_baseline(d, min_chars=a.min_chars)
    import json as _json
    b = _json.loads(bj.read_text(encoding="utf-8"))
    print(f"✓ {bj}\n✓ {bm}")
    print(f"\n语料：{b['counts']['standalone']} 个独立短篇 + "
          f"{b['counts']['chaptered']} 个长篇分章")

    sec = a.section
    d2 = b.get(sec) or {}
    if not d2:
        print(f"（{sec} 这一类没有样本）")
        return
    print(f"\n【{sec} 单篇分布】")
    print(f"{'指标':<24}{'p3':>8}{'p10':>8}{'p50':>8}{'p90':>8}{'max':>9}  维度")
    for k, v in d2.items():
        tag = "文风⚠" if k in NATIVE_KEYS else ("结构" if k in GENRE_KEYS else "")
        print(f"{k:<24}{v['p3']:>8}{v['p10']:>8}{v['p50']:>8}"
              f"{v['p90']:>8}{v['max']:>9}  {tag}")

    print("\n【据此建议的 [targets]】（只是建议，要人看过才算数）")
    for k, t in suggest_targets(b, section=sec).items():
        warn = "  ← 文风维度，译本语料别用这项" if t["native"] else ""
        print(f"  [targets.{k}]{warn}")
        print(f"    lo = {t['lo']}\n    hi = {t['hi']}\n    hard = {t['hard']}")
        if t.get("warn"):
            print(f"    # ⚠ {t['warn']}")
    print("\n标「文风⚠」的维度：若语料是译本，用原创中文语料定这几项。")


def cmd_redo(a) -> None:
    """定点重写第 k 章及之后。

    **state 和磁盘必须一起回退**。只改 state 的话，闸门会从磁盘读到旧正文当历史比，
    于是新写的那一章永远「与历史重复」—— 这是本设计最容易写出 bug 的地方。
    """
    from .graph import build_app
    app = build_app()
    cfg = _cfg(a.slug)
    st = app.get_state(cfg).values
    if not st:
        print(f"没有 thread {a.slug!r}")
        return
    k = a.chapter
    moved = RunStore(a.slug).rewind(k)
    print(f"归档了 {len(moved)} 个章节文件：{', '.join(moved) or '（无）'}")
    keep_ch = {kk: vv for kk, vv in (st.get("chapters") or {}).items()
               if int(kk) < k}
    keep_sum = {kk: vv for kk, vv in (st.get("summaries") or {}).items()
                if int(kk) < k}
    app.update_state(cfg, {
        "chapters": Overwrite(keep_ch),
        "summaries": Overwrite(keep_sum),
        "cursor": k, "scene_idx": 1, "attempts": 0, "scenes_draft": [],
        "draft_body": "", "draft_title": "", "draft_summary": "", "verdict": None,
        "candidates": Overwrite([]),
        "bans": Overwrite({"titles": [], "sentences": [], "templates": []}),
    }, as_node="approve_scenes")
    print(f"已回退到第 {k} 章。继续：novel-agent resume {a.slug}")


def cmd_endpoints(a) -> None:
    """打印两个端点的解析结果，可选真打一次最小调用。

    存在的理由：绑第三方时唯一真正要确认的事（key 有效、模型 id 存在、方言
    对不对）不该靠「开一部小说看它崩不崩」来验 —— 那要烧 GPU 和配额，
    而且失败发生在十几分钟后的某个节点里。
    """
    from . import llm
    eps = [C.struct_endpoint(), C.prose_endpoint()]
    for ep in eps:
        d = ep.dialect
        who = "本地" if ep.provider == "vllm" else "第三方（计费）"
        print(f"  {ep.role:7} {ep.provider:12} {ep.model:22} "
              f"方言={d.sampling:9} 窗口={d.context:>7}  {who}")
        if ep.provider == "anthropic" and not ep.workspace:
            print(f"           ⚠ 没设 NOVEL_{ep.role.upper()}_WORKSPACE_ID："
                  f"user 级 key（sk-ant-usr-…）会每请求 400")
    print(f"  上下文硬顶 = min(两端) = {C.model_context()}")

    if not a.probe:
        print("\n加 --probe 可以真打一次最小调用（第三方端点会计费，约几十 token）")
        return
    for ep in eps:
        s = llm.Sampling(temperature=0.3, max_tokens=24, effort="low")
        try:
            text, tele = llm.call("只回两个字：收到", s, role=ep.role)
            print(f"  {ep.role:7} ✅ {text.strip()[:20]!r}  用量={tele.get('usage')}")
        except Exception as e:                                    # noqa: BLE001
            print(f"  {ep.role:7} ❌ {type(e).__name__}: {str(e)[:220]}")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="novel-agent",
                                description="基于 LangGraph 的短篇小说生成（本地 vLLM）")
    sub = p.add_subparsers(dest="cmd", required=True)

    n = sub.add_parser("new", help="开一部新短篇")
    n.add_argument("slug")
    n.add_argument("--genre", required=True, help="题材，要具体")
    n.add_argument("--title", default="")
    from .config import list_profiles
    n.add_argument("--profile", default="default", choices=list_profiles(),
                   help="题材档位，决定闸门阈值与「场景驱动力」的语义")
    # 默认 None = 用档位的 [meta]。给了值才覆盖。
    n.add_argument("--chapters", type=int, default=None,
                   help="分几段写。不给就用档位的 [meta].chapters")
    n.add_argument("--target", type=int, default=None,
                   help="总字数。不给就用档位的 [meta].target_total_chars")
    n.add_argument("--gate", default="observe", choices=["observe", "enforce"],
                   help="observe=只记录不拦（首次必须用它标定分布）")
    n.add_argument("--prose-model", default="", dest="prose_model",
                   help="novel-sft3（LoRA）或 qwen3-8b（基座）")
    n.set_defaults(func=cmd_new)

    r = sub.add_parser("resume", help="断点续跑")
    r.add_argument("slug")
    r.set_defaults(func=cmd_resume)

    ap = sub.add_parser("approve", help="在卡点处拍板")
    ap.add_argument("slug")
    ap.add_argument("--accept", action="store_true")
    ap.add_argument("--revise", default="", help="打回并给出意见")
    ap.add_argument("--edit", default="", help="改好的 JSON 文件路径")
    ap.set_defaults(func=cmd_approve)

    s = sub.add_parser("status", help="看进度")
    s.add_argument("slug")
    s.set_defaults(func=cmd_status)

    c = sub.add_parser("calls", help="查看 LLM 调用现场（prompt / completion）")
    c.add_argument("slug")
    c.add_argument("--tag", default="", help="按 tag 前缀过滤，如 scene / scene:ch3 / plan")
    c.add_argument("--show", type=int, default=None, help="打印第 N 条的全文")
    c.add_argument("--bad", type=int, default=0, metavar="N",
                   help="只看分数最低的 N 个场景候选")
    c.add_argument("--failed", action="store_true", help="只看失败的调用")
    c.set_defaults(func=cmd_calls)

    bl = sub.add_parser("baseline", help="把 profiles-sft/<档位>/ 的语料算成基线")
    bl.add_argument("profile", choices=list_profiles())
    bl.add_argument("--min-chars", type=int, default=1500, dest="min_chars",
                    help="小于这个字数的单元不计入（滤掉前言/目录）")
    bl.add_argument("--section", default="standalone",
                    choices=["standalone", "chaptered"],
                    help="看哪一类的分布。标定短篇生成器用 standalone")
    bl.set_defaults(func=cmd_baseline)

    e = sub.add_parser("endpoints", help="看两个端点解析到哪儿（绑第三方后先跑这个）")
    e.add_argument("--probe", action="store_true",
                   help="真打一次最小调用验 key / 模型 id（第三方会计费）")
    e.set_defaults(func=cmd_endpoints)

    d = sub.add_parser("redo", help="定点重写某章及之后")
    d.add_argument("slug")
    d.add_argument("--chapter", type=int, required=True)
    d.set_defaults(func=cmd_redo)

    a = p.parse_args(argv)
    rc = a.func(a)
    return rc if isinstance(rc, int) else EXIT_DONE


if __name__ == "__main__":
    sys.exit(main())
