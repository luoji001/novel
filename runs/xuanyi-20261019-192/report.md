# 纸条上的时间 生成报告

slug：`xuanyi-20261019-192`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：16087
LLM 调用：68 次，累计 246.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 屏幕亮起的瞬间 | 1809 | short | 100.0 | 0 |  | 2 |
| 2 | 快递单上的地址 | 4055 | normal | 90.2 | 0 |  | 3 |
| 3 | 纸条上的时间 | 3850 | normal | 89.7 | 0 |  | 3 |
| 4 | 时间提前的电脑 | 3913 | normal | 90.6 | 0 |  | 2 |
| 5 | 广告牌下的日期 | 2455 | short | 91.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「“我不知道」×3、「陈玉兰的」×3
  - narration_para_pct 12.5 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×4、「陈玉兰的」×4、「”陈玉兰轻」×3
  - narration_para_pct 12.5 低于目标 20.0
  - [observe] 章内自我复读 9 句（如「但我觉得这件事并不简单。你知道吗？我爸曾经说过，…」）
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×3、「他知道这」×3
  - narration_para_pct 4.5 低于目标 20.0
  - attr_adv_pct 18.8 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「林志远的」×4、「“我不知道」×3
  - narration_para_pct 17.0 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「林志远站在」×3、「陈玉兰的」×3、「为什么会」×3
  - 情节与已写章节重复 0.64 ≥ 0.62（撞上「林志远发现网吧07号电脑存在异常登录记录，并逐渐揭开其背…」）
  - narration_para_pct 3.3 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 15265
chapter_chars_mean: 3053
chapter_chars_median: 3659
chapter_chars_cv: 0.32
paragraphs_mean: 74.4
dialogue_chars_pct: 48.2
dialogue_para_pct: 82.9
interiority_para_pct: 6.8
narration_para_pct: 10.3
turn_under20_pct: 71.7
turn_over200_pct: 0.0
attr_say_pct: 30.0
attr_adv_pct: 7.8
scenes_per_chapter: 3.6
dialogue_run_mean: 6.8
turn_len_median: 13
```
