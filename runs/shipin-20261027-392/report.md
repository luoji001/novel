# 药瓶 生成报告

slug：`shipin-20261027-392`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5518
LLM 调用：57 次，累计 123.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药瓶与登记本对峙 | 569 | short | 38.4 | 0 |  | 1 |
| 2 | 登记本上的裂痕 | 961 | normal | 90.9 | 0 |  | 3 |
| 3 | 注射器划破玻璃 | 994 | normal | 91.3 | 0 |  | 1 |
| 4 | 药瓶滚落输液椅 | 1028 | normal | 90.2 | 0 |  | 0 |
| 5 | 病历卡在光斑里 | 1090 | normal | 90.4 | 0 |  | 1 |
| 6 | 药瓶与病历卡对峙 | 870 | normal | 36.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 523 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「陈雪梅的」×3
  - narration_para_pct 30.4 低于目标 35.0
  - dialogue_run_mean 5.3 高于目标 4.0
- 第 3 章：
  - narration_para_pct 34.8 低于目标 35.0
- 第 5 章：
  - narration_para_pct 29.2 低于目标 35.0
- 第 6 章：
  - narration_para_pct 28.6 低于目标 35.0
  - [observe] 章节过短 812 < 870（本章目标 1582 字的 55%）
  - [observe] 标题与《药瓶与登记本对峙》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5162
chapter_chars_mean: 860
chapter_chars_median: 916
chapter_chars_cv: 0.21
paragraphs_mean: 21.5
dialogue_chars_pct: 26.8
dialogue_para_pct: 65.2
interiority_para_pct: 0.8
narration_para_pct: 34.0
turn_under20_pct: 94.8
turn_over200_pct: 0.0
attr_say_pct: 33.9
attr_adv_pct: 1.8
scenes_per_chapter: 1
dialogue_run_mean: 2.8
turn_len_median: 9
```
