# 签单 生成报告

slug：`shuangwen-20261022-82`
档位：爽文　闸门模式：observe
章数：10　总字数：18988
LLM 调用：97 次，累计 413.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 文件折叠角秘密 | 1623 | normal | 98.4 | 0 |  | 0 |
| 2 | 签字笔书写真相 | 2182 | normal | 94.9 | 0 |  | 0 |
| 3 | 记录本交锋 | 1747 | normal | 92.1 | 0 |  | 2 |
| 4 | 签字笔画勾 | 2445 | normal | 94.1 | 0 |  | 1 |
| 5 | 签字笔划破合同 | 1935 | normal | 90.3 | 0 |  | 1 |
| 6 | 签字笔划破合同 | 1513 | normal | 93.7 | 0 |  | 2 |
| 7 | 签字笔划破合同 | 1738 | normal | 91.1 | 0 |  | 2 |
| 8 | 签字笔划破合同 | 1564 | normal | 92.8 | 0 |  | 3 |
| 9 | 签字笔划破合同 | 1836 | normal | 93.6 | 0 |  | 1 |
| 10 | 签字笔划去清单 | 2395 | long | 36.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - 单条套路句式超限：「李国强的」×7
  - attr_adv_pct 15.4 高于目标 12.0
- 第 4 章：
  - attr_adv_pct 13.8 高于目标 12.0
- 第 5 章：
  - dialogue_run_mean 18 高于目标 14.0
- 第 6 章：
  - narration_para_pct 4.5 低于目标 5.0
  - [observe] 标题重复：「签字笔划破合同」已存在
- 第 7 章：
  - 单条套路句式超限：「李国强的」×3
  - [observe] 标题重复：「签字笔划破合同」已存在
- 第 8 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李国强的」×3
  - [observe] 标题重复：「签字笔划破合同」已存在
- 第 9 章：
  - [observe] 标题重复：「签字笔划破合同」已存在
- 第 10 章：
  - dialogue_run_mean 18.5 高于目标 14.0
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）

## 整书结构指标

```
chapters: 10
total_chars: 18026
chapter_chars_mean: 1803
chapter_chars_median: 1700
chapter_chars_cv: 0.18
paragraphs_mean: 40.3
dialogue_chars_pct: 50.4
dialogue_para_pct: 84.2
interiority_para_pct: 5.0
narration_para_pct: 10.8
turn_under20_pct: 67.8
turn_over200_pct: 0.0
attr_say_pct: 24.1
attr_adv_pct: 8.4
scenes_per_chapter: 2.1
dialogue_run_mean: 8.8
turn_len_median: 13
```
