# 绣针裂痕 生成报告

slug：`xuanyi-20261019-198`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14695
LLM 调用：68 次，累计 242.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 绣面的针脚 | 1703 | short | 100.0 | 0 |  | 2 |
| 2 | 绣线拂过账本 | 3678 | normal | 88.7 | 0 |  | 4 |
| 3 | 绣针落入掌心 | 3434 | normal | 92.6 | 0 |  | 3 |
| 4 | 绣线比对账本 | 3734 | normal | 91.5 | 0 |  | 3 |
| 5 | 绣线拂过账本 | 2141 | short | 91.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「顾怀远的」×5、「沈佩兰的」×4
  - narration_para_pct 12.1 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「顾怀远的」×8、「沈佩兰的」×8
  - 情节与已写章节重复 0.64 ≥ 0.62（撞上「沈佩兰发现一幅绣品的针法与顾怀远的手艺不符，并质疑其去向…」）
  - interiority_para_pct 21.5 高于目标 20.0
  - narration_para_pct 3.1 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「沈佩兰的」×6、「顾怀远的」×3
  - narration_para_pct 4.8 低于目标 20.0
  - [observe] attr_adv_pct 20.6 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「顾怀远的」×11、「沈佩兰的」×6、「苏城绣艺行会」×3
  - narration_para_pct 9.6 低于目标 20.0
  - [observe] 标题与《绣线拂过账本》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「顾怀远的」×9、「沈佩兰的」×4
  - narration_para_pct 4.4 低于目标 20.0
  - [observe] 标题重复：「绣线拂过账本」已存在

## 整书结构指标

```
chapters: 5
total_chars: 14005
chapter_chars_mean: 2801
chapter_chars_median: 3254
chapter_chars_cv: 0.32
paragraphs_mean: 59.8
dialogue_chars_pct: 42.0
dialogue_para_pct: 80.0
interiority_para_pct: 13.6
narration_para_pct: 6.4
turn_under20_pct: 71.6
turn_over200_pct: 0.0
attr_say_pct: 18.7
attr_adv_pct: 5.8
scenes_per_chapter: 2.6
dialogue_run_mean: 5.9
turn_len_median: 14
```
