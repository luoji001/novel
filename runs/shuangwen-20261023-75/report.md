# 私章 生成报告

slug：`shuangwen-20261023-75`
档位：爽文　闸门模式：observe
章数：10　总字数：19408
LLM 调用：97 次，累计 431.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 验收单边角摩挲 | 2003 | normal | 39.1 | 0 |  | 2 |
| 2 | 验收单边角摩挲 | 2068 | normal | 92.1 | 0 |  | 1 |
| 3 | 验收单边角摩挲 | 1825 | normal | 92.3 | 0 |  | 2 |
| 4 | 验收单边角摩挲 | 2037 | normal | 92.5 | 0 |  | 2 |
| 5 | 验收单边角摩挲 | 1742 | normal | 37.1 | 0 |  | 3 |
| 6 | 验收单边角摩挲 | 1797 | normal | 93.7 | 0 |  | 2 |
| 7 | 验收单边角摩挲 | 1836 | normal | 91.5 | 0 |  | 4 |
| 8 | 验收单边角摩挲 | 1788 | normal | 91.3 | 0 |  | 4 |
| 9 | 验收单边角摩挲 | 1842 | normal | 92.8 | 0 |  | 2 |
| 10 | 红印晕染成花朵 | 2460 | long | 89.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×4、「他知道这」×3
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 2 章：
  - [observe] 标题重复：「验收单边角摩挲」已存在
- 第 3 章：
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「验收单边角摩挲」已存在
- 第 4 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「验收单边角摩挲」已存在
- 第 5 章：
  - 单条套路句式超限：「陈晓阳的」×3
  - [observe] attr_adv_pct 50.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「验收单边角摩挲」已存在
- 第 6 章：
  - narration_para_pct 3.4 低于目标 5.0
  - [observe] 标题重复：「验收单边角摩挲」已存在
- 第 7 章：
  - narration_para_pct 2.5 低于目标 5.0
  - attr_adv_pct 18.8 高于目标 12.0
  - dialogue_run_mean 19.5 高于目标 14.0
  - [observe] 标题重复：「验收单边角摩挲」已存在
- 第 8 章：
  - narration_para_pct 4.8 低于目标 5.0
  - attr_adv_pct 23.1 高于目标 12.0
  - dialogue_run_mean 19 高于目标 14.0
  - [observe] 标题重复：「验收单边角摩挲」已存在
- 第 9 章：
  - narration_para_pct 2.5 低于目标 5.0
  - [observe] 标题重复：「验收单边角摩挲」已存在
- 第 10 章：
  - 单条套路句式超限：「李国强点」×4
  - narration_para_pct 2.0 低于目标 5.0
  - dialogue_run_mean 24 高于目标 14.0

## 整书结构指标

```
chapters: 10
total_chars: 18422
chapter_chars_mean: 1842
chapter_chars_median: 1744
chapter_chars_cv: 0.12
paragraphs_mean: 40.5
dialogue_chars_pct: 50.1
dialogue_para_pct: 86.2
interiority_para_pct: 4.6
narration_para_pct: 9.2
turn_under20_pct: 70.9
turn_over200_pct: 0.0
attr_say_pct: 25.3
attr_adv_pct: 15.5
scenes_per_chapter: 2.2
dialogue_run_mean: 10.9
turn_len_median: 13
```
