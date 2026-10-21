# 墨盒 生成报告

slug：`aiyuce-20261021-253`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12963
LLM 调用：57 次，累计 225.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的数字变化 | 2341 | normal | 93.0 | 0 |  | 2 |
| 2 | 折旧表上的数字 | 2081 | normal | 36.9 | 0 |  | 1 |
| 3 | 核对报价单数据 | 2662 | normal | 91.0 | 0 |  | 1 |
| 4 | 检查AI代写服务数据 | 2024 | normal | 91.4 | 0 |  | 0 |
| 5 | 核对电费单数据 | 2525 | normal | 87.2 | 0 |  | 4 |
| 6 | 核对电费单数据 | 1324 | short | 36.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 47.1 高于目标 40.0
  - narration_para_pct 41.2 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 36.8 低于目标 45.0
- 第 5 章：
  - 单条套路句式超限：「他知道这」×4
  - interiority_para_pct 58.8 高于目标 40.0
  - narration_para_pct 11.8 低于目标 45.0
  - [observe] 标题与《核对报价单数据》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 41.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对电费单数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12670
chapter_chars_mean: 2112
chapter_chars_median: 2163
chapter_chars_cv: 0.22
paragraphs_mean: 16
dialogue_chars_pct: 5.4
dialogue_para_pct: 28.2
interiority_para_pct: 32.9
narration_para_pct: 38.9
turn_under20_pct: 73.9
turn_over200_pct: 0.0
attr_say_pct: 8.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.1
turn_len_median: 10
```
