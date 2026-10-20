# 水表暗格 生成报告

slug：`xuanyi-20261019-48`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14793
LLM 调用：68 次，累计 243.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 水表后的秘密 | 2006 | short | 98.3 | 0 |  | 1 |
| 2 | 剪刀与账单 | 3475 | normal | 87.7 | 0 |  | 4 |
| 3 | 水表下的暗红印记 | 3804 | normal | 37.1 | 0 |  | 5 |
| 4 | 水表旁的皱纸 | 3516 | normal | 88.2 | 0 |  | 2 |
| 5 | 摩挲铜环 | 1987 | short | 93.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 19.6 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林振邦的」×4、「带着一丝」×3
  - narration_para_pct 12.3 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 章内自我复读 19 句（如「然而就在那一刻，他忽然停下手中的动作——一个念头…」）
- 第 3 章：
  - 单条套路句式超限：「林振邦的」×6、「林振邦站在」×3、「他知道这」×3
  - dialogue_chars_pct 11.2 低于目标 20.0
  - interiority_para_pct 23.3 高于目标 20.0
  - dialogue_run_mean 1.3 低于目标 1.5
  - [observe] 章内自我复读 20 句（如「当他摸到一件黑色的裤子时，突然想起了什么，快速地…」）
- 第 4 章：
  - 单条套路句式超限：「林振邦站在」×4、「为什么会」×4、「他知道这」×3
  - dialogue_chars_pct 18.2 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「林振邦的」×4
  - narration_para_pct 15.0 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 14203
chapter_chars_mean: 2841
chapter_chars_median: 3348
chapter_chars_cv: 0.31
paragraphs_mean: 51.6
dialogue_chars_pct: 24.8
dialogue_para_pct: 59.0
interiority_para_pct: 17.5
narration_para_pct: 23.5
turn_under20_pct: 74.4
turn_over200_pct: 0.0
attr_say_pct: 25.6
attr_adv_pct: 5.0
scenes_per_chapter: 4.4
dialogue_run_mean: 3.1
turn_len_median: 12
```
