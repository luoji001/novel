# 红票 生成报告

slug：`xuanyi-20261019-186`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13986
LLM 调用：68 次，累计 224.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 触摸钥匙牌 | 1541 | short | 89.7 | 0 |  | 3 |
| 2 | 擦拭钥匙牌 | 4155 | normal | 87.6 | 0 |  | 3 |
| 3 | 摩挲红布面封面 | 3369 | normal | 88.7 | 0 |  | 3 |
| 4 | 摩挲皮包拉链 | 3245 | normal | 0.0 | 0 |  | 5 |
| 5 | 窥视钥匙牌变化 | 1671 | short | 89.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林婉秋的」×4
  - interiority_para_pct 26.1 高于目标 20.0
  - narration_para_pct 13.0 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林婉秋的」×4、「为什么会」×4
  - narration_para_pct 12.5 低于目标 20.0
  - [observe] 标题与《触摸钥匙牌》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「林婉秋的」×9、「”林婉秋轻」×4、「“我不知道」×3
  - narration_para_pct 13.2 低于目标 20.0
  - attr_adv_pct 15.4 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「不仅仅是」×3
  - dialogue_chars_pct 12.7 低于目标 20.0
  - narration_para_pct 19.5 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
  - [observe] interiority_para_pct 36.6 > 32.0（结构塌缩）
- 第 5 章：
  - narration_para_pct 10.0 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
  - dialogue_run_mean 11.5 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13409
chapter_chars_mean: 2682
chapter_chars_median: 3147
chapter_chars_cv: 0.41
paragraphs_mean: 50
dialogue_chars_pct: 29.4
dialogue_para_pct: 65.3
interiority_para_pct: 20.6
narration_para_pct: 14.1
turn_under20_pct: 76.9
turn_over200_pct: 0.0
attr_say_pct: 23.7
attr_adv_pct: 11.0
scenes_per_chapter: 4.6
dialogue_run_mean: 5.1
turn_len_median: 12
```
