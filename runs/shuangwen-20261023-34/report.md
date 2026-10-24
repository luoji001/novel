# 账本底稿 生成报告

slug：`shuangwen-20261023-34`
档位：爽文　闸门模式：observe
章数：10　总字数：18817
LLM 调用：97 次，累计 414.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔的墨迹 | 1714 | normal | 99.5 | 0 |  | 1 |
| 2 | 签字笔的墨迹 | 2187 | normal | 93.8 | 0 |  | 2 |
| 3 | 计算器的数字 | 1653 | normal | 93.7 | 0 |  | 1 |
| 4 | 账本底稿的对峙 | 2523 | normal | 90.7 | 0 |  | 4 |
| 5 | 账本边缘的空白处 | 1929 | normal | 92.8 | 0 |  | 1 |
| 6 | 账本边缘的空白处 | 1635 | normal | 93.4 | 0 |  | 3 |
| 7 | 撕碎的纸张 | 1783 | normal | 91.0 | 0 |  | 3 |
| 8 | 纸张边缘的褶痕 | 1467 | normal | 36.8 | 0 |  | 1 |
| 9 | 单据边缘的褶痕 | 1775 | normal | 88.9 | 0 |  | 3 |
| 10 | 账本底稿的对峙 | 2141 | long | 89.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 3.0 低于目标 5.0
- 第 2 章：
  - 单条套路句式超限：「陈志强的」×4
  - [observe] 标题重复：「签字笔的墨迹」已存在
- 第 3 章：
  - 单条套路句式超限：「他知道这」×4
- 第 4 章：
  - 单条套路句式超限：「陈志强点」×3
  - narration_para_pct 4.7 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 16.2 高于目标 14.0
- 第 5 章：
  - 单条套路句式超限：「周振华的」×4
- 第 6 章：
  - 单条套路句式超限：「周振华的」×3
  - narration_para_pct 3.2 低于目标 5.0
  - [observe] 标题重复：「账本边缘的空白处」已存在
- 第 7 章：
  - 单条套路句式超限：「陈志强的」×5
  - narration_para_pct 2.9 低于目标 5.0
  - dialogue_run_mean 17 高于目标 14.0
- 第 8 章：
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 9 章：
  - narration_para_pct 2.3 低于目标 5.0
  - dialogue_run_mean 42 高于目标 14.0
  - [observe] 标题与《纸张边缘的褶痕》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「陈志强的」×6、「变得更加」×3
  - narration_para_pct 2.3 低于目标 5.0
  - dialogue_run_mean 21.5 高于目标 14.0
  - [observe] 标题重复：「账本底稿的对峙」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17841
chapter_chars_mean: 1784
chapter_chars_median: 1686
chapter_chars_cv: 0.16
paragraphs_mean: 41
dialogue_chars_pct: 55.5
dialogue_para_pct: 88.8
interiority_para_pct: 4.2
narration_para_pct: 7.1
turn_under20_pct: 67.4
turn_over200_pct: 0.0
attr_say_pct: 24.5
attr_adv_pct: 8.5
scenes_per_chapter: 1.5
dialogue_run_mean: 13.2
turn_len_median: 14
```
