# 打印店的墨水 生成报告

slug：`aiyuce-20261021-217`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11821
LLM 调用：57 次，累计 218.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 报表的折痕 | 1808 | normal | 38.0 | 0 |  | 1 |
| 2 | 核对服务器使用时间 | 2327 | normal | 35.5 | 0 |  | 1 |
| 3 | 修订报价单 | 2128 | normal | 88.7 | 0 |  | 1 |
| 4 | 问卷的折痕 | 2294 | normal | 36.2 | 0 |  | 2 |
| 5 | 修改声明的笔尖 | 1914 | normal | 36.8 | 0 |  | 2 |
| 6 | 报表上的折痕 | 1344 | short | 89.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 4 句（如「很简单，只需要有一天，AI代写服务的实际成交金额…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 29.4 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「一条关键性的推论会被什么推翻…」）
  - [observe] 标题与《报表的折痕》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 23.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 标题与《报表的折痕》近似 0.91 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11551
chapter_chars_mean: 1925
chapter_chars_median: 1972
chapter_chars_cv: 0.19
paragraphs_mean: 14.8
dialogue_chars_pct: 8.2
dialogue_para_pct: 31.9
interiority_para_pct: 18.1
narration_para_pct: 50.0
turn_under20_pct: 57.3
turn_over200_pct: 0.0
attr_say_pct: 15.5
attr_adv_pct: 10.1
scenes_per_chapter: 1
dialogue_run_mean: 1.5
turn_len_median: 18
```
