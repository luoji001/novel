# 电光纸影 生成报告

slug：`aiyuce-20261021-133`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13483
LLM 调用：57 次，累计 241.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的数字变化 | 2048 | normal | 95.7 | 0 |  | 1 |
| 2 | 折旧表上的账面价值 | 2492 | normal | 35.2 | 0 |  | 2 |
| 3 | 报价单上的数字 | 2572 | normal | 35.9 | 0 |  | 3 |
| 4 | 作业本上的字数统计 | 2372 | normal | 35.8 | 0 |  | 2 |
| 5 | AI代写服务定价 | 2608 | normal | 34.7 | 0 |  | 1 |
| 6 | 电费单上的数字变化 | 1385 | short | 35.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 29.4 低于目标 45.0
- 第 2 章：
  - 单条套路句式超限：「临泉县文印社」×6、「临泉县文印社的」×5、「临泉县供电公司」×3
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - 单条套路句式超限：「临泉县文印社」×5
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《电费单上的数字变化》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「临泉县文印社」×5
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「电费单上的数字变化」已存在

## 整书结构指标

```
chapters: 6
total_chars: 13176
chapter_chars_mean: 2196
chapter_chars_median: 2383
chapter_chars_cv: 0.21
paragraphs_mean: 16.8
dialogue_chars_pct: 4.3
dialogue_para_pct: 26.5
interiority_para_pct: 9.8
narration_para_pct: 63.8
turn_under20_pct: 87.0
turn_over200_pct: 0.0
attr_say_pct: 8.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.4
turn_len_median: 6
```
