# 当票 生成报告

slug：`xuanyi-20261019-82`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14054
LLM 调用：68 次，累计 234.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 镯子的低语 | 1637 | short | 94.2 | 0 |  | 3 |
| 2 | 铜镯的低语 | 4177 | normal | 90.7 | 0 |  | 3 |
| 3 | 当票的倒置 | 3265 | normal | 90.9 | 0 |  | 0 |
| 4 | 铜镯的重量 | 3264 | normal | 89.1 | 0 |  | 3 |
| 5 | 信纸的摩挲 | 1706 | short | 90.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 17.7 低于目标 20.0
  - interiority_para_pct 21.4 高于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「沈文渊的」×5、「周慕云的」×4
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 标题与《镯子的低语》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「沈文渊的」×7、「“我不知道」×3、「周慕云的」×3
  - narration_para_pct 17.4 低于目标 20.0
  - [observe] 标题与《铜镯的低语》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3、「沈文渊的」×3
  - narration_para_pct 18.2 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13400
chapter_chars_mean: 2680
chapter_chars_median: 3066
chapter_chars_cv: 0.39
paragraphs_mean: 58.2
dialogue_chars_pct: 31.9
dialogue_para_pct: 67.6
interiority_para_pct: 11.6
narration_para_pct: 20.8
turn_under20_pct: 80.8
turn_over200_pct: 0.0
attr_say_pct: 23.4
attr_adv_pct: 12.0
scenes_per_chapter: 3.2
dialogue_run_mean: 3.1
turn_len_median: 11
```
