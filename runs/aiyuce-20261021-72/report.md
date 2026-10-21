# 模型图纸 生成报告

slug：`aiyuce-20261021-72`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11555
LLM 调用：57 次，累计 216.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅成绩统计表 | 1532 | normal | 89.3 | 0 |  | 3 |
| 2 | 图纸交付讨论 | 1944 | normal | 34.1 | 0 |  | 4 |
| 3 | 模型使用频次调整 | 2373 | normal | 35.3 | 0 |  | 3 |
| 4 | 翻阅成绩统计表 | 1981 | normal | 78.7 | 0 |  | 4 |
| 5 | 实地考察模型教学 | 2560 | normal | 35.0 | 0 |  | 1 |
| 6 | 翻阅成绩统计表 | 1159 | short | 33.2 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 56.5 高于目标 18.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - narration_para_pct 9.5 低于目标 45.0
- 第 2 章：
  - 单条套路句式超限：「他知道这」×3
  - dialogue_chars_pct 33.0 高于目标 18.0
  - narration_para_pct 20.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 24.3 高于目标 18.0
  - narration_para_pct 44.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 64.1 高于目标 18.0
  - dialogue_run_mean 7.5 高于目标 4.0
  - narration_para_pct 6.2 低于目标 45.0
  - [observe] 标题重复：「翻阅成绩统计表」已存在
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 58.0 高于目标 18.0
  - narration_para_pct 16.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「翻阅成绩统计表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11224
chapter_chars_mean: 1871
chapter_chars_median: 1908
chapter_chars_cv: 0.27
paragraphs_mean: 19.5
dialogue_chars_pct: 34.8
dialogue_para_pct: 58.4
interiority_para_pct: 2.7
narration_para_pct: 38.8
turn_under20_pct: 39.2
turn_over200_pct: 0.0
attr_say_pct: 27.5
attr_adv_pct: 4.3
scenes_per_chapter: 2.7
dialogue_run_mean: 4.1
turn_len_median: 25
```
