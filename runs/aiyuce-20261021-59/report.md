# 检索清单 生成报告

slug：`aiyuce-20261021-59`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11262
LLM 调用：57 次，累计 217.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 看薪酬明细表 | 2034 | normal | 36.2 | 0 |  | 1 |
| 2 | 翻阅案件处理统计表 | 2041 | normal | 35.2 | 0 |  | 3 |
| 3 | 核对案件处理统计表 | 1926 | normal | 35.4 | 0 |  | 2 |
| 4 | 翻阅客户满意度报告 | 2291 | normal | 90.9 | 0 |  | 1 |
| 5 | 翻阅错误案例清单 | 1715 | normal | 34.3 | 0 |  | 3 |
| 6 | 查看薪酬明细表 | 1249 | short | 80.7 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - dialogue_chars_pct 68.8 高于目标 18.0
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《翻阅案件处理统计表》近似 0.78 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - narration_para_pct 28.6 低于目标 45.0
- 第 5 章：
  - dialogue_chars_pct 34.9 高于目标 18.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 39.0 高于目标 18.0
  - dialogue_run_mean 7 高于目标 4.0
  - narration_para_pct 22.2 低于目标 45.0
  - [observe] 标题与《看薪酬明细表》近似 0.92 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 10974
chapter_chars_mean: 1829
chapter_chars_median: 1928
chapter_chars_cv: 0.19
paragraphs_mean: 15.5
dialogue_chars_pct: 25.6
dialogue_para_pct: 50.3
interiority_para_pct: 7.8
narration_para_pct: 41.9
turn_under20_pct: 37.1
turn_over200_pct: 0.0
attr_say_pct: 12.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 3.5
turn_len_median: 24
```
