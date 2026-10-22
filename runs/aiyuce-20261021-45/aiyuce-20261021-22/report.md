# 证书风波 生成报告

slug：`aiyuce-20261021-22`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13521
LLM 调用：57 次，累计 217.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 薪资条上的持证标记 | 2101 | normal | 37.7 | 0 |  | 1 |
| 2 | 敲击键盘的招聘JD | 2925 | normal | 23.4 | 0 |  | 2 |
| 3 | 敲击桌面的报价单 | 2638 | normal | 88.7 | 0 |  | 0 |
| 4 | 盯住统计表的指腹 | 2139 | normal | 35.7 | 0 |  | 1 |
| 5 | 盯住误差率的指腹 | 2128 | normal | 34.8 | 0 |  | 4 |
| 6 | 盯着误差率的指腹 | 1584 | short | 32.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 18.4 高于目标 18.0
  - narration_para_pct 27.8 低于目标 45.0
  - [observe] 章内自我复读 4 句（如「比如，如果新入职的持证人员培训时间较长，或者他们…」）
  - [observe] 标题与《盯住统计表的指腹》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 47.3 高于目标 18.0
  - narration_para_pct 27.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《盯住误差率的指腹》近似 0.88 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 13215
chapter_chars_mean: 2202
chapter_chars_median: 2084
chapter_chars_cv: 0.21
paragraphs_mean: 16.8
dialogue_chars_pct: 11.1
dialogue_para_pct: 30.2
interiority_para_pct: 21.4
narration_para_pct: 48.4
turn_under20_pct: 60.2
turn_over200_pct: 0.0
attr_say_pct: 20.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.4
turn_len_median: 16
```
