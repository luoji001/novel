# 电表指针 生成报告

slug：`aiyuce-20261021-14`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12439
LLM 调用：57 次，累计 231.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电费单 | 1933 | normal | 94.5 | 0 |  | 0 |
| 2 | 盯着电费单 | 2268 | normal | 36.1 | 0 |  | 2 |
| 3 | 核对报价单上的交付周期 | 2356 | normal | 34.5 | 0 |  | 1 |
| 4 | 数着损耗数据 | 2716 | normal | 89.7 | 0 |  | 1 |
| 5 | 分析订单增长趋势 | 1945 | normal | 35.4 | 0 |  | 1 |
| 6 | 核对电费单 | 1215 | short | 90.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《核对电费单》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 章内自我复读 2 句（如「如果有足够多的实际交易案例能够证明当前价位确实优…」）
- 第 4 章：
  - 单条套路句式超限：「到了一个」×3
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 标题重复：「核对电费单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12159
chapter_chars_mean: 2026
chapter_chars_median: 2060
chapter_chars_cv: 0.25
paragraphs_mean: 15.5
dialogue_chars_pct: 2.3
dialogue_para_pct: 16.8
interiority_para_pct: 20.9
narration_para_pct: 62.4
turn_under20_pct: 84.6
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.1
turn_len_median: 9
```
