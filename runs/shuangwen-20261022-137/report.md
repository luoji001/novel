# 账单 生成报告

slug：`shuangwen-20261022-137`
档位：爽文　闸门模式：observe
章数：10　总字数：19238
LLM 调用：97 次，累计 444.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账单与地图的错位 | 1862 | normal | 100.0 | 0 |  | 1 |
| 2 | 账单与地图的错位 | 1819 | normal | 92.1 | 0 |  | 2 |
| 3 | 账单上的裂痕 | 1894 | normal | 37.6 | 0 |  | 2 |
| 4 | 账单指向木桌裂痕 | 1880 | normal | 36.9 | 0 |  | 2 |
| 5 | 账单指向木桌裂痕 | 1607 | normal | 94.1 | 0 |  | 2 |
| 6 | 账单指向木桌裂痕 | 1997 | normal | 92.8 | 0 |  | 3 |
| 7 | 账单指向木桌裂痕 | 1770 | normal | 94.2 | 0 |  | 2 |
| 8 | 账单指向木桌裂痕 | 1918 | normal | 87.7 | 0 |  | 4 |
| 9 | 账单指向木桌裂痕 | 1994 | normal | 92.7 | 0 |  | 2 |
| 10 | 账单指向木桌裂痕 | 2487 | long | 92.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李秋生的」×6
- 第 2 章：
  - 单条套路句式超限：「赵长风的」×11
  - [observe] 标题重复：「账单与地图的错位」已存在
- 第 3 章：
  - 单条套路句式超限：「赵长风的」×5、「山门登记处」×3
  - [observe] attr_adv_pct 35.7 > 25.0（结构塌缩）
- 第 4 章：
  - dialogue_run_mean 15 高于目标 14.0
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「赵长风的」×4
  - [observe] 标题重复：「账单指向木桌裂痕」已存在
- 第 6 章：
  - 单条套路句式超限：「赵长风的」×4、「知道自己」×3
  - attr_adv_pct 15.4 高于目标 12.0
  - [observe] 标题重复：「账单指向木桌裂痕」已存在
- 第 7 章：
  - 单条套路句式超限：「赵长风的」×7
  - [observe] 标题重复：「账单指向木桌裂痕」已存在
- 第 8 章：
  - dialogue_chars_pct 73.4 高于目标 70.0
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 44 高于目标 14.0
  - [observe] 标题重复：「账单指向木桌裂痕」已存在
- 第 9 章：
  - 单条套路句式超限：「山门登记处」×7、「赵长风的」×3
  - [observe] 标题重复：「账单指向木桌裂痕」已存在
- 第 10 章：
  - 单条套路句式超限：「赵长风的」×6、「他知道这」×3
  - attr_adv_pct 19.0 高于目标 12.0
  - [observe] 标题重复：「账单指向木桌裂痕」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18242
chapter_chars_mean: 1824
chapter_chars_median: 1796
chapter_chars_cv: 0.12
paragraphs_mean: 41.4
dialogue_chars_pct: 53.6
dialogue_para_pct: 86.8
interiority_para_pct: 4.0
narration_para_pct: 9.1
turn_under20_pct: 70.6
turn_over200_pct: 0.0
attr_say_pct: 22.5
attr_adv_pct: 13.8
scenes_per_chapter: 1.5
dialogue_run_mean: 11.3
turn_len_median: 14
```
