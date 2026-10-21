# 模型清单 生成报告

slug：`aiyuce-20261021-48`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12626
LLM 调用：57 次，累计 223.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 备课记录表上的数字 | 1729 | normal | 94.8 | 0 |  | 1 |
| 2 | 模型清单上的勾号 | 2842 | normal | 81.9 | 0 |  | 3 |
| 3 | 模型制作时间分配 | 2043 | normal | 88.7 | 0 |  | 1 |
| 4 | 核对成本明细表 | 2100 | normal | 91.8 | 0 |  | 2 |
| 5 | 模型备课法的应用效果 | 2497 | normal | 88.6 | 0 |  | 0 |
| 6 | 核对成绩分布趋势 | 1409 | short | 34.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 13.3 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 39.4 高于目标 18.0
  - dialogue_run_mean 7.5 高于目标 4.0
  - narration_para_pct 8.6 低于目标 45.0
- 第 3 章：
  - 单条套路句式超限：「李建国的」×8
- 第 4 章：
  - 单条套路句式超限：「李建国的」×3
  - narration_para_pct 35.3 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 30.9 高于目标 18.0
  - narration_para_pct 18.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12304
chapter_chars_mean: 2051
chapter_chars_median: 2028
chapter_chars_cv: 0.25
paragraphs_mean: 17.3
dialogue_chars_pct: 15.7
dialogue_para_pct: 42.7
interiority_para_pct: 16.4
narration_para_pct: 40.9
turn_under20_pct: 69.8
turn_over200_pct: 0.0
attr_say_pct: 10.2
attr_adv_pct: 5.9
scenes_per_chapter: 1.3
dialogue_run_mean: 2.6
turn_len_median: 10
```
