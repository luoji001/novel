# 旧账本 生成报告

slug：`shuangwen-20261023-146`
档位：爽文　闸门模式：observe
章数：10　总字数：18487
LLM 调用：97 次，累计 429.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 秤杆的重量 | 1743 | normal | 40.0 | 0 |  | 2 |
| 2 | 朱砂笔的痕迹 | 1694 | normal | 95.4 | 0 |  | 2 |
| 3 | 账本上的签名线 | 1980 | normal | 93.6 | 0 |  | 1 |
| 4 | 称重的砝码 | 1687 | normal | 94.2 | 0 |  | 0 |
| 5 | 签字的笔尖 | 1800 | normal | 37.0 | 0 |  | 2 |
| 6 | 账本上的签名线 | 1712 | normal | 94.5 | 0 |  | 3 |
| 7 | 账本上的签名线 | 2017 | normal | 37.0 | 0 |  | 3 |
| 8 | 账本上的签名线 | 1835 | normal | 94.2 | 0 |  | 2 |
| 9 | 账本上的签名线 | 1746 | normal | 94.6 | 0 |  | 4 |
| 10 | 账本上的签名线 | 2263 | long | 87.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「张老三的」×6
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「张老三的」×3
  - attr_adv_pct 15.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「张老三的」×5
- 第 5 章：
  - 单条套路句式超限：「张老三的」×6
  - [observe] attr_adv_pct 35.0 > 25.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 13.0 高于目标 12.0
  - [observe] 标题重复：「账本上的签名线」已存在
- 第 7 章：
  - 单条套路句式超限：「张老三的」×8
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「账本上的签名线」已存在
- 第 8 章：
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 标题重复：「账本上的签名线」已存在
- 第 9 章：
  - 单条套路句式超限：「张老三的」×5
  - narration_para_pct 4.7 低于目标 5.0
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题重复：「账本上的签名线」已存在
- 第 10 章：
  - dialogue_run_mean 29.5 高于目标 14.0
  - [observe] 标题重复：「账本上的签名线」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17442
chapter_chars_mean: 1744
chapter_chars_median: 1670
chapter_chars_cv: 0.1
paragraphs_mean: 44.6
dialogue_chars_pct: 52.9
dialogue_para_pct: 86.7
interiority_para_pct: 3.6
narration_para_pct: 9.7
turn_under20_pct: 77.3
turn_over200_pct: 0.0
attr_say_pct: 32.4
attr_adv_pct: 16.2
scenes_per_chapter: 1.7
dialogue_run_mean: 9.6
turn_len_median: 12
```
