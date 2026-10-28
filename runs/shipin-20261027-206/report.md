# 铜匙 生成报告

slug：`shipin-20261027-206`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6111
LLM 调用：57 次，累计 137.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙板滑落桌面 | 672 | short | 95.6 | 0 |  | 0 |
| 2 | 钥匙滑落桌面 | 1114 | normal | 90.7 | 0 |  | 2 |
| 3 | 水壶裂痕与钥匙凹痕 | 1069 | normal | 36.5 | 0 |  | 1 |
| 4 | 钥匙滑落桌面 | 1213 | normal | 88.2 | 0 |  | 3 |
| 5 | 房卡边缘的划痕 | 1063 | normal | 90.7 | 0 |  | 2 |
| 6 | 擦拭玻璃上的雾气 | 974 | normal | 42.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 29.0 低于目标 35.0
  - [observe] 标题与《钥匙板滑落桌面》近似 0.92 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 章内自我复读 2 句（如「下午三点之后就没客人了…」）
- 第 4 章：
  - narration_para_pct 21.7 低于目标 35.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - [observe] 标题重复：「钥匙滑落桌面」已存在
- 第 5 章：
  - narration_para_pct 18.2 低于目标 35.0
  - dialogue_run_mean 6 高于目标 4.0
- 第 6 章：
  - dialogue_chars_pct 0.9 低于目标 5.0
  - narration_para_pct 95.2 高于目标 90.0

## 整书结构指标

```
chapters: 6
total_chars: 5727
chapter_chars_mean: 954
chapter_chars_median: 998
chapter_chars_cv: 0.19
paragraphs_mean: 23.7
dialogue_chars_pct: 23.4
dialogue_para_pct: 57.5
interiority_para_pct: 0.0
narration_para_pct: 42.5
turn_under20_pct: 94.1
turn_over200_pct: 0.0
attr_say_pct: 90.9
attr_adv_pct: 0.0
scenes_per_chapter: 2.3
dialogue_run_mean: 2.9
turn_len_median: 10
```
