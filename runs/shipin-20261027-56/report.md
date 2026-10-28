# 药瓶倾斜 生成报告

slug：`shipin-20261027-56`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5470
LLM 调用：57 次，累计 119.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药瓶紧贴胸口 | 600 | short | 21.9 | 0 |  | 1 |
| 2 | 药瓶与病历本相遇 | 1093 | normal | 89.8 | 0 |  | 2 |
| 3 | 药瓶紧贴胸口 | 1088 | normal | 92.2 | 0 |  | 2 |
| 4 | 药瓶跌地响 | 961 | normal | 90.9 | 0 |  | 0 |
| 5 | 体温计跌地响 | 704 | normal | 36.1 | 0 |  | 1 |
| 6 | 药瓶悬在空中 | 1018 | normal | 91.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 536 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「陈雪梅的」×4
  - dialogue_run_mean 4.7 高于目标 4.0
- 第 3 章：
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 标题重复：「药瓶紧贴胸口」已存在
- 第 5 章：
  - [observe] 章节过短 640 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - 单条套路句式超限：「陈雪梅的」×3

## 整书结构指标

```
chapters: 6
total_chars: 5047
chapter_chars_mean: 841
chapter_chars_median: 910
chapter_chars_cv: 0.24
paragraphs_mean: 27.5
dialogue_chars_pct: 23.7
dialogue_para_pct: 51.4
interiority_para_pct: 0.0
narration_para_pct: 48.6
turn_under20_pct: 96.6
turn_over200_pct: 0.0
attr_say_pct: 61.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.7
turn_len_median: 10
```
