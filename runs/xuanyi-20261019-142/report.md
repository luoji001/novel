# 怀表 生成报告

slug：`xuanyi-20261019-142`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13920
LLM 调用：68 次，累计 228.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 当票上的日期差 | 1848 | short | 96.6 | 0 |  | 1 |
| 2 | 账簿里的陌生名字 | 3600 | normal | 87.8 | 0 |  | 4 |
| 3 | 暗格里的信件 | 3041 | normal | 91.0 | 0 |  | 3 |
| 4 | 怀表与当票的关联 | 3553 | normal | 85.7 | 0 |  | 3 |
| 5 | 地图边缘的墨渍 | 1873 | short | 91.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈文远的」×4
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「“我不知道」×3、「点了点头」×3、「不仅仅是」×3
  - narration_para_pct 18.8 低于目标 20.0
  - [observe] attr_adv_pct 28.6 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「陆秋实的」×5、「沈文远的」×5
  - narration_para_pct 15.4 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「沈文远的」×4、「陆秋实的」×3
  - attr_adv_pct 19.2 高于目标 10.0
  - [observe] 章内自我复读 20 句（如「他只是说：“我知道你一直在寻找答案，但也许你应该…」）
- 第 5 章：
  - 单条套路句式超限：「沈文远的」×3
  - narration_para_pct 10.8 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13307
chapter_chars_mean: 2661
chapter_chars_median: 2923
chapter_chars_cv: 0.32
paragraphs_mean: 53.2
dialogue_chars_pct: 31.1
dialogue_para_pct: 70.7
interiority_para_pct: 11.4
narration_para_pct: 17.9
turn_under20_pct: 77.0
turn_over200_pct: 0.0
attr_say_pct: 27.4
attr_adv_pct: 14.8
scenes_per_chapter: 2.2
dialogue_run_mean: 3.4
turn_len_median: 14
```
