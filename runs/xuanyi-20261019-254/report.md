# 麻袋 生成报告

slug：`xuanyi-20261019-254`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14355
LLM 调用：68 次，累计 231.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 布料的重量 | 1711 | short | 98.4 | 0 |  | 3 |
| 2 | 撕碎的进货单 | 3758 | normal | 90.8 | 0 |  | 2 |
| 3 | 摩挲账页的手指 | 3257 | normal | 86.7 | 0 |  | 5 |
| 4 | 摩挲布料的手指 | 3646 | normal | 90.0 | 0 |  | 4 |
| 5 | 摩挲红绳的手指 | 1978 | short | 90.9 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈国栋站在」×3
  - narration_para_pct 16.2 低于目标 20.0
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「周婉秋的」×11、「陈国栋的」×5
  - narration_para_pct 10.8 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×7、「陈国栋的」×7、「”周婉秋轻」×4
  - dialogue_chars_pct 58.4 高于目标 58.0
  - narration_para_pct 3.8 低于目标 20.0
  - attr_adv_pct 14.8 高于目标 10.0
  - dialogue_run_mean 14.8 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「周婉秋的」×3
  - narration_para_pct 15.7 低于目标 20.0
  - attr_adv_pct 11.8 高于目标 10.0
  - [observe] 标题与《摩挲账页的手指》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「陈国栋的」×7
  - narration_para_pct 17.5 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 标题与《摩挲账页的手指》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13678
chapter_chars_mean: 2736
chapter_chars_median: 3084
chapter_chars_cv: 0.34
paragraphs_mean: 60
dialogue_chars_pct: 43.1
dialogue_para_pct: 80.1
interiority_para_pct: 7.8
narration_para_pct: 12.0
turn_under20_pct: 78.5
turn_over200_pct: 0.0
attr_say_pct: 12.9
attr_adv_pct: 12.9
scenes_per_chapter: 4.6
dialogue_run_mean: 6.5
turn_len_median: 13
```
