# 雨靴的归属 生成报告

slug：`shipin-20261027-173`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5861
LLM 调用：57 次，累计 120.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲杯声 | 842 | short | 96.5 | 0 |  | 0 |
| 2 | 钥匙与雨靴的对峙 | 861 | normal | 37.6 | 0 |  | 1 |
| 3 | 靴子与纸条的相遇 | 1124 | normal | 37.6 | 0 |  | 2 |
| 4 | 面饼悬空 | 944 | normal | 90.1 | 0 |  | 1 |
| 5 | 保温杯的回声 | 1035 | normal | 92.1 | 0 |  | 2 |
| 6 | 钥匙转动的瞬间 | 1049 | normal | 91.4 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章节过短 765 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - 单条套路句式超限：「陈素英站在」×3
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
- 第 4 章：
  - dialogue_chars_pct 3.9 低于目标 5.0
- 第 5 章：
  - 单条套路句式超限：「陈素英的」×3
  - narration_para_pct 32.4 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 5371
chapter_chars_mean: 895
chapter_chars_median: 918
chapter_chars_cv: 0.12
paragraphs_mean: 33.3
dialogue_chars_pct: 15.1
dialogue_para_pct: 35.9
interiority_para_pct: 1.2
narration_para_pct: 62.9
turn_under20_pct: 96.6
turn_over200_pct: 0.0
attr_say_pct: 16.4
attr_adv_pct: 7.8
scenes_per_chapter: 2
dialogue_run_mean: 1.9
turn_len_median: 8
```
