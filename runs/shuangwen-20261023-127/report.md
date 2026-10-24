# 田契 生成报告

slug：`shuangwen-20261023-127`
档位：爽文　闸门模式：observe
章数：10　总字数：18732
LLM 调用：97 次，累计 419.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙开启地窖 | 1961 | normal | 99.2 | 0 |  | 1 |
| 2 | 铜锁与田契对峙 | 1969 | normal | 94.6 | 0 |  | 1 |
| 3 | 铜锁与田契对峙 | 1711 | normal | 37.1 | 0 |  | 2 |
| 4 | 钥匙开启地窖 | 1752 | normal | 92.8 | 0 |  | 2 |
| 5 | 田契与老墙对话 | 1550 | normal | 95.6 | 0 |  | 1 |
| 6 | 铜锁与田契对峙 | 1903 | normal | 37.8 | 0 |  | 2 |
| 7 | 田契与旧档案对峙 | 1773 | normal | 94.1 | 0 |  | 0 |
| 8 | 铜锁与田契对峙 | 1998 | normal | 93.9 | 0 |  | 2 |
| 9 | 田契对峙铜锁 | 1861 | normal | 36.5 | 0 |  | 5 |
| 10 | 田契对峙铜锁 | 2244 | long | 93.1 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「赵德昌的」×6
- 第 2 章：
  - 单条套路句式超限：「赵德昌的」×13
- 第 3 章：
  - [observe] attr_adv_pct 29.4 > 25.0（结构塌缩）
  - [observe] 标题重复：「铜锁与田契对峙」已存在
- 第 4 章：
  - narration_para_pct 4.7 低于目标 5.0
  - [observe] 标题重复：「钥匙开启地窖」已存在
- 第 5 章：
  - attr_adv_pct 16.7 高于目标 12.0
- 第 6 章：
  - [observe] attr_adv_pct 44.4 > 25.0（结构塌缩）
  - [observe] 标题重复：「铜锁与田契对峙」已存在
- 第 8 章：
  - 单条套路句式超限：「赵德昌的」×5、「李怀远的」×3
  - [observe] 标题重复：「铜锁与田契对峙」已存在
- 第 9 章：
  - 单条套路句式超限：「李怀远点」×3
  - narration_para_pct 4.3 低于目标 5.0
  - dialogue_run_mean 22 高于目标 14.0
  - [observe] attr_adv_pct 29.6 > 25.0（结构塌缩）
  - [observe] 标题与《铜锁与田契对峙》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「赵德昌的」×7、「李怀远的」×3
  - narration_para_pct 4.8 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「田契对峙铜锁」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17777
chapter_chars_mean: 1778
chapter_chars_median: 1782
chapter_chars_cv: 0.1
paragraphs_mean: 39.9
dialogue_chars_pct: 48.9
dialogue_para_pct: 85.0
interiority_para_pct: 3.7
narration_para_pct: 11.3
turn_under20_pct: 71.3
turn_over200_pct: 0.0
attr_say_pct: 30.2
attr_adv_pct: 15.4
scenes_per_chapter: 1.5
dialogue_run_mean: 8.5
turn_len_median: 14
```
