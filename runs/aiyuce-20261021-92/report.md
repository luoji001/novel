# 校对钟 生成报告

slug：`aiyuce-20261021-92`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11056
LLM 调用：57 次，累计 215.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 校对小时的计算 | 1864 | normal | 96.5 | 0 |  | 1 |
| 2 | 核对电费单细节 | 2035 | normal | 91.0 | 0 |  | 0 |
| 3 | 校对培训课程 | 2020 | normal | 36.4 | 0 |  | 1 |
| 4 | 核对报价单细节 | 1972 | normal | 81.4 | 0 |  | 4 |
| 5 | 核对报价单细节 | 1834 | normal | 35.7 | 0 |  | 2 |
| 6 | 核对折旧表细节 | 1325 | short | 35.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 38.5 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 55.8 高于目标 18.0
  - dialogue_run_mean 15 高于目标 4.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 标题与《核对电费单细节》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对报价单细节」已存在
- 第 6 章：
  - dialogue_chars_pct 22.3 高于目标 18.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 10791
chapter_chars_mean: 1798
chapter_chars_median: 1870
chapter_chars_cv: 0.15
paragraphs_mean: 14.2
dialogue_chars_pct: 19.3
dialogue_para_pct: 41.0
interiority_para_pct: 11.8
narration_para_pct: 47.2
turn_under20_pct: 44.9
turn_over200_pct: 0.0
attr_say_pct: 37.2
attr_adv_pct: 10.1
scenes_per_chapter: 1
dialogue_run_mean: 4.2
turn_len_median: 26
```
