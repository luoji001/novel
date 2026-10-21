# 验码 生成报告

slug：`aiyuce-20261021-247`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11961
LLM 调用：57 次，累计 213.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电费单数据 | 2222 | normal | 95.0 | 0 |  | 0 |
| 2 | 审阅招聘JD | 2412 | normal | 90.4 | 0 |  | 0 |
| 3 | 审阅代码验证手册 | 2106 | normal | 36.2 | 0 |  | 2 |
| 4 | 核对代码验证手册 | 2488 | normal | 34.8 | 0 |  | 2 |
| 5 | 审阅代码验证手册 | 1540 | normal | 89.5 | 0 |  | 2 |
| 6 | 审阅代码验证报告 | 1187 | short | 34.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - dialogue_chars_pct 18.5 高于目标 18.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《审阅代码验证手册》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 35.7 低于目标 45.0
  - [observe] 标题重复：「审阅代码验证手册」已存在
- 第 6 章：
  - dialogue_chars_pct 34.4 高于目标 18.0
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《审阅代码验证手册》近似 0.75 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11668
chapter_chars_mean: 1945
chapter_chars_median: 2112
chapter_chars_cv: 0.26
paragraphs_mean: 16.2
dialogue_chars_pct: 11.4
dialogue_para_pct: 33.3
interiority_para_pct: 17.6
narration_para_pct: 49.1
turn_under20_pct: 44.9
turn_over200_pct: 0.0
attr_say_pct: 30.9
attr_adv_pct: 5.2
scenes_per_chapter: 1.5
dialogue_run_mean: 1.8
turn_len_median: 26
```
