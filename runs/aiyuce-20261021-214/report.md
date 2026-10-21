# 证书 生成报告

slug：`aiyuce-20261021-214`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13245
LLM 调用：57 次，累计 232.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 工时记录表 | 2663 | normal | 94.7 | 0 |  | 1 |
| 2 | 报价单上的数字 | 2127 | normal | 90.0 | 0 |  | 1 |
| 3 | 未通过的考试报名表 | 2049 | normal | 36.5 | 0 |  | 2 |
| 4 | 盯着证书要求看 | 2734 | normal | 36.0 | 0 |  | 2 |
| 5 | 质量校验系统 | 2187 | normal | 54.9 | 0 |  | 0 |
| 6 | 审核流程文件 | 1479 | short | 36.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 31.8 低于目标 45.0
- 第 2 章：
  - narration_para_pct 20.0 低于目标 45.0
- 第 3 章：
  - narration_para_pct 41.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - 单条套路句式超限：「变得更加」×3
  - [observe] 章内自我复读 2 句（如「比如说如果有大量不具备证书却又表现优异的人能够在…」）
- 第 6 章：
  - narration_para_pct 36.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12947
chapter_chars_mean: 2158
chapter_chars_median: 2114
chapter_chars_cv: 0.21
paragraphs_mean: 16.5
dialogue_chars_pct: 6.8
dialogue_para_pct: 32.2
interiority_para_pct: 21.7
narration_para_pct: 46.2
turn_under20_pct: 62.4
turn_over200_pct: 0.0
attr_say_pct: 10.6
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 1.6
turn_len_median: 15
```
