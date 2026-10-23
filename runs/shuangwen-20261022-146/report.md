# 账本副本 生成报告

slug：`shuangwen-20261022-146`
档位：爽文　闸门模式：observe
章数：10　总字数：21260
LLM 调用：97 次，累计 470.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 数字与单据的对峙 | 2069 | normal | 99.1 | 0 |  | 1 |
| 2 | 签字笔停在纸面 | 1994 | normal | 36.8 | 0 |  | 2 |
| 3 | 签字笔划破纸张 | 2164 | normal | 93.3 | 0 |  | 1 |
| 4 | 签字笔划破纸张 | 1913 | normal | 92.4 | 0 |  | 4 |
| 5 | 签字笔点在数字上 | 2204 | normal | 37.6 | 0 |  | 2 |
| 6 | 签字笔点在数字上 | 2395 | normal | 92.0 | 0 |  | 4 |
| 7 | 签字笔点在数字上 | 2046 | normal | 93.6 | 0 |  | 3 |
| 8 | 签字笔点在数字上 | 2058 | normal | 37.4 | 0 |  | 3 |
| 9 | 名册上的缺失费用 | 1890 | normal | 91.7 | 0 |  | 3 |
| 10 | 签字笔点在数字上 | 2517 | long | 36.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 0.0 低于目标 5.0
- 第 2 章：
  - 单条套路句式超限：「陈志远的」×7
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
- 第 3 章：
  - attr_adv_pct 21.1 高于目标 12.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈志远的」×3
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题重复：「签字笔划破纸张」已存在
- 第 5 章：
  - 单条套路句式超限：「陈志远的」×4
  - [observe] attr_adv_pct 29.4 > 25.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「陈志远的」×5
  - narration_para_pct 4.1 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「签字笔点在数字上」已存在
- 第 7 章：
  - narration_para_pct 3.8 低于目标 5.0
  - attr_adv_pct 17.6 高于目标 12.0
  - [observe] 标题重复：「签字笔点在数字上」已存在
- 第 8 章：
  - narration_para_pct 4.3 低于目标 5.0
  - [observe] attr_adv_pct 43.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔点在数字上」已存在
- 第 9 章：
  - 单条套路句式超限：「点了点头」×4、「陈志远的」×3
  - narration_para_pct 2.4 低于目标 5.0
  - attr_adv_pct 23.5 高于目标 12.0
- 第 10 章：
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔点在数字上」已存在

## 整书结构指标

```
chapters: 10
total_chars: 20138
chapter_chars_mean: 2014
chapter_chars_median: 1960
chapter_chars_cv: 0.1
paragraphs_mean: 46.5
dialogue_chars_pct: 50.1
dialogue_para_pct: 87.2
interiority_para_pct: 5.1
narration_para_pct: 7.7
turn_under20_pct: 69.5
turn_over200_pct: 0.0
attr_say_pct: 27.6
attr_adv_pct: 23.2
scenes_per_chapter: 1.6
dialogue_run_mean: 8.3
turn_len_median: 13
```
