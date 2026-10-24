# 旧账本 生成报告

slug：`shuangwen-20261023-121`
档位：爽文　闸门模式：observe
章数：10　总字数：17109
LLM 调用：97 次，累计 422.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本与计算器的博弈 | 1469 | normal | 96.6 | 0 |  | 1 |
| 2 | 旧账本被计算器取代 | 1673 | normal | 36.8 | 0 |  | 2 |
| 3 | 签名指向旧账本 | 1641 | normal | 92.9 | 0 |  | 0 |
| 4 | 账本上的便条飘落 | 2141 | normal | 91.0 | 0 |  | 0 |
| 5 | 旧账本被计算器取代 | 1577 | normal | 92.4 | 0 |  | 1 |
| 6 | 账本上的旧签章 | 1486 | normal | 92.4 | 0 |  | 0 |
| 7 | 旧账本摊开时 | 1732 | normal | 89.6 | 0 |  | 2 |
| 8 | 账本推向对方 | 1391 | normal | 91.5 | 0 |  | 2 |
| 9 | 签字划去旧账本 | 1549 | normal | 93.1 | 0 |  | 2 |
| 10 | 签字笔划过旧账本 | 2440 | long | 37.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 12.5 高于目标 12.0
- 第 2 章：
  - narration_para_pct 2.9 低于目标 5.0
  - [observe] attr_adv_pct 40.0 > 25.0（结构塌缩）
- 第 5 章：
  - [observe] 标题重复：「旧账本被计算器取代」已存在
- 第 7 章：
  - narration_para_pct 3.8 低于目标 5.0
  - dialogue_run_mean 17 高于目标 14.0
- 第 8 章：
  - 单条套路句式超限：「李国强的」×3
  - attr_adv_pct 25.0 高于目标 12.0
- 第 9 章：
  - attr_adv_pct 18.8 高于目标 12.0
  - dialogue_run_mean 15 高于目标 14.0
- 第 10 章：
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题与《签字划去旧账本》近似 0.80 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 16117
chapter_chars_mean: 1612
chapter_chars_median: 1518
chapter_chars_cv: 0.19
paragraphs_mean: 41.2
dialogue_chars_pct: 51.4
dialogue_para_pct: 84.0
interiority_para_pct: 5.9
narration_para_pct: 10.1
turn_under20_pct: 74.6
turn_over200_pct: 0.0
attr_say_pct: 28.7
attr_adv_pct: 16.0
scenes_per_chapter: 1.7
dialogue_run_mean: 8.7
turn_len_median: 12
```
