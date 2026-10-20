# 当票 生成报告

slug：`xuanyi-20261019-262`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14699
LLM 调用：68 次，累计 235.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钟的低鸣 | 1961 | short | 99.6 | 0 |  | 2 |
| 2 | 当票的折痕 | 3308 | normal | 93.1 | 0 |  | 3 |
| 3 | 摩挲银戒的指尖 | 3476 | normal | 93.2 | 0 |  | 2 |
| 4 | 摩挲怀表的刻痕 | 3904 | normal | 89.8 | 0 |  | 3 |
| 5 | 铜钟停摆的时刻 | 2045 | short | 92.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 19.1 低于目标 20.0
  - [observe] attr_adv_pct 30.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×5、「为什么会」×3
  - narration_para_pct 13.9 低于目标 20.0
  - attr_adv_pct 15.6 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「周怀瑾的」×5
  - narration_para_pct 16.9 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「带着一丝」×4、「微微一笑」×3、「沈慕云的」×3
  - narration_para_pct 10.5 低于目标 20.0
  - attr_adv_pct 11.8 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「为什么会」×4、「“我不知道」×3
  - narration_para_pct 6.7 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13964
chapter_chars_mean: 2793
chapter_chars_median: 3152
chapter_chars_cv: 0.3
paragraphs_mean: 66
dialogue_chars_pct: 40.1
dialogue_para_pct: 77.8
interiority_para_pct: 8.8
narration_para_pct: 13.4
turn_under20_pct: 74.4
turn_over200_pct: 0.0
attr_say_pct: 16.5
attr_adv_pct: 12.5
scenes_per_chapter: 3.2
dialogue_run_mean: 5.3
turn_len_median: 13
```
