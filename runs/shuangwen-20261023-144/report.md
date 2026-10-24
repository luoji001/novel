# 伪造凭证 生成报告

slug：`shuangwen-20261023-144`
档位：爽文　闸门模式：observe
章数：10　总字数：18215
LLM 调用：97 次，累计 419.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一张作废的纸张 | 1514 | normal | 100.0 | 0 |  | 2 |
| 2 | 账簿上的划痕 | 1980 | normal | 37.2 | 0 |  | 1 |
| 3 | 未签字的优先权 | 1724 | normal | 92.1 | 0 |  | 1 |
| 4 | 缴费的灵石 | 1721 | normal | 92.9 | 0 |  | 2 |
| 5 | 缴费的灵石 | 1881 | normal | 37.4 | 0 |  | 3 |
| 6 | 撕碎的优先权 | 1998 | normal | 90.1 | 0 |  | 1 |
| 7 | 缴费的灵石 | 1568 | normal | 91.5 | 0 |  | 3 |
| 8 | 签署优先权协议 | 1637 | normal | 92.6 | 0 |  | 1 |
| 9 | 撕碎的优先权 | 1828 | normal | 92.9 | 0 |  | 2 |
| 10 | 撕碎的优先权 | 2354 | long | 92.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「苏长风的」×3
  - attr_adv_pct 14.3 高于目标 12.0
- 第 2 章：
  - [observe] attr_adv_pct 44.4 > 25.0（结构塌缩）
- 第 3 章：
  - attr_adv_pct 20.0 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「苏长风的」×3
  - attr_adv_pct 16.7 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「苏长风的」×3
  - [observe] attr_adv_pct 42.9 > 25.0（结构塌缩）
  - [observe] 标题重复：「缴费的灵石」已存在
- 第 6 章：
  - [observe] 标题与《未签字的优先权》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 命中套话收尾句
  - 单条套路句式超限：「苏长风的」×3
  - [observe] 标题重复：「缴费的灵石」已存在
- 第 8 章：
  - 单条套路句式超限：「他知道这」×4
- 第 9 章：
  - 单条套路句式超限：「他知道自己」×3
  - [observe] 标题重复：「撕碎的优先权」已存在
- 第 10 章：
  - 命中套话收尾句
  - 单条套路句式超限：「苏长风的」×7
  - attr_adv_pct 15.6 高于目标 12.0
  - [observe] 标题重复：「撕碎的优先权」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17263
chapter_chars_mean: 1726
chapter_chars_median: 1689
chapter_chars_cv: 0.14
paragraphs_mean: 40.1
dialogue_chars_pct: 48.0
dialogue_para_pct: 80.5
interiority_para_pct: 6.4
narration_para_pct: 13.1
turn_under20_pct: 67.9
turn_over200_pct: 0.0
attr_say_pct: 16.4
attr_adv_pct: 16.6
scenes_per_chapter: 2.4
dialogue_run_mean: 5.8
turn_len_median: 14
```
