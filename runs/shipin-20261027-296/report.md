# 推子 生成报告

slug：`shipin-20261027-296`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5736
LLM 调用：57 次，累计 130.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 打磨镜子 | 604 | short | 37.6 | 0 |  | 1 |
| 2 | 擦拭镜子 | 1215 | normal | 91.6 | 0 |  | 0 |
| 3 | 称镜子 | 838 | normal | 34.1 | 0 |  | 4 |
| 4 | 打磨镜子 | 712 | normal | 16.8 | 0 |  | 4 |
| 5 | 写记账本 | 1032 | normal | 55.6 | 0 |  | 2 |
| 6 | 推子划镜 | 1329 | normal | 55.2 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 560 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 0.0 低于目标 35.0
  - dialogue_run_mean 6 高于目标 4.0
  - [observe] 章内自我复读 6 句（如「铜锈气息混着木屑味道漫过鼻腔，货架间的灰尘随着气…」）
  - [observe] 章节过短 815 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - dialogue_chars_pct 2.3 低于目标 5.0
  - narration_para_pct 96.7 高于目标 90.0
  - [observe] 章节过短 529 < 870（本章目标 1582 字的 55%）
  - [observe] 标题重复：「打磨镜子」已存在
- 第 5 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - interiority_para_pct 10.0 高于目标 6.0

## 整书结构指标

```
chapters: 6
total_chars: 5332
chapter_chars_mean: 889
chapter_chars_median: 908
chapter_chars_cv: 0.35
paragraphs_mean: 23
dialogue_chars_pct: 12.5
dialogue_para_pct: 34.3
interiority_para_pct: 2.0
narration_para_pct: 63.7
turn_under20_pct: 87.7
turn_over200_pct: 0.0
attr_say_pct: 26.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.3
turn_len_median: 10
```
