# 代码灯 生成报告

slug：`aiyuce-20261021-271`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12906
LLM 调用：57 次，累计 217.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 审视招聘JD | 2724 | normal | 96.3 | 0 |  | 2 |
| 2 | 浏览招聘JD | 2379 | normal | 34.6 | 0 |  | 2 |
| 3 | 核对电费单 | 2181 | normal | 36.8 | 0 |  | 1 |
| 4 | 指指点点报价单 | 2166 | normal | 35.0 | 0 |  | 3 |
| 5 | 核对代码提交记录 | 2350 | normal | 36.6 | 0 |  | 1 |
| 6 | 摩挲咖啡杯沿 | 1100 | short | 89.5 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「深圳某科技园区」×3
  - narration_para_pct 33.3 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《审视招聘JD》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 4 章：
  - dialogue_chars_pct 43.1 高于目标 18.0
  - narration_para_pct 25.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的事实推翻呢…」）

## 整书结构指标

```
chapters: 6
total_chars: 12598
chapter_chars_mean: 2100
chapter_chars_median: 2218
chapter_chars_cv: 0.26
paragraphs_mean: 18
dialogue_chars_pct: 12.2
dialogue_para_pct: 35.7
interiority_para_pct: 16.3
narration_para_pct: 47.9
turn_under20_pct: 77.2
turn_over200_pct: 0.0
attr_say_pct: 18.6
attr_adv_pct: 1.8
scenes_per_chapter: 1.8
dialogue_run_mean: 2.0
turn_len_median: 8
```
