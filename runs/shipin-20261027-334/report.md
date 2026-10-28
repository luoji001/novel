# 硬币密码 生成报告

slug：`shipin-20261027-334`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5840
LLM 调用：57 次，累计 122.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 捡起硬币的清晨 | 614 | short | 37.0 | 0 |  | 2 |
| 2 | 摩挲硬币的清晨 | 1045 | normal | 92.0 | 0 |  | 1 |
| 3 | 回放硬币的时刻 | 932 | normal | 23.0 | 0 |  | 3 |
| 4 | 摩挲钥匙串的清晨 | 1109 | normal | 95.6 | 0 |  | 3 |
| 5 | 摩挲停车牌的清晨 | 964 | normal | 59.3 | 0 |  | 1 |
| 6 | 摩挲硬币的清晨 | 1170 | normal | 90.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 7.1 高于目标 6.0
  - [observe] 章节过短 571 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 标题与《捡起硬币的清晨》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - dialogue_chars_pct 4.0 低于目标 5.0
  - narration_para_pct 94.4 高于目标 90.0
  - [observe] 章节过短 721 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - narration_para_pct 28.6 低于目标 35.0
  - dialogue_run_mean 4.2 高于目标 4.0
  - [observe] 标题与《摩挲硬币的清晨》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 标题与《摩挲硬币的清晨》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 4.5 低于目标 5.0
  - [observe] 标题重复：「摩挲硬币的清晨」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5318
chapter_chars_mean: 886
chapter_chars_median: 945
chapter_chars_cv: 0.23
paragraphs_mean: 30.8
dialogue_chars_pct: 10.8
dialogue_para_pct: 34.3
interiority_para_pct: 1.9
narration_para_pct: 63.8
turn_under20_pct: 100.0
turn_over200_pct: 0.0
attr_say_pct: 39.9
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 1.7
turn_len_median: 7
```
