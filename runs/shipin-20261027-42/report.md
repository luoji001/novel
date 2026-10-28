# 药瓶归属 生成报告

slug：`shipin-20261027-42`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5980
LLM 调用：57 次，累计 127.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红绳与登记本 | 456 | short | 37.7 | 0 |  | 1 |
| 2 | 登记本的褶皱 | 960 | normal | 89.2 | 0 |  | 2 |
| 3 | 输液架上的药瓶 | 973 | normal | 36.6 | 0 |  | 1 |
| 4 | 药瓶坠地回声 | 1220 | normal | 93.0 | 0 |  | 0 |
| 5 | 药瓶与玻璃裂痕 | 1199 | normal | 91.4 | 0 |  | 2 |
| 6 | 药瓶与登记本的褶皱 | 1166 | normal | 85.4 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 408 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 33.3 低于目标 35.0
  - dialogue_run_mean 4.5 高于目标 4.0
- 第 3 章：
  - [observe] 章节过短 858 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - 单条套路句式超限：「张晓梅的」×4
  - attr_adv_pct 14.3 高于目标 10.0
- 第 6 章：
  - 单条套路句式超限：「周素芬的」×3
  - interiority_para_pct 9.1 高于目标 6.0
  - narration_para_pct 31.8 低于目标 35.0
  - [observe] 标题与《登记本的褶皱》近似 0.80 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5553
chapter_chars_mean: 926
chapter_chars_median: 998
chapter_chars_cv: 0.31
paragraphs_mean: 27.7
dialogue_chars_pct: 23.8
dialogue_para_pct: 54.2
interiority_para_pct: 1.8
narration_para_pct: 44.0
turn_under20_pct: 95.4
turn_over200_pct: 0.0
attr_say_pct: 39.0
attr_adv_pct: 3.8
scenes_per_chapter: 1.3
dialogue_run_mean: 2.5
turn_len_median: 10
```
