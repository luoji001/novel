# 旧账单 生成报告

slug：`shuangwen-20261023-28`
档位：爽文　闸门模式：observe
章数：10　总字数：19474
LLM 调用：97 次，累计 434.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜秤称旧账单 | 1580 | normal | 98.7 | 0 |  | 1 |
| 2 | 账本上的阴晴天气 | 1848 | normal | 37.5 | 0 |  | 2 |
| 3 | 铜秤压旧账单 | 1828 | normal | 93.8 | 0 |  | 1 |
| 4 | 铜秤压旧账单 | 2031 | normal | 93.4 | 0 |  | 2 |
| 5 | 铜秤压旧账单 | 2003 | normal | 93.1 | 0 |  | 2 |
| 6 | 铜秤压旧账单 | 1690 | normal | 87.2 | 0 |  | 4 |
| 7 | 铜秤压旧账单 | 1792 | normal | 93.5 | 0 |  | 1 |
| 8 | 铜秤压旧账单 | 1535 | normal | 37.6 | 0 |  | 4 |
| 9 | 旧账单的褶皱 | 2653 | normal | 92.8 | 0 |  | 1 |
| 10 | 翻阅账本的指尖 | 2504 | long | 36.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李怀远的」×7
- 第 2 章：
  - 单条套路句式超限：「李怀远的」×4
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 3 章：
  - [observe] 标题与《铜秤称旧账单》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「李怀远的」×4
  - [observe] 标题重复：「铜秤压旧账单」已存在
- 第 5 章：
  - 单条套路句式超限：「李怀远的」×8
  - [observe] 标题重复：「铜秤压旧账单」已存在
- 第 6 章：
  - narration_para_pct 3.2 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
  - dialogue_run_mean 30 高于目标 14.0
  - [observe] 标题重复：「铜秤压旧账单」已存在
- 第 7 章：
  - [observe] 标题重复：「铜秤压旧账单」已存在
- 第 8 章：
  - 单条套路句式超限：「李怀远的」×3
  - narration_para_pct 2.7 低于目标 5.0
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「铜秤压旧账单」已存在
- 第 9 章：
  - 单条套路句式超限：「李怀远的」×4
- 第 10 章：
  - 单条套路句式超限：「李怀远的」×7
  - dialogue_run_mean 16.7 高于目标 14.0
  - [observe] attr_adv_pct 45.5 > 25.0（结构塌缩）

## 整书结构指标

```
chapters: 10
total_chars: 18453
chapter_chars_mean: 1845
chapter_chars_median: 1738
chapter_chars_cv: 0.19
paragraphs_mean: 43.4
dialogue_chars_pct: 50.7
dialogue_para_pct: 85.4
interiority_para_pct: 4.9
narration_para_pct: 9.7
turn_under20_pct: 76.6
turn_over200_pct: 0.0
attr_say_pct: 26.5
attr_adv_pct: 17.8
scenes_per_chapter: 1.6
dialogue_run_mean: 9.6
turn_len_median: 12
```
