# 批改机 生成报告

slug：`aiyuce-20261021-21`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11746
LLM 调用：57 次，累计 212.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅听课记录表 | 1789 | normal | 38.2 | 0 |  | 3 |
| 2 | 翻看批改报告 | 2021 | normal | 34.5 | 0 |  | 3 |
| 3 | 翻看教师反馈问卷 | 2289 | normal | 35.8 | 0 |  | 1 |
| 4 | 查看AI批改报告 | 2340 | normal | 83.8 | 0 |  | 3 |
| 5 | 对比两份批改样本 | 1904 | normal | 35.6 | 0 |  | 1 |
| 6 | 翻看作文样本 | 1397 | short | 33.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 19.1 高于目标 18.0
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - dialogue_chars_pct 43.1 高于目标 18.0
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 36.6 高于目标 18.0
  - narration_para_pct 41.2 低于目标 45.0
  - [observe] 标题与《翻看批改报告》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「一条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 59.9 高于目标 18.0
  - narration_para_pct 16.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 11455
chapter_chars_mean: 1909
chapter_chars_median: 1912
chapter_chars_cv: 0.18
paragraphs_mean: 16.2
dialogue_chars_pct: 27.7
dialogue_para_pct: 55.6
interiority_para_pct: 5.3
narration_para_pct: 39.1
turn_under20_pct: 31.3
turn_over200_pct: 0.0
attr_say_pct: 34.2
attr_adv_pct: 3.7
scenes_per_chapter: 1.5
dialogue_run_mean: 2.6
turn_len_median: 28
```
