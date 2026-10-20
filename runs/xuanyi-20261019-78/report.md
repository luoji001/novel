# 金线 生成报告

slug：`xuanyi-20261019-78`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13723
LLM 调用：68 次，累计 227.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 绣品上的金线 | 1664 | short | 98.4 | 0 |  | 2 |
| 2 | 金线拂过绣绷 | 3337 | normal | 89.7 | 0 |  | 4 |
| 3 | 金线拂过绣品 | 3500 | normal | 90.9 | 0 |  | 3 |
| 4 | 绣鞋的凹陷 | 3452 | normal | 92.6 | 0 |  | 4 |
| 5 | 金线映入瞳孔 | 1765 | short | 91.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 20.0 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「沈砚秋的」×6、「“我不知道」×4
  - dialogue_chars_pct 59.5 高于目标 58.0
  - narration_para_pct 8.6 低于目标 20.0
  - dialogue_run_mean 10.4 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×4、「沈砚秋的」×4、「顾怀瑾的」×3
  - narration_para_pct 16.9 低于目标 20.0
  - [observe] 标题与《金线拂过绣绷》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈砚秋的」×10、「顾怀瑾的」×3
  - narration_para_pct 11.4 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「顾怀瑾的」×3、「沈砚秋的」×3
  - narration_para_pct 2.9 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13053
chapter_chars_mean: 2611
chapter_chars_median: 3137
chapter_chars_cv: 0.35
paragraphs_mean: 59.6
dialogue_chars_pct: 45.8
dialogue_para_pct: 80.9
interiority_para_pct: 6.5
narration_para_pct: 12.6
turn_under20_pct: 74.3
turn_over200_pct: 0.0
attr_say_pct: 20.2
attr_adv_pct: 9.3
scenes_per_chapter: 3
dialogue_run_mean: 6.7
turn_len_median: 12
```
