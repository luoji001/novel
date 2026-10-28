# 胶片 生成报告

slug：`shipin-20261027-165`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6823
LLM 调用：57 次，累计 130.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 抚摸铜耳环 | 523 | short | 37.8 | 0 |  | 1 |
| 2 | 触碰放映机裂痕 | 1378 | normal | 94.5 | 0 |  | 0 |
| 3 | 触碰放映机裂痕 | 1136 | normal | 91.3 | 0 |  | 1 |
| 4 | 触碰放映机裂痕 | 1366 | normal | 90.6 | 0 |  | 1 |
| 5 | 擦拭螺丝刀 | 1229 | normal | 91.6 | 0 |  | 0 |
| 6 | 触碰铜耳环 | 1185 | normal | 7.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 486 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - [observe] 标题重复：「触碰放映机裂痕」已存在
- 第 4 章：
  - [observe] 标题重复：「触碰放映机裂痕」已存在
- 第 6 章：
  - interiority_para_pct 14.3 高于目标 6.0
  - dialogue_run_mean 5 高于目标 4.0
  - [observe] 标题与《抚摸铜耳环》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6413
chapter_chars_mean: 1069
chapter_chars_median: 1147
chapter_chars_cv: 0.28
paragraphs_mean: 26.7
dialogue_chars_pct: 25.3
dialogue_para_pct: 51.3
interiority_para_pct: 2.5
narration_para_pct: 46.2
turn_under20_pct: 84.0
turn_over200_pct: 0.0
attr_say_pct: 47.1
attr_adv_pct: 0.0
scenes_per_chapter: 2.7
dialogue_run_mean: 2.1
turn_len_median: 10
```
