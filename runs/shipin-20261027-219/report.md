# 钥心 生成报告

slug：`shipin-20261027-219`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5583
LLM 调用：57 次，累计 112.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 关闭摄像头的红光 | 642 | short | 21.6 | 0 |  | 2 |
| 2 | 写下日期的红色记事本 | 1148 | normal | 91.4 | 0 |  | 0 |
| 3 | 钥匙串坠入口袋的瞬间 | 669 | normal | 16.7 | 0 |  | 3 |
| 4 | 红色腕带的温度 | 813 | normal | 20.3 | 0 |  | 3 |
| 5 | 触摸钥匙背面的刻痕 | 1190 | normal | 82.2 | 0 |  | 2 |
| 6 | 屏幕角落的模糊身影 | 1115 | normal | 88.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 3.8 低于目标 5.0
  - [observe] 章节过短 584 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 610 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - dialogue_chars_pct 2.4 低于目标 5.0
  - narration_para_pct 94.6 高于目标 90.0
  - [observe] 章节过短 633 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - dialogue_chars_pct 3.4 低于目标 5.0
  - interiority_para_pct 9.5 高于目标 6.0
- 第 6 章：
  - interiority_para_pct 7.7 高于目标 6.0

## 整书结构指标

```
chapters: 6
total_chars: 5066
chapter_chars_mean: 844
chapter_chars_median: 840
chapter_chars_cv: 0.31
paragraphs_mean: 29.5
dialogue_chars_pct: 7.8
dialogue_para_pct: 22.8
interiority_para_pct: 5.3
narration_para_pct: 71.9
turn_under20_pct: 98.6
turn_over200_pct: 0.0
attr_say_pct: 58.4
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 1.1
turn_len_median: 9
```
