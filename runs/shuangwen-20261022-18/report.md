# 工艺图 生成报告

slug：`shuangwen-20261022-18`
档位：爽文　闸门模式：observe
章数：10　总字数：18914
LLM 调用：97 次，累计 364.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔下的工艺图 | 1798 | normal | 100.0 | 0 |  | 1 |
| 2 | 青瓷盏上的凹陷处 | 1780 | normal | 93.3 | 0 |  | 0 |
| 3 | 签字笔下的新工艺图 | 2037 | normal | 93.9 | 0 |  | 1 |
| 4 | 工艺图上的新改进 | 2051 | normal | 92.6 | 0 |  | 0 |
| 5 | 工艺图上的新改进 | 1816 | normal | 90.4 | 0 |  | 3 |
| 6 | 钢笔划过验收单 | 1823 | normal | 34.8 | 0 |  | 3 |
| 7 | 工艺图上的新改进 | 1658 | normal | 92.8 | 0 |  | 2 |
| 8 | 钢笔划过验收单 | 1985 | normal | 92.9 | 0 |  | 2 |
| 9 | 工艺图上的新改进 | 1703 | normal | 93.1 | 0 |  | 2 |
| 10 | 钢笔划过验收单 | 2253 | long | 93.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3、「沈志远的」×3
- 第 3 章：
  - [observe] 标题与《签字笔下的工艺图》近似 0.94 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「周振华的」×5、「沈志远的」×3
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题重复：「工艺图上的新改进」已存在
- 第 6 章：
  - 单条套路句式超限：「沈志远的」×3
  - dialogue_chars_pct 24.6 低于目标 30.0
  - [observe] attr_adv_pct 42.9 > 25.0（结构塌缩）
- 第 7 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 标题重复：「工艺图上的新改进」已存在
- 第 8 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「钢笔划过验收单」已存在
- 第 9 章：
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「工艺图上的新改进」已存在
- 第 10 章：
  - 单条套路句式超限：「周振华的」×4
  - [observe] 标题重复：「钢笔划过验收单」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18032
chapter_chars_mean: 1803
chapter_chars_median: 1740
chapter_chars_cv: 0.1
paragraphs_mean: 35.6
dialogue_chars_pct: 43.9
dialogue_para_pct: 77.0
interiority_para_pct: 7.9
narration_para_pct: 15.1
turn_under20_pct: 65.9
turn_over200_pct: 0.0
attr_say_pct: 14.3
attr_adv_pct: 14.7
scenes_per_chapter: 1.7
dialogue_run_mean: 5.0
turn_len_median: 16
```
