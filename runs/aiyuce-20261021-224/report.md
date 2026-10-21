# 计费尺 生成报告

slug：`aiyuce-20261021-224`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11623
LLM 调用：57 次，累计 206.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对报价单 | 2096 | normal | 94.4 | 0 |  | 0 |
| 2 | 核对校对明细表 | 1953 | normal | 35.6 | 0 |  | 1 |
| 3 | 核对校对明细表 | 2020 | normal | 34.7 | 0 |  | 2 |
| 4 | 核对校对明细表 | 2164 | normal | 34.4 | 0 |  | 2 |
| 5 | 核对校对明细表 | 2100 | normal | 80.9 | 0 |  | 4 |
| 6 | 踱步报价单 | 1284 | short | 37.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 2 句（如「如果实际上所有项目的交付周期都没有发生变化，而且…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对校对明细表」已存在
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对校对明细表」已存在
- 第 5 章：
  - dialogue_chars_pct 54.3 高于目标 18.0
  - dialogue_run_mean 9 高于目标 4.0
  - narration_para_pct 5.3 低于目标 45.0
  - [observe] 标题重复：「核对校对明细表」已存在
- 第 6 章：
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻？…」）
  - [observe] 标题与《核对报价单》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11359
chapter_chars_mean: 1893
chapter_chars_median: 2013
chapter_chars_cv: 0.17
paragraphs_mean: 14.3
dialogue_chars_pct: 13.3
dialogue_para_pct: 38.4
interiority_para_pct: 7.9
narration_para_pct: 53.7
turn_under20_pct: 53.5
turn_over200_pct: 0.0
attr_say_pct: 5.1
attr_adv_pct: 2.6
scenes_per_chapter: 1.2
dialogue_run_mean: 3.1
turn_len_median: 22
```
