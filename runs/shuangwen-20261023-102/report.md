# 旧合同 生成报告

slug：`shuangwen-20261023-102`
档位：爽文　闸门模式：observe
章数：10　总字数：18358
LLM 调用：97 次，累计 399.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一张报价单 | 1810 | normal | 98.7 | 0 |  | 0 |
| 2 | 一张旧合同 | 1902 | normal | 92.7 | 0 |  | 0 |
| 3 | 一道压痕 | 1838 | normal | 93.0 | 0 |  | 1 |
| 4 | 一记钢笔印 | 1799 | normal | 93.4 | 0 |  | 0 |
| 5 | 一张旧合同 | 1994 | normal | 94.5 | 0 |  | 3 |
| 6 | 一记钢笔印 | 2030 | normal | 92.3 | 0 |  | 3 |
| 7 | 撕碎的报价单 | 1778 | normal | 93.3 | 0 |  | 0 |
| 8 | 一记钢笔印 | 1674 | normal | 92.2 | 0 |  | 4 |
| 9 | 一张新合同 | 1487 | normal | 92.6 | 0 |  | 1 |
| 10 | 一张旧合同 | 2036 | long | 91.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - attr_adv_pct 20.0 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「李国强点了点头」×3
  - attr_adv_pct 17.2 高于目标 12.0
  - [observe] 标题重复：「一张旧合同」已存在
- 第 6 章：
  - narration_para_pct 2.6 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「一记钢笔印」已存在
- 第 8 章：
  - 单条套路句式超限：「李国强的」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 15.5 高于目标 14.0
  - [observe] 标题重复：「一记钢笔印」已存在
- 第 9 章：
  - [observe] 标题与《一张旧合同》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - narration_para_pct 4.3 低于目标 5.0
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 标题重复：「一张旧合同」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17427
chapter_chars_mean: 1743
chapter_chars_median: 1733
chapter_chars_cv: 0.09
paragraphs_mean: 39.5
dialogue_chars_pct: 48.8
dialogue_para_pct: 85.9
interiority_para_pct: 5.5
narration_para_pct: 8.7
turn_under20_pct: 69.2
turn_over200_pct: 0.0
attr_say_pct: 27.4
attr_adv_pct: 11.3
scenes_per_chapter: 2
dialogue_run_mean: 8.2
turn_len_median: 12
```
