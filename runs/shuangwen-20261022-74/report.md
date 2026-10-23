# 旧账单 生成报告

slug：`shuangwen-20261022-74`
档位：爽文　闸门模式：observe
章数：10　总字数：18454
LLM 调用：97 次，累计 437.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账单上的未还之债 | 1638 | normal | 92.6 | 0 |  | 2 |
| 2 | 账单上的名字缺失 | 2175 | normal | 90.7 | 0 |  | 3 |
| 3 | 账本与印泥的对峙 | 1762 | normal | 93.1 | 0 |  | 0 |
| 4 | 账本上的凹陷指纹 | 2073 | normal | 94.0 | 0 |  | 1 |
| 5 | 墨水瓶倒映的真相 | 1782 | normal | 37.0 | 0 |  | 2 |
| 6 | 账本摊开的瞬间 | 1641 | normal | 93.0 | 0 |  | 4 |
| 7 | 账单摊开的瞬间 | 1870 | normal | 92.8 | 0 |  | 1 |
| 8 | 账本摊开的瞬间 | 1714 | normal | 92.3 | 0 |  | 2 |
| 9 | 账单上的指纹痕迹 | 1569 | normal | 92.3 | 0 |  | 3 |
| 10 | 账本摊开的瞬间 | 2220 | long | 91.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 46 高于目标 14.0
- 第 2 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 20.8 高于目标 12.0
  - dialogue_run_mean 19.5 高于目标 14.0
- 第 4 章：
  - 单条套路句式超限：「周德昌的」×4
- 第 5 章：
  - 单条套路句式超限：「周德昌的」×8、「周怀远的」×3
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「周德昌的」×3
  - narration_para_pct 2.9 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 16 高于目标 14.0
- 第 7 章：
  - [observe] 标题与《账本摊开的瞬间》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - narration_para_pct 3.0 低于目标 5.0
  - [observe] 标题重复：「账本摊开的瞬间」已存在
- 第 9 章：
  - 单条套路句式超限：「周德昌的」×5
  - narration_para_pct 3.4 低于目标 5.0
  - [observe] 标题与《账本上的凹陷指纹》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「周德昌的」×6
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「账本摊开的瞬间」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17496
chapter_chars_mean: 1750
chapter_chars_median: 1686
chapter_chars_cv: 0.13
paragraphs_mean: 39.6
dialogue_chars_pct: 50.6
dialogue_para_pct: 88.3
interiority_para_pct: 4.9
narration_para_pct: 6.8
turn_under20_pct: 71.4
turn_over200_pct: 0.0
attr_say_pct: 31.0
attr_adv_pct: 10.2
scenes_per_chapter: 1.6
dialogue_run_mean: 14.0
turn_len_median: 14
```
