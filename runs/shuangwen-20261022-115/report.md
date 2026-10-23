# 铜壶 生成报告

slug：`shuangwen-20261022-115`
档位：爽文　闸门模式：observe
章数：10　总字数：18059
LLM 调用：97 次，累计 433.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜壶印痕 | 1433 | normal | 100.0 | 0 |  | 1 |
| 2 | 门牌真假风波 | 1463 | normal | 94.9 | 0 |  | 0 |
| 3 | 登记簿空白处 | 1926 | normal | 94.2 | 0 |  | 0 |
| 4 | 登记簿空白处 | 1576 | normal | 94.1 | 0 |  | 3 |
| 5 | 铜壶盖章 | 2064 | normal | 93.7 | 0 |  | 4 |
| 6 | 铜壶验货 | 2003 | normal | 93.0 | 0 |  | 1 |
| 7 | 门牌签字 | 1934 | normal | 95.0 | 0 |  | 0 |
| 8 | 手稿摊开处 | 1464 | normal | 93.8 | 0 |  | 2 |
| 9 | 签名摊开处 | 1988 | normal | 92.4 | 0 |  | 2 |
| 10 | 手稿摊开处 | 2198 | long | 92.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李长河的」×3
- 第 4 章：
  - 单条套路句式超限：「李长河的」×3
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「登记簿空白处」已存在
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李长河的」×5、「验货台」×3
  - narration_para_pct 4.3 低于目标 5.0
  - dialogue_run_mean 14.7 高于目标 14.0
- 第 6 章：
  - 单条套路句式超限：「李长河的」×6、「他知道这」×3
- 第 8 章：
  - 单条套路句式超限：「验货台」×4、「李长河的」×3
  - attr_adv_pct 16.7 高于目标 12.0
- 第 9 章：
  - 单条套路句式超限：「李长河的」×8
  - [observe] 标题与《手稿摊开处》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「李长河的」×7
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「手稿摊开处」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17102
chapter_chars_mean: 1710
chapter_chars_median: 1827
chapter_chars_cv: 0.17
paragraphs_mean: 40.9
dialogue_chars_pct: 46.6
dialogue_para_pct: 84.4
interiority_para_pct: 5.0
narration_para_pct: 10.6
turn_under20_pct: 77.0
turn_over200_pct: 0.0
attr_say_pct: 27.3
attr_adv_pct: 9.2
scenes_per_chapter: 1.2
dialogue_run_mean: 7.7
turn_len_median: 10
```
