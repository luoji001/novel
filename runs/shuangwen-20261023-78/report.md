# 账本副本 生成报告

slug：`shuangwen-20261023-78`
档位：爽文　闸门模式：observe
章数：10　总字数：19241
LLM 调用：97 次，累计 432.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔的博弈 | 1528 | normal | 98.1 | 0 |  | 1 |
| 2 | 账本副本的浮现 | 2043 | normal | 88.4 | 0 |  | 3 |
| 3 | 签字笔的抉择 | 1816 | normal | 36.5 | 0 |  | 2 |
| 4 | 账本副本的浮现 | 2246 | normal | 92.7 | 0 |  | 2 |
| 5 | 工龄证明的冲击 | 1790 | normal | 91.7 | 0 |  | 0 |
| 6 | 签字笔的较量 | 1978 | normal | 95.1 | 0 |  | 3 |
| 7 | 签字笔的确认 | 1725 | normal | 37.6 | 0 |  | 4 |
| 8 | 签字笔的确认 | 2051 | normal | 93.6 | 0 |  | 2 |
| 9 | 签字笔的确认 | 1741 | normal | 37.2 | 0 |  | 3 |
| 10 | 签字笔的确认 | 2313 | long | 93.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3
- 第 2 章：
  - narration_para_pct 3.9 低于目标 5.0
  - attr_adv_pct 18.2 高于目标 12.0
  - dialogue_run_mean 49 高于目标 14.0
- 第 3 章：
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题与《签字笔的博弈》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「”陈文低」×4
  - [observe] 标题重复：「账本副本的浮现」已存在
- 第 6 章：
  - narration_para_pct 4.9 低于目标 5.0
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题与《签字笔的抉择》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×5
  - [observe] attr_adv_pct 35.0 > 25.0（结构塌缩）
  - [observe] 标题与《签字笔的较量》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「签字笔的确认」已存在
- 第 9 章：
  - narration_para_pct 3.4 低于目标 5.0
  - [observe] attr_adv_pct 31.2 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔的确认」已存在
- 第 10 章：
  - attr_adv_pct 23.5 高于目标 12.0
  - [observe] 标题重复：「签字笔的确认」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18274
chapter_chars_mean: 1827
chapter_chars_median: 1806
chapter_chars_cv: 0.13
paragraphs_mean: 40.7
dialogue_chars_pct: 51.9
dialogue_para_pct: 85.9
interiority_para_pct: 5.3
narration_para_pct: 8.8
turn_under20_pct: 69.6
turn_over200_pct: 0.0
attr_say_pct: 27.7
attr_adv_pct: 18.6
scenes_per_chapter: 1.4
dialogue_run_mean: 11.7
turn_len_median: 14
```
