# 红印 生成报告

slug：`shuangwen-20261022-60`
档位：爽文　闸门模式：observe
章数：10　总字数：19170
LLM 调用：97 次，累计 457.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 点朱砂 | 1559 | normal | 99.0 | 0 |  | 2 |
| 2 | 铜铃压红印 | 1844 | normal | 93.0 | 0 |  | 1 |
| 3 | 一袋银元压账簿 | 2190 | normal | 38.0 | 0 |  | 2 |
| 4 | 翻账见红印 | 1643 | normal | 37.1 | 0 |  | 3 |
| 5 | 翻账见红印 | 1950 | normal | 91.6 | 0 |  | 3 |
| 6 | 红印压账簿 | 1940 | normal | 36.4 | 0 |  | 2 |
| 7 | 点朱砂 | 2004 | normal | 87.6 | 0 |  | 4 |
| 8 | 翻账见红印 | 1730 | normal | 37.1 | 0 |  | 3 |
| 9 | 翻账见红印 | 1946 | normal | 91.8 | 0 |  | 4 |
| 10 | 点朱砂 | 2354 | long | 37.1 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李怀安的」×3
  - attr_adv_pct 12.5 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「李怀安的」×3
- 第 3 章：
  - 单条套路句式超限：「林子墨点」×3、「李怀安的」×3
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「李怀安的」×10
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 章内自我复读 2 句（如「因为我每天都在核对账目…」）
- 第 5 章：
  - 单条套路句式超限：「他知道这」×5
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「翻账见红印」已存在
- 第 6 章：
  - 单条套路句式超限：「李怀安的」×6
  - [observe] attr_adv_pct 36.4 > 25.0（结构塌缩）
- 第 7 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - dialogue_run_mean 34 高于目标 14.0
  - [observe] 标题重复：「点朱砂」已存在
- 第 8 章：
  - narration_para_pct 0.0 低于目标 5.0
  - [observe] attr_adv_pct 40.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「翻账见红印」已存在
- 第 9 章：
  - 单条套路句式超限：「李怀安的」×5
  - narration_para_pct 4.4 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「翻账见红印」已存在
- 第 10 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李怀安的」×8
  - [observe] attr_adv_pct 27.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「点朱砂」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18282
chapter_chars_mean: 1828
chapter_chars_median: 1849
chapter_chars_cv: 0.13
paragraphs_mean: 36.9
dialogue_chars_pct: 49.5
dialogue_para_pct: 86.8
interiority_para_pct: 5.3
narration_para_pct: 7.9
turn_under20_pct: 70.2
turn_over200_pct: 0.0
attr_say_pct: 22.1
attr_adv_pct: 22.5
scenes_per_chapter: 1.6
dialogue_run_mean: 9.4
turn_len_median: 14
```
