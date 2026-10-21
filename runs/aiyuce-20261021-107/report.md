# 误检 生成报告

slug：`aiyuce-20261021-107`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12691
LLM 调用：57 次，累计 221.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 模型服务费用明细单 | 1822 | normal | 88.3 | 0 |  | 2 |
| 2 | 翻查案件检索报告 | 2579 | normal | 35.5 | 0 |  | 1 |
| 3 | 调整参数观察效果 | 2101 | normal | 35.8 | 0 |  | 1 |
| 4 | 调取费用明细单 | 2465 | normal | 35.2 | 0 |  | 2 |
| 5 | 拍桌投诉记录 | 2337 | normal | 36.2 | 0 |  | 3 |
| 6 | 翻看判决书一角 | 1381 | short | 36.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 43.4 高于目标 18.0
  - narration_para_pct 31.2 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《模型服务费用明细单》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - dialogue_chars_pct 20.4 高于目标 18.0
  - narration_para_pct 41.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 21.0 高于目标 18.0
  - narration_para_pct 35.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12402
chapter_chars_mean: 2067
chapter_chars_median: 2173
chapter_chars_cv: 0.22
paragraphs_mean: 15.8
dialogue_chars_pct: 14.7
dialogue_para_pct: 36.9
interiority_para_pct: 13.1
narration_para_pct: 50.0
turn_under20_pct: 50.9
turn_over200_pct: 0.0
attr_say_pct: 22.4
attr_adv_pct: 2.7
scenes_per_chapter: 2.3
dialogue_run_mean: 1.8
turn_len_median: 24
```
