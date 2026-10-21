# 质检员月度工作量统计表 生成报告

slug：`aiyuce-20261021-197`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12900
LLM 调用：57 次，累计 223.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扫描质检员工作量数据 | 1897 | normal | 96.4 | 0 |  | 0 |
| 2 | 扫描预算报表数据 | 2455 | normal | 89.0 | 0 |  | 0 |
| 3 | 扫描投诉记录数据 | 2486 | normal | 80.4 | 0 |  | 3 |
| 4 | AI评分模块比例调整 | 2099 | normal | 34.0 | 0 |  | 2 |
| 5 | 折叠JD文件一角 | 2364 | normal | 36.2 | 0 |  | 1 |
| 6 | 讨论误判率与人力成本 | 1593 | short | 33.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - dialogue_chars_pct 53.8 高于目标 18.0
  - dialogue_run_mean 7.5 高于目标 4.0
  - narration_para_pct 23.8 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 31.5 高于目标 18.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「但这是否就意味着整个质检团队会变得更高效…」）
- 第 6 章：
  - dialogue_chars_pct 44.4 高于目标 18.0
  - narration_para_pct 44.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12554
chapter_chars_mean: 2092
chapter_chars_median: 2172
chapter_chars_cv: 0.17
paragraphs_mean: 19.2
dialogue_chars_pct: 25.9
dialogue_para_pct: 46.0
interiority_para_pct: 6.9
narration_para_pct: 47.1
turn_under20_pct: 39.2
turn_over200_pct: 0.0
attr_say_pct: 30.1
attr_adv_pct: 1.5
scenes_per_chapter: 1.5
dialogue_run_mean: 2.9
turn_len_median: 27
```
