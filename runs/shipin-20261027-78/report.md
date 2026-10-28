# 鱼箱 生成报告

slug：`shipin-20261027-78`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6474
LLM 调用：57 次，累计 134.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 鱼刀划破塑料布 | 643 | short | 38.7 | 0 |  | 1 |
| 2 | 鱼刀割破塑料布 | 1156 | normal | 90.6 | 0 |  | 1 |
| 3 | 鱼秤坠地 | 685 | normal | 23.3 | 0 |  | 1 |
| 4 | 皮尺与鱼箱的对峙 | 1302 | normal | 90.2 | 0 |  | 2 |
| 5 | 鱼刀与银环相撞 | 1515 | normal | 91.2 | 0 |  | 3 |
| 6 | 鱼刀撬开鱼箱 | 1167 | normal | 91.0 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 590 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 标题与《鱼刀划破塑料布》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 章节过短 547 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - narration_para_pct 21.2 低于目标 35.0
  - dialogue_run_mean 5.2 高于目标 4.0
- 第 5 章：
  - narration_para_pct 21.1 低于目标 35.0
  - attr_adv_pct 14.3 高于目标 10.0
  - dialogue_run_mean 4.8 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 5945
chapter_chars_mean: 991
chapter_chars_median: 1082
chapter_chars_cv: 0.35
paragraphs_mean: 33
dialogue_chars_pct: 28.2
dialogue_para_pct: 58.9
interiority_para_pct: 1.2
narration_para_pct: 39.9
turn_under20_pct: 94.0
turn_over200_pct: 0.0
attr_say_pct: 50.5
attr_adv_pct: 3.8
scenes_per_chapter: 1.3
dialogue_run_mean: 2.7
turn_len_median: 10
```
