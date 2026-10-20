# 铜钥匙 生成报告

slug：`xuanyi-20261019-244`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14056
LLM 调用：68 次，累计 228.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 粮价表与地图的对照 | 1740 | short | 98.3 | 0 |  | 2 |
| 2 | 账本边缘的折痕 | 3609 | normal | 92.7 | 0 |  | 2 |
| 3 | 钥匙转动的瞬间 | 3511 | normal | 90.4 | 0 |  | 1 |
| 4 | 麻袋边的裂纹 | 3602 | normal | 90.3 | 0 |  | 3 |
| 5 | 印章边缘的折痕 | 1589 | short | 91.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 15.2 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「陈国栋的」×10、「周玉兰的」×8
  - narration_para_pct 5.6 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「陈国栋的」×5、「周玉兰的」×3、「他知道这」×3
- 第 4 章：
  - 单条套路句式超限：「陈国栋的」×11、「周玉兰的」×5
  - 情节与已写章节重复 0.66 ≥ 0.62（撞上「周玉兰发现粮价表与运输记录不符，质疑陈国栋隐瞒真相，两人…」）
  - narration_para_pct 9.0 低于目标 20.0
- 第 5 章：
  - narration_para_pct 8.8 低于目标 20.0
  - [observe] 标题与《账本边缘的折痕》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13421
chapter_chars_mean: 2684
chapter_chars_median: 3352
chapter_chars_cv: 0.38
paragraphs_mean: 55.4
dialogue_chars_pct: 43.0
dialogue_para_pct: 81.7
interiority_para_pct: 5.8
narration_para_pct: 12.5
turn_under20_pct: 71.4
turn_over200_pct: 0.0
attr_say_pct: 24.2
attr_adv_pct: 6.3
scenes_per_chapter: 3.6
dialogue_run_mean: 6.5
turn_len_median: 14
```
