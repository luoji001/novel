# 旧合同 生成报告

slug：`shuangwen-20261022-62`
档位：爽文　闸门模式：observe
章数：10　总字数：18511
LLM 调用：97 次，累计 405.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红章压住旧合同 | 1485 | normal | 98.6 | 0 |  | 1 |
| 2 | 红章压住旧合同 | 2130 | normal | 93.4 | 0 |  | 2 |
| 3 | 红笔戳破旧合同 | 1651 | normal | 87.8 | 0 |  | 2 |
| 4 | 红笔戳破旧合同 | 1739 | normal | 92.8 | 0 |  | 1 |
| 5 | 红笔戳破旧合同 | 1902 | normal | 34.8 | 0 |  | 4 |
| 6 | 红笔戳破旧合同 | 1604 | normal | 36.9 | 0 |  | 2 |
| 7 | 红笔划掉旧合同 | 1888 | normal | 92.0 | 0 |  | 1 |
| 8 | 红笔划掉旧合同 | 1678 | normal | 92.9 | 0 |  | 3 |
| 9 | 手指抚过旧合同 | 1661 | normal | 94.6 | 0 |  | 1 |
| 10 | 手指抚过新协议 | 2763 | long | 92.8 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 14.3 高于目标 12.0
- 第 2 章：
  - 命中套话收尾句
  - [observe] 标题重复：「红章压住旧合同」已存在
- 第 3 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 27 高于目标 14.0
- 第 4 章：
  - [observe] 标题重复：「红笔戳破旧合同」已存在
- 第 5 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 33 高于目标 14.0
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「红笔戳破旧合同」已存在
- 第 6 章：
  - [observe] attr_adv_pct 37.5 > 25.0（结构塌缩）
  - [observe] 标题重复：「红笔戳破旧合同」已存在
- 第 7 章：
  - [observe] 标题与《红笔戳破旧合同》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「他知道这」×3
  - narration_para_pct 3.8 低于目标 5.0
  - [observe] 标题重复：「红笔划掉旧合同」已存在
- 第 9 章：
  - attr_adv_pct 14.3 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 17685
chapter_chars_mean: 1768
chapter_chars_median: 1638
chapter_chars_cv: 0.2
paragraphs_mean: 33.3
dialogue_chars_pct: 54.4
dialogue_para_pct: 89.4
interiority_para_pct: 2.5
narration_para_pct: 8.1
turn_under20_pct: 59.9
turn_over200_pct: 0.0
attr_say_pct: 25.0
attr_adv_pct: 10.8
scenes_per_chapter: 1.7
dialogue_run_mean: 12.5
turn_len_median: 16
```
