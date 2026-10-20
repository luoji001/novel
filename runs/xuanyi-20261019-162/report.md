# 当票 生成报告

slug：`xuanyi-20261019-162`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13772
LLM 调用：68 次，累计 219.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 当票背面的签名 | 1627 | short | 63.4 | 0 |  | 3 |
| 2 | 账簿中的编号 | 3103 | normal | 90.7 | 0 |  | 4 |
| 3 | 铜钥匙的低语 | 3154 | normal | 92.4 | 0 |  | 2 |
| 4 | 当票与怀表的重逢 | 3754 | normal | 89.0 | 0 |  | 3 |
| 5 | 银元的归属 | 2129 | short | 92.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 7.9 低于目标 20.0
  - interiority_para_pct 24.0 高于目标 20.0
  - dialogue_run_mean 1 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「周慕云的」×6、「沈文渊的」×4、「他知道这」×3
  - narration_para_pct 18.9 低于目标 20.0
  - [observe] 章内自我复读 5 句（如「他知道，这场谈话将会揭开许多尘封已久的秘密，而他…」）
  - [observe] attr_adv_pct 23.1 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「沈文渊的」×10、「周慕云的」×5、「他知道这」×3
  - attr_adv_pct 18.2 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「周慕云的」×9、「沈文渊的」×8、「沈文渊站在」×3
  - narration_para_pct 9.1 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「沈文渊没有回答，只是再次看向那块怀表，仿佛想要从…」）
- 第 5 章：
  - 单条套路句式超限：「周慕云的」×4、「沈文渊的」×3
  - narration_para_pct 18.8 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13084
chapter_chars_mean: 2617
chapter_chars_median: 2983
chapter_chars_cv: 0.31
paragraphs_mean: 59.6
dialogue_chars_pct: 31.9
dialogue_para_pct: 68.6
interiority_para_pct: 12.3
narration_para_pct: 19.1
turn_under20_pct: 87.9
turn_over200_pct: 0.0
attr_say_pct: 13.1
attr_adv_pct: 11.4
scenes_per_chapter: 2.4
dialogue_run_mean: 3.2
turn_len_median: 11
```
