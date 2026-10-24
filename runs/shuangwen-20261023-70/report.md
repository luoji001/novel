# 旧借条 生成报告

slug：`shuangwen-20261023-70`
档位：爽文　闸门模式：observe
章数：10　总字数：19526
LLM 调用：93 次，累计 442.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 借条上的红印 | 1634 | normal | 39.0 | 0 |  | 2 |
| 2 | 借条上的红印 | 1133 | normal | 37.2 | 0 |  | 4 |
| 3 | 借条摊开的瞬间 | 1879 | normal | 93.9 | 0 |  | 1 |
| 4 | 借条递上的一瞬 | 1853 | normal | 94.5 | 0 |  | 3 |
| 5 | 借条递上的一瞬 | 1775 | normal | 93.4 | 0 |  | 5 |
| 6 | 借条摊开的瞬间 | 2300 | normal | 92.4 | 0 |  | 3 |
| 7 | 借条轻扬的刹那 | 1584 | normal | 94.1 | 0 |  | 2 |
| 8 | 借条递上的一瞬 | 2672 | normal | 93.3 | 0 |  | 3 |
| 9 | 借条轻扬的刹那 | 1844 | normal | 92.8 | 0 |  | 1 |
| 10 | 算盘压住借据 | 2842 | long | 92.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「张怀远的」×5、「他知道这」×3
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「他知道自己」×3
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 章节过短 1013 < 1068（本章目标 1942 字的 55%）
  - [observe] 标题重复：「借条上的红印」已存在
- 第 3 章：
  - attr_adv_pct 18.2 高于目标 12.0
- 第 4 章：
  - narration_para_pct 2.5 低于目标 5.0
  - attr_adv_pct 13.6 高于目标 12.0
  - [observe] 标题与《借条上的红印》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「山门管委会」×3
  - narration_para_pct 3.1 低于目标 5.0
  - dialogue_run_mean 15 高于目标 14.0
  - [observe] 标题重复：「借条递上的一瞬」已存在
- 第 6 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
  - [observe] 标题重复：「借条摊开的瞬间」已存在
- 第 7 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×4
- 第 8 章：
  - 命中套话收尾句
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「借条递上的一瞬」已存在
- 第 9 章：
  - [observe] 标题重复：「借条轻扬的刹那」已存在
- 第 10 章：
  - narration_para_pct 1.7 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 18398
chapter_chars_mean: 1840
chapter_chars_median: 1755
chapter_chars_cv: 0.27
paragraphs_mean: 45
dialogue_chars_pct: 47.7
dialogue_para_pct: 82.9
interiority_para_pct: 7.2
narration_para_pct: 9.8
turn_under20_pct: 75.1
turn_over200_pct: 0.0
attr_say_pct: 34.7
attr_adv_pct: 12.2
scenes_per_chapter: 1.3
dialogue_run_mean: 7.4
turn_len_median: 14
```
