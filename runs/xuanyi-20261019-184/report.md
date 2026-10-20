# 火柴盒 生成报告

slug：`xuanyi-20261019-184`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13716
LLM 调用：68 次，累计 230.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本上的数字 | 1433 | short | 98.6 | 0 |  | 1 |
| 2 | 账本上的四毛钱 | 3223 | normal | 91.0 | 0 |  | 3 |
| 3 | 触摸结婚证边缘 | 3606 | normal | 89.2 | 0 |  | 2 |
| 4 | 抚摸火柴盒边缘 | 3453 | normal | 86.7 | 0 |  | 2 |
| 5 | 掀开铁皮盒瞬间 | 1996 | short | 87.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 12.9 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「他知道这」×4、「陈国忠的」×4、「为什么会」×3
  - attr_adv_pct 11.1 高于目标 10.0
  - [observe] 标题与《账本上的数字》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3、「陈国忠的」×3
  - narration_para_pct 15.3 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「他知道自己」×5、「点了点头」×4、「赵素梅的」×3
  - [observe] 章内自我复读 2 句（如「他知道，自己正站在一个重要的十字路口，而前方等待…」）
- 第 5 章：
  - attr_adv_pct 15.4 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13091
chapter_chars_mean: 2618
chapter_chars_median: 3076
chapter_chars_cv: 0.36
paragraphs_mean: 54.6
dialogue_chars_pct: 28.3
dialogue_para_pct: 66.1
interiority_para_pct: 13.6
narration_para_pct: 20.3
turn_under20_pct: 79.6
turn_over200_pct: 0.0
attr_say_pct: 28.7
attr_adv_pct: 5.6
scenes_per_chapter: 4.4
dialogue_run_mean: 3.4
turn_len_median: 11
```
