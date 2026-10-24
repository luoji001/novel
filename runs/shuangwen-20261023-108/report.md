# 旧契书 生成报告

slug：`shuangwen-20261023-108`
档位：爽文　闸门模式：observe
章数：10　总字数：18128
LLM 调用：97 次，累计 454.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜秤晃动 | 1474 | normal | 98.9 | 0 |  | 2 |
| 2 | 铜秤对契书 | 1752 | normal | 93.8 | 0 |  | 1 |
| 3 | 契书对账本 | 1819 | normal | 36.0 | 0 |  | 3 |
| 4 | 签字权较量 | 1500 | normal | 37.1 | 0 |  | 2 |
| 5 | 铜秤对账本 | 1806 | normal | 91.5 | 0 |  | 3 |
| 6 | 印章对职级 | 1671 | normal | 37.6 | 0 |  | 1 |
| 7 | 契书对玉佩 | 2044 | normal | 93.7 | 0 |  | 2 |
| 8 | 账本对契书 | 2089 | normal | 93.4 | 0 |  | 3 |
| 9 | 账本对契书 | 1637 | normal | 93.2 | 0 |  | 2 |
| 10 | 账本对契书 | 2326 | long | 90.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「验货台」×4
  - attr_adv_pct 20.0 高于目标 12.0
- 第 2 章：
  - attr_adv_pct 15.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「验货台」×4
  - dialogue_run_mean 17.5 高于目标 14.0
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 4 章：
  - narration_para_pct 3.7 低于目标 5.0
  - [observe] attr_adv_pct 26.7 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「验货台」×3
  - attr_adv_pct 13.6 高于目标 12.0
  - [observe] 标题与《铜秤对契书》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
- 第 7 章：
  - 单条套路句式超限：「青云坊市」×3
  - [observe] 标题与《契书对账本》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「验货台」×3
  - narration_para_pct 4.8 低于目标 5.0
  - [observe] 标题与《铜秤对契书》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「验货台」×5
  - [observe] 标题重复：「账本对契书」已存在
- 第 10 章：
  - 单条套路句式超限：「青云坊市」×3
  - [observe] 标题重复：「账本对契书」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17259
chapter_chars_mean: 1726
chapter_chars_median: 1680
chapter_chars_cv: 0.15
paragraphs_mean: 36.5
dialogue_chars_pct: 47.1
dialogue_para_pct: 84.5
interiority_para_pct: 6.5
narration_para_pct: 9.1
turn_under20_pct: 68.7
turn_over200_pct: 0.0
attr_say_pct: 36.7
attr_adv_pct: 15.1
scenes_per_chapter: 1.5
dialogue_run_mean: 7.1
turn_len_median: 13
```
