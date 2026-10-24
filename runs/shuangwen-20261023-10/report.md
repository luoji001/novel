# 旧凭牌 生成报告

slug：`shuangwen-20261023-10`
档位：爽文　闸门模式：observe
章数：10　总字数：19069
LLM 调用：97 次，累计 426.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧凭牌与铜钥匙 | 1685 | normal | 98.9 | 0 |  | 1 |
| 2 | 签字纸上的旧签名 | 1836 | normal | 92.0 | 0 |  | 2 |
| 3 | 旧凭牌的失效时刻 | 1700 | normal | 89.7 | 0 |  | 3 |
| 4 | 旧凭牌的失效时刻 | 1917 | normal | 92.6 | 0 |  | 3 |
| 5 | 旧凭牌的摩挲痕迹 | 1950 | normal | 93.0 | 0 |  | 0 |
| 6 | 旧凭牌的摩挲痕迹 | 1943 | normal | 89.4 | 0 |  | 2 |
| 7 | 旧凭牌的摩挲痕迹 | 1788 | normal | 88.4 | 0 |  | 4 |
| 8 | 旧凭牌的摩挲痕迹 | 1852 | normal | 90.6 | 0 |  | 2 |
| 9 | 旧凭牌的摩挲痕迹 | 1948 | normal | 36.7 | 0 |  | 3 |
| 10 | 旧凭牌的摩挲痕迹 | 2440 | long | 93.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李长河的」×6
- 第 2 章：
  - 单条套路句式超限：「李长河的」×7
  - attr_adv_pct 16.7 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「李长河点了点头」×3、「”李长河低」×3
  - narration_para_pct 4.2 低于目标 5.0
  - dialogue_run_mean 15 高于目标 14.0
- 第 4 章：
  - 单条套路句式超限：「沈秋实的」×4
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题重复：「旧凭牌的失效时刻」已存在
- 第 6 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「旧凭牌的摩挲痕迹」已存在
- 第 7 章：
  - 单条套路句式超限：「李长河的」×4
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 34 高于目标 14.0
  - [observe] 标题重复：「旧凭牌的摩挲痕迹」已存在
- 第 8 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 标题重复：「旧凭牌的摩挲痕迹」已存在
- 第 9 章：
  - 单条套路句式超限：「李长河的」×6
  - [observe] attr_adv_pct 38.5 > 25.0（结构塌缩）
  - [observe] 标题重复：「旧凭牌的摩挲痕迹」已存在
- 第 10 章：
  - 单条套路句式超限：「李长河的」×5
  - attr_adv_pct 19.2 高于目标 12.0
  - [observe] 标题重复：「旧凭牌的摩挲痕迹」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18036
chapter_chars_mean: 1804
chapter_chars_median: 1784
chapter_chars_cv: 0.11
paragraphs_mean: 43.1
dialogue_chars_pct: 44.6
dialogue_para_pct: 82.0
interiority_para_pct: 7.8
narration_para_pct: 10.2
turn_under20_pct: 81.3
turn_over200_pct: 0.0
attr_say_pct: 32.2
attr_adv_pct: 13.2
scenes_per_chapter: 2.1
dialogue_run_mean: 8.5
turn_len_median: 12
```
