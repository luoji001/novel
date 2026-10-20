# 当票 生成报告

slug：`xuanyi-20261019-222`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13334
LLM 调用：68 次，累计 231.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 当票边缘的焦痕 | 1429 | short | 98.4 | 0 |  | 2 |
| 2 | 账簿与木牌的对峙 | 3447 | normal | 89.2 | 0 |  | 2 |
| 3 | 怀表背面的刻痕 | 3298 | normal | 89.7 | 0 |  | 3 |
| 4 | 当票上的折痕 | 3400 | normal | 88.9 | 0 |  | 4 |
| 5 | 当票背面的指纹 | 1755 | short | 89.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周慕云的」×3
  - narration_para_pct 19.5 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周慕云的」×10
  - narration_para_pct 17.6 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「沈文远的」×9、「周慕云的」×6、「他知道这」×3
  - narration_para_pct 16.7 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「周慕云的」×5、「沈文远的」×3
  - narration_para_pct 8.1 低于目标 20.0
  - attr_adv_pct 17.6 高于目标 10.0
  - [observe] 标题与《当票边缘的焦痕》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「周慕云的」×4
  - narration_para_pct 3.4 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 12710
chapter_chars_mean: 2542
chapter_chars_median: 3151
chapter_chars_cv: 0.38
paragraphs_mean: 54.4
dialogue_chars_pct: 37.3
dialogue_para_pct: 74.8
interiority_para_pct: 11.9
narration_para_pct: 13.3
turn_under20_pct: 70.2
turn_over200_pct: 0.0
attr_say_pct: 27.7
attr_adv_pct: 10.0
scenes_per_chapter: 3.2
dialogue_run_mean: 4.3
turn_len_median: 13
```
