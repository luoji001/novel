# 校准记录 生成报告

slug：`shuangwen-20261022-47`
档位：爽文　闸门模式：observe
章数：10　总字数：20411
LLM 调用：97 次，累计 399.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一纸真实磅单 | 2005 | normal | 97.5 | 0 |  | 1 |
| 2 | 一纸真实磅单 | 2117 | normal | 37.4 | 0 |  | 3 |
| 3 | 一张皱巴巴的磅单 | 2001 | normal | 37.1 | 0 |  | 2 |
| 4 | 一纸真实磅单 | 2026 | normal | 94.5 | 0 |  | 2 |
| 5 | 一张皱巴巴的纸条 | 2125 | normal | 93.2 | 0 |  | 2 |
| 6 | 签字的笔尖 | 2083 | normal | 92.8 | 0 |  | 3 |
| 7 | 一纸真实磅单 | 1781 | normal | 37.0 | 0 |  | 3 |
| 8 | 一张皱巴巴的磅单 | 2187 | normal | 91.9 | 0 |  | 2 |
| 9 | 一张皱巴巴的磅单 | 1855 | normal | 93.6 | 0 |  | 2 |
| 10 | 一纸真实磅单 | 2221 | long | 91.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李振强的」×8
- 第 2 章：
  - 单条套路句式超限：「周志远的」×4
  - [observe] attr_adv_pct 60.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「一纸真实磅单」已存在
- 第 3 章：
  - 单条套路句式超限：「李振强的」×3、「周志远的」×3
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「周志远的」×6、「他知道这」×4
  - [observe] 标题重复：「一纸真实磅单」已存在
- 第 5 章：
  - 单条套路句式超限：「李振强的」×8
  - [observe] 标题与《一张皱巴巴的磅单》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李振强的」×4
  - attr_adv_pct 12.5 高于目标 12.0
- 第 7 章：
  - dialogue_run_mean 18 高于目标 14.0
  - [observe] attr_adv_pct 31.6 > 25.0（结构塌缩）
  - [observe] 标题重复：「一纸真实磅单」已存在
- 第 8 章：
  - 单条套路句式超限：「李振强的」×4
  - [observe] 标题重复：「一张皱巴巴的磅单」已存在
- 第 9 章：
  - attr_adv_pct 18.8 高于目标 12.0
  - [observe] 标题重复：「一张皱巴巴的磅单」已存在
- 第 10 章：
  - 单条套路句式超限：「李振强的」×4
  - [observe] 标题重复：「一纸真实磅单」已存在

## 整书结构指标

```
chapters: 10
total_chars: 19364
chapter_chars_mean: 1936
chapter_chars_median: 1955
chapter_chars_cv: 0.07
paragraphs_mean: 44.5
dialogue_chars_pct: 49.4
dialogue_para_pct: 84.7
interiority_para_pct: 4.8
narration_para_pct: 10.5
turn_under20_pct: 73.9
turn_over200_pct: 0.0
attr_say_pct: 25.9
attr_adv_pct: 17.1
scenes_per_chapter: 2.4
dialogue_run_mean: 7.5
turn_len_median: 12
```
