# 铁盒 生成报告

slug：`shipin-20261027-359`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6199
LLM 调用：57 次，累计 126.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙转动 | 556 | short | 16.5 | 0 |  | 3 |
| 2 | 钥匙转动 | 1107 | normal | 53.6 | 0 |  | 1 |
| 3 | 钥匙触碰玻璃 | 1343 | normal | 92.7 | 0 |  | 1 |
| 4 | 钥匙触碰玻璃 | 1029 | normal | 14.9 | 0 |  | 3 |
| 5 | 钥匙触碰玻璃 | 1030 | normal | 92.0 | 0 |  | 2 |
| 6 | 撬棍抵屏 | 1128 | normal | 91.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 1.2 低于目标 5.0
  - narration_para_pct 93.8 高于目标 90.0
  - [observe] 章节过短 512 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 标题重复：「钥匙转动」已存在
- 第 3 章：
  - 单条套路句式超限：「小林站在」×4
- 第 4 章：
  - [observe] 章内自我复读 9 句（如「他皱眉看着屏幕，拇指擦过屏幕表面…」）
  - [observe] 章节过短 842 < 870（本章目标 1582 字的 55%）
  - [observe] 标题重复：「钥匙触碰玻璃」已存在
- 第 5 章：
  - dialogue_chars_pct 3.2 低于目标 5.0
  - [observe] 标题重复：「钥匙触碰玻璃」已存在
- 第 6 章：
  - 单条套路句式超限：「小林站在」×3

## 整书结构指标

```
chapters: 6
total_chars: 5562
chapter_chars_mean: 927
chapter_chars_median: 943
chapter_chars_cv: 0.27
paragraphs_mean: 38.8
dialogue_chars_pct: 13.8
dialogue_para_pct: 28.8
interiority_para_pct: 1.5
narration_para_pct: 69.8
turn_under20_pct: 95.8
turn_over200_pct: 0.0
attr_say_pct: 9.8
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 1.4
turn_len_median: 8
```
