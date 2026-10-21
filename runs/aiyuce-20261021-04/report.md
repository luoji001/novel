# 电闸 生成报告

slug：`aiyuce-20261021-04`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12594
LLM 调用：57 次，累计 222.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅电费单 | 2219 | normal | 95.3 | 0 |  | 0 |
| 2 | 发布招聘JD | 2133 | normal | 36.3 | 0 |  | 2 |
| 3 | 划线的电费单边缘 | 2399 | normal | 35.2 | 0 |  | 1 |
| 4 | 翻阅电费单边缘 | 2232 | normal | 59.0 | 0 |  | 2 |
| 5 | 翻阅折旧表边缘 | 2271 | normal | 36.3 | 0 |  | 2 |
| 6 | 翻阅电力需求报告 | 1334 | short | 81.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「A市供电局」×3
  - [observe] 章内自我复读 1 句（如「这意味着市场上确实存在对具备特定技能技术人员的巨…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 42.1 低于目标 45.0
  - [observe] 标题与《翻阅电费单》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 31.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 47.4 高于目标 18.0
  - dialogue_run_mean 6 高于目标 4.0
  - narration_para_pct 7.7 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 12317
chapter_chars_mean: 2053
chapter_chars_median: 2176
chapter_chars_cv: 0.19
paragraphs_mean: 15.2
dialogue_chars_pct: 8.7
dialogue_para_pct: 29.5
interiority_para_pct: 17.7
narration_para_pct: 52.7
turn_under20_pct: 65.2
turn_over200_pct: 0.0
attr_say_pct: 41.9
attr_adv_pct: 9.8
scenes_per_chapter: 1.2
dialogue_run_mean: 2.1
turn_len_median: 16
```
