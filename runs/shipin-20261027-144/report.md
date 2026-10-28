# 当票 生成报告

slug：`shipin-20261027-144`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6730
LLM 调用：57 次，累计 129.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 纸条的摩挲声 | 618 | short | 36.7 | 0 |  | 3 |
| 2 | 纸条的摩挲声 | 1004 | normal | 86.8 | 0 |  | 3 |
| 3 | 钥匙串的摇晃声 | 1304 | normal | 93.6 | 0 |  | 1 |
| 4 | 铁皮盒里的铅笔画 | 1138 | normal | 36.2 | 0 |  | 2 |
| 5 | 时刻表的摩挲声 | 1298 | normal | 92.9 | 0 |  | 1 |
| 6 | 纸条的摩挲声 | 1362 | normal | 37.3 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 5.6 低于目标 35.0
  - dialogue_run_mean 17 高于目标 4.0
  - [observe] 章节过短 568 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 16.0 低于目标 35.0
  - dialogue_run_mean 10.5 高于目标 4.0
  - [observe] 标题重复：「纸条的摩挲声」已存在
- 第 3 章：
  - narration_para_pct 33.3 低于目标 35.0
- 第 4 章：
  - narration_para_pct 91.1 高于目标 90.0
  - [observe] 章节过短 842 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - [observe] 标题与《纸条的摩挲声》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 23.4 低于目标 35.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
  - [observe] 标题重复：「纸条的摩挲声」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6021
chapter_chars_mean: 1004
chapter_chars_median: 1068
chapter_chars_cv: 0.27
paragraphs_mean: 44.7
dialogue_chars_pct: 28.7
dialogue_para_pct: 62.4
interiority_para_pct: 1.2
narration_para_pct: 36.4
turn_under20_pct: 99.0
turn_over200_pct: 0.0
attr_say_pct: 48.8
attr_adv_pct: 5.2
scenes_per_chapter: 2.2
dialogue_run_mean: 6.3
turn_len_median: 10
```
