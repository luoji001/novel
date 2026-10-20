# 注销卡 生成报告

slug：`xuanyi-20261019-60`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14999
LLM 调用：68 次，累计 236.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 发现注销卡异常 | 2112 | short | 97.4 | 0 |  | 2 |
| 2 | 摩挲考勤表边缘 | 3780 | normal | 88.1 | 0 |  | 1 |
| 3 | 摩挲便签纸边缘 | 3336 | normal | 88.5 | 0 |  | 2 |
| 4 | 摩挲登记簿边缘 | 3778 | normal | 90.2 | 0 |  | 3 |
| 5 | 摩挲工牌边缘 | 1988 | short | 91.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周晓芸的」×3、「他知道这」×3
  - attr_adv_pct 11.1 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「周晓芸的」×6
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
  - dialogue_chars_pct 19.7 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「点了点头」×3、「带着一丝」×3、「林振华的」×3
  - narration_para_pct 8.7 低于目标 20.0
  - dialogue_run_mean 10.3 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「周晓芸的」×4、「林振华站在」×3
  - narration_para_pct 18.4 低于目标 20.0
  - [observe] 标题与《摩挲便签纸边缘》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 14378
chapter_chars_mean: 2876
chapter_chars_median: 3207
chapter_chars_cv: 0.3
paragraphs_mean: 54.2
dialogue_chars_pct: 32.1
dialogue_para_pct: 69.5
interiority_para_pct: 8.9
narration_para_pct: 21.5
turn_under20_pct: 70.0
turn_over200_pct: 0.0
attr_say_pct: 21.1
attr_adv_pct: 4.4
scenes_per_chapter: 2.8
dialogue_run_mean: 4.6
turn_len_median: 13
```
