# 旧磅单 生成报告

slug：`shuangwen-20261023-99`
档位：爽文　闸门模式：observe
章数：10　总字数：19875
LLM 调用：97 次，累计 426.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧磅单的重量 | 1910 | normal | 39.8 | 0 |  | 2 |
| 2 | 旧磅单的重量 | 1830 | normal | 89.5 | 0 |  | 3 |
| 3 | 签字笔的重量 | 1694 | normal | 93.3 | 0 |  | 1 |
| 4 | 签字笔的重量 | 2012 | normal | 93.2 | 0 |  | 1 |
| 5 | 旧磅单的重量 | 2088 | normal | 91.4 | 0 |  | 1 |
| 6 | 签字笔的重量 | 1953 | normal | 91.7 | 0 |  | 1 |
| 7 | 证件上的钢印 | 1897 | normal | 92.5 | 0 |  | 1 |
| 8 | 旧磅单的重量 | 1785 | normal | 89.5 | 0 |  | 1 |
| 9 | 旧磅单的重量 | 1819 | normal | 34.3 | 0 |  | 4 |
| 10 | 旧磅单的重量 | 2877 | long | 88.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] attr_adv_pct 26.3 > 25.0（结构塌缩）
- 第 2 章：
  - narration_para_pct 3.1 低于目标 5.0
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题重复：「旧磅单的重量」已存在
- 第 3 章：
  - 单条套路句式超限：「过磅房」×3
- 第 4 章：
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 5 章：
  - [observe] 标题重复：「旧磅单的重量」已存在
- 第 6 章：
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 7 章：
  - 单条套路句式超限：「点了点头」×3
- 第 8 章：
  - [observe] 标题重复：「旧磅单的重量」已存在
- 第 9 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 31 高于目标 14.0
  - [observe] attr_adv_pct 50.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「旧磅单的重量」已存在
- 第 10 章：
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题重复：「旧磅单的重量」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18871
chapter_chars_mean: 1887
chapter_chars_median: 1810
chapter_chars_cv: 0.17
paragraphs_mean: 42.7
dialogue_chars_pct: 45.4
dialogue_para_pct: 83.6
interiority_para_pct: 5.6
narration_para_pct: 10.8
turn_under20_pct: 70.1
turn_over200_pct: 0.0
attr_say_pct: 26.4
attr_adv_pct: 13.9
scenes_per_chapter: 2.1
dialogue_run_mean: 8.1
turn_len_median: 14
```
