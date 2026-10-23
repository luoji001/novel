# 旧磅单 生成报告

slug：`shuangwen-20261022-127`
档位：爽文　闸门模式：observe
章数：10　总字数：19413
LLM 调用：97 次，累计 423.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 校准电子秤 | 1836 | normal | 96.5 | 0 |  | 1 |
| 2 | 校准电子秤 | 2084 | normal | 89.8 | 0 |  | 2 |
| 3 | 划痕 | 1906 | normal | 91.8 | 0 |  | 0 |
| 4 | 捻纸一角 | 2244 | normal | 93.4 | 0 |  | 4 |
| 5 | 校准电子秤 | 2089 | normal | 93.5 | 0 |  | 2 |
| 6 | 签字权 | 1833 | normal | 37.0 | 0 |  | 1 |
| 7 | 校准电子秤 | 1601 | normal | 89.9 | 0 |  | 2 |
| 8 | 校准电子秤 | 1616 | normal | 92.1 | 0 |  | 2 |
| 9 | 拍桌 | 1753 | normal | 91.9 | 0 |  | 1 |
| 10 | 校准电子秤 | 2441 | long | 91.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3
- 第 2 章：
  - 单条套路句式超限：「李浩点了点头」×3
  - [observe] 标题重复：「校准电子秤」已存在
- 第 4 章：
  - 单条套路句式超限：「王主任的」×3
  - narration_para_pct 2.2 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - dialogue_run_mean 14.7 高于目标 14.0
- 第 5 章：
  - attr_adv_pct 15.8 高于目标 12.0
  - [observe] 标题重复：「校准电子秤」已存在
- 第 6 章：
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 7 章：
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「校准电子秤」已存在
- 第 8 章：
  - 命中套话收尾句
  - [observe] 标题重复：「校准电子秤」已存在
- 第 9 章：
  - 单条套路句式超限：「王主任的」×4
- 第 10 章：
  - 单条套路句式超限：「王主任的」×6
  - narration_para_pct 4.7 低于目标 5.0
  - [observe] 标题重复：「校准电子秤」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18490
chapter_chars_mean: 1849
chapter_chars_median: 1788
chapter_chars_cv: 0.14
paragraphs_mean: 38.9
dialogue_chars_pct: 45.8
dialogue_para_pct: 84.6
interiority_para_pct: 6.1
narration_para_pct: 9.3
turn_under20_pct: 66.4
turn_over200_pct: 0.0
attr_say_pct: 17.8
attr_adv_pct: 9.2
scenes_per_chapter: 2.3
dialogue_run_mean: 7.2
turn_len_median: 14
```
