# 模型清单 生成报告

slug：`aiyuce-20261021-204`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12296
LLM 调用：57 次，累计 225.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻看电费单 | 2277 | normal | 95.1 | 0 |  | 0 |
| 2 | 翻看电费单 | 2209 | normal | 36.0 | 0 |  | 2 |
| 3 | 翻看成绩统计表 | 1748 | normal | 88.1 | 0 |  | 1 |
| 4 | 翻看物理模型清单 | 2494 | normal | 35.0 | 0 |  | 1 |
| 5 | 翻看招聘JD | 2400 | normal | 34.9 | 0 |  | 1 |
| 6 | 翻看成绩统计表 | 1162 | short | 88.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「翻看电费单」已存在
- 第 3 章：
  - narration_para_pct 30.8 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 标题重复：「翻看成绩统计表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12022
chapter_chars_mean: 2004
chapter_chars_median: 2200
chapter_chars_cv: 0.25
paragraphs_mean: 15
dialogue_chars_pct: 6.0
dialogue_para_pct: 23.7
interiority_para_pct: 16.6
narration_para_pct: 59.8
turn_under20_pct: 63.6
turn_over200_pct: 0.0
attr_say_pct: 6.3
attr_adv_pct: 3.1
scenes_per_chapter: 1.5
dialogue_run_mean: 1.1
turn_len_median: 10
```
