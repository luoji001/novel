# 旧钢笔 生成报告

slug：`xuanyi-20261019-84`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13610
LLM 调用：68 次，累计 224.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 算盘珠子的震颤 | 1384 | short | 97.5 | 0 |  | 0 |
| 2 | 工资单上的死亡日期 | 3606 | normal | 90.8 | 0 |  | 2 |
| 3 | 撕去日期的指尖 | 3138 | normal | 89.7 | 0 |  | 2 |
| 4 | 墨水瓶的焦糊味 | 3435 | normal | 93.4 | 0 |  | 2 |
| 5 | 指尖抚过空白页 | 2042 | short | 92.3 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「周淑芬的」×8、「陈永年的」×8、「他知道这」×4
  - narration_para_pct 12.8 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「周淑芬的」×6、「”周淑芬轻」×3
  - narration_para_pct 15.5 低于目标 20.0
- 第 4 章：
  - narration_para_pct 12.5 低于目标 20.0
  - attr_adv_pct 15.4 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 12906
chapter_chars_mean: 2581
chapter_chars_median: 3007
chapter_chars_cv: 0.35
paragraphs_mean: 57.6
dialogue_chars_pct: 40.9
dialogue_para_pct: 78.5
interiority_para_pct: 6.2
narration_para_pct: 15.3
turn_under20_pct: 74.2
turn_over200_pct: 0.0
attr_say_pct: 30.3
attr_adv_pct: 7.4
scenes_per_chapter: 2.8
dialogue_run_mean: 5.3
turn_len_median: 12
```
