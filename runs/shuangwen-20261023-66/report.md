# 红笔划掉 生成报告

slug：`shuangwen-20261023-66`
档位：爽文　闸门模式：observe
章数：10　总字数：19602
LLM 调用：97 次，累计 464.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药单被揉皱 | 1749 | normal | 100.0 | 0 |  | 2 |
| 2 | 红笔点纸 | 2536 | normal | 37.6 | 0 |  | 2 |
| 3 | 红笔划线 | 1852 | normal | 91.1 | 0 |  | 1 |
| 4 | 木箱钥匙递出去 | 2427 | normal | 36.8 | 0 |  | 2 |
| 5 | 红笔划掉 | 1927 | normal | 92.6 | 0 |  | 1 |
| 6 | 红笔划线 | 1812 | normal | 36.6 | 0 |  | 2 |
| 7 | 红笔划线 | 1712 | normal | 91.1 | 0 |  | 3 |
| 8 | 红笔划线 | 1701 | normal | 37.0 | 0 |  | 4 |
| 9 | 红笔划线 | 1825 | normal | 94.7 | 0 |  | 3 |
| 10 | 红笔划线 | 2051 | long | 92.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李德顺的」×6
  - narration_para_pct 0.0 低于目标 5.0
- 第 2 章：
  - 单条套路句式超限：「周明远的」×3
  - [observe] attr_adv_pct 42.9 > 25.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「周明远的」×4
- 第 4 章：
  - 单条套路句式超限：「李德顺的」×7、「他知道这」×3
  - [observe] 章内自我复读 2 句（如「嗯……确实有些出入。不过这些都是小事，我们慢慢解…」）
- 第 5 章：
  - [observe] 标题与《红笔划线》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] attr_adv_pct 60.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「红笔划线」已存在
- 第 7 章：
  - 命中套话收尾句
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「红笔划线」已存在
- 第 8 章：
  - 单条套路句式超限：「李德顺的」×4
  - narration_para_pct 3.1 低于目标 5.0
  - [observe] attr_adv_pct 40.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「红笔划线」已存在
- 第 9 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李德顺的」×3
  - [observe] 标题重复：「红笔划线」已存在
- 第 10 章：
  - 单条套路句式超限：「李德顺的」×9
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「红笔划线」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18689
chapter_chars_mean: 1869
chapter_chars_median: 1751
chapter_chars_cv: 0.15
paragraphs_mean: 38.9
dialogue_chars_pct: 44.5
dialogue_para_pct: 81.4
interiority_para_pct: 7.9
narration_para_pct: 10.8
turn_under20_pct: 59.0
turn_over200_pct: 0.0
attr_say_pct: 22.7
attr_adv_pct: 22.0
scenes_per_chapter: 1.4
dialogue_run_mean: 6.4
turn_len_median: 15
```
