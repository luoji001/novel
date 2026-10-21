# 审码录 生成报告

slug：`aiyuce-20261021-43`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12206
LLM 调用：57 次，累计 218.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 审核报表悄然变动 | 2148 | normal | 96.5 | 0 |  | 0 |
| 2 | 绩效考核表数据分析 | 2275 | normal | 35.5 | 0 |  | 1 |
| 3 | 代码审查工具性能测试报告 | 2071 | normal | 89.4 | 0 |  | 0 |
| 4 | 试用期延长审批单 | 2131 | normal | 87.1 | 0 |  | 3 |
| 5 | 敲击键盘审代码 | 2303 | normal | 35.7 | 0 |  | 2 |
| 6 | 审代码时手机震动 | 1272 | short | 91.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 25.9 高于目标 18.0
  - dialogue_run_mean 5 高于目标 4.0
  - narration_para_pct 42.1 低于目标 45.0
- 第 5 章：
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - narration_para_pct 44.4 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11920
chapter_chars_mean: 1987
chapter_chars_median: 2088
chapter_chars_cv: 0.19
paragraphs_mean: 15
dialogue_chars_pct: 9.9
dialogue_para_pct: 30.2
interiority_para_pct: 13.9
narration_para_pct: 55.9
turn_under20_pct: 52.3
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 13.7
scenes_per_chapter: 1.8
dialogue_run_mean: 2.2
turn_len_median: 22
```
