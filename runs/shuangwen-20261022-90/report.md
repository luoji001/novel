# 账本 生成报告

slug：`shuangwen-20261022-90`
档位：爽文　闸门模式：observe
章数：10　总字数：19621
LLM 调用：97 次，累计 428.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔下的账本风波 | 1632 | normal | 39.1 | 0 |  | 2 |
| 2 | 账本上的指纹密码 | 1865 | normal | 93.5 | 0 |  | 1 |
| 3 | 账本上的指纹密码 | 1840 | normal | 94.0 | 0 |  | 2 |
| 4 | 指纹下的贷款时间 | 2452 | normal | 88.5 | 0 |  | 4 |
| 5 | 指纹下的贷款时间 | 1529 | normal | 34.6 | 0 |  | 6 |
| 6 | 账本上的指纹密码 | 2170 | normal | 91.5 | 0 |  | 3 |
| 7 | 账本上的指纹密码 | 2058 | normal | 92.5 | 0 |  | 3 |
| 8 | 账本上的贷款编号 | 1769 | normal | 90.5 | 0 |  | 1 |
| 9 | 账本上的贷款编号 | 1516 | normal | 92.9 | 0 |  | 3 |
| 10 | 指纹下的贷款时间 | 2780 | long | 92.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「王建国的」×6
  - [observe] 章内自我复读 2 句（如「好吧，我给你一次机会…」）
- 第 2 章：
  - 单条套路句式超限：「王建国的」×3
- 第 3 章：
  - 单条套路句式超限：「王建国的」×3
  - [observe] 标题重复：「账本上的指纹密码」已存在
- 第 4 章：
  - 单条套路句式超限：「王建国的」×4
  - narration_para_pct 2.0 低于目标 5.0
  - attr_adv_pct 13.3 高于目标 12.0
  - dialogue_run_mean 25 高于目标 14.0
- 第 5 章：
  - 单条套路句式超限：「王建国的」×3、「李小强的」×3
  - dialogue_chars_pct 71.7 高于目标 70.0
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 30 高于目标 14.0
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「指纹下的贷款时间」已存在
- 第 6 章：
  - 单条套路句式超限：「王建国的」×7、「李小强的」×6
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「账本上的指纹密码」已存在
- 第 7 章：
  - 单条套路句式超限：「王建国的」×5
  - attr_adv_pct 13.6 高于目标 12.0
  - [observe] 标题重复：「账本上的指纹密码」已存在
- 第 8 章：
  - 单条套路句式超限：「王建国的」×6
- 第 9 章：
  - 命中套话收尾句
  - 单条套路句式超限：「王建国的」×5
  - [observe] 标题重复：「账本上的贷款编号」已存在
- 第 10 章：
  - 单条套路句式超限：「李小强的」×7、「王建国的」×6
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「指纹下的贷款时间」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18668
chapter_chars_mean: 1867
chapter_chars_median: 1768
chapter_chars_cv: 0.21
paragraphs_mean: 39.1
dialogue_chars_pct: 51.3
dialogue_para_pct: 85.9
interiority_para_pct: 4.5
narration_para_pct: 9.6
turn_under20_pct: 68.4
turn_over200_pct: 0.0
attr_say_pct: 22.7
attr_adv_pct: 10.1
scenes_per_chapter: 1.5
dialogue_run_mean: 10.6
turn_len_median: 14
```
