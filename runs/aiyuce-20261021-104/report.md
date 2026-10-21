# 校对小时 生成报告

slug：`aiyuce-20261021-104`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13862
LLM 调用：57 次，累计 241.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲报价单 | 2411 | normal | 96.8 | 0 |  | 1 |
| 2 | 测试报告 | 2618 | normal | 35.7 | 0 |  | 1 |
| 3 | 翻阅投诉记录 | 2420 | normal | 53.8 | 0 |  | 0 |
| 4 | 翻阅离职统计 | 2317 | normal | 35.1 | 0 |  | 3 |
| 5 | 翻阅预算调整方案 | 2707 | normal | 33.6 | 0 |  | 1 |
| 6 | 敲击桌面 | 1383 | short | 86.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现。

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 17.6 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 18.6 高于目标 18.0
  - narration_para_pct 22.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 34.3 高于目标 18.0
  - narration_para_pct 14.3 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 13593
chapter_chars_mean: 2266
chapter_chars_median: 2370
chapter_chars_cv: 0.21
paragraphs_mean: 15.2
dialogue_chars_pct: 8.7
dialogue_para_pct: 30.1
interiority_para_pct: 18.8
narration_para_pct: 51.1
turn_under20_pct: 76.7
turn_over200_pct: 0.0
attr_say_pct: 29.4
attr_adv_pct: 3.2
scenes_per_chapter: 1.5
dialogue_run_mean: 1.5
turn_len_median: 8
```
