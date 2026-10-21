# 模型教室 生成报告

slug：`aiyuce-20261021-24`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11405
LLM 调用：57 次，累计 204.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 实验器材清单更新 | 2013 | normal | 91.4 | 0 |  | 2 |
| 2 | 预算报表的核对 | 1964 | normal | 35.2 | 0 |  | 1 |
| 3 | 培训课程报名记录的更新 | 1895 | normal | 89.1 | 0 |  | 2 |
| 4 | 课堂表现评估表的修订 | 2508 | normal | 34.8 | 0 |  | 3 |
| 5 | 成绩统计表的分析 | 1906 | normal | 84.1 | 0 |  | 2 |
| 6 | 备课记录表的修订 | 1113 | short | 80.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 41.0 高于目标 18.0
  - narration_para_pct 30.4 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 5 句（如「然而就在那一刻，教研组长突然想到一个问题，那就是…」）
- 第 3 章：
  - dialogue_chars_pct 21.8 高于目标 18.0
  - narration_para_pct 42.1 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 23.7 高于目标 18.0
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的情况削弱呢…」）
- 第 5 章：
  - dialogue_chars_pct 38.6 高于目标 18.0
  - narration_para_pct 15.0 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 66.3 高于目标 18.0
  - dialogue_run_mean 11 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11087
chapter_chars_mean: 1848
chapter_chars_median: 1882
chapter_chars_cv: 0.24
paragraphs_mean: 17.7
dialogue_chars_pct: 32.0
dialogue_para_pct: 61.6
interiority_para_pct: 6.1
narration_para_pct: 32.3
turn_under20_pct: 36.3
turn_over200_pct: 0.0
attr_say_pct: 28.3
attr_adv_pct: 1.2
scenes_per_chapter: 1.3
dialogue_run_mean: 4.9
turn_len_median: 28
```
