# 雨靴 生成报告

slug：`shipin-20261027-47`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6609
LLM 调用：57 次，累计 139.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙与雨靴对峙 | 606 | short | 39.5 | 0 |  | 1 |
| 2 | 雨靴与拐杖对峙 | 1054 | normal | 90.9 | 0 |  | 0 |
| 3 | 钥匙与落叶对峙 | 1279 | normal | 89.1 | 0 |  | 3 |
| 4 | 擦亮雨靴的夜晚 | 1408 | normal | 47.4 | 0 |  | 1 |
| 5 | 钥匙划过雨靴 | 1279 | normal | 90.6 | 0 |  | 1 |
| 6 | 钥匙触碰雨靴时刻 | 977 | normal | 35.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 561 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 16.7 低于目标 35.0
  - dialogue_run_mean 5 高于目标 4.0
  - [observe] 标题与《钥匙与雨靴对峙》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - dialogue_chars_pct 1.1 低于目标 5.0
- 第 5 章：
  - [observe] 标题与《钥匙与雨靴对峙》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 章节过短 859 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 6133
chapter_chars_mean: 1022
chapter_chars_median: 1072
chapter_chars_cv: 0.28
paragraphs_mean: 31.7
dialogue_chars_pct: 19.4
dialogue_para_pct: 37.5
interiority_para_pct: 1.3
narration_para_pct: 61.2
turn_under20_pct: 89.8
turn_over200_pct: 0.0
attr_say_pct: 73.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.1
turn_len_median: 10
```
