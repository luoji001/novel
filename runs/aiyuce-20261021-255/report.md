# 初筛 生成报告

slug：`aiyuce-20261021-255`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11417
LLM 调用：53 次，累计 203.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅统计表 | 2158 | normal | 37.8 | 0 |  | 1 |
| 2 | 翻阅统计表 | 2199 | normal | 88.0 | 0 |  | 1 |
| 3 | 翻阅报价单 | 2520 | normal | 34.2 | 0 |  | 4 |
| 4 | 翻阅年度预算明细 | 2181 | normal | 35.3 | 0 |  | 1 |
| 5 | 翻阅招聘JD | 1063 | normal | 91.3 | 0 |  | 0 |
| 6 | 翻阅CT检查量统计表 | 1290 | short | 86.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 标题重复：「翻阅统计表」已存在
- 第 3 章：
  - dialogue_chars_pct 48.1 高于目标 18.0
  - dialogue_run_mean 5.2 高于目标 4.0
  - narration_para_pct 13.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 标题与《翻阅统计表》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11160
chapter_chars_mean: 1860
chapter_chars_median: 2131
chapter_chars_cv: 0.31
paragraphs_mean: 13.7
dialogue_chars_pct: 11.8
dialogue_para_pct: 31.1
interiority_para_pct: 15.6
narration_para_pct: 53.3
turn_under20_pct: 75.0
turn_over200_pct: 0.0
attr_say_pct: 15.9
attr_adv_pct: 5.3
scenes_per_chapter: 1.2
dialogue_run_mean: 1.9
turn_len_median: 5
```
