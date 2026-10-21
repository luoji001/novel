# 报价单 生成报告

slug：`aiyuce-20261021-162`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12320
LLM 调用：57 次，累计 208.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对报价单 | 1808 | normal | 90.9 | 0 |  | 2 |
| 2 | 核对公告文本 | 2281 | normal | 36.6 | 0 |  | 1 |
| 3 | 核对财务报表 | 2165 | normal | 35.2 | 0 |  | 1 |
| 4 | 核对合同文本 | 2312 | normal | 34.4 | 0 |  | 5 |
| 5 | 核对行业报告 | 2388 | normal | 36.0 | 0 |  | 1 |
| 6 | 核对报价单变化 | 1360 | short | 89.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 58.3 高于目标 40.0
  - narration_para_pct 33.3 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 31.2 高于目标 18.0
  - dialogue_run_mean 4.3 高于目标 4.0
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《核对公告文本》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 标题与《核对报价单》近似 0.83 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 12044
chapter_chars_mean: 2007
chapter_chars_median: 2179
chapter_chars_cv: 0.2
paragraphs_mean: 14.8
dialogue_chars_pct: 9.7
dialogue_para_pct: 30.5
interiority_para_pct: 22.3
narration_para_pct: 47.1
turn_under20_pct: 76.1
turn_over200_pct: 0.0
attr_say_pct: 8.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.9
turn_len_median: 13
```
