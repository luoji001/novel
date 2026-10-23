# 供奉凭证 生成报告

slug：`shuangwen-20261022-80`
档位：爽文　闸门模式：observe
章数：10　总字数：19567
LLM 调用：97 次，累计 457.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 登记簿上的划痕 | 2184 | normal | 39.2 | 0 |  | 1 |
| 2 | 墨迹未干的供奉凭证 | 1880 | normal | 37.0 | 0 |  | 1 |
| 3 | 墨迹未干的供奉凭证 | 1853 | normal | 37.0 | 0 |  | 3 |
| 4 | 供奉凭证的交接 | 1798 | normal | 36.1 | 0 |  | 2 |
| 5 | 撕碎的供奉名册 | 2093 | normal | 92.0 | 0 |  | 2 |
| 6 | 铜钱入掌 | 2065 | normal | 92.7 | 0 |  | 1 |
| 7 | 供奉凭证的交接 | 1982 | normal | 93.1 | 0 |  | 1 |
| 8 | 名册上的划痕浮现 | 1876 | normal | 93.5 | 0 |  | 1 |
| 9 | 银元入掌 | 1641 | normal | 90.6 | 0 |  | 2 |
| 10 | 银元入掌 | 2185 | long | 90.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 36.4 > 25.0（结构塌缩）
- 第 2 章：
  - [observe] attr_adv_pct 35.3 > 25.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「李怀远的」×3
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「墨迹未干的供奉凭证」已存在
- 第 4 章：
  - 单条套路句式超限：「李怀远的」×3
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「李怀远的」×8、「林九安的」×4
  - attr_adv_pct 14.3 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「李怀远的」×8
- 第 7 章：
  - [observe] 标题重复：「供奉凭证的交接」已存在
- 第 8 章：
  - attr_adv_pct 14.3 高于目标 12.0
- 第 9 章：
  - 单条套路句式超限：「李怀远的」×3
  - narration_para_pct 3.1 低于目标 5.0
- 第 10 章：
  - 单条套路句式超限：「李怀远的」×4
  - dialogue_run_mean 17.5 高于目标 14.0
  - [observe] 标题重复：「银元入掌」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18645
chapter_chars_mean: 1864
chapter_chars_median: 1834
chapter_chars_cv: 0.09
paragraphs_mean: 38.3
dialogue_chars_pct: 51.3
dialogue_para_pct: 86.6
interiority_para_pct: 4.6
narration_para_pct: 8.8
turn_under20_pct: 64.7
turn_over200_pct: 0.0
attr_say_pct: 16.2
attr_adv_pct: 16.4
scenes_per_chapter: 2.1
dialogue_run_mean: 8.5
turn_len_median: 16
```
