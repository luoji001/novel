# 钥匙牌漂流 生成报告

slug：`xuanyi-20261019-166`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13969
LLM 调用：68 次，累计 226.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 登记簿的铅笔字 | 1449 | short | 96.2 | 0 |  | 2 |
| 2 | 钥匙牌的排列顺序 | 3793 | normal | 93.3 | 0 |  | 3 |
| 3 | 火车票贴胸口 | 3304 | normal | 89.4 | 0 |  | 3 |
| 4 | 梦见钢笔的光芒 | 3583 | normal | 25.0 | 0 |  | 5 |
| 5 | 撬开挂钟的秘密 | 1835 | short | 91.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈雪梅的」×3、「周振邦的」×3
  - narration_para_pct 19.2 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周振邦的」×8、「沈雪梅的」×3
  - narration_para_pct 11.4 低于目标 20.0
  - attr_adv_pct 10.5 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「周振邦的」×8、「沈雪梅的」×3
  - narration_para_pct 17.9 低于目标 20.0
  - attr_adv_pct 13.3 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「沈雪梅的」×3
  - dialogue_chars_pct 9.5 低于目标 20.0
  - interiority_para_pct 23.1 高于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 章内自我复读 14 句（如「梦里的场景并不清晰，只是在某个角落，有一盏昏黄的…」）
- 第 5 章：
  - dialogue_chars_pct 18.7 低于目标 20.0
  - narration_para_pct 17.1 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13371
chapter_chars_mean: 2674
chapter_chars_median: 3156
chapter_chars_cv: 0.39
paragraphs_mean: 51.8
dialogue_chars_pct: 25.9
dialogue_para_pct: 59.1
interiority_para_pct: 17.5
narration_para_pct: 23.5
turn_under20_pct: 77.4
turn_over200_pct: 0.0
attr_say_pct: 19.3
attr_adv_pct: 11.8
scenes_per_chapter: 4.6
dialogue_run_mean: 3.5
turn_len_median: 11
```
