# 校对小时 生成报告

slug：`aiyuce-20261021-164`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11525
LLM 调用：57 次，累计 209.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对千字报价 | 1938 | normal | 97.6 | 0 |  | 0 |
| 2 | 校对服务满意度 | 2197 | normal | 37.4 | 0 |  | 2 |
| 3 | 核对折旧表数据 | 2096 | normal | 35.8 | 0 |  | 1 |
| 4 | 核对报价单边缘 | 2113 | normal | 36.1 | 0 |  | 3 |
| 5 | 核对工作时间记录 | 1811 | normal | 35.4 | 0 |  | 1 |
| 6 | 校对成本占比数据 | 1364 | short | 90.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《核对千字报价》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的情况所推翻…」）
- 第 6 章：
  - dialogue_chars_pct 19.2 高于目标 18.0
  - narration_para_pct 22.2 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11260
chapter_chars_mean: 1877
chapter_chars_median: 1968
chapter_chars_cv: 0.16
paragraphs_mean: 14
dialogue_chars_pct: 7.3
dialogue_para_pct: 36.1
interiority_para_pct: 19.8
narration_para_pct: 44.1
turn_under20_pct: 70.4
turn_over200_pct: 0.0
attr_say_pct: 23.4
attr_adv_pct: 22.5
scenes_per_chapter: 1
dialogue_run_mean: 1.7
turn_len_median: 10
```
