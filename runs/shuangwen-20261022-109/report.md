# 红章 生成报告

slug：`shuangwen-20261022-109`
档位：爽文　闸门模式：observe
章数：10　总字数：18602
LLM 调用：97 次，累计 422.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 拍桌 | 1652 | normal | 39.9 | 0 |  | 2 |
| 2 | 翻阅旧客户名单 | 1664 | normal | 95.0 | 0 |  | 1 |
| 3 | 签字笔点睛 | 1671 | normal | 37.7 | 0 |  | 2 |
| 4 | 翻阅旧客户名单 | 2024 | normal | 92.7 | 0 |  | 3 |
| 5 | 签字笔点睛 | 1818 | normal | 92.0 | 0 |  | 1 |
| 6 | 签字笔点睛 | 1865 | normal | 93.0 | 0 |  | 2 |
| 7 | 翻阅旧客户名单 | 1582 | normal | 93.5 | 0 |  | 2 |
| 8 | 翻阅旧客户名单 | 2007 | normal | 93.1 | 0 |  | 2 |
| 9 | 翻阅旧客户名单 | 1683 | normal | 93.4 | 0 |  | 1 |
| 10 | 翻阅旧客户名单 | 2626 | long | 92.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 2 章：
  - 命中套话收尾句
- 第 3 章：
  - 单条套路句式超限：「不仅仅是」×3、「他知道这」×3
  - [observe] 章内自我复读 3 句（如「林海微笑着点点头，他知道，这个结果不仅仅是因为他…」）
- 第 4 章：
  - 单条套路句式超限：「周子安的」×4
  - dialogue_run_mean 15 高于目标 14.0
  - [observe] 标题重复：「翻阅旧客户名单」已存在
- 第 5 章：
  - [observe] 标题重复：「签字笔点睛」已存在
- 第 6 章：
  - 单条套路句式超限：「周子安的」×4
  - [observe] 标题重复：「签字笔点睛」已存在
- 第 7 章：
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「翻阅旧客户名单」已存在
- 第 8 章：
  - 单条套路句式超限：「周子安的」×4
  - [observe] 标题重复：「翻阅旧客户名单」已存在
- 第 9 章：
  - [observe] 标题重复：「翻阅旧客户名单」已存在
- 第 10 章：
  - 单条套路句式超限：「他知道这」×5、「周子安的」×3
  - attr_adv_pct 15.8 高于目标 12.0
  - [observe] 标题重复：「翻阅旧客户名单」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17669
chapter_chars_mean: 1767
chapter_chars_median: 1670
chapter_chars_cv: 0.17
paragraphs_mean: 39.2
dialogue_chars_pct: 51.7
dialogue_para_pct: 85.0
interiority_para_pct: 3.9
narration_para_pct: 11.1
turn_under20_pct: 68.3
turn_over200_pct: 0.0
attr_say_pct: 29.7
attr_adv_pct: 11.1
scenes_per_chapter: 1.4
dialogue_run_mean: 8.0
turn_len_median: 13
```
