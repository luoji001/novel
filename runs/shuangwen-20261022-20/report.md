# 清单覆账 生成报告

slug：`shuangwen-20261022-20`
档位：爽文　闸门模式：observe
章数：10　总字数：18477
LLM 调用：97 次，累计 369.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本摊开 | 1838 | normal | 100.0 | 0 |  | 2 |
| 2 | 签字权落 | 1749 | normal | 37.9 | 0 |  | 3 |
| 3 | 算盘拨动 | 1966 | normal | 37.2 | 0 |  | 2 |
| 4 | 铜牌落地 | 2023 | normal | 93.9 | 0 |  | 1 |
| 5 | 墨迹未干 | 1647 | normal | 94.5 | 0 |  | 2 |
| 6 | 墨迹未干 | 1574 | normal | 92.5 | 0 |  | 3 |
| 7 | 账本掀开 | 1906 | normal | 93.8 | 0 |  | 4 |
| 8 | 账本摩挲 | 1716 | normal | 91.1 | 0 |  | 2 |
| 9 | 供奉凭证摩挲 | 1837 | normal | 92.3 | 0 |  | 2 |
| 10 | 铜尺点案 | 2211 | long | 92.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李怀安的」×3、「议事厅」×3
  - attr_adv_pct 21.4 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「李怀安的」×5
  - narration_para_pct 4.0 低于目标 5.0
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「议事厅」×3
  - [observe] attr_adv_pct 40.0 > 25.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3、「议事厅」×3
- 第 5 章：
  - 单条套路句式超限：「李怀安的」×4、「议事厅」×3
  - attr_adv_pct 12.5 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「议事厅」×4、「他知道自己」×3
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「墨迹未干」已存在
- 第 7 章：
  - narration_para_pct 3.1 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
  - dialogue_run_mean 15 高于目标 14.0
  - [observe] 标题与《账本摊开》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「李怀安的」×3
  - attr_adv_pct 22.2 高于目标 12.0
- 第 9 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李怀安的」×5
- 第 10 章：
  - 单条套路句式超限：「李怀安的」×3
  - attr_adv_pct 25.0 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 17521
chapter_chars_mean: 1752
chapter_chars_median: 1734
chapter_chars_cv: 0.1
paragraphs_mean: 41.2
dialogue_chars_pct: 46.7
dialogue_para_pct: 81.7
interiority_para_pct: 8.6
narration_para_pct: 9.7
turn_under20_pct: 70.3
turn_over200_pct: 0.2
attr_say_pct: 21.0
attr_adv_pct: 20.3
scenes_per_chapter: 1.5
dialogue_run_mean: 6.9
turn_len_median: 14
```
