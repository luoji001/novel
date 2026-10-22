# 契书 生成报告

slug：`shuangwen-20261022-35`
档位：爽文　闸门模式：observe
章数：10　总字数：18953
LLM 调用：97 次，累计 375.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 半张契书的重量 | 1441 | normal | 98.3 | 0 |  | 0 |
| 2 | 契书上的折痕 | 1781 | normal | 95.0 | 0 |  | 0 |
| 3 | 银锭震落秤杆 | 1927 | normal | 93.8 | 0 |  | 1 |
| 4 | 铜秤的重量 | 2124 | normal | 94.3 | 0 |  | 2 |
| 5 | 契书上的指纹 | 1556 | normal | 95.0 | 0 |  | 2 |
| 6 | 半张契书的重量 | 2133 | normal | 94.0 | 0 |  | 3 |
| 7 | 契书上的折痕 | 2023 | normal | 93.2 | 0 |  | 2 |
| 8 | 铜秤压纸 | 1583 | normal | 36.7 | 0 |  | 1 |
| 9 | 铜秤压纸 | 1560 | normal | 94.8 | 0 |  | 3 |
| 10 | 铜秤压纸 | 2815 | long | 93.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - 单条套路句式超限：「他知道自己」×3、「验货台」×3
- 第 4 章：
  - 单条套路句式超限：「验货台」×3
  - attr_adv_pct 19.2 高于目标 12.0
- 第 5 章：
  - narration_para_pct 3.7 低于目标 5.0
  - [observe] 标题与《契书上的折痕》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「验货台」×5
  - attr_adv_pct 17.6 高于目标 12.0
  - [observe] 标题重复：「半张契书的重量」已存在
- 第 7 章：
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题重复：「契书上的折痕」已存在
- 第 8 章：
  - [observe] attr_adv_pct 50.0 > 25.0（结构塌缩）
- 第 9 章：
  - 单条套路句式超限：「验货台」×8
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「铜秤压纸」已存在
- 第 10 章：
  - 单条套路句式超限：「验货台」×7、「林远站在」×4
  - attr_adv_pct 17.9 高于目标 12.0
  - [observe] 标题重复：「铜秤压纸」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17940
chapter_chars_mean: 1794
chapter_chars_median: 1750
chapter_chars_cv: 0.22
paragraphs_mean: 43.4
dialogue_chars_pct: 47.6
dialogue_para_pct: 79.7
interiority_para_pct: 7.2
narration_para_pct: 13.1
turn_under20_pct: 74.2
turn_over200_pct: 0.0
attr_say_pct: 27.4
attr_adv_pct: 16.2
scenes_per_chapter: 1.8
dialogue_run_mean: 5.9
turn_len_median: 12
```
