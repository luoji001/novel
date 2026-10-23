# 签批 生成报告

slug：`shuangwen-20261022-111`
档位：爽文　闸门模式：observe
章数：10　总字数：19469
LLM 调用：97 次，累计 442.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账簿的折痕 | 1761 | normal | 97.1 | 0 |  | 1 |
| 2 | 签字笔的震颤 | 2057 | normal | 91.6 | 0 |  | 0 |
| 3 | 账本上的指纹 | 1840 | normal | 94.0 | 0 |  | 2 |
| 4 | 账簿上的损耗条 | 2107 | normal | 93.7 | 0 |  | 3 |
| 5 | 签字笔的震颤 | 1843 | normal | 37.2 | 0 |  | 2 |
| 6 | 账本上的损耗条 | 1786 | normal | 86.5 | 0 |  | 4 |
| 7 | 账本与名册的对峙 | 2018 | normal | 36.0 | 0 |  | 1 |
| 8 | 签字笔的震颤 | 1685 | normal | 91.5 | 0 |  | 1 |
| 9 | 账本上的损耗条 | 1942 | normal | 91.6 | 0 |  | 4 |
| 10 | 印章的真假对决 | 2420 | long | 92.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陆长风的」×3
- 第 3 章：
  - 单条套路句式超限：「陆长风的」×5
  - attr_adv_pct 20.0 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「他知道自己」×3
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 13.3 高于目标 12.0
- 第 5 章：
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔的震颤」已存在
- 第 6 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - dialogue_run_mean 31 高于目标 14.0
  - [observe] 标题与《账簿上的损耗条》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - [observe] attr_adv_pct 40.0 > 25.0（结构塌缩）
- 第 8 章：
  - [observe] 标题重复：「签字笔的震颤」已存在
- 第 9 章：
  - narration_para_pct 3.6 低于目标 5.0
  - attr_adv_pct 18.5 高于目标 12.0
  - dialogue_run_mean 18 高于目标 14.0
  - [observe] 标题重复：「账本上的损耗条」已存在
- 第 10 章：
  - 单条套路句式超限：「陆长风的」×4、「他知道这」×3
  - narration_para_pct 2.0 低于目标 5.0
  - attr_adv_pct 18.2 高于目标 12.0
  - dialogue_run_mean 15.7 高于目标 14.0

## 整书结构指标

```
chapters: 10
total_chars: 18496
chapter_chars_mean: 1850
chapter_chars_median: 1791
chapter_chars_cv: 0.11
paragraphs_mean: 40.9
dialogue_chars_pct: 53.0
dialogue_para_pct: 88.2
interiority_para_pct: 4.8
narration_para_pct: 7.0
turn_under20_pct: 68.0
turn_over200_pct: 0.0
attr_say_pct: 22.9
attr_adv_pct: 17.0
scenes_per_chapter: 1.5
dialogue_run_mean: 11.8
turn_len_median: 14
```
