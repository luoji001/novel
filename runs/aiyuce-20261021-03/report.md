# 胶片 生成报告

slug：`aiyuce-20261021-03`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12612
LLM 调用：57 次，累计 247.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击桌面 | 1934 | normal | 95.2 | 0 |  | 1 |
| 2 | 敲击表格单元格 | 2042 | normal | 35.8 | 0 |  | 3 |
| 3 | 翻阅预算报表 | 2321 | normal | 79.9 | 0 |  | 3 |
| 4 | 翻阅采购清单 | 2562 | normal | 87.9 | 0 |  | 1 |
| 5 | 翻阅招聘JD | 2307 | normal | 88.6 | 0 |  | 1 |
| 6 | 翻阅统计表 | 1440 | short | 87.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 23.1 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 23.6 高于目标 18.0
  - narration_para_pct 21.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 61.1 高于目标 18.0
  - dialogue_run_mean 12 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
- 第 4 章：
  - narration_para_pct 35.7 低于目标 45.0
- 第 5 章：
  - narration_para_pct 37.5 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 29.8 高于目标 18.0
  - narration_para_pct 11.1 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 12342
chapter_chars_mean: 2057
chapter_chars_median: 2128
chapter_chars_cv: 0.19
paragraphs_mean: 15.2
dialogue_chars_pct: 22.9
dialogue_para_pct: 59.3
interiority_para_pct: 18.3
narration_para_pct: 22.4
turn_under20_pct: 52.2
turn_over200_pct: 0.0
attr_say_pct: 8.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 3.5
turn_len_median: 20
```
