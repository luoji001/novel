# 木牌 生成报告

slug：`xuanyi-20261019-214`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14359
LLM 调用：68 次，累计 233.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 抚摸布料标签 | 2084 | short | 98.2 | 0 |  | 2 |
| 2 | 摸锁芯听异响 | 3477 | normal | 90.8 | 0 |  | 3 |
| 3 | 布料标签边缘磨损 | 3373 | normal | 88.2 | 0 |  | 3 |
| 4 | 抚摸木牌刻痕 | 3529 | normal | 91.6 | 0 |  | 3 |
| 5 | 摩挲纸边褶皱 | 1891 | short | 91.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈德昌的」×6、「周素英的」×3
  - narration_para_pct 7.7 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈德昌的」×4、「县供销社」×3
  - narration_para_pct 11.8 低于目标 20.0
  - attr_adv_pct 18.2 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「”周素英轻」×4、「周素英点」×4、「陈德昌点了点头」×3
  - narration_para_pct 2.7 低于目标 20.0
  - [observe] 章内自我复读 19 句（如「陈德昌心中一紧，他开始意识到，这个看似简单的仓库…」）
- 第 4 章：
  - 单条套路句式超限：「他知道这」×4、「变得更加」×3
  - narration_para_pct 10.7 低于目标 20.0
  - [observe] attr_adv_pct 30.4 > 20.0（结构塌缩）
- 第 5 章：
  - narration_para_pct 7.5 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13691
chapter_chars_mean: 2738
chapter_chars_median: 3209
chapter_chars_cv: 0.28
paragraphs_mean: 59.2
dialogue_chars_pct: 43.0
dialogue_para_pct: 84.7
interiority_para_pct: 7.0
narration_para_pct: 8.2
turn_under20_pct: 70.6
turn_over200_pct: 0.0
attr_say_pct: 14.8
attr_adv_pct: 14.6
scenes_per_chapter: 2.2
dialogue_run_mean: 7.2
turn_len_median: 14
```
