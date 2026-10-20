# 蓝布 生成报告

slug：`xuanyi-20261019-54`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14458
LLM 调用：68 次，累计 238.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙在掌心发烫 | 2011 | short | 96.8 | 0 |  | 0 |
| 2 | 账本滑落桌面 | 3565 | normal | 92.0 | 0 |  | 2 |
| 3 | 抚摸蓝色棉布纹理 | 3631 | normal | 91.0 | 0 |  | 2 |
| 4 | 撕碎的进货单浮现 | 3466 | normal | 90.8 | 0 |  | 2 |
| 5 | 擦拭木牌上的灰尘 | 1780 | short | 91.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「周玉兰点了点头」×3、「供销社」×3
  - narration_para_pct 15.1 低于目标 20.0
- 第 3 章：
  - narration_para_pct 13.7 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「陈德发站在」×3、「带着一丝」×3
  - narration_para_pct 7.3 低于目标 20.0
- 第 5 章：
  - narration_para_pct 15.6 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13796
chapter_chars_mean: 2759
chapter_chars_median: 3286
chapter_chars_cv: 0.32
paragraphs_mean: 58
dialogue_chars_pct: 41.5
dialogue_para_pct: 77.4
interiority_para_pct: 9.0
narration_para_pct: 13.6
turn_under20_pct: 70.2
turn_over200_pct: 0.0
attr_say_pct: 20.3
attr_adv_pct: 4.6
scenes_per_chapter: 3.8
dialogue_run_mean: 5.6
turn_len_median: 14
```
