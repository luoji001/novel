# 验单风波 生成报告

slug：`shuangwen-20261022-03`
档位：爽文　闸门模式：observe
章数：10　总字数：18460
LLM 调用：97 次，累计 395.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 清单的对峙 | 1715 | normal | 99.6 | 0 |  | 2 |
| 2 | 清单的对峙 | 2526 | normal | 37.1 | 0 |  | 2 |
| 3 | 签字笔悬空 | 1578 | normal | 94.4 | 0 |  | 2 |
| 4 | 签字笔悬空 | 1775 | normal | 92.7 | 0 |  | 2 |
| 5 | 签字笔悬空 | 1590 | normal | 93.3 | 0 |  | 1 |
| 6 | 签字笔悬空 | 1483 | normal | 87.9 | 0 |  | 6 |
| 7 | 签字笔悬空 | 1895 | normal | 35.1 | 0 |  | 4 |
| 8 | 签字笔悬空 | 1774 | normal | 92.6 | 0 |  | 3 |
| 9 | 签字笔悬空 | 1706 | normal | 93.0 | 0 |  | 2 |
| 10 | 签字笔悬空 | 2408 | long | 91.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×3
  - attr_adv_pct 22.2 高于目标 12.0
- 第 2 章：
  - [observe] attr_adv_pct 39.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「清单的对峙」已存在
- 第 3 章：
  - 单条套路句式超限：「李国强的」×3
  - narration_para_pct 4.3 低于目标 5.0
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 标题重复：「签字笔悬空」已存在
- 第 5 章：
  - [observe] 标题重复：「签字笔悬空」已存在
- 第 6 章：
  - 单条套路句式超限：「市卫健委」×3
  - dialogue_chars_pct 73.2 高于目标 70.0
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 18.2 高于目标 12.0
  - dialogue_run_mean 27 高于目标 14.0
  - [observe] 标题重复：「签字笔悬空」已存在
- 第 7 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 33 高于目标 14.0
  - [observe] attr_adv_pct 37.5 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔悬空」已存在
- 第 8 章：
  - 单条套路句式超限：「李国强的」×5
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「签字笔悬空」已存在
- 第 9 章：
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「签字笔悬空」已存在
- 第 10 章：
  - 单条套路句式超限：「李国强的」×3
  - attr_adv_pct 13.0 高于目标 12.0
  - [observe] 标题重复：「签字笔悬空」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17592
chapter_chars_mean: 1759
chapter_chars_median: 1662
chapter_chars_cv: 0.18
paragraphs_mean: 36.3
dialogue_chars_pct: 57.8
dialogue_para_pct: 89.3
interiority_para_pct: 3.7
narration_para_pct: 7.1
turn_under20_pct: 62.1
turn_over200_pct: 0.0
attr_say_pct: 28.7
attr_adv_pct: 18.9
scenes_per_chapter: 2.1
dialogue_run_mean: 12.8
turn_len_median: 16
```
