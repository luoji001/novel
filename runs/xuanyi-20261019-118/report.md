# 绣绷上的余线 生成报告

slug：`xuanyi-20261019-118`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14476
LLM 调用：68 次，累计 235.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本上的针脚 | 1761 | short | 99.3 | 0 |  | 4 |
| 2 | 账本上的绣线痕迹 | 3571 | normal | 91.3 | 0 |  | 3 |
| 3 | 绣绷上的暗纹 | 3524 | normal | 90.0 | 0 |  | 3 |
| 4 | 绣品上的新针痕 | 3875 | normal | 88.5 | 0 |  | 3 |
| 5 | 绣品上的旧标记 | 1740 | short | 91.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「”陆文远轻」×3
  - narration_para_pct 2.2 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - dialogue_run_mean 10.2 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「沈佩兰的」×8
  - narration_para_pct 12.2 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「陆文远的」×5
  - narration_para_pct 12.5 低于目标 20.0
  - attr_adv_pct 17.6 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「沈佩兰的」×12、「陆文远的」×4
  - narration_para_pct 10.2 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「那你为什么不告诉我？…」）
- 第 5 章：
  - narration_para_pct 10.8 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13765
chapter_chars_mean: 2753
chapter_chars_median: 3382
chapter_chars_cv: 0.37
paragraphs_mean: 63.2
dialogue_chars_pct: 40.7
dialogue_para_pct: 78.9
interiority_para_pct: 10.8
narration_para_pct: 10.4
turn_under20_pct: 74.2
turn_over200_pct: 0.0
attr_say_pct: 16.6
attr_adv_pct: 10.0
scenes_per_chapter: 1.6
dialogue_run_mean: 5.9
turn_len_median: 12
```
