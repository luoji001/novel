# 灯影 生成报告

slug：`shipin-20261027-06`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6529
LLM 调用：57 次，累计 138.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 应急灯微调位置 | 362 | short | 23.4 | 0 |  | 3 |
| 2 | 铅笔断在霜花中 | 1419 | normal | 92.4 | 0 |  | 1 |
| 3 | 铜铃静止 | 1355 | normal | 84.7 | 0 |  | 1 |
| 4 | 保温杯凝霜 | 1387 | normal | 91.7 | 0 |  | 2 |
| 5 | 试卷边缘摩挲 | 1109 | normal | 89.4 | 0 |  | 1 |
| 6 | 应急灯闪烁红光 | 891 | normal | 36.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 4.3 低于目标 5.0
  - interiority_para_pct 8.3 高于目标 6.0
  - [observe] 章节过短 323 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 31.2 低于目标 35.0
- 第 3 章：
  - interiority_para_pct 9.5 高于目标 6.0
- 第 4 章：
  - narration_para_pct 24.1 低于目标 35.0
  - dialogue_run_mean 4.2 高于目标 4.0
- 第 5 章：
  - 单条套路句式超限：「王小雨的」×3
- 第 6 章：
  - 单条套路句式超限：「李国强站在」×3
  - [observe] 章节过短 842 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 6167
chapter_chars_mean: 1028
chapter_chars_median: 1173
chapter_chars_cv: 0.39
paragraphs_mean: 22.7
dialogue_chars_pct: 18.2
dialogue_para_pct: 54.0
interiority_para_pct: 3.2
narration_para_pct: 42.8
turn_under20_pct: 96.4
turn_over200_pct: 0.0
attr_say_pct: 18.1
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 2.0
turn_len_median: 10
```
