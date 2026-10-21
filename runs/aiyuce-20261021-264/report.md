# 模型教学 生成报告

slug：`aiyuce-20261021-264`
档位：AI 推演　闸门模式：observe
章数：6　总字数：10856
LLM 调用：57 次，累计 202.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 标注培训费用 | 2009 | normal | 86.8 | 0 |  | 3 |
| 2 | 空调运行时间核查 | 1914 | normal | 37.3 | 0 |  | 1 |
| 3 | 翻看作业本 | 1849 | normal | 57.9 | 0 |  | 2 |
| 4 | 翻看培训费用明细 | 1823 | normal | 35.4 | 0 |  | 2 |
| 5 | 翻看成绩统计表 | 1912 | normal | 91.7 | 0 |  | 0 |
| 6 | 翻看预算表 | 1343 | short | 89.3 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 31.5 高于目标 18.0
  - dialogue_run_mean 7 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 3 章：
  - interiority_para_pct 41.7 高于目标 40.0
  - narration_para_pct 41.7 低于目标 45.0
- 第 4 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 10611
chapter_chars_mean: 1768
chapter_chars_median: 1839
chapter_chars_cv: 0.13
paragraphs_mean: 12.7
dialogue_chars_pct: 12.5
dialogue_para_pct: 38.4
interiority_para_pct: 17.8
narration_para_pct: 43.8
turn_under20_pct: 63.4
turn_over200_pct: 0.0
attr_say_pct: 19.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.6
turn_len_median: 18
```
