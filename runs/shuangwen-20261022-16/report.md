# 铜铃 生成报告

slug：`shuangwen-20261022-16`
档位：爽文　闸门模式：observe
章数：10　总字数：19129
LLM 调用：97 次，累计 372.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一张借据 | 2116 | normal | 39.9 | 0 |  | 2 |
| 2 | 一张借据 | 2082 | normal | 91.2 | 0 |  | 3 |
| 3 | 一张借据 | 1499 | normal | 94.2 | 0 |  | 2 |
| 4 | 一张借据 | 1854 | normal | 93.3 | 0 |  | 4 |
| 5 | 一张借据 | 1961 | normal | 91.9 | 0 |  | 2 |
| 6 | 一张借据 | 1763 | normal | 37.0 | 0 |  | 3 |
| 7 | 一张借据 | 1463 | normal | 91.5 | 0 |  | 5 |
| 8 | 一张借据 | 1707 | normal | 90.8 | 0 |  | 2 |
| 9 | 一张借据 | 1983 | normal | 91.9 | 0 |  | 1 |
| 10 | 一张借据 | 2691 | long | 92.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李知远的」×6、「讲经堂」×3
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「李知远的」×5
  - attr_adv_pct 15.0 高于目标 12.0
  - [observe] 标题重复：「一张借据」已存在
- 第 3 章：
  - attr_adv_pct 19.2 高于目标 12.0
  - [observe] 标题重复：「一张借据」已存在
- 第 4 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 22.7 高于目标 12.0
  - dialogue_run_mean 15.7 高于目标 14.0
  - [observe] 标题重复：「一张借据」已存在
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 标题重复：「一张借据」已存在
- 第 6 章：
  - 单条套路句式超限：「李知远的」×4
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「一张借据」已存在
- 第 7 章：
  - 单条套路句式超限：「青云寺」×4
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 15.5 高于目标 14.0
  - [observe] 标题重复：「一张借据」已存在
- 第 8 章：
  - dialogue_run_mean 18 高于目标 14.0
  - [observe] 标题重复：「一张借据」已存在
- 第 9 章：
  - [observe] 标题重复：「一张借据」已存在
- 第 10 章：
  - 单条套路句式超限：「了自己的」×3
  - attr_adv_pct 14.9 高于目标 12.0
  - [observe] 标题重复：「一张借据」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18131
chapter_chars_mean: 1813
chapter_chars_median: 1808
chapter_chars_cv: 0.18
paragraphs_mean: 43.4
dialogue_chars_pct: 49.0
dialogue_para_pct: 83.0
interiority_para_pct: 5.1
narration_para_pct: 11.9
turn_under20_pct: 75.4
turn_over200_pct: 0.0
attr_say_pct: 27.5
attr_adv_pct: 16.7
scenes_per_chapter: 2.3
dialogue_run_mean: 8.7
turn_len_median: 12
```
