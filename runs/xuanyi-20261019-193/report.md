# 铜钱 生成报告

slug：`xuanyi-20261019-193`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13418
LLM 调用：68 次，累计 227.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 掀开账本的一角 | 1518 | short | 97.3 | 0 |  | 1 |
| 2 | 铜钱与陶罐对谈 | 3340 | normal | 94.0 | 0 |  | 3 |
| 3 | 墨水瓶里的玉碎痕迹 | 3107 | normal | 89.8 | 0 |  | 3 |
| 4 | 镇纸边缘的裂痕 | 3426 | normal | 90.9 | 0 |  | 3 |
| 5 | 铜印上的凹痕 | 2022 | short | 90.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 30.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「周怀瑾点」×3、「说道“我」×3
  - narration_para_pct 8.7 低于目标 20.0
  - [observe] attr_adv_pct 28.6 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「沈文渊的」×4、「他知道这」×3
  - narration_para_pct 18.5 低于目标 20.0
  - [observe] 章内自我复读 19 句（如「陆秋实接过铜印仔细端详了一会儿，然后抬起头看向沈…」）
- 第 4 章：
  - 单条套路句式超限：「绍兴当铺」×27、「“我不知道」×5
  - narration_para_pct 11.0 低于目标 20.0
  - attr_adv_pct 10.3 高于目标 10.0
- 第 5 章：
  - dialogue_chars_pct 18.0 低于目标 20.0
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 12749
chapter_chars_mean: 2550
chapter_chars_median: 2960
chapter_chars_cv: 0.32
paragraphs_mean: 58.6
dialogue_chars_pct: 37.3
dialogue_para_pct: 75.1
interiority_para_pct: 8.3
narration_para_pct: 16.7
turn_under20_pct: 76.9
turn_over200_pct: 0.0
attr_say_pct: 24.8
attr_adv_pct: 16.5
scenes_per_chapter: 3.2
dialogue_run_mean: 4.5
turn_len_median: 11
```
