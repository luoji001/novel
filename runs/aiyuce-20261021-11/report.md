# 页码 生成报告

slug：`aiyuce-20261021-11`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12103
LLM 调用：57 次，累计 211.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钢笔圈出关键数据 | 2240 | normal | 92.9 | 0 |  | 3 |
| 2 | 扫描报价单数据 | 2192 | normal | 34.8 | 0 |  | 3 |
| 3 | 手指圈住数据表格 | 2391 | normal | 81.5 | 0 |  | 3 |
| 4 | 圈住数据表格 | 1944 | normal | 36.2 | 0 |  | 2 |
| 5 | 手指圈住数据表格 | 1873 | normal | 86.4 | 0 |  | 4 |
| 6 | 手指圈住数据表格 | 1457 | short | 37.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 28.4 高于目标 18.0
  - dialogue_run_mean 4.3 高于目标 4.0
  - narration_para_pct 23.8 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 31.2 高于目标 18.0
  - narration_para_pct 23.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 64.7 高于目标 18.0
  - dialogue_run_mean 11 高于目标 4.0
  - narration_para_pct 7.9 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 3 句（如「比如当某个关键性的客户反馈表明他们对于某些类型案…」）
  - [observe] 标题与《手指圈住数据表格》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - dialogue_chars_pct 33.8 高于目标 18.0
  - dialogue_run_mean 5.5 高于目标 4.0
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 标题重复：「手指圈住数据表格」已存在
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「手指圈住数据表格」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11737
chapter_chars_mean: 1956
chapter_chars_median: 2018
chapter_chars_cv: 0.16
paragraphs_mean: 22.2
dialogue_chars_pct: 32.0
dialogue_para_pct: 58.6
interiority_para_pct: 9.6
narration_para_pct: 31.8
turn_under20_pct: 41.1
turn_over200_pct: 0.0
attr_say_pct: 31.2
attr_adv_pct: 7.5
scenes_per_chapter: 1.7
dialogue_run_mean: 4.8
turn_len_median: 28
```
