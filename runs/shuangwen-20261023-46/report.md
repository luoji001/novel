# 药方残页 生成报告

slug：`shuangwen-20261023-46`
档位：爽文　闸门模式：observe
章数：10　总字数：18775
LLM 调用：97 次，累计 435.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药秤称量药方残页 | 1951 | normal | 98.1 | 0 |  | 3 |
| 2 | 药方残页的火光 | 1824 | normal | 92.2 | 0 |  | 2 |
| 3 | 药方残页的指尖 | 1979 | normal | 93.6 | 0 |  | 2 |
| 4 | 药秤称量药方残页 | 1590 | normal | 93.4 | 0 |  | 1 |
| 5 | 药秤称量当归 | 2005 | normal | 90.9 | 0 |  | 1 |
| 6 | 药方残页的火光 | 1745 | normal | 92.9 | 0 |  | 2 |
| 7 | 药秤称量当归 | 1815 | normal | 36.9 | 0 |  | 3 |
| 8 | 药秤称量当归 | 1681 | normal | 36.6 | 0 |  | 3 |
| 9 | 药方残页的指纹 | 1743 | normal | 92.7 | 0 |  | 1 |
| 10 | 药秤称量当归 | 2432 | long | 94.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陆怀瑾的」×3、「他知道这」×3
  - dialogue_chars_pct 29.6 低于目标 30.0
  - attr_adv_pct 20.0 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 22.2 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「沈砚秋的」×4
  - [observe] 标题与《药方残页的火光》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] 标题重复：「药秤称量药方残页」已存在
- 第 5 章：
  - 单条套路句式超限：「沈砚秋的」×3
- 第 6 章：
  - 单条套路句式超限：「沈砚秋的」×5、「沈砚秋站在」×3
  - [observe] 标题重复：「药方残页的火光」已存在
- 第 7 章：
  - 单条套路句式超限：「陆怀瑾的」×5
  - [observe] attr_adv_pct 37.5 > 25.0（结构塌缩）
  - [observe] 标题重复：「药秤称量当归」已存在
- 第 8 章：
  - 单条套路句式超限：「沈砚秋的」×3
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「药秤称量当归」已存在
- 第 9 章：
  - [observe] 标题与《药方残页的指尖》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「药秤称量当归」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17824
chapter_chars_mean: 1782
chapter_chars_median: 1736
chapter_chars_cv: 0.12
paragraphs_mean: 39.7
dialogue_chars_pct: 36.8
dialogue_para_pct: 75.8
interiority_para_pct: 9.2
narration_para_pct: 15.0
turn_under20_pct: 78.1
turn_over200_pct: 0.0
attr_say_pct: 25.1
attr_adv_pct: 16.6
scenes_per_chapter: 1.9
dialogue_run_mean: 4.2
turn_len_median: 13
```
