# 智控电价 生成报告

slug：`aiyuce-20261021-227`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11070
LLM 调用：57 次，累计 207.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻电费单算能耗 | 1677 | normal | 95.9 | 0 |  | 0 |
| 2 | 招聘JD上的指纹 | 2111 | normal | 37.4 | 0 |  | 1 |
| 3 | 翻看折旧表谈效益 | 1967 | normal | 35.4 | 0 |  | 3 |
| 4 | 翻看报价单算效率 | 2307 | normal | 93.3 | 0 |  | 1 |
| 5 | 翻电费单算能耗 | 1916 | normal | 34.6 | 0 |  | 5 |
| 6 | 翻看报价单算效率 | 1086 | short | 34.4 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 3 章：
  - dialogue_chars_pct 39.1 高于目标 18.0
  - narration_para_pct 21.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 27.8 低于目标 45.0
- 第 5 章：
  - dialogue_chars_pct 65.6 高于目标 18.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - narration_para_pct 13.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「翻电费单算能耗」已存在
- 第 6 章：
  - dialogue_chars_pct 62.6 高于目标 18.0
  - dialogue_run_mean 5 高于目标 4.0
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
  - [observe] 标题重复：「翻看报价单算效率」已存在

## 整书结构指标

```
chapters: 6
total_chars: 10759
chapter_chars_mean: 1793
chapter_chars_median: 1881
chapter_chars_cv: 0.24
paragraphs_mean: 17.7
dialogue_chars_pct: 30.9
dialogue_para_pct: 57.3
interiority_para_pct: 9.1
narration_para_pct: 33.5
turn_under20_pct: 45.1
turn_over200_pct: 0.0
attr_say_pct: 20.8
attr_adv_pct: 1.5
scenes_per_chapter: 1.8
dialogue_run_mean: 3.2
turn_len_median: 22
```
