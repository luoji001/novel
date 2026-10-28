# 雨靴 生成报告

slug：`shipin-20261027-271`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6048
LLM 调用：57 次，累计 135.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 争夺钥匙 | 504 | short | 39.2 | 0 |  | 1 |
| 2 | 钥匙与冰碴 | 1028 | normal | 90.6 | 0 |  | 1 |
| 3 | 房产证上的印章 | 796 | normal | 23.9 | 0 |  | 3 |
| 4 | 钥匙落在地上的瞬间 | 1230 | normal | 91.7 | 0 |  | 0 |
| 5 | 叩击靴面 | 1143 | normal | 93.7 | 0 |  | 0 |
| 6 | 铁靴踏冰 | 1341 | normal | 94.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 458 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 22.2 低于目标 35.0
- 第 3 章：
  - dialogue_chars_pct 0.9 低于目标 5.0
  - narration_para_pct 97.2 高于目标 90.0
  - [observe] 章节过短 582 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - narration_para_pct 33.3 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 5469
chapter_chars_mean: 912
chapter_chars_median: 1028
chapter_chars_cv: 0.35
paragraphs_mean: 35.3
dialogue_chars_pct: 24.5
dialogue_para_pct: 53.0
interiority_para_pct: 1.1
narration_para_pct: 45.9
turn_under20_pct: 86.5
turn_over200_pct: 0.0
attr_say_pct: 23.4
attr_adv_pct: 0.0
scenes_per_chapter: 2.5
dialogue_run_mean: 1.9
turn_len_median: 10
```
