# 电笔 生成报告

slug：`aiyuce-20261021-69`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12294
LLM 调用：57 次，累计 211.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的增减 | 2098 | normal | 37.1 | 0 |  | 3 |
| 2 | AI报价单的阅读 | 2323 | normal | 87.8 | 0 |  | 2 |
| 3 | 服务器折旧表的展示 | 2348 | normal | 84.2 | 0 |  | 3 |
| 4 | 邮件发送瞬间 | 2208 | normal | 90.7 | 0 |  | 1 |
| 5 | 电费单的对照分析 | 2274 | normal | 89.5 | 0 |  | 0 |
| 6 | 空调用电数据对比 | 1037 | short | 35.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 28.9 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「如果教研组在接下来的一个月中没有采取任何实质性措…」）
- 第 2 章：
  - interiority_para_pct 71.4 高于目标 40.0
  - narration_para_pct 7.1 低于目标 45.0
- 第 3 章：
  - dialogue_chars_pct 39.6 高于目标 18.0
  - dialogue_run_mean 5 高于目标 4.0
  - narration_para_pct 10.0 低于目标 45.0
- 第 4 章：
  - narration_para_pct 35.3 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 60.1 高于目标 18.0
  - narration_para_pct 16.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）

## 整书结构指标

```
chapters: 6
total_chars: 12011
chapter_chars_mean: 2002
chapter_chars_median: 2196
chapter_chars_cv: 0.25
paragraphs_mean: 15.2
dialogue_chars_pct: 21.1
dialogue_para_pct: 46.9
interiority_para_pct: 23.6
narration_para_pct: 29.5
turn_under20_pct: 52.6
turn_over200_pct: 0.0
attr_say_pct: 23.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 2.5
turn_len_median: 26
```
