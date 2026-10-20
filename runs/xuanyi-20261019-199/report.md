# 渔网 生成报告

slug：`xuanyi-20261019-199`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13676
LLM 调用：68 次，累计 231.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲汇款单的指尖 | 1706 | short | 98.3 | 0 |  | 2 |
| 2 | 摩挲渔网的指尖 | 3476 | normal | 93.5 | 0 |  | 3 |
| 3 | 摩挲账簿的指尖 | 3481 | normal | 91.2 | 0 |  | 3 |
| 4 | 摩挲账本的指尖 | 3411 | normal | 88.0 | 0 |  | 6 |
| 5 | 摩挲账簿的指尖 | 1597 | short | 90.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林秋实的」×3
  - narration_para_pct 19.4 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林秋实的」×4、「林秋实站在」×3
  - narration_para_pct 17.5 低于目标 20.0
  - [observe] 标题与《摩挲汇款单的指尖》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×6、「陈德昌的」×6、「他知道这」×4
  - narration_para_pct 14.3 低于目标 20.0
  - [observe] 标题与《摩挲渔网的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「陈德昌的」×4、「林秋实的」×3
  - dialogue_chars_pct 59.9 高于目标 58.0
  - narration_para_pct 4.1 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
  - dialogue_run_mean 13.8 高于目标 10.0
  - [observe] 标题与《摩挲账簿的指尖》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 11.5 低于目标 20.0
  - [observe] 标题重复：「摩挲账簿的指尖」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13055
chapter_chars_mean: 2611
chapter_chars_median: 3250
chapter_chars_cv: 0.36
paragraphs_mean: 54
dialogue_chars_pct: 40.7
dialogue_para_pct: 77.5
interiority_para_pct: 9.6
narration_para_pct: 12.9
turn_under20_pct: 76.9
turn_over200_pct: 0.0
attr_say_pct: 30.2
attr_adv_pct: 7.4
scenes_per_chapter: 2.2
dialogue_run_mean: 6.0
turn_len_median: 13
```
