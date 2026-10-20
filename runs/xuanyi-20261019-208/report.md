# 水表 生成报告

slug：`xuanyi-20261019-208`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13878
LLM 调用：68 次，累计 215.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 开门见镜 | 1797 | short | 97.6 | 0 |  | 1 |
| 2 | 玻璃杯倒影 | 3479 | normal | 89.6 | 0 |  | 4 |
| 3 | 神秘男子的身影 | 3123 | normal | 91.2 | 0 |  | 3 |
| 4 | 鞋子的秘密 | 3613 | normal | 91.0 | 0 |  | 1 |
| 5 | 指纹迷雾 | 1861 | short | 92.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 11.1 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「苏婉清的」×6、「”苏婉清轻」×4
  - narration_para_pct 5.5 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
  - dialogue_run_mean 17 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×5、「林修远的」×4、「苏婉清的」×3
  - narration_para_pct 13.8 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「林修远站在」×3、「不仅仅是」×3、「他知道这」×3
- 第 5 章：
  - 单条套路句式超限：「林修远的」×3
  - narration_para_pct 4.7 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13201
chapter_chars_mean: 2640
chapter_chars_median: 2978
chapter_chars_cv: 0.31
paragraphs_mean: 60.6
dialogue_chars_pct: 39.7
dialogue_para_pct: 75.5
interiority_para_pct: 8.4
narration_para_pct: 16.2
turn_under20_pct: 76.3
turn_over200_pct: 0.0
attr_say_pct: 19.9
attr_adv_pct: 8.0
scenes_per_chapter: 4
dialogue_run_mean: 7.7
turn_len_median: 12
```
