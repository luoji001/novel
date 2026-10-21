# 校对主管的担忧 生成报告

slug：`aiyuce-20261021-152`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12012
LLM 调用：57 次，累计 223.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电费单 | 2062 | normal | 93.8 | 0 |  | 0 |
| 2 | 校对电脑的运行声 | 2344 | normal | 87.6 | 0 |  | 2 |
| 3 | 校对小时制测算 | 2210 | normal | 36.0 | 0 |  | 1 |
| 4 | 核对折旧表 | 2010 | normal | 87.8 | 0 |  | 1 |
| 5 | 核对报价单 | 1895 | normal | 36.4 | 0 |  | 3 |
| 6 | 电费单金额稳定 | 1485 | short | 34.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - dialogue_chars_pct 36.2 高于目标 18.0
  - narration_para_pct 30.4 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 38.5 低于目标 45.0
- 第 5 章：
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「如果我们能把这项技术整合进我们的服务体系中………」）
  - [observe] 标题与《核对电费单》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 11747
chapter_chars_mean: 1958
chapter_chars_median: 1998
chapter_chars_cv: 0.15
paragraphs_mean: 14.5
dialogue_chars_pct: 10.1
dialogue_para_pct: 26.6
interiority_para_pct: 10.6
narration_para_pct: 62.9
turn_under20_pct: 67.7
turn_over200_pct: 0.0
attr_say_pct: 22.4
attr_adv_pct: 7.5
scenes_per_chapter: 1.7
dialogue_run_mean: 2.0
turn_len_median: 9
```
