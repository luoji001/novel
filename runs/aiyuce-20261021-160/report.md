# 电表红光 生成报告

slug：`aiyuce-20261021-160`
档位：AI 推演　闸门模式：observe
章数：6　总字数：10870
LLM 调用：53 次，累计 200.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的数字变化 | 2209 | normal | 94.4 | 0 |  | 0 |
| 2 | 面试候选人 | 2219 | normal | 36.2 | 0 |  | 1 |
| 3 | 指尖划过报价单 | 1073 | normal | 90.8 | 0 |  | 0 |
| 4 | 指尖划过折旧表 | 2211 | normal | 36.3 | 0 |  | 1 |
| 5 | 指尖划过电费单 | 1930 | normal | 36.1 | 0 |  | 3 |
| 6 | 手指摩挲纸张边缘 | 1222 | short | 91.8 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 3 句（如「因此，在考虑招聘的同时，他还计划着手评估现有硬件…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 38.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《指尖划过报价单》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 10607
chapter_chars_mean: 1768
chapter_chars_median: 2020
chapter_chars_cv: 0.3
paragraphs_mean: 13.8
dialogue_chars_pct: 6.7
dialogue_para_pct: 27.0
interiority_para_pct: 13.3
narration_para_pct: 59.7
turn_under20_pct: 70.8
turn_over200_pct: 0.0
attr_say_pct: 8.5
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 1.7
turn_len_median: 16
```
