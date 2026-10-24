# 磅单 生成报告

slug：`shuangwen-20261023-19`
档位：爽文　闸门模式：observe
章数：10　总字数：18455
LLM 调用：97 次，累计 414.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲纸张的指尖 | 1701 | normal | 99.4 | 0 |  | 1 |
| 2 | 核对磅单 | 1802 | normal | 88.3 | 0 |  | 3 |
| 3 | 摩挲纸张的指尖 | 1911 | normal | 93.8 | 0 |  | 1 |
| 4 | 撕碎的过磅单 | 2232 | normal | 36.3 | 0 |  | 2 |
| 5 | 摩挲金属把手 | 1449 | normal | 91.7 | 0 |  | 1 |
| 6 | 核对磅单 | 1966 | normal | 37.2 | 0 |  | 3 |
| 7 | 摩挲纸张的指尖 | 1598 | normal | 92.3 | 0 |  | 3 |
| 8 | 摩挲纸张的指尖 | 1653 | normal | 93.8 | 0 |  | 2 |
| 9 | 摩挲纸张的指尖 | 1702 | normal | 93.8 | 0 |  | 1 |
| 10 | 撕碎的资历证书 | 2431 | long | 94.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×4
- 第 2 章：
  - narration_para_pct 2.7 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 36 高于目标 14.0
- 第 3 章：
  - [observe] 标题重复：「摩挲纸张的指尖」已存在
- 第 4 章：
  - 单条套路句式超限：「李国强的」×4
  - [observe] 章内自我复读 1 句（如「我只是做了我应该做的事情…」）
- 第 5 章：
  - 单条套路句式超限：「李国强的」×3
- 第 6 章：
  - 单条套路句式超限：「李国强的」×3
  - [observe] attr_adv_pct 31.6 > 25.0（结构塌缩）
  - [observe] 标题重复：「核对磅单」已存在
- 第 7 章：
  - narration_para_pct 2.4 低于目标 5.0
  - dialogue_run_mean 19.5 高于目标 14.0
  - [observe] 标题重复：「摩挲纸张的指尖」已存在
- 第 8 章：
  - 单条套路句式超限：「李国强的」×5
  - [observe] 标题重复：「摩挲纸张的指尖」已存在
- 第 9 章：
  - [observe] 标题重复：「摩挲纸张的指尖」已存在
- 第 10 章：
  - 单条套路句式超限：「李国强的」×7
  - attr_adv_pct 25.0 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 17359
chapter_chars_mean: 1736
chapter_chars_median: 1666
chapter_chars_cv: 0.16
paragraphs_mean: 47.2
dialogue_chars_pct: 51.0
dialogue_para_pct: 86.3
interiority_para_pct: 4.4
narration_para_pct: 9.3
turn_under20_pct: 77.6
turn_over200_pct: 0.0
attr_say_pct: 34.8
attr_adv_pct: 13.4
scenes_per_chapter: 2.8
dialogue_run_mean: 11.0
turn_len_median: 12
```
