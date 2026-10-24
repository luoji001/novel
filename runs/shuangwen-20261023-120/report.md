# 旧工号牌 生成报告

slug：`shuangwen-20261023-120`
档位：爽文　闸门模式：observe
章数：10　总字数：18491
LLM 调用：97 次，累计 431.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 递出旧工号牌 | 1572 | normal | 39.2 | 0 |  | 2 |
| 2 | 铜牌对峙 | 2598 | normal | 91.0 | 0 |  | 2 |
| 3 | 铜牌对峙 | 1963 | normal | 86.5 | 0 |  | 3 |
| 4 | 工号牌对峙 | 1732 | normal | 92.0 | 0 |  | 3 |
| 5 | 掏出记事本 | 1645 | normal | 91.4 | 0 |  | 0 |
| 6 | 工号牌按在合同上 | 1776 | normal | 92.9 | 0 |  | 1 |
| 7 | 工号牌对峙 | 1623 | normal | 88.2 | 0 |  | 4 |
| 8 | 工号牌按在合同上 | 1779 | normal | 90.1 | 0 |  | 3 |
| 9 | 工号牌按在合同上 | 1690 | normal | 93.0 | 0 |  | 3 |
| 10 | 工号牌按在合同上 | 2103 | long | 91.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 3.3 低于目标 5.0
  - [observe] 章内自我复读 2 句（如「可你现在已经不在编了…」）
- 第 2 章：
  - narration_para_pct 3.6 低于目标 5.0
  - dialogue_run_mean 17.7 高于目标 14.0
- 第 3 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 40 高于目标 14.0
  - [observe] 标题重复：「铜牌对峙」已存在
- 第 4 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 17.3 高于目标 14.0
  - [observe] 标题与《铜牌对峙》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - attr_adv_pct 22.2 高于目标 12.0
- 第 7 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
  - dialogue_run_mean 32 高于目标 14.0
  - [observe] 标题重复：「工号牌对峙」已存在
- 第 8 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - dialogue_run_mean 18 高于目标 14.0
  - [observe] 标题重复：「工号牌按在合同上」已存在
- 第 9 章：
  - 单条套路句式超限：「王德顺的」×4
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「工号牌按在合同上」已存在
- 第 10 章：
  - 单条套路句式超限：「李小满的」×6
  - [observe] 标题重复：「工号牌按在合同上」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17590
chapter_chars_mean: 1759
chapter_chars_median: 1650
chapter_chars_cv: 0.17
paragraphs_mean: 37.5
dialogue_chars_pct: 54.5
dialogue_para_pct: 90.5
interiority_para_pct: 3.8
narration_para_pct: 5.7
turn_under20_pct: 66.9
turn_over200_pct: 0.0
attr_say_pct: 26.6
attr_adv_pct: 9.6
scenes_per_chapter: 1.5
dialogue_run_mean: 15.4
turn_len_median: 14
```
