# 课表 生成报告

slug：`aiyuce-20261021-120`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11378
LLM 调用：57 次，累计 209.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 标准差数值波动 | 1867 | normal | 36.4 | 0 |  | 4 |
| 2 | 指针滑过课程设计表 | 2526 | normal | 34.8 | 0 |  | 3 |
| 3 | 培训费用支出凭证 | 2143 | normal | 80.0 | 0 |  | 3 |
| 4 | 问卷样本被反复核对 | 1559 | normal | 80.9 | 0 |  | 3 |
| 5 | 教师培训费用支出凭证 | 2011 | normal | 83.4 | 0 |  | 4 |
| 6 | 成绩统计表被轻敲 | 1266 | short | 88.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 33.2 高于目标 18.0
  - dialogue_run_mean 4.3 高于目标 4.0
  - narration_para_pct 27.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - dialogue_chars_pct 25.7 高于目标 18.0
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「说着他又看向那张课程设计表，“我们会在这份教案的…」）
- 第 3 章：
  - dialogue_chars_pct 52.6 高于目标 18.0
  - dialogue_run_mean 7 高于目标 4.0
  - narration_para_pct 12.5 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 59.5 高于目标 18.0
  - dialogue_run_mean 17 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
- 第 5 章：
  - dialogue_chars_pct 53.7 高于目标 18.0
  - dialogue_run_mean 6 高于目标 4.0
  - narration_para_pct 9.5 低于目标 45.0
  - [observe] 标题与《培训费用支出凭证》近似 0.89 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 30.8 高于目标 18.0
  - narration_para_pct 18.2 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11063
chapter_chars_mean: 1844
chapter_chars_median: 1884
chapter_chars_cv: 0.24
paragraphs_mean: 17.5
dialogue_chars_pct: 42.1
dialogue_para_pct: 75.1
interiority_para_pct: 4.7
narration_para_pct: 20.2
turn_under20_pct: 35.8
turn_over200_pct: 0.0
attr_say_pct: 11.2
attr_adv_pct: 4.5
scenes_per_chapter: 1
dialogue_run_mean: 6.9
turn_len_median: 25
```
