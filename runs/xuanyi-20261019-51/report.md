# 铜锁 生成报告

slug：`xuanyi-20261019-51`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13556
LLM 调用：68 次，累计 220.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅泛黄账本 | 1479 | short | 99.1 | 0 |  | 0 |
| 2 | 钥匙与雨夜的对话 | 3532 | normal | 91.9 | 0 |  | 4 |
| 3 | 钥匙与地图的对峙 | 3221 | normal | 85.8 | 0 |  | 4 |
| 4 | 地图上的神秘标记 | 3458 | normal | 90.5 | 0 |  | 2 |
| 5 | 钥匙开启第一道锁 | 1861 | short | 90.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「周怀远的」×4
  - dialogue_chars_pct 58.4 高于目标 58.0
  - narration_para_pct 3.4 低于目标 20.0
  - [observe] attr_adv_pct 23.3 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「沈墨感到」×3
  - dialogue_chars_pct 16.7 低于目标 20.0
  - interiority_para_pct 20.3 高于目标 20.0
  - [observe] 标题与《钥匙与雨夜的对话》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「沈墨站在」×3
  - attr_adv_pct 10.5 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「周怀远的」×3
  - narration_para_pct 6.4 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 12875
chapter_chars_mean: 2575
chapter_chars_median: 3087
chapter_chars_cv: 0.36
paragraphs_mean: 59.8
dialogue_chars_pct: 38.1
dialogue_para_pct: 71.1
interiority_para_pct: 11.9
narration_para_pct: 17.0
turn_under20_pct: 75.6
turn_over200_pct: 0.0
attr_say_pct: 19.1
attr_adv_pct: 8.7
scenes_per_chapter: 3.6
dialogue_run_mean: 5.5
turn_len_median: 12
```
