# 铜秤 生成报告

slug：`xuanyi-20261019-173`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14882
LLM 调用：68 次，累计 236.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本上的缺角 | 1836 | short | 84.3 | 0 |  | 3 |
| 2 | 铜秤盘上的微光 | 3791 | normal | 85.0 | 0 |  | 4 |
| 3 | 木屑下的秘密 | 3979 | normal | 37.1 | 0 |  | 2 |
| 4 | 纸页上的折痕 | 3486 | normal | 89.9 | 0 |  | 4 |
| 5 | 纸边上的凹陷 | 1785 | short | 90.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道自己」×3、「沈文远的」×3
  - interiority_para_pct 27.6 高于目标 20.0
  - [observe] 章内自我复读 5 句（如「他低声重复了一遍，声音越来越低，几乎听不见，“可…」）
- 第 2 章：
  - 单条套路句式超限：「周怀瑾的」×5、「沈文远的」×3
  - narration_para_pct 18.0 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
  - [observe] 章内自我复读 33 句（如「如果这把秤不准，那它的重量究竟该怎么算？比如那次…」）
- 第 3 章：
  - dialogue_chars_pct 11.2 低于目标 20.0
  - interiority_para_pct 24.6 高于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「沈文远的」×5、「他知道自己」×3、「周怀瑾的」×3
  - interiority_para_pct 21.3 高于目标 20.0
  - narration_para_pct 8.2 低于目标 20.0
  - attr_adv_pct 15.8 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「沈文远的」×4
  - narration_para_pct 11.1 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 14326
chapter_chars_mean: 2865
chapter_chars_median: 3349
chapter_chars_cv: 0.36
paragraphs_mean: 47.8
dialogue_chars_pct: 23.3
dialogue_para_pct: 61.2
interiority_para_pct: 20.5
narration_para_pct: 18.3
turn_under20_pct: 78.3
turn_over200_pct: 0.0
attr_say_pct: 18.6
attr_adv_pct: 13.0
scenes_per_chapter: 3
dialogue_run_mean: 2.7
turn_len_median: 13
```
