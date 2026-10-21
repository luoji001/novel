# 听课笔记 生成报告

slug：`aiyuce-20261021-129`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11121
LLM 调用：53 次，累计 187.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 整理听课记录表 | 1960 | normal | 94.9 | 0 |  | 1 |
| 2 | 合同草稿 | 2552 | normal | 36.6 | 0 |  | 2 |
| 3 | 整理听课记录表 | 1193 | normal | 87.9 | 0 |  | 4 |
| 4 | 翻阅预算报表 | 1942 | normal | 34.1 | 0 |  | 3 |
| 5 | 翻阅问卷笔记 | 2197 | normal | 89.4 | 0 |  | 1 |
| 6 | 核对听课记录表 | 1271 | short | 35.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 31.2 低于目标 45.0
- 第 2 章：
  - narration_para_pct 35.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 20.1 高于目标 18.0
  - dialogue_run_mean 6 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题重复：「整理听课记录表」已存在
- 第 4 章：
  - dialogue_chars_pct 30.1 高于目标 18.0
  - narration_para_pct 5.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 26.7 低于目标 45.0
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《整理听课记录表》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 10864
chapter_chars_mean: 1811
chapter_chars_median: 1902
chapter_chars_cv: 0.29
paragraphs_mean: 13.8
dialogue_chars_pct: 15.5
dialogue_para_pct: 49.2
interiority_para_pct: 21.1
narration_para_pct: 29.8
turn_under20_pct: 51.3
turn_over200_pct: 0.0
attr_say_pct: 17.6
attr_adv_pct: 4.6
scenes_per_chapter: 1.3
dialogue_run_mean: 2.4
turn_len_median: 22
```
