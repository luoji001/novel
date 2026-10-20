# real-01 生成报告

档位：论辩驱动　闸门模式：observe
章数：4　总字数：5969
LLM 调用：73 次，累计 346.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 调试注塑机 | 957 | short | 94.6 | 0 |  | 5 |
| 2 | 维修旧机器 | 1983 | normal | 93.2 | 0 |  | 4 |
| 3 | 摩挲钱袋 | 1785 | normal | 90.7 | 0 |  | 5 |
| 4 | 摩挲财务报表 | 1240 | short | 90.8 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 64.9 高于目标 58.0
  - narration_para_pct 0.0 低于目标 10.0
  - turn_under20_pct 81.6 高于目标 72.0
  - attr_say_pct 0.0 低于目标 70.0
  - dialogue_run_mean 21 高于目标 10.0
- 第 2 章：
  - narration_para_pct 4.9 低于目标 10.0
  - attr_say_pct 23.8 低于目标 70.0
  - attr_adv_pct 9.5 高于目标 8.0
  - dialogue_run_mean 19.5 高于目标 10.0
- 第 3 章：
  - dialogue_chars_pct 62.6 高于目标 58.0
  - narration_para_pct 2.6 低于目标 10.0
  - turn_under20_pct 75.0 高于目标 72.0
  - attr_say_pct 20.0 低于目标 70.0
  - dialogue_run_mean 12 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「陈志远的」×3
  - narration_para_pct 0.0 低于目标 10.0
  - turn_under20_pct 31.8 低于目标 45.0
  - attr_say_pct 45.5 低于目标 70.0
  - dialogue_run_mean 15 高于目标 10.0

## 整书结构指标

```
chapters: 4
total_chars: 5683
chapter_chars_mean: 1421
chapter_chars_median: 1446
chapter_chars_cv: 0.32
paragraphs_mean: 28.8
dialogue_chars_pct: 59.2
dialogue_para_pct: 96.8
interiority_para_pct: 0.8
narration_para_pct: 2.4
turn_under20_pct: 63.7
turn_over200_pct: 0.0
attr_say_pct: 23.5
attr_adv_pct: 5.2
scenes_per_chapter: 1.8
dialogue_run_mean: 16.9
turn_len_median: 14
```
