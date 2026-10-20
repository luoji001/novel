# U盘 生成报告

slug：`xuanyi-20261019-232`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15242
LLM 调用：68 次，累计 232.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | U盘插入门缝的瞬间 | 1724 | short | 98.2 | 0 |  | 1 |
| 2 | 抚摸账单边缘的指尖 | 3531 | normal | 92.7 | 0 |  | 3 |
| 3 | U盘上的刻痕 | 4196 | normal | 89.9 | 0 |  | 3 |
| 4 | 触碰U盘的凸起纹路 | 3933 | normal | 84.8 | 0 |  | 5 |
| 5 | 触摸发票边缘的指尖 | 1853 | short | 91.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 11.8 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×4、「为什么会」×4、「”苏婉如轻」×3
  - narration_para_pct 15.9 低于目标 20.0
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×5、「林振东点了点头」×3、「林振东的」×3
  - narration_para_pct 12.2 低于目标 20.0
  - attr_adv_pct 12.9 高于目标 10.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「到了一个」×4、「他知道这」×4
  - interiority_para_pct 20.8 高于目标 20.0
  - attr_adv_pct 17.4 高于目标 10.0
  - [observe] 章内自我复读 13 句（如「他记得这只U盘是从那个神秘的顾客那里得到的，当时…」）
- 第 5 章：
  - 单条套路句式超限：「林振东的」×4
  - [observe] 标题与《抚摸账单边缘的指尖》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 14514
chapter_chars_mean: 2903
chapter_chars_median: 3376
chapter_chars_cv: 0.38
paragraphs_mean: 61
dialogue_chars_pct: 35.2
dialogue_para_pct: 72.6
interiority_para_pct: 10.2
narration_para_pct: 17.2
turn_under20_pct: 74.2
turn_over200_pct: 0.0
attr_say_pct: 22.3
attr_adv_pct: 13.2
scenes_per_chapter: 3.8
dialogue_run_mean: 5.4
turn_len_median: 12
```
