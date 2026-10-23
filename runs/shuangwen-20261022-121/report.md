# 账本 生成报告

slug：`shuangwen-20261022-121`
档位：爽文　闸门模式：observe
章数：10　总字数：19224
LLM 调用：97 次，累计 449.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本上的时间戳 | 1717 | normal | 97.3 | 0 |  | 1 |
| 2 | 账本边缘的铅笔痕 | 2034 | normal | 92.5 | 0 |  | 2 |
| 3 | 签字笔的博弈 | 1811 | normal | 91.9 | 0 |  | 0 |
| 4 | 存折边缘的冷笑 | 1721 | normal | 37.4 | 0 |  | 2 |
| 5 | 签字笔的重量 | 2092 | normal | 93.7 | 0 |  | 2 |
| 6 | 签字笔的重量 | 1549 | normal | 93.7 | 0 |  | 2 |
| 7 | 签字笔的裂痕 | 1674 | normal | 93.6 | 0 |  | 3 |
| 8 | 签字笔的裂痕 | 1878 | normal | 87.7 | 0 |  | 5 |
| 9 | 签字笔的裂痕 | 2201 | normal | 91.8 | 0 |  | 3 |
| 10 | 账本边缘的摩挲 | 2537 | long | 92.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×9
- 第 2 章：
  - 单条套路句式超限：「周小满的」×3
  - attr_adv_pct 17.6 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「李建国的」×4
  - [observe] attr_adv_pct 36.4 > 25.0（结构塌缩）
- 第 5 章：
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题与《签字笔的博弈》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「他知道这」×4
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 7 章：
  - 单条套路句式超限：「李建国的」×3、「周小满的」×3
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题与《签字笔的博弈》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「李建国的」×4
  - narration_para_pct 4.1 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - dialogue_run_mean 47 高于目标 14.0
  - [observe] 标题重复：「签字笔的裂痕」已存在
- 第 9 章：
  - 单条套路句式超限：「李建国的」×8
  - attr_adv_pct 18.8 高于目标 12.0
  - [observe] 标题重复：「签字笔的裂痕」已存在
- 第 10 章：
  - 单条套路句式超限：「周小满的」×4
  - [observe] 标题与《账本边缘的铅笔痕》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 18165
chapter_chars_mean: 1816
chapter_chars_median: 1734
chapter_chars_cv: 0.16
paragraphs_mean: 45.2
dialogue_chars_pct: 47.1
dialogue_para_pct: 82.7
interiority_para_pct: 6.0
narration_para_pct: 11.4
turn_under20_pct: 74.0
turn_over200_pct: 0.0
attr_say_pct: 21.2
attr_adv_pct: 14.7
scenes_per_chapter: 1.2
dialogue_run_mean: 9.4
turn_len_median: 12
```
