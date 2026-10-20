# 行李箱 生成报告

slug：`xuanyi-20261019-243`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14903
LLM 调用：68 次，累计 235.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 行李箱未动 | 1877 | short | 99.8 | 0 |  | 2 |
| 2 | 行李箱未动 | 3532 | normal | 90.0 | 0 |  | 4 |
| 3 | 汇款单浮现异样 | 3475 | normal | 89.9 | 0 |  | 2 |
| 4 | 撕碎的身份证碎片 | 3906 | normal | 89.0 | 0 |  | 2 |
| 5 | 行李箱未动 | 2108 | short | 92.3 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林志远的」×3
  - narration_para_pct 14.7 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林志远的」×9、「“我不知道」×5、「林志远站在」×4
  - narration_para_pct 12.4 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「一个声音打断了他的思绪…」）
  - [observe] 标题重复：「行李箱未动」已存在
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×4、「说道“我」×4、「林志远的」×4
  - narration_para_pct 11.4 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「南方电子厂」×19、「他知道这」×3
  - narration_para_pct 19.0 低于目标 20.0
- 第 5 章：
  - narration_para_pct 16.4 低于目标 20.0
  - attr_adv_pct 15.0 高于目标 10.0
  - dialogue_run_mean 11 高于目标 10.0
  - [observe] 标题重复：「行李箱未动」已存在

## 整书结构指标

```
chapters: 5
total_chars: 14132
chapter_chars_mean: 2826
chapter_chars_median: 3320
chapter_chars_cv: 0.31
paragraphs_mean: 69.6
dialogue_chars_pct: 44.7
dialogue_para_pct: 77.6
interiority_para_pct: 7.7
narration_para_pct: 14.7
turn_under20_pct: 75.3
turn_over200_pct: 0.0
attr_say_pct: 26.7
attr_adv_pct: 7.2
scenes_per_chapter: 4
dialogue_run_mean: 5.9
turn_len_median: 12
```
