# 模型 生成报告

slug：`aiyuce-20261021-12`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12647
LLM 调用：57 次，累计 220.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲成绩统计表 | 2226 | normal | 95.6 | 0 |  | 1 |
| 2 | 摩挲备课笔记 | 2297 | normal | 89.8 | 0 |  | 0 |
| 3 | 摩挲图纸标注细节 | 2515 | normal | 33.9 | 0 |  | 3 |
| 4 | 摩挲成绩统计表 | 2309 | normal | 35.9 | 0 |  | 2 |
| 5 | 摩挲力学模型部件 | 1988 | normal | 80.6 | 0 |  | 3 |
| 6 | 摩挲成绩统计表 | 1306 | short | 87.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 31.2 低于目标 45.0
- 第 3 章：
  - dialogue_chars_pct 38.5 高于目标 18.0
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的数据推翻呢…」）
  - [observe] 标题重复：「摩挲成绩统计表」已存在
- 第 5 章：
  - dialogue_chars_pct 59.7 高于目标 18.0
  - dialogue_run_mean 10.5 高于目标 4.0
  - narration_para_pct 4.2 低于目标 45.0
- 第 6 章：
  - 情节与已写章节重复 0.75 ≥ 0.72（撞上「陈志远分析2023年物理统考成绩，发现平均分上升、标准差…」）
  - [observe] 标题重复：「摩挲成绩统计表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12340
chapter_chars_mean: 2057
chapter_chars_median: 2213
chapter_chars_cv: 0.2
paragraphs_mean: 17.5
dialogue_chars_pct: 19.8
dialogue_para_pct: 43.0
interiority_para_pct: 18.7
narration_para_pct: 38.3
turn_under20_pct: 66.0
turn_over200_pct: 0.0
attr_say_pct: 21.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 3.0
turn_len_median: 14
```
