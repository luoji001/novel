# 信绳 生成报告

slug：`shipin-20261027-162`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5873
LLM 调用：57 次，累计 153.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 争信 | 695 | short | 95.7 | 0 |  | 0 |
| 2 | 撕碎的账单一角 | 1213 | normal | 37.6 | 0 |  | 3 |
| 3 | 撕秤杆 | 913 | normal | 38.3 | 0 |  | 3 |
| 4 | 红布袋的提绳 | 1257 | normal | 36.2 | 0 |  | 1 |
| 5 | 摩挲账本边沿 | 797 | normal | 22.5 | 0 |  | 2 |
| 6 | 信封坠入鱼筐 | 992 | normal | 90.6 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「陈德发的」×6
  - narration_para_pct 34.2 低于目标 35.0
  - [observe] 章内自我复读 1 句（如「老张低头看着账单，眼神空洞…」）
- 第 3 章：
  - 单条套路句式超限：「陈德发的」×3
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 章节过短 842 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「老张愣了一下，随即摇头…」）
- 第 5 章：
  - narration_para_pct 92.4 高于目标 90.0
  - [observe] 章节过短 597 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5253
chapter_chars_mean: 876
chapter_chars_median: 866
chapter_chars_cv: 0.28
paragraphs_mean: 40.2
dialogue_chars_pct: 21.0
dialogue_para_pct: 42.5
interiority_para_pct: 0.0
narration_para_pct: 57.5
turn_under20_pct: 97.0
turn_over200_pct: 0.0
attr_say_pct: 39.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.5
turn_len_median: 8
```
