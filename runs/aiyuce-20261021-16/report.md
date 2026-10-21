# 降压器 生成报告

slug：`aiyuce-20261021-16`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13165
LLM 调用：57 次，累计 224.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电力调度员的岗位说明书 | 2393 | normal | 56.5 | 0 |  | 0 |
| 2 | 电费单核对分析 | 2032 | normal | 34.8 | 0 |  | 1 |
| 3 | 触摸折旧表边缘 | 2373 | normal | 36.2 | 0 |  | 1 |
| 4 | 触摸折旧表边缘 | 2354 | normal | 89.0 | 0 |  | 1 |
| 5 | 触摸岗位说明书边缘 | 2545 | normal | 89.5 | 0 |  | 0 |
| 6 | 核对电费单 | 1462 | short | 35.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 标题重复：「触摸折旧表边缘」已存在
- 第 6 章：
  - dialogue_chars_pct 34.2 高于目标 18.0
  - narration_para_pct 18.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12889
chapter_chars_mean: 2148
chapter_chars_median: 2316
chapter_chars_cv: 0.18
paragraphs_mean: 14.7
dialogue_chars_pct: 6.1
dialogue_para_pct: 21.4
interiority_para_pct: 16.9
narration_para_pct: 61.7
turn_under20_pct: 69.0
turn_over200_pct: 0.0
attr_say_pct: 23.6
attr_adv_pct: 23.6
scenes_per_chapter: 1.5
dialogue_run_mean: 1.7
turn_len_median: 13
```
