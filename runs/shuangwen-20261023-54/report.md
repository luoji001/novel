# 合同副本 生成报告

slug：`shuangwen-20261023-54`
档位：爽文　闸门模式：observe
章数：10　总字数：19621
LLM 调用：97 次，累计 430.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 合同副本的交锋 | 1991 | normal | 99.7 | 0 |  | 2 |
| 2 | 合同副本的交锋 | 1840 | normal | 91.0 | 0 |  | 1 |
| 3 | 手指摩挲合同边缘 | 2127 | normal | 90.8 | 0 |  | 2 |
| 4 | 手指摩挲纸角 | 1764 | normal | 91.7 | 0 |  | 1 |
| 5 | 手指摩挲纸角 | 1756 | normal | 93.2 | 0 |  | 2 |
| 6 | 手指摩挲纸角 | 1606 | normal | 90.5 | 0 |  | 1 |
| 7 | 手指摩挲报表边缘 | 2158 | normal | 91.0 | 0 |  | 2 |
| 8 | 笔记本的较量 | 2246 | normal | 92.7 | 0 |  | 2 |
| 9 | 手指摩挲纸角 | 1993 | normal | 91.0 | 0 |  | 1 |
| 10 | 授权书压桌面 | 2130 | long | 92.4 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×5
  - attr_adv_pct 25.0 高于目标 12.0
- 第 2 章：
  - [observe] 标题重复：「合同副本的交锋」已存在
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
- 第 4 章：
  - 单条套路句式超限：「他知道自己」×4
- 第 5 章：
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题重复：「手指摩挲纸角」已存在
- 第 6 章：
  - [observe] 标题重复：「手指摩挲纸角」已存在
- 第 7 章：
  - narration_para_pct 3.4 低于目标 5.0
  - [observe] 标题与《手指摩挲合同边缘》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「李国强的」×5
  - attr_adv_pct 12.5 高于目标 12.0
- 第 9 章：
  - [observe] 标题重复：「手指摩挲纸角」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18731
chapter_chars_mean: 1873
chapter_chars_median: 1902
chapter_chars_cv: 0.11
paragraphs_mean: 36.7
dialogue_chars_pct: 48.5
dialogue_para_pct: 84.4
interiority_para_pct: 5.7
narration_para_pct: 9.9
turn_under20_pct: 62.2
turn_over200_pct: 0.0
attr_say_pct: 23.8
attr_adv_pct: 10.3
scenes_per_chapter: 2
dialogue_run_mean: 6.9
turn_len_median: 16
```
