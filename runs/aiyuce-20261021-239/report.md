# 合同签约 生成报告

slug：`aiyuce-20261021-239`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11407
LLM 调用：57 次，累计 218.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字的合同文件 | 2335 | normal | 96.4 | 0 |  | 0 |
| 2 | 准确率对比报告 | 1985 | normal | 34.8 | 0 |  | 3 |
| 3 | 收入明细表上的指痕 | 1738 | normal | 87.4 | 0 |  | 2 |
| 4 | 翻阅收入明细表 | 1939 | normal | 33.3 | 0 |  | 4 |
| 5 | 翻阅预算调整方案 | 2123 | normal | 23.7 | 0 |  | 1 |
| 6 | 翻阅准确率对比报告 | 1281 | short | 82.6 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - dialogue_chars_pct 46.1 高于目标 18.0
  - narration_para_pct 23.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 41.6 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 58.4 高于目标 18.0
  - narration_para_pct 14.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《收入明细表上的指痕》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 56.7 高于目标 18.0
  - dialogue_run_mean 6 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题与《准确率对比报告》近似 0.88 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11107
chapter_chars_mean: 1851
chapter_chars_median: 1912
chapter_chars_cv: 0.2
paragraphs_mean: 16.2
dialogue_chars_pct: 32.9
dialogue_para_pct: 52.8
interiority_para_pct: 4.6
narration_para_pct: 42.6
turn_under20_pct: 26.6
turn_over200_pct: 0.0
attr_say_pct: 22.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 3.6
turn_len_median: 31
```
