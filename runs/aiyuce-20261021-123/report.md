# 电表 生成报告

slug：`aiyuce-20261021-123`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11190
LLM 调用：57 次，累计 203.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单的疑问 | 1631 | normal | 89.0 | 0 |  | 2 |
| 2 | 电费单的疑问 | 2307 | normal | 35.2 | 0 |  | 4 |
| 3 | 误诊率对比分析 | 2276 | normal | 89.6 | 0 |  | 2 |
| 4 | 误诊率统计报告 | 1670 | normal | 36.6 | 0 |  | 1 |
| 5 | 误诊率统计报告 | 2053 | normal | 34.5 | 0 |  | 4 |
| 6 | 电费单的质疑 | 1247 | short | 82.1 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 47.4 高于目标 18.0
  - narration_para_pct 26.3 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 43.3 高于目标 18.0
  - narration_para_pct 24.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「电费单的疑问」已存在
- 第 3 章：
  - 命中套话收尾句
  - narration_para_pct 28.6 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 28.3 高于目标 18.0
  - narration_para_pct 11.1 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「误诊率统计报告」已存在
- 第 6 章：
  - dialogue_chars_pct 74.6 高于目标 18.0
  - dialogue_run_mean 14 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题与《电费单的疑问》近似 0.83 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 10895
chapter_chars_mean: 1816
chapter_chars_median: 1818
chapter_chars_cv: 0.23
paragraphs_mean: 16.8
dialogue_chars_pct: 32.6
dialogue_para_pct: 65.1
interiority_para_pct: 11.5
narration_para_pct: 23.5
turn_under20_pct: 35.4
turn_over200_pct: 0.0
attr_say_pct: 17.1
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 4.2
turn_len_median: 30
```
