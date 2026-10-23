# 清单 生成报告

slug：`shuangwen-20261022-126`
档位：爽文　闸门模式：observe
章数：10　总字数：18999
LLM 调用：97 次，累计 415.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 碎纸机运转 | 1695 | normal | 99.3 | 0 |  | 1 |
| 2 | 清单对峙 | 2228 | normal | 91.6 | 0 |  | 1 |
| 3 | 签字对峙 | 2063 | normal | 92.5 | 0 |  | 2 |
| 4 | 碎纸机吞清单 | 1650 | normal | 36.9 | 0 |  | 2 |
| 5 | 核对账目 | 1808 | normal | 92.9 | 0 |  | 0 |
| 6 | 划痕对峙 | 2065 | normal | 37.2 | 0 |  | 1 |
| 7 | 对峙清单 | 1869 | normal | 93.4 | 0 |  | 1 |
| 8 | 签署许可纸条 | 1523 | normal | 93.0 | 0 |  | 2 |
| 9 | 签字笔对峙 | 1765 | normal | 91.1 | 0 |  | 1 |
| 10 | 撕开账本一角 | 2323 | long | 92.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_run_mean 15.5 高于目标 14.0
- 第 2 章：
  - attr_adv_pct 15.4 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 12.5 高于目标 12.0
- 第 4 章：
  - 命中套话收尾句
  - [observe] attr_adv_pct 50.0 > 25.0（结构塌缩）
- 第 6 章：
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 7 章：
  - attr_adv_pct 22.2 高于目标 12.0
- 第 8 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×6
- 第 9 章：
  - [observe] 标题与《签字对峙》近似 0.89 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - attr_adv_pct 13.2 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 17921
chapter_chars_mean: 1792
chapter_chars_median: 1722
chapter_chars_cv: 0.14
paragraphs_mean: 47
dialogue_chars_pct: 46.8
dialogue_para_pct: 81.9
interiority_para_pct: 3.6
narration_para_pct: 14.5
turn_under20_pct: 76.7
turn_over200_pct: 0.0
attr_say_pct: 32.0
attr_adv_pct: 16.6
scenes_per_chapter: 2.6
dialogue_run_mean: 6.7
turn_len_median: 14
```
