# 电表 生成报告

slug：`aiyuce-20261021-208`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12398
LLM 调用：57 次，累计 225.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 计算电费单 | 2135 | normal | 38.4 | 0 |  | 1 |
| 2 | 划线计算电费单 | 2578 | normal | 90.5 | 0 |  | 2 |
| 3 | 划线计算电费单 | 2432 | normal | 87.8 | 0 |  | 1 |
| 4 | 划线计算电费单 | 2104 | normal | 36.4 | 0 |  | 2 |
| 5 | 划线计算电费单 | 1978 | normal | 22.2 | 0 |  | 2 |
| 6 | 查看电价涨幅数据 | 1165 | short | 88.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 21.4 低于目标 45.0
  - [observe] 标题与《计算电费单》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 标题重复：「划线计算电费单」已存在
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「划线计算电费单」已存在
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「划线计算电费单」已存在
- 第 6 章：
  - narration_para_pct 44.4 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 12135
chapter_chars_mean: 2022
chapter_chars_median: 2074
chapter_chars_cv: 0.24
paragraphs_mean: 14
dialogue_chars_pct: 4.0
dialogue_para_pct: 19.6
interiority_para_pct: 23.4
narration_para_pct: 57.1
turn_under20_pct: 70.2
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.7
turn_len_median: 10
```
