# 摘句 生成报告

slug：`aiyuce-20261021-167`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12238
LLM 调用：57 次，累计 231.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 案件检索委托单 | 2145 | normal | 37.4 | 0 |  | 1 |
| 2 | 法律条文摘要 | 2527 | normal | 88.7 | 0 |  | 2 |
| 3 | 翻阅计费明细表 | 1995 | normal | 90.2 | 0 |  | 0 |
| 4 | 核对报价单数据 | 2102 | normal | 35.6 | 0 |  | 3 |
| 5 | 翻阅年度成本分析报告 | 2209 | normal | 35.6 | 0 |  | 1 |
| 6 | 翻阅案件检索委托单 | 1254 | short | 34.3 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 3 句（如「根据现行市场价格测算，若采用该人工智能辅助系统，…」）
- 第 2 章：
  - dialogue_chars_pct 26.1 高于目标 18.0
  - narration_para_pct 24.0 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 21.7 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 64.2 高于目标 18.0
  - dialogue_run_mean 4.3 高于目标 4.0
  - narration_para_pct 13.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《案件检索委托单》近似 0.88 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11944
chapter_chars_mean: 1991
chapter_chars_median: 2076
chapter_chars_cv: 0.21
paragraphs_mean: 15.7
dialogue_chars_pct: 17.8
dialogue_para_pct: 45.7
interiority_para_pct: 14.2
narration_para_pct: 40.1
turn_under20_pct: 59.5
turn_over200_pct: 0.0
attr_say_pct: 15.8
attr_adv_pct: 4.2
scenes_per_chapter: 1.2
dialogue_run_mean: 2.1
turn_len_median: 16
```
