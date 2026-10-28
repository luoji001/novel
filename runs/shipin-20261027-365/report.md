# 银环 生成报告

slug：`shipin-20261027-365`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6950
LLM 调用：57 次，累计 140.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 夺袋 | 828 | short | 97.9 | 0 |  | 0 |
| 2 | 报纸在窗边 | 1423 | normal | 36.9 | 0 |  | 2 |
| 3 | 登记本在风中翻页 | 1227 | normal | 92.2 | 0 |  | 1 |
| 4 | 红布条落地 | 915 | normal | 36.9 | 0 |  | 1 |
| 5 | 银环滚落角落 | 1262 | normal | 92.5 | 0 |  | 2 |
| 6 | 铜钥匙在掌心晃动 | 1289 | normal | 92.0 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「王翠兰的」×3
  - [observe] attr_adv_pct 20.0 > 18.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「王翠兰的」×3
- 第 4 章：
  - [observe] 章节过短 858 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - 单条套路句式超限：「李建军的」×3
  - attr_adv_pct 14.3 高于目标 10.0

## 整书结构指标

```
chapters: 6
total_chars: 6480
chapter_chars_mean: 1080
chapter_chars_median: 1162
chapter_chars_cv: 0.2
paragraphs_mean: 31.8
dialogue_chars_pct: 22.9
dialogue_para_pct: 54.2
interiority_para_pct: 0.5
narration_para_pct: 45.3
turn_under20_pct: 96.8
turn_over200_pct: 0.0
attr_say_pct: 55.0
attr_adv_pct: 6.7
scenes_per_chapter: 1.5
dialogue_run_mean: 1.9
turn_len_median: 8
```
