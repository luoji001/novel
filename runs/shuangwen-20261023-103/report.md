# 流水单 生成报告

slug：`shuangwen-20261023-103`
档位：爽文　闸门模式：observe
章数：10　总字数：18797
LLM 调用：97 次，累计 429.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔的划痕 | 1839 | normal | 40.0 | 0 |  | 2 |
| 2 | 银行流水单的日期 | 1738 | normal | 92.3 | 0 |  | 1 |
| 3 | 签字笔的划痕 | 1856 | normal | 94.2 | 0 |  | 3 |
| 4 | 身份证的边缘 | 1892 | normal | 92.2 | 0 |  | 3 |
| 5 | 签字笔的递出 | 1776 | normal | 91.1 | 0 |  | 1 |
| 6 | 流水单的传递 | 2064 | normal | 89.6 | 0 |  | 4 |
| 7 | 签字笔的划痕 | 1556 | normal | 92.8 | 0 |  | 3 |
| 8 | 签字笔的划痕 | 1842 | normal | 93.0 | 0 |  | 3 |
| 9 | 签字笔的划痕 | 1729 | normal | 91.7 | 0 |  | 3 |
| 10 | 银行流水单的日期 | 2495 | long | 92.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「吴志远的」×3
  - [observe] attr_adv_pct 26.7 > 25.0（结构塌缩）
- 第 2 章：
  - 命中套话收尾句
- 第 3 章：
  - 单条套路句式超限：「吴志远的」×5、「他知道这」×3
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「签字笔的划痕」已存在
- 第 4 章：
  - narration_para_pct 3.8 低于目标 5.0
  - attr_adv_pct 13.0 高于目标 12.0
  - dialogue_run_mean 16.3 高于目标 14.0
- 第 5 章：
  - [observe] 标题与《签字笔的划痕》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「李国强的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 21.1 高于目标 12.0
  - dialogue_run_mean 22 高于目标 14.0
- 第 7 章：
  - 命中套话收尾句
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「签字笔的划痕」已存在
- 第 8 章：
  - 单条套路句式超限：「李国强的」×3
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「签字笔的划痕」已存在
- 第 9 章：
  - 单条套路句式超限：「李国强点」×3、「吴志远的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - [observe] 标题重复：「签字笔的划痕」已存在
- 第 10 章：
  - 单条套路句式超限：「点了点头」×3、「吴志远的」×3
  - [observe] 标题重复：「银行流水单的日期」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17860
chapter_chars_mean: 1786
chapter_chars_median: 1746
chapter_chars_cv: 0.14
paragraphs_mean: 39.2
dialogue_chars_pct: 49.0
dialogue_para_pct: 86.1
interiority_para_pct: 4.7
narration_para_pct: 9.2
turn_under20_pct: 63.6
turn_over200_pct: 0.0
attr_say_pct: 30.2
attr_adv_pct: 13.5
scenes_per_chapter: 2.7
dialogue_run_mean: 9.7
turn_len_median: 14
```
