# 雨靴的归属 生成报告

slug：`shipin-20261027-159`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6596
LLM 调用：57 次，累计 135.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扫帚敲击垃圾桶 | 780 | short | 95.2 | 0 |  | 0 |
| 2 | 靴子与按钮的争执 | 1222 | normal | 94.7 | 0 |  | 2 |
| 3 | 钥匙与雨靴的对峙 | 1324 | normal | 36.9 | 0 |  | 1 |
| 4 | 纸条与维修记录 | 1028 | normal | 37.0 | 0 |  | 1 |
| 5 | 触摸靴底的裂痕 | 851 | normal | 22.4 | 0 |  | 1 |
| 6 | 拾靴如拾旧时光 | 1385 | normal | 95.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 27.8 低于目标 35.0
  - dialogue_run_mean 4.3 高于目标 4.0
- 第 3 章：
  - [observe] 章内自我复读 2 句（如「上周有人报修，说电梯常停在七楼…」）
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「他翻了几页，语气带着几分无奈，“上周还特意跑来交…」）
- 第 5 章：
  - [observe] 章节过短 798 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - interiority_para_pct 6.2 高于目标 6.0
  - narration_para_pct 21.9 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 6230
chapter_chars_mean: 1038
chapter_chars_median: 1066
chapter_chars_cv: 0.24
paragraphs_mean: 22.3
dialogue_chars_pct: 19.8
dialogue_para_pct: 57.1
interiority_para_pct: 2.6
narration_para_pct: 40.3
turn_under20_pct: 94.5
turn_over200_pct: 0.0
attr_say_pct: 53.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.3
turn_len_median: 10
```
