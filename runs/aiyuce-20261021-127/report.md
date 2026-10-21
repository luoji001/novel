# 审码 生成报告

slug：`aiyuce-20261021-127`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11864
LLM 调用：57 次，累计 213.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击键盘 | 2595 | normal | 95.6 | 0 |  | 1 |
| 2 | 手指滑动折旧表 | 2350 | normal | 36.4 | 0 |  | 1 |
| 3 | 手指滑动审核日报 | 1547 | normal | 89.3 | 0 |  | 0 |
| 4 | 手指滑动评估报告 | 2105 | normal | 84.8 | 0 |  | 4 |
| 5 | 核对电费单 | 2014 | normal | 86.4 | 0 |  | 2 |
| 6 | 核对评估报告 | 1247 | short | 81.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 43.5 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 47.6 高于目标 18.0
  - dialogue_run_mean 4.7 高于目标 4.0
  - narration_para_pct 17.6 低于目标 45.0
  - [observe] 标题与《手指滑动审核日报》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - dialogue_chars_pct 28.4 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 75.4 高于目标 18.0
  - dialogue_run_mean 6.5 高于目标 4.0
  - narration_para_pct 7.1 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11576
chapter_chars_mean: 1929
chapter_chars_median: 2010
chapter_chars_cv: 0.26
paragraphs_mean: 16.3
dialogue_chars_pct: 24.2
dialogue_para_pct: 44.7
interiority_para_pct: 15.9
narration_para_pct: 39.4
turn_under20_pct: 42.9
turn_over200_pct: 0.0
attr_say_pct: 15.2
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 2.8
turn_len_median: 25
```
