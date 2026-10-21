# 合同 生成报告

slug：`aiyuce-20261021-234`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12723
LLM 调用：57 次，累计 226.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 放大镜下的合同条款 | 2625 | normal | 38.4 | 0 |  | 1 |
| 2 | 核对付款凭证签名 | 1909 | normal | 35.2 | 0 |  | 1 |
| 3 | 核对财务报表数字 | 2169 | normal | 59.1 | 0 |  | 1 |
| 4 | 核对报价单页码 | 2134 | normal | 34.9 | 0 |  | 2 |
| 5 | 核对市场调研报告 | 2412 | normal | 88.2 | 0 |  | 2 |
| 6 | 核对合同单价数字 | 1468 | short | 35.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 40.0 低于目标 45.0
- 第 4 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3
  - narration_para_pct 43.8 低于目标 45.0
- 第 6 章：
  - narration_para_pct 36.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12443
chapter_chars_mean: 2074
chapter_chars_median: 2106
chapter_chars_cv: 0.19
paragraphs_mean: 14.8
dialogue_chars_pct: 4.7
dialogue_para_pct: 27.7
interiority_para_pct: 27.6
narration_para_pct: 44.8
turn_under20_pct: 85.3
turn_over200_pct: 0.0
attr_say_pct: 4.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.5
turn_len_median: 12
```
