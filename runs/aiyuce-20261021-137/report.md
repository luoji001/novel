# 铜铃 生成报告

slug：`aiyuce-20261021-137`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12877
LLM 调用：57 次，累计 228.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 质检JD的泛黄页面 | 2280 | normal | 85.7 | 0 |  | 3 |
| 2 | AI测试报告的争论 | 2064 | normal | 33.8 | 0 |  | 3 |
| 3 | 翻阅投诉记录 | 2037 | normal | 32.1 | 0 |  | 4 |
| 4 | 翻阅考勤表核实缺口 | 2559 | normal | 35.4 | 0 |  | 1 |
| 5 | 翻阅成本报表讨论 | 2439 | normal | 33.4 | 0 |  | 4 |
| 6 | 摩挲招聘JD页面 | 1492 | short | 77.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 68.2 高于目标 18.0
  - dialogue_run_mean 9.5 高于目标 4.0
  - narration_para_pct 9.1 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 64.9 高于目标 18.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 61.9 高于目标 18.0
  - dialogue_run_mean 8.3 高于目标 4.0
  - narration_para_pct 7.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「这笔费用如果能在保证服务质量的前提下得到有效控制…」）
- 第 5 章：
  - dialogue_chars_pct 61.7 高于目标 18.0
  - dialogue_run_mean 5.2 高于目标 4.0
  - narration_para_pct 13.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 37.8 高于目标 18.0
  - dialogue_run_mean 8 高于目标 4.0
  - narration_para_pct 10.0 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 12514
chapter_chars_mean: 2086
chapter_chars_median: 2113
chapter_chars_cv: 0.18
paragraphs_mean: 21.7
dialogue_chars_pct: 49.8
dialogue_para_pct: 73.3
interiority_para_pct: 4.8
narration_para_pct: 21.9
turn_under20_pct: 30.2
turn_over200_pct: 0.0
attr_say_pct: 9.6
attr_adv_pct: 2.7
scenes_per_chapter: 1.5
dialogue_run_mean: 5.9
turn_len_median: 30
```
