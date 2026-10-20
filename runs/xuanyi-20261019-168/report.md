# 水表转动 生成报告

slug：`xuanyi-20261019-168`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15363
LLM 调用：68 次，累计 242.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 水表停滞的时刻 | 1582 | short | 96.6 | 0 |  | 2 |
| 2 | 收据上的小备注 | 4742 | normal | 92.4 | 0 |  | 4 |
| 3 | 触摸仙人掌的指尖 | 3695 | normal | 89.5 | 0 |  | 3 |
| 4 | 水泥袋的重量 | 3601 | normal | 91.2 | 0 |  | 3 |
| 5 | 触碰收据的指尖 | 1738 | short | 92.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 13.8 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「周婉如的」×5、「周婉如点」×4、「”周婉如低」×3
  - narration_para_pct 9.0 低于目标 20.0
  - attr_adv_pct 13.8 高于目标 10.0
  - [observe] 章内自我复读 6 句（如「周婉如回答道，“只要我们能找到更多的线索…」）
- 第 3 章：
  - 单条套路句式超限：「”周婉如轻」×3、「周婉如的」×3、「他知道这」×3
  - narration_para_pct 9.0 低于目标 20.0
  - [observe] 章内自我复读 11 句（如「他的目光落在屋内的窗台上，那里摆放着一盆仙人掌，…」）
- 第 4 章：
  - 单条套路句式超限：「周婉如的」×6、「林秋实站在」×3
  - narration_para_pct 15.9 低于目标 20.0
  - [observe] attr_adv_pct 30.8 > 20.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「周婉如的」×6、「林秋实的」×3
  - narration_para_pct 8.9 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14576
chapter_chars_mean: 2915
chapter_chars_median: 3449
chapter_chars_cv: 0.44
paragraphs_mean: 70.8
dialogue_chars_pct: 42.0
dialogue_para_pct: 78.7
interiority_para_pct: 10.1
narration_para_pct: 11.1
turn_under20_pct: 74.4
turn_over200_pct: 0.0
attr_say_pct: 17.1
attr_adv_pct: 16.6
scenes_per_chapter: 3.6
dialogue_run_mean: 5.9
turn_len_median: 14
```
