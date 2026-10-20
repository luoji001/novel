# 水表 生成报告

slug：`xuanyi-20261019-248`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15034
LLM 调用：68 次，累计 240.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 水表被移动位置 | 1657 | short | 91.7 | 0 |  | 2 |
| 2 | 水表数字持续增长 | 4086 | normal | 91.2 | 0 |  | 3 |
| 3 | 伪造水电账单 | 3427 | normal | 91.5 | 0 |  | 2 |
| 4 | 手机震动时刻意忽略 | 3873 | normal | 90.8 | 0 |  | 3 |
| 5 | 身份证失踪现场 | 1986 | short | 93.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周晓芸的」×3
  - dialogue_run_mean 1.3 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「陈文远的」×8、「周晓芸点」×5、「”周晓芸轻」×4
  - narration_para_pct 12.7 低于目标 20.0
  - attr_adv_pct 18.9 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「陈文远的」×8、「陈文远站在」×3、「微微一笑」×3
  - narration_para_pct 10.1 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「陈文远的」×3
  - narration_para_pct 8.3 低于目标 20.0
  - attr_adv_pct 13.3 高于目标 10.0
- 第 5 章：
  - narration_para_pct 14.3 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「他知道，这场游戏还没有结束，而他自己，也许才是真…」）

## 整书结构指标

```
chapters: 5
total_chars: 14295
chapter_chars_mean: 2859
chapter_chars_median: 3275
chapter_chars_cv: 0.37
paragraphs_mean: 65.4
dialogue_chars_pct: 38.9
dialogue_para_pct: 76.4
interiority_para_pct: 9.2
narration_para_pct: 14.3
turn_under20_pct: 75.6
turn_over200_pct: 0.0
attr_say_pct: 27.8
attr_adv_pct: 11.2
scenes_per_chapter: 3.8
dialogue_run_mean: 4.8
turn_len_median: 12
```
