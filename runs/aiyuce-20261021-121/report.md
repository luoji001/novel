# 代写订单 生成报告

slug：`aiyuce-20261021-121`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12486
LLM 调用：57 次，累计 219.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对月度财务报表 | 1700 | normal | 94.5 | 0 |  | 1 |
| 2 | 盯价格清单的手指 | 2602 | normal | 36.9 | 0 |  | 1 |
| 3 | 盯着客户订单记录 | 2494 | normal | 36.8 | 0 |  | 2 |
| 4 | 核对论文相似度 | 2075 | normal | 92.4 | 0 |  | 1 |
| 5 | 盯着客户订单记录 | 2126 | normal | 35.8 | 0 |  | 3 |
| 6 | 盯月度财务报表 | 1483 | short | 90.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 25.0 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 42.1 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 4 章：
  - narration_para_pct 28.6 低于目标 45.0
- 第 5 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
  - [observe] 标题重复：「盯着客户订单记录」已存在
- 第 6 章：
  - [observe] 标题与《核对月度财务报表》近似 0.80 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 12196
chapter_chars_mean: 2033
chapter_chars_median: 2051
chapter_chars_cv: 0.21
paragraphs_mean: 15.8
dialogue_chars_pct: 6.4
dialogue_para_pct: 34.0
interiority_para_pct: 19.9
narration_para_pct: 46.1
turn_under20_pct: 69.0
turn_over200_pct: 0.0
attr_say_pct: 10.4
attr_adv_pct: 19.0
scenes_per_chapter: 2.3
dialogue_run_mean: 1.8
turn_len_median: 10
```
