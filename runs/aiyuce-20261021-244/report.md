# 电表指针 生成报告

slug：`aiyuce-20261021-244`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11744
LLM 调用：57 次，累计 219.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电费单 | 1939 | normal | 95.8 | 0 |  | 1 |
| 2 | 查看招聘JD | 2304 | normal | 36.3 | 0 |  | 1 |
| 3 | 核对折旧表 | 2497 | normal | 36.6 | 0 |  | 1 |
| 4 | 核对报价单 | 1821 | normal | 81.5 | 0 |  | 5 |
| 5 | 核对电费单 | 1940 | normal | 91.5 | 0 |  | 2 |
| 6 | 核对报价单 | 1237 | short | 92.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 26.7 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3
  - dialogue_chars_pct 39.1 高于目标 18.0
  - dialogue_run_mean 8 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题与《核对电费单》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 26.7 低于目标 45.0
  - [observe] 标题重复：「核对电费单」已存在
- 第 6 章：
  - [observe] 标题重复：「核对报价单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11469
chapter_chars_mean: 1912
chapter_chars_median: 1896
chapter_chars_cv: 0.23
paragraphs_mean: 15.8
dialogue_chars_pct: 12.1
dialogue_para_pct: 37.8
interiority_para_pct: 23.5
narration_para_pct: 38.7
turn_under20_pct: 54.2
turn_over200_pct: 0.0
attr_say_pct: 4.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 3.0
turn_len_median: 20
```
