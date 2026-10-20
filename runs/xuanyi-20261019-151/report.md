# 钥匙 生成报告

slug：`xuanyi-20261019-151`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14449
LLM 调用：68 次，累计 238.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钥匙的秘密 | 1537 | short | 100.0 | 0 |  | 2 |
| 2 | 火柴盒的倒影 | 3911 | normal | 90.5 | 0 |  | 3 |
| 3 | 摩挲铜锁的指尖 | 3731 | normal | 90.0 | 0 |  | 2 |
| 4 | 摩挲怀表的指尖 | 3403 | normal | 89.6 | 0 |  | 3 |
| 5 | 摩挲铜钥匙的指尖 | 1862 | short | 90.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈佩兰的」×3、「为什么会」×3
  - narration_para_pct 15.4 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周慕云的」×8、「沈佩兰的」×7、「“我不知道」×4
  - narration_para_pct 8.1 低于目标 20.0
  - dialogue_run_mean 11.2 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「周慕云的」×9、「沈佩兰的」×8、「“我不知道」×3
  - narration_para_pct 9.5 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「沈佩兰的」×4
  - narration_para_pct 11.5 低于目标 20.0
  - [observe] 标题与《摩挲铜锁的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「沈佩兰的」×4
  - narration_para_pct 7.3 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 标题与《摩挲铜锁的指尖》近似 0.80 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13712
chapter_chars_mean: 2742
chapter_chars_median: 3262
chapter_chars_cv: 0.39
paragraphs_mean: 62.8
dialogue_chars_pct: 44.8
dialogue_para_pct: 82.9
interiority_para_pct: 7.2
narration_para_pct: 9.9
turn_under20_pct: 73.6
turn_over200_pct: 0.0
attr_say_pct: 29.1
attr_adv_pct: 3.1
scenes_per_chapter: 3.2
dialogue_run_mean: 6.4
turn_len_median: 13
```
