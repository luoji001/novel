# 铜铃 生成报告

slug：`aiyuce-20261021-77`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12739
LLM 调用：57 次，累计 225.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅质检成本明细 | 2170 | normal | 94.3 | 0 |  | 1 |
| 2 | 翻阅质检成本明细 | 2340 | normal | 33.7 | 0 |  | 2 |
| 3 | 翻阅预算分配表 | 2438 | normal | 35.0 | 0 |  | 2 |
| 4 | 翻阅编制表数据 | 2280 | normal | 34.8 | 0 |  | 1 |
| 5 | 翻阅编制表数据 | 2202 | normal | 87.4 | 0 |  | 1 |
| 6 | 核对质检成本明细 | 1303 | short | 34.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 40.0 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「翻阅质检成本明细」已存在
- 第 3 章：
  - 单条套路句式超限：「了自己的」×3
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「2023年质检岗人员编制表…」）
- 第 5 章：
  - [observe] 标题重复：「翻阅编制表数据」已存在
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《翻阅质检成本明细》近似 0.75 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 12490
chapter_chars_mean: 2082
chapter_chars_median: 2201
chapter_chars_cv: 0.2
paragraphs_mean: 12.5
dialogue_chars_pct: 1.9
dialogue_para_pct: 17.1
interiority_para_pct: 19.3
narration_para_pct: 63.6
turn_under20_pct: 79.0
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.8
turn_len_median: 12
```
