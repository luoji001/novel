# 铜推子 生成报告

slug：`shipin-20261027-226`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5698
LLM 调用：57 次，累计 118.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 推子轻响 | 461 | short | 14.4 | 0 |  | 3 |
| 2 | 推子轻响 | 1128 | normal | 58.4 | 0 |  | 1 |
| 3 | 摩挲账本 | 935 | normal | 37.0 | 0 |  | 1 |
| 4 | 摩挲推子 | 1302 | normal | 89.2 | 0 |  | 1 |
| 5 | 推子嗡鸣 | 872 | normal | 36.0 | 0 |  | 2 |
| 6 | 撕碎账页 | 994 | normal | 59.0 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 395 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 标题重复：「推子轻响」已存在
- 第 3 章：
  - [observe] 章节过短 869 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - narration_para_pct 20.7 低于目标 35.0
- 第 5 章：
  - 单条套路句式超限：「老张站在」×3
  - [observe] 章节过短 773 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5229
chapter_chars_mean: 872
chapter_chars_median: 902
chapter_chars_cv: 0.32
paragraphs_mean: 32.5
dialogue_chars_pct: 26.4
dialogue_para_pct: 45.8
interiority_para_pct: 2.0
narration_para_pct: 52.1
turn_under20_pct: 91.7
turn_over200_pct: 0.0
attr_say_pct: 29.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.7
turn_len_median: 10
```
