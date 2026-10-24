# Vendor 记录

这两个文件是从生产线复制来的，**字节级一致**，便于 diff 检测漂移。不要手改。
规则改造一律放在 `rules.py` / `checks.py` 里。

| 本地文件 | 上游 | vendor 时的上游 mtime | sha256 |
|---|---|---|---|
| `metrics.py` | `/home/liang/llm-api/train/novel_metrics.py` | 2026-10-07 15:11:57 | `4361320fe3a2557cf74fc6f291ec3fe44d314e91906acb8261707ab91838043c` |
| `blacklist.json` | `/home/liang/llm-api/train/data/style_blacklist.json` | — | `58a7f029c759204e08791eba1feac1d13fe3d6aaad7fe318265615cadb676cd2` |

vendor 日期：2026-10-18

## 检查漂移

```bash
cd /mnt/c/code/novel-agent/src/novel_agent/quality
diff metrics.py   /home/liang/llm-api/train/novel_metrics.py
diff blacklist.json /home/liang/llm-api/train/data/style_blacklist.json
```

两条都该无输出。有差异时**先跑 `pytest tests/test_quality.py`**，确认参照书的真章
仍然全部通过闸门，再决定是否同步过来——上游的改动可能是针对长篇场景的。

## 为什么是 vendor 而不是 import

`sys.path` 指向 `/home/liang/llm-api/train/` 会让本项目依赖生产线的目录结构，
生产线一动就断；把生产线做成可编辑包要改它的目录，而本项目的前提是**不动它一行**。

vendor 的代价是漂移，用上面的 diff 命令和 `tests/test_quality.py` 的行为回归兜住。

## 规则层相对上游的改造

见 `rules.py` 和 `checks.py` 的模块 docstring。三点：阈值参数化（上游读
`NOVEL_LOOP_*` 环境变量）、`_CAST` 从模块全局变成参数、`validate_chapter`
拆成 `hard_checks` / `title_checks` / `soft_checks`。
