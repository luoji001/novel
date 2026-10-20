# 当票 生成报告

slug：`xuanyi-20261019-122`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13576
LLM 调用：68 次，累计 227.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 怀表与铜锁 | 1607 | short | 81.6 | 0 |  | 3 |
| 2 | 摩挲当票副本 | 3150 | normal | 92.8 | 0 |  | 1 |
| 3 | 摩挲当票副本 | 3501 | normal | 91.4 | 0 |  | 3 |
| 4 | 摩挲账簿边缘 | 3499 | normal | 91.0 | 0 |  | 2 |
| 5 | 摩挲铜锁缝隙 | 1814 | short | 93.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 32.1 高于目标 20.0
  - narration_para_pct 10.7 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
- 第 2 章：
  - narration_para_pct 9.0 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×4、「说道“我」×3、「沈慕云的」×3
  - narration_para_pct 17.7 低于目标 20.0
  - [observe] 标题重复：「摩挲当票副本」已存在
- 第 4 章：
  - 单条套路句式超限：「沈慕云的」×4
  - narration_para_pct 11.9 低于目标 20.0
- 第 5 章：
  - narration_para_pct 18.8 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 12890
chapter_chars_mean: 2578
chapter_chars_median: 2969
chapter_chars_cv: 0.34
paragraphs_mean: 58
dialogue_chars_pct: 40.8
dialogue_para_pct: 75.8
interiority_para_pct: 10.7
narration_para_pct: 13.5
turn_under20_pct: 71.7
turn_over200_pct: 0.0
attr_say_pct: 22.6
attr_adv_pct: 6.0
scenes_per_chapter: 3.4
dialogue_run_mean: 4.2
turn_len_median: 12
```
