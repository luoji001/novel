# 欠条 生成报告

slug：`shuangwen-20261022-21`
档位：爽文　闸门模式：observe
章数：10　总字数：19889
LLM 调用：97 次，累计 372.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一笔旧账 | 1984 | normal | 98.5 | 0 |  | 1 |
| 2 | 欠条上的名字 | 1898 | normal | 92.6 | 0 |  | 3 |
| 3 | 欠条的背面 | 1748 | normal | 36.2 | 0 |  | 2 |
| 4 | 欠条的重量 | 1983 | normal | 91.3 | 0 |  | 2 |
| 5 | 欠条的重量 | 1803 | normal | 93.1 | 0 |  | 1 |
| 6 | 一份贷款凭证 | 2022 | normal | 91.7 | 0 |  | 3 |
| 7 | 欠条的重量 | 2076 | normal | 93.9 | 0 |  | 3 |
| 8 | 欠条的重量 | 2018 | normal | 37.4 | 0 |  | 6 |
| 9 | 手指摩挲欠条 | 2095 | normal | 93.2 | 0 |  | 1 |
| 10 | 手指摩挲欠条 | 2252 | long | 93.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「王振华的」×5
- 第 2 章：
  - narration_para_pct 2.1 低于目标 5.0
  - attr_adv_pct 22.2 高于目标 12.0
  - dialogue_run_mean 15 高于目标 14.0
- 第 3 章：
  - dialogue_run_mean 16.5 高于目标 14.0
  - [observe] attr_adv_pct 26.7 > 25.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「王振华的」×8
  - [observe] 标题与《欠条的背面》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 标题重复：「欠条的重量」已存在
- 第 6 章：
  - 单条套路句式超限：「王振华的」×7
  - narration_para_pct 2.6 低于目标 5.0
  - attr_adv_pct 18.8 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「王振华的」×5、「李国强的」×5
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「欠条的重量」已存在
- 第 8 章：
  - 单条套路句式超限：「王振华的」×3
  - 情节与已写章节重复 0.75 ≥ 0.7（撞上「李国强拿出欠条逼迫王振华承认三年前的债务，揭露其供货单未…」）
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 15.7 高于目标 14.0
  - [observe] attr_adv_pct 36.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「欠条的重量」已存在
- 第 9 章：
  - attr_adv_pct 20.0 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「王振华的」×7
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「手指摩挲欠条」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18840
chapter_chars_mean: 1884
chapter_chars_median: 1882
chapter_chars_cv: 0.08
paragraphs_mean: 45
dialogue_chars_pct: 49.7
dialogue_para_pct: 85.9
interiority_para_pct: 6.4
narration_para_pct: 7.7
turn_under20_pct: 74.6
turn_over200_pct: 0.0
attr_say_pct: 24.9
attr_adv_pct: 17.8
scenes_per_chapter: 1.6
dialogue_run_mean: 8.5
turn_len_median: 12
```
