# 铜秤 生成报告

slug：`xuanyi-20261019-113`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14420
LLM 调用：68 次，累计 241.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钥匙与账本残页 | 1859 | short | 96.5 | 0 |  | 1 |
| 2 | 钥匙开启账本残页 | 3745 | normal | 84.1 | 0 |  | 4 |
| 3 | 铜秤上的冰凉触感 | 3084 | normal | 91.3 | 0 |  | 3 |
| 4 | 墨水瓶的异常凹陷 | 3596 | normal | 89.9 | 0 |  | 3 |
| 5 | 水渍映照的后院门 | 2131 | short | 92.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈文渊的」×5
- 第 2 章：
  - dialogue_chars_pct 16.1 低于目标 20.0
  - interiority_para_pct 22.5 高于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 标题与《铜钥匙与账本残页》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「沈文渊的」×5
  - narration_para_pct 15.0 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「这铜秤确实比普通秤重许多，我猜定是因为它曾经用来…」）
- 第 4 章：
  - 单条套路句式超限：「周素娥的」×4、「沈文渊的」×3
  - narration_para_pct 18.9 低于目标 20.0
  - [observe] attr_adv_pct 28.6 > 20.0（结构塌缩）
- 第 5 章：
  - narration_para_pct 17.8 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13763
chapter_chars_mean: 2753
chapter_chars_median: 2948
chapter_chars_cv: 0.3
paragraphs_mean: 57
dialogue_chars_pct: 25.6
dialogue_para_pct: 61.9
interiority_para_pct: 15.4
narration_para_pct: 22.7
turn_under20_pct: 80.6
turn_over200_pct: 0.0
attr_say_pct: 23.3
attr_adv_pct: 10.9
scenes_per_chapter: 3.6
dialogue_run_mean: 3.0
turn_len_median: 13
```
