# 表中人 生成报告

slug：`xuanyi-20261019-155`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14535
LLM 调用：68 次，累计 234.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 咖啡机缓缓开启 | 1942 | short | 97.3 | 0 |  | 1 |
| 2 | 黑色西装上的怀表 | 4297 | normal | 91.2 | 0 |  | 2 |
| 3 | 擦拭冰箱的长柄刷 | 3447 | normal | 87.1 | 0 |  | 3 |
| 4 | 摩挲表壳边缘 | 3027 | normal | 90.3 | 0 |  | 3 |
| 5 | 指针指向清晨六点 | 1817 | short | 91.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3
- 第 2 章：
  - 单条套路句式超限：「他知道这」×4、「沈嘉诚站在」×3、「“我不知道」×3
  - narration_para_pct 15.0 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×4、「为什么会」×4
  - narration_para_pct 12.2 低于目标 20.0
  - [observe] 章内自我复读 3 句（如「那是昨天晚上失踪的女人，她手里拿着一瓶香水，脸上…」）
- 第 4 章：
  - 单条套路句式超限：「“我不知道」×3
  - narration_para_pct 9.4 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「南方市殡仪馆」×11、「“我不知道」×3
  - narration_para_pct 12.3 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13693
chapter_chars_mean: 2739
chapter_chars_median: 2843
chapter_chars_cv: 0.36
paragraphs_mean: 76
dialogue_chars_pct: 40.0
dialogue_para_pct: 77.3
interiority_para_pct: 8.5
narration_para_pct: 14.2
turn_under20_pct: 82.4
turn_over200_pct: 0.0
attr_say_pct: 21.5
attr_adv_pct: 6.9
scenes_per_chapter: 3.4
dialogue_run_mean: 6.0
turn_len_median: 11
```
