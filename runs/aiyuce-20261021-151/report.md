# 审查笔记 生成报告

slug：`aiyuce-20261021-151`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12815
LLM 调用：57 次，累计 222.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一份代码审查记录表 | 2190 | normal | 37.6 | 0 |  | 1 |
| 2 | 电费单上的用电增量 | 2345 | normal | 35.9 | 0 |  | 2 |
| 3 | 报价单上的推理成本 | 2341 | normal | 35.3 | 0 |  | 1 |
| 4 | 一份折旧表的矛盾 | 2105 | normal | 34.2 | 0 |  | 3 |
| 5 | 一份招聘JD的矛盾 | 2487 | normal | 35.4 | 0 |  | 1 |
| 6 | 一行修改后的代码注释 | 1341 | short | 35.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 27.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 3 句（如「如果报价单的实际计算结果显示差错只是由于四舍五入…」）
- 第 4 章：
  - dialogue_chars_pct 31.6 高于目标 18.0
  - narration_para_pct 20.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - narration_para_pct 36.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「如果有新的测试方法能够在不依赖人工的情况下准确识…」）

## 整书结构指标

```
chapters: 6
total_chars: 12486
chapter_chars_mean: 2081
chapter_chars_median: 2210
chapter_chars_cv: 0.2
paragraphs_mean: 18.5
dialogue_chars_pct: 16.6
dialogue_para_pct: 44.0
interiority_para_pct: 18.0
narration_para_pct: 38.0
turn_under20_pct: 51.9
turn_over200_pct: 0.0
attr_say_pct: 18.5
attr_adv_pct: 15.2
scenes_per_chapter: 1.7
dialogue_run_mean: 2.1
turn_len_median: 19
```
