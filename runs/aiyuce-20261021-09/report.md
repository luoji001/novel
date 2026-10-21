# 听笔 生成报告

slug：`aiyuce-20261021-09`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11848
LLM 调用：57 次，累计 213.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 记录本的页数减少 | 1666 | normal | 89.8 | 0 |  | 3 |
| 2 | 签字栏的最后一笔 | 2489 | normal | 34.7 | 0 |  | 3 |
| 3 | 预算明细表的变化 | 2149 | normal | 90.1 | 0 |  | 2 |
| 4 | 作文样本集 | 2314 | normal | 79.8 | 0 |  | 3 |
| 5 | 使用次数增长 | 2078 | normal | 82.2 | 0 |  | 3 |
| 6 | 记录本的页数变化 | 1146 | short | 35.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 51.7 高于目标 18.0
  - dialogue_run_mean 4.7 高于目标 4.0
  - narration_para_pct 5.9 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 49.9 高于目标 18.0
  - narration_para_pct 17.2 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「这时，外面传来一阵脚步声，似乎是其他几位老师也陆…」）
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
  - narration_para_pct 25.0 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 61.9 高于目标 18.0
  - dialogue_run_mean 19 高于目标 4.0
  - narration_para_pct 5.0 低于目标 45.0
- 第 5 章：
  - dialogue_chars_pct 44.1 高于目标 18.0
  - dialogue_run_mean 5.7 高于目标 4.0
  - narration_para_pct 9.1 低于目标 45.0
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《记录本的页数减少》近似 0.75 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11503
chapter_chars_mean: 1917
chapter_chars_median: 2056
chapter_chars_cv: 0.25
paragraphs_mean: 18.8
dialogue_chars_pct: 40.8
dialogue_para_pct: 71.0
interiority_para_pct: 11.0
narration_para_pct: 18.0
turn_under20_pct: 30.5
turn_over200_pct: 0.0
attr_say_pct: 14.7
attr_adv_pct: 3.0
scenes_per_chapter: 2
dialogue_run_mean: 7.0
turn_len_median: 29
```
