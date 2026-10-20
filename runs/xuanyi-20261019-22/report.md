# 当票 生成报告

slug：`xuanyi-20261019-22`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14308
LLM 调用：68 次，累计 227.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 玉佩暗格 | 1698 | short | 84.4 | 0 |  | 2 |
| 2 | 账簿夹层 | 3717 | normal | 89.5 | 0 |  | 2 |
| 3 | 怀表背面日期 | 3378 | normal | 92.3 | 0 |  | 2 |
| 4 | 暗格藏书 | 3922 | normal | 89.3 | 0 |  | 3 |
| 5 | 当票撕裂 | 1588 | short | 92.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 13.3 低于目标 20.0
  - dialogue_run_mean 1.4 低于目标 1.5
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈砚秋的」×5
- 第 3 章：
  - narration_para_pct 10.7 低于目标 20.0
  - attr_adv_pct 13.2 高于目标 10.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈砚秋的」×5、「陆文渊的」×3
  - narration_para_pct 18.0 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「沈砚秋的」×6
  - narration_para_pct 10.9 低于目标 20.0
  - dialogue_run_mean 10.2 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13593
chapter_chars_mean: 2719
chapter_chars_median: 3196
chapter_chars_cv: 0.4
paragraphs_mean: 64.6
dialogue_chars_pct: 37.0
dialogue_para_pct: 71.9
interiority_para_pct: 8.2
narration_para_pct: 19.9
turn_under20_pct: 78.1
turn_over200_pct: 0.0
attr_say_pct: 18.5
attr_adv_pct: 7.2
scenes_per_chapter: 3.6
dialogue_run_mean: 5.5
turn_len_median: 12
```
