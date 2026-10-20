# 当票 生成报告

slug：`xuanyi-20261019-242`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14282
LLM 调用：68 次，累计 242.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 青瓷茶壶的低语 | 1369 | short | 59.6 | 0 |  | 3 |
| 2 | 当票上的错位时间 | 4425 | normal | 81.9 | 0 |  | 5 |
| 3 | 摩挲玉纹的余温 | 3651 | normal | 90.6 | 0 |  | 3 |
| 4 | 摩挲铜钥的余温 | 3358 | normal | 88.5 | 0 |  | 3 |
| 5 | 表链上的小痣 | 1474 | short | 94.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈砚秋的」×5
  - dialogue_chars_pct 16.5 低于目标 20.0
  - [observe] attr_adv_pct 50.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「他知道这」×9、「沈砚秋的」×7、「陆文渊的」×5
  - dialogue_chars_pct 16.3 低于目标 20.0
  - interiority_para_pct 22.2 高于目标 20.0
  - [observe] 章内自我复读 3 句（如「我一直都很高兴能成为你的朋友…」）
  - [observe] attr_adv_pct 23.5 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「陆文渊的」×10、「“我不知道」×4、「沈砚秋点了点头」×3
  - narration_para_pct 4.9 低于目标 20.0
  - [observe] attr_adv_pct 20.7 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「沈砚秋的」×16、「陆文渊的」×10
  - narration_para_pct 9.2 低于目标 20.0
  - [observe] 标题与《摩挲玉纹的余温》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「沈砚秋的」×6
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 13632
chapter_chars_mean: 2726
chapter_chars_median: 3191
chapter_chars_cv: 0.48
paragraphs_mean: 57.2
dialogue_chars_pct: 33.2
dialogue_para_pct: 68.9
interiority_para_pct: 12.3
narration_para_pct: 18.8
turn_under20_pct: 77.6
turn_over200_pct: 0.0
attr_say_pct: 17.7
attr_adv_pct: 20.0
scenes_per_chapter: 2.8
dialogue_run_mean: 4.2
turn_len_median: 13
```
