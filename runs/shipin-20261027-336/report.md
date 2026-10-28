# 药瓶传递 生成报告

slug：`shipin-20261027-336`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5872
LLM 调用：57 次，累计 123.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 紧握药瓶 | 644 | short | 94.3 | 0 |  | 0 |
| 2 | 药瓶倾斜痕迹 | 1050 | normal | 90.8 | 0 |  | 1 |
| 3 | 药瓶凹痕 | 863 | normal | 36.7 | 0 |  | 2 |
| 4 | 烧伤疤痕浮现 | 905 | normal | 36.6 | 0 |  | 2 |
| 5 | 药瓶传递 | 1295 | normal | 94.4 | 0 |  | 2 |
| 6 | 药瓶折射光芒 | 1109 | normal | 93.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「陈素云的」×3
- 第 3 章：
  - [observe] 章节过短 809 < 870（本章目标 1582 字的 55%）
  - [observe] 标题与《药瓶倾斜痕迹》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「林小满的」×5
  - [observe] 章节过短 829 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - 单条套路句式超限：「林小满的」×4
  - narration_para_pct 28.6 低于目标 35.0
- 第 6 章：
  - narration_para_pct 29.2 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 5470
chapter_chars_mean: 912
chapter_chars_median: 914
chapter_chars_cv: 0.23
paragraphs_mean: 26.5
dialogue_chars_pct: 21.7
dialogue_para_pct: 51.1
interiority_para_pct: 0.4
narration_para_pct: 48.4
turn_under20_pct: 90.8
turn_over200_pct: 0.0
attr_say_pct: 45.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 1.9
turn_len_median: 7
```
