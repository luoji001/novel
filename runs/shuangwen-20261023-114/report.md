# 客户名单 生成报告

slug：`shuangwen-20261023-114`
档位：爽文　闸门模式：observe
章数：10　总字数：19311
LLM 调用：97 次，累计 398.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字裂痕 | 1807 | normal | 99.8 | 0 |  | 0 |
| 2 | 财务报表的对峙 | 1657 | normal | 91.9 | 0 |  | 2 |
| 3 | 翻阅客户名单 | 1947 | normal | 36.1 | 0 |  | 1 |
| 4 | 签字笔的重量 | 1983 | normal | 92.5 | 0 |  | 1 |
| 5 | 签字笔的裂痕 | 1556 | normal | 91.4 | 0 |  | 2 |
| 6 | 签字笔的裂痕 | 1494 | normal | 88.9 | 0 |  | 3 |
| 7 | 签字笔的裂痕 | 1751 | normal | 91.4 | 0 |  | 1 |
| 8 | 签字笔的裂痕 | 2149 | normal | 86.5 | 0 |  | 4 |
| 9 | 签字笔的裂痕 | 1796 | normal | 86.8 | 0 |  | 3 |
| 10 | 翻阅客户名单 | 3161 | long | 36.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 3.6 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
- 第 3 章：
  - [observe] 章内自我复读 3 句（如「你这是在挑战总部的权威…」）
- 第 4 章：
  - narration_para_pct 2.4 低于目标 5.0
- 第 5 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题与《签字裂痕》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 22 高于目标 14.0
  - [observe] 标题重复：「签字笔的裂痕」已存在
- 第 7 章：
  - [observe] 标题重复：「签字笔的裂痕」已存在
- 第 8 章：
  - dialogue_chars_pct 73.3 高于目标 70.0
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 40 高于目标 14.0
  - [observe] 标题重复：「签字笔的裂痕」已存在
- 第 9 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 28 高于目标 14.0
  - [observe] 标题重复：「签字笔的裂痕」已存在
- 第 10 章：
  - narration_para_pct 4.2 低于目标 5.0
  - [observe] 章内自我复读 4 句（如「我觉得只要按照规则办事，胜利总是属于有能力的人…」）
  - [observe] 标题重复：「翻阅客户名单」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18426
chapter_chars_mean: 1843
chapter_chars_median: 1714
chapter_chars_cv: 0.24
paragraphs_mean: 36.8
dialogue_chars_pct: 57.3
dialogue_para_pct: 89.6
interiority_para_pct: 4.0
narration_para_pct: 6.4
turn_under20_pct: 59.9
turn_over200_pct: 0.0
attr_say_pct: 26.7
attr_adv_pct: 9.0
scenes_per_chapter: 2.4
dialogue_run_mean: 13.9
turn_len_median: 16
```
