# 药本残页 生成报告

slug：`xuanyi-20261019-05`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15751
LLM 调用：68 次，累计 255.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 监控画面中的身影 | 1844 | short | 82.1 | 0 |  | 3 |
| 2 | 账本上的新记录 | 3566 | normal | 90.9 | 0 |  | 3 |
| 3 | 屏幕上的剪影对话 | 4024 | normal | 91.4 | 0 |  | 2 |
| 4 | 药箱里的秘密 | 4332 | normal | 80.0 | 0 |  | 4 |
| 5 | 卡片上的特殊符号 | 1980 | short | 83.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林子安的」×4
  - dialogue_chars_pct 10.7 低于目标 20.0
  - dialogue_run_mean 1.4 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「就在这时」×3
  - attr_adv_pct 15.4 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「他猛地睁开眼睛，盯着那行记录看了许久，终于开口说…」）
- 第 3 章：
  - 单条套路句式超限：「陈文远的」×4、「林子安的」×4、「为什么会」×3
  - narration_para_pct 11.6 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「林子安点了点头」×3、「他知道自己」×3、「他知道这」×3
  - dialogue_chars_pct 15.5 低于目标 20.0
  - interiority_para_pct 20.9 高于目标 20.0
  - [observe] 章内自我复读 17 句（如「电话另一端传来一阵沉默，然后才有人回答道：“抱歉…」）
- 第 5 章：
  - dialogue_chars_pct 13.4 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 15097
chapter_chars_mean: 3019
chapter_chars_median: 3423
chapter_chars_cv: 0.37
paragraphs_mean: 57.2
dialogue_chars_pct: 25.4
dialogue_para_pct: 58.7
interiority_para_pct: 12.4
narration_para_pct: 28.8
turn_under20_pct: 79.2
turn_over200_pct: 0.0
attr_say_pct: 17.9
attr_adv_pct: 7.3
scenes_per_chapter: 5
dialogue_run_mean: 3.5
turn_len_median: 11
```
