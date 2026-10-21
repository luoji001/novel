# 标价单 生成报告

slug：`aiyuce-20261021-10`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13191
LLM 调用：57 次，累计 220.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 培训计划草案 | 2164 | normal | 36.7 | 0 |  | 3 |
| 2 | 分析报价单与招聘JD关联 | 2650 | normal | 36.1 | 0 |  | 2 |
| 3 | 电费单的能耗推算 | 2393 | normal | 34.3 | 0 |  | 1 |
| 4 | 折旧表的损耗率变化 | 2344 | normal | 91.0 | 0 |  | 1 |
| 5 | 培训计划草案 | 2266 | normal | 90.5 | 0 |  | 1 |
| 6 | 计算单价与工时变化 | 1368 | short | 90.3 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 31.1 高于目标 18.0
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 38.9 低于目标 45.0
  - [observe] 章内自我复读 5 句（如「如果市场上突然出现了大量具备相关资质的新从业者加…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 27.8 低于目标 45.0
- 第 5 章：
  - [observe] 标题重复：「培训计划草案」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12878
chapter_chars_mean: 2146
chapter_chars_median: 2258
chapter_chars_cv: 0.2
paragraphs_mean: 16.8
dialogue_chars_pct: 10.0
dialogue_para_pct: 28.3
interiority_para_pct: 17.5
narration_para_pct: 54.2
turn_under20_pct: 54.7
turn_over200_pct: 0.0
attr_say_pct: 14.0
attr_adv_pct: 8.3
scenes_per_chapter: 1.7
dialogue_run_mean: 1.8
turn_len_median: 23
```
