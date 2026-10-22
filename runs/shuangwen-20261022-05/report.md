# 工龄证明 生成报告

slug：`shuangwen-20261022-05`
档位：爽文　闸门模式：observe
章数：10　总字数：19631
LLM 调用：97 次，累计 381.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 递出工龄证明 | 1826 | normal | 97.9 | 0 |  | 2 |
| 2 | 递出工龄证明 | 2080 | normal | 88.5 | 0 |  | 4 |
| 3 | 签字簿上的裂痕 | 1848 | normal | 93.1 | 0 |  | 2 |
| 4 | 抽屉边缘的纸角 | 2080 | normal | 91.9 | 0 |  | 1 |
| 5 | 递出工龄证明 | 1881 | normal | 35.3 | 0 |  | 5 |
| 6 | 工龄证明对峙 | 2155 | normal | 91.5 | 0 |  | 4 |
| 7 | 工龄证明对峙 | 1717 | normal | 92.2 | 0 |  | 3 |
| 8 | 翻出泛黄工资单 | 1898 | normal | 36.4 | 0 |  | 2 |
| 9 | 翻出泛黄名册 | 1763 | normal | 91.9 | 0 |  | 2 |
| 10 | 纸飞机坠入裂缝 | 2373 | long | 93.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×5
  - attr_adv_pct 20.0 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「说道“我」×3
  - narration_para_pct 4.1 低于目标 5.0
  - dialogue_run_mean 23.5 高于目标 14.0
  - [observe] 标题重复：「递出工龄证明」已存在
- 第 3 章：
  - 单条套路句式超限：「李国强的」×5
  - attr_adv_pct 23.1 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「李国强的」×4
- 第 5 章：
  - 单条套路句式超限：「李国强的」×5
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 25 高于目标 14.0
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「递出工龄证明」已存在
- 第 6 章：
  - 单条套路句式超限：「李国强的」×5
  - narration_para_pct 4.7 低于目标 5.0
  - attr_adv_pct 21.7 高于目标 12.0
  - [observe] 标题与《递出工龄证明》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 18 高于目标 14.0
  - [observe] 标题重复：「工龄证明对峙」已存在
- 第 8 章：
  - 单条套路句式超限：「李国强的」×4
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
- 第 9 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题与《翻出泛黄工资单》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - narration_para_pct 4.7 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 18579
chapter_chars_mean: 1858
chapter_chars_median: 1778
chapter_chars_cv: 0.11
paragraphs_mean: 44.9
dialogue_chars_pct: 52.7
dialogue_para_pct: 89.3
interiority_para_pct: 4.0
narration_para_pct: 6.7
turn_under20_pct: 75.1
turn_over200_pct: 0.0
attr_say_pct: 32.7
attr_adv_pct: 16.0
scenes_per_chapter: 1.5
dialogue_run_mean: 11.8
turn_len_median: 13
```
