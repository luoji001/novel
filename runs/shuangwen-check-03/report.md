# 令牌风云 生成报告

slug：`shuangwen-check-03`
档位：爽文　闸门模式：observe
章数：10　总字数：19646
LLM 调用：97 次，累计 454.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 令牌对碰 | 2045 | normal | 96.2 | 0 |  | 2 |
| 2 | 令牌入符 | 2124 | normal | 86.0 | 0 |  | 3 |
| 3 | 令牌对碰 | 1958 | normal | 93.9 | 0 |  | 3 |
| 4 | 令牌对碰 | 1832 | normal | 86.7 | 0 |  | 4 |
| 5 | 地图裂痕 | 1731 | normal | 92.0 | 0 |  | 1 |
| 6 | 朱砂划规 | 1953 | normal | 93.5 | 0 |  | 3 |
| 7 | 玉佩初现 | 1883 | normal | 87.2 | 0 |  | 3 |
| 8 | 令牌对碰 | 1891 | normal | 91.7 | 0 |  | 4 |
| 9 | 令牌对碰 | 1890 | normal | 92.6 | 0 |  | 3 |
| 10 | 令牌对碰 | 2329 | long | 94.1 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「苏长风的」×6
  - narration_para_pct 14.7 低于目标 15.0
- 第 2 章：
  - 单条套路句式超限：「苏长风的」×3
  - narration_para_pct 3.4 低于目标 15.0
  - dialogue_run_mean 25 高于目标 14.0
- 第 3 章：
  - narration_para_pct 5.8 低于目标 15.0
  - attr_adv_pct 19.0 高于目标 12.0
  - [observe] 标题重复：「令牌对碰」已存在
- 第 4 章：
  - narration_para_pct 0.0 低于目标 15.0
  - attr_adv_pct 15.0 高于目标 12.0
  - dialogue_run_mean 31 高于目标 14.0
  - [observe] 标题重复：「令牌对碰」已存在
- 第 5 章：
  - narration_para_pct 6.7 低于目标 15.0
- 第 6 章：
  - 单条套路句式超限：「苏长风的」×3
  - narration_para_pct 6.5 低于目标 15.0
  - attr_adv_pct 15.4 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「苏长风的」×6
  - narration_para_pct 2.2 低于目标 15.0
  - dialogue_run_mean 44 高于目标 14.0
- 第 8 章：
  - 单条套路句式超限：「苏长风的」×8
  - narration_para_pct 12.3 低于目标 15.0
  - attr_adv_pct 14.7 高于目标 12.0
  - [observe] 标题重复：「令牌对碰」已存在
- 第 9 章：
  - 单条套路句式超限：「苏长风的」×5
  - narration_para_pct 4.4 低于目标 15.0
  - [observe] 标题重复：「令牌对碰」已存在
- 第 10 章：
  - 单条套路句式超限：「苏长风的」×4
  - narration_para_pct 2.2 低于目标 15.0
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 标题重复：「令牌对碰」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18686
chapter_chars_mean: 1869
chapter_chars_median: 1815
chapter_chars_cv: 0.09
paragraphs_mean: 41.5
dialogue_chars_pct: 52.8
dialogue_para_pct: 89.7
interiority_para_pct: 4.5
narration_para_pct: 5.8
turn_under20_pct: 70.4
turn_over200_pct: 0.0
attr_say_pct: 18.4
attr_adv_pct: 10.4
scenes_per_chapter: 1.5
dialogue_run_mean: 15.4
turn_len_median: 14
```
