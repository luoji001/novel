# 校对小时 生成报告

slug：`aiyuce-20261021-272`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11818
LLM 调用：57 次，累计 222.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻译报价单的数字 | 1822 | normal | 94.5 | 0 |  | 0 |
| 2 | 核对电费单数据 | 2272 | normal | 35.0 | 0 |  | 1 |
| 3 | 审视招聘JD | 2202 | normal | 36.0 | 0 |  | 2 |
| 4 | 审视推理报价单 | 2063 | normal | 91.8 | 0 |  | 1 |
| 5 | 审视机器折旧表 | 2254 | normal | 87.0 | 0 |  | 0 |
| 6 | 敲打报价单 | 1199 | short | 81.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 35.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 33.3 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 37.0 高于目标 18.0
  - dialogue_run_mean 7 高于目标 4.0
  - narration_para_pct 18.2 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11558
chapter_chars_mean: 1926
chapter_chars_median: 2088
chapter_chars_cv: 0.21
paragraphs_mean: 13.2
dialogue_chars_pct: 6.0
dialogue_para_pct: 25.7
interiority_para_pct: 16.3
narration_para_pct: 58.1
turn_under20_pct: 82.3
turn_over200_pct: 0.0
attr_say_pct: 82.4
attr_adv_pct: 7.0
scenes_per_chapter: 1.3
dialogue_run_mean: 3.0
turn_len_median: 10
```
