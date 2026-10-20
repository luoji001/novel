# 旧信笺 生成报告

slug：`xuanyi-20261019-39`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14176
LLM 调用：68 次，累计 227.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲汇款单的手指 | 1673 | short | 98.2 | 0 |  | 2 |
| 2 | 摩挲账本的手指 | 4126 | normal | 90.6 | 0 |  | 3 |
| 3 | 摩挲算珠的手指 | 3207 | normal | 87.6 | 0 |  | 5 |
| 4 | 摩挲铜牌的手指 | 3513 | normal | 91.7 | 0 |  | 2 |
| 5 | 盖章的手指 | 1652 | short | 89.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 11.4 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「林永年盯着那份单据看了许久，直到太阳快要落山才终…」）
- 第 2 章：
  - 单条套路句式超限：「林永年的」×6
  - attr_adv_pct 15.4 高于目标 10.0
  - [observe] 标题与《摩挲汇款单的手指》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「周桂花的」×6、「林永年的」×4、「带着一丝」×3
  - 情节与已写章节重复 0.63 ≥ 0.62（撞上「林永年发现一张泛黄汇款单上的地址与已废弃的渔村小学有关，…」）
  - narration_para_pct 18.2 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
  - [observe] 标题与《摩挲账本的手指》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - narration_para_pct 8.8 低于目标 20.0
  - [observe] 标题与《摩挲账本的手指》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 6.5 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13590
chapter_chars_mean: 2718
chapter_chars_median: 3082
chapter_chars_cv: 0.4
paragraphs_mean: 52.2
dialogue_chars_pct: 29.1
dialogue_para_pct: 73.4
interiority_para_pct: 11.7
narration_para_pct: 14.9
turn_under20_pct: 77.9
turn_over200_pct: 0.0
attr_say_pct: 19.8
attr_adv_pct: 8.2
scenes_per_chapter: 2.6
dialogue_run_mean: 4.8
turn_len_median: 12
```
