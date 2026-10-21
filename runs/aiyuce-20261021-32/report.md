# 校对钟 生成报告

slug：`aiyuce-20261021-32`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11621
LLM 调用：57 次，累计 209.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对校对费用表 | 2006 | normal | 95.5 | 0 |  | 1 |
| 2 | 校对工时记录表 | 2212 | normal | 35.5 | 0 |  | 1 |
| 3 | 翻阅客户反馈报告 | 1948 | normal | 88.5 | 0 |  | 0 |
| 4 | 查看校对工时记录 | 2397 | normal | 35.4 | 0 |  | 4 |
| 5 | 翻阅AI测试数据 | 1816 | normal | 80.8 | 0 |  | 3 |
| 6 | 审视AI测试数据 | 1236 | short | 82.1 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 43.8 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 26.3 高于目标 18.0
  - narration_para_pct 36.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
  - [observe] 标题与《校对工时记录表》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - dialogue_chars_pct 63.0 高于目标 18.0
  - dialogue_run_mean 16 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 25.0 高于目标 18.0
  - dialogue_run_mean 7 高于目标 4.0
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 标题与《翻阅AI测试数据》近似 0.75 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11329
chapter_chars_mean: 1888
chapter_chars_median: 1932
chapter_chars_cv: 0.21
paragraphs_mean: 15.7
dialogue_chars_pct: 19.7
dialogue_para_pct: 46.1
interiority_para_pct: 17.0
narration_para_pct: 36.9
turn_under20_pct: 57.7
turn_over200_pct: 0.0
attr_say_pct: 30.8
attr_adv_pct: 1.7
scenes_per_chapter: 1.2
dialogue_run_mean: 5.2
turn_len_median: 18
```
