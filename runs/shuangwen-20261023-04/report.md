# 旧契书 生成报告

slug：`shuangwen-20261023-04`
档位：爽文　闸门模式：observe
章数：10　总字数：19896
LLM 调用：97 次，累计 442.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 攥契书 | 1815 | normal | 100.0 | 0 |  | 1 |
| 2 | 撕裂契约 | 1588 | normal | 92.8 | 0 |  | 1 |
| 3 | 攥契书 | 1999 | normal | 92.9 | 0 |  | 2 |
| 4 | 撕契书 | 1976 | normal | 88.1 | 0 |  | 5 |
| 5 | 焚契心火 | 1712 | normal | 95.3 | 0 |  | 1 |
| 6 | 指印对契 | 2325 | normal | 93.6 | 0 |  | 2 |
| 7 | 攥契书 | 1875 | normal | 91.5 | 0 |  | 3 |
| 8 | 点契生风 | 2018 | normal | 93.5 | 0 |  | 2 |
| 9 | 夺契风波 | 2104 | normal | 37.4 | 0 |  | 2 |
| 10 | 攥契书 | 2474 | long | 91.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李长老的」×3
- 第 2 章：
  - narration_para_pct 0.0 低于目标 5.0
- 第 3 章：
  - narration_para_pct 2.8 低于目标 5.0
  - [observe] 标题重复：「攥契书」已存在
- 第 4 章：
  - 单条套路句式超限：「李长老的」×3
  - narration_para_pct 2.2 低于目标 5.0
  - attr_adv_pct 19.0 高于目标 12.0
  - dialogue_run_mean 45 高于目标 14.0
  - [observe] 标题与《攥契书》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - attr_adv_pct 25.0 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「李长老的」×5
  - narration_para_pct 4.8 低于目标 5.0
- 第 7 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李长老的」×4
  - [observe] 标题重复：「攥契书」已存在
- 第 8 章：
  - 命中套话收尾句
  - attr_adv_pct 18.8 高于目标 12.0
- 第 9 章：
  - 单条套路句式超限：「李长老的」×6、「他知道这」×3
  - [observe] attr_adv_pct 36.4 > 25.0（结构塌缩）
- 第 10 章：
  - 单条套路句式超限：「李长老的」×4
  - attr_adv_pct 18.8 高于目标 12.0
  - [observe] 标题重复：「攥契书」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18993
chapter_chars_mean: 1899
chapter_chars_median: 1894
chapter_chars_cv: 0.13
paragraphs_mean: 38.9
dialogue_chars_pct: 51.7
dialogue_para_pct: 85.6
interiority_para_pct: 5.0
narration_para_pct: 9.4
turn_under20_pct: 60.8
turn_over200_pct: 0.0
attr_say_pct: 20.1
attr_adv_pct: 15.8
scenes_per_chapter: 2.2
dialogue_run_mean: 11.6
turn_len_median: 16
```
