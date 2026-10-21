# 折旧表 生成报告

slug：`aiyuce-20261021-26`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12906
LLM 调用：57 次，累计 234.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的数字 | 2120 | normal | 37.6 | 0 |  | 1 |
| 2 | 张贴招聘JD | 2660 | normal | 34.4 | 0 |  | 2 |
| 3 | 订单确认流程 | 2169 | normal | 36.9 | 0 |  | 3 |
| 4 | 核对计算器按键 | 2389 | normal | 89.1 | 0 |  | 1 |
| 5 | 核对计算器按键 | 2052 | normal | 35.9 | 0 |  | 2 |
| 6 | 核对计算器按键 | 1510 | short | 88.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 2 句（如「如果电力公司突然上调电价，那么实际支出将会高于预…」）
- 第 2 章：
  - interiority_para_pct 41.2 高于目标 40.0
  - [observe] 章内自我复读 6 句（如「因此，他在做出这个决策的时候，心里很清楚地意识到…」）
- 第 3 章：
  - dialogue_run_mean 4.5 高于目标 4.0
  - narration_para_pct 35.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对计算器按键」已存在
- 第 6 章：
  - dialogue_run_mean 5 高于目标 4.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 标题重复：「核对计算器按键」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12634
chapter_chars_mean: 2106
chapter_chars_median: 2097
chapter_chars_cv: 0.18
paragraphs_mean: 14.8
dialogue_chars_pct: 3.5
dialogue_para_pct: 23.9
interiority_para_pct: 23.7
narration_para_pct: 52.4
turn_under20_pct: 69.2
turn_over200_pct: 0.0
attr_say_pct: 13.6
attr_adv_pct: 13.6
scenes_per_chapter: 1.2
dialogue_run_mean: 2.2
turn_len_median: 11
```
