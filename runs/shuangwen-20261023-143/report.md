# 录音带 生成报告

slug：`shuangwen-20261023-143`
档位：爽文　闸门模式：observe
章数：10　总字数：18418
LLM 调用：97 次，累计 412.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红印压合同 | 1863 | normal | 96.0 | 0 |  | 2 |
| 2 | 签字笔压合同 | 1917 | normal | 90.5 | 0 |  | 0 |
| 3 | 账册掀开一角 | 1666 | normal | 93.6 | 0 |  | 3 |
| 4 | 递出200元纸币 | 1763 | normal | 94.9 | 0 |  | 1 |
| 5 | 计算器亮屏 | 1752 | normal | 92.9 | 0 |  | 1 |
| 6 | 磁带压合同 | 1597 | normal | 37.5 | 0 |  | 3 |
| 7 | 签字笔压合同 | 1761 | normal | 93.6 | 0 |  | 2 |
| 8 | 档案摊开 | 2009 | normal | 93.5 | 0 |  | 2 |
| 9 | 证件压合同 | 1849 | normal | 91.3 | 0 |  | 2 |
| 10 | 红印压合同 | 2231 | long | 93.1 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 17.6 高于目标 12.0
  - dialogue_run_mean 18.5 高于目标 14.0
- 第 3 章：
  - 单条套路句式超限：「王德发的」×3
  - narration_para_pct 3.4 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
- 第 4 章：
  - attr_adv_pct 13.3 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「王德发的」×5
- 第 6 章：
  - 单条套路句式超限：「王德发的」×5
  - [observe] 章内自我复读 2 句（如「这是我跟担保人的通话记录，上面有他们签字的日期…」）
  - [observe] 标题与《红印压合同》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - attr_adv_pct 23.5 高于目标 12.0
  - [observe] 标题重复：「签字笔压合同」已存在
- 第 8 章：
  - 单条套路句式超限：「王德发的」×3、「李建平的」×3
  - attr_adv_pct 23.8 高于目标 12.0
- 第 9 章：
  - 单条套路句式超限：「王德发的」×3
  - [observe] 标题与《磁带压合同》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 命中套话收尾句
  - 单条套路句式超限：「王德发的」×4、「他知道这」×3
  - attr_adv_pct 15.4 高于目标 12.0
  - [observe] 标题重复：「红印压合同」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17475
chapter_chars_mean: 1748
chapter_chars_median: 1710
chapter_chars_cv: 0.1
paragraphs_mean: 39.9
dialogue_chars_pct: 51.5
dialogue_para_pct: 83.7
interiority_para_pct: 5.1
narration_para_pct: 11.2
turn_under20_pct: 65.8
turn_over200_pct: 0.0
attr_say_pct: 29.6
attr_adv_pct: 12.6
scenes_per_chapter: 2.3
dialogue_run_mean: 7.5
turn_len_median: 14
```
