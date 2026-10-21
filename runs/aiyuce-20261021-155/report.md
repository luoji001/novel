# 页码之争 生成报告

slug：`aiyuce-20261021-155`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12537
LLM 调用：57 次，累计 227.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅案件处理清单 | 2331 | normal | 37.3 | 0 |  | 1 |
| 2 | 翻阅计费报价单 | 2442 | normal | 33.6 | 0 |  | 5 |
| 3 | 翻阅满意度调查表 | 2171 | normal | 92.5 | 0 |  | 1 |
| 4 | 翻开计费报价单 | 2265 | normal | 89.3 | 0 |  | 1 |
| 5 | 翻阅统计表 | 2155 | normal | 34.7 | 0 |  | 3 |
| 6 | 审视统计表 | 1167 | short | 88.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - 单条套路句式超限：「点了点头」×3
  - dialogue_chars_pct 52.5 高于目标 18.0
  - dialogue_run_mean 5.8 高于目标 4.0
  - narration_para_pct 13.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被模型复核系统出现严重的误判率而推翻…」）
- 第 3 章：
  - narration_para_pct 33.3 低于目标 45.0
- 第 4 章：
  - [observe] 标题与《翻阅计费报价单》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - dialogue_chars_pct 64.3 高于目标 18.0
  - narration_para_pct 18.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 24.3 高于目标 18.0
  - narration_para_pct 30.0 低于目标 45.0
  - [observe] 标题与《翻阅统计表》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 12198
chapter_chars_mean: 2033
chapter_chars_median: 2166
chapter_chars_cv: 0.22
paragraphs_mean: 18.5
dialogue_chars_pct: 28.9
dialogue_para_pct: 52.7
interiority_para_pct: 6.6
narration_para_pct: 40.7
turn_under20_pct: 56.1
turn_over200_pct: 0.0
attr_say_pct: 14.7
attr_adv_pct: 1.1
scenes_per_chapter: 1.3
dialogue_run_mean: 2.8
turn_len_median: 21
```
