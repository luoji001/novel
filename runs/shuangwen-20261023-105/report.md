# 玉牌风波 生成报告

slug：`shuangwen-20261023-105`
档位：爽文　闸门模式：observe
章数：10　总字数：19280
LLM 调用：97 次，累计 453.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 玉牌映符文 | 1747 | normal | 99.4 | 0 |  | 2 |
| 2 | 玉牌现龙纹 | 2002 | normal | 37.5 | 0 |  | 1 |
| 3 | 玉牌映龙纹 | 1922 | normal | 93.2 | 0 |  | 2 |
| 4 | 玉牌现龙纹 | 1901 | normal | 88.1 | 0 |  | 4 |
| 5 | 玉牌现龙纹 | 2012 | normal | 92.9 | 0 |  | 3 |
| 6 | 玉牌现龙纹 | 1870 | normal | 92.9 | 0 |  | 3 |
| 7 | 玉牌按典籍 | 1940 | normal | 93.6 | 0 |  | 1 |
| 8 | 玉牌映符文 | 1768 | normal | 92.9 | 0 |  | 3 |
| 9 | 玉牌换令牌 | 1688 | normal | 93.5 | 0 |  | 0 |
| 10 | 玉牌落石碑 | 2420 | long | 90.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「藏经阁」×3
  - attr_adv_pct 23.5 高于目标 12.0
- 第 2 章：
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 3 章：
  - narration_para_pct 2.6 低于目标 5.0
  - [observe] 标题与《玉牌现龙纹》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「林子安的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 44 高于目标 14.0
  - [observe] 标题重复：「玉牌现龙纹」已存在
- 第 5 章：
  - 单条套路句式超限：「李长风的」×5、「藏经阁」×3
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题重复：「玉牌现龙纹」已存在
- 第 6 章：
  - 单条套路句式超限：「李长风的」×8
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「玉牌现龙纹」已存在
- 第 7 章：
  - 单条套路句式超限：「藏经阁」×4
- 第 8 章：
  - 单条套路句式超限：「李长风的」×6、「藏经阁」×3
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「玉牌映符文」已存在
- 第 10 章：
  - 单条套路句式超限：「藏经阁」×8、「林子安的」×4、「李长风的」×3
  - attr_adv_pct 22.2 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 18265
chapter_chars_mean: 1826
chapter_chars_median: 1808
chapter_chars_cv: 0.11
paragraphs_mean: 43.8
dialogue_chars_pct: 49.6
dialogue_para_pct: 85.9
interiority_para_pct: 4.2
narration_para_pct: 9.8
turn_under20_pct: 71.2
turn_over200_pct: 0.0
attr_say_pct: 20.9
attr_adv_pct: 14.7
scenes_per_chapter: 1.7
dialogue_run_mean: 10.2
turn_len_median: 13
```
