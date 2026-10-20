# 铜印 生成报告

slug：`xuanyi-20261019-144`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15548
LLM 调用：68 次，累计 233.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红墨水圈出的数字 | 1915 | short | 98.8 | 0 |  | 3 |
| 2 | 转私户的手势 | 4158 | normal | 91.3 | 0 |  | 4 |
| 3 | 按压印章 | 4025 | normal | 83.5 | 0 |  | 5 |
| 4 | 纸条上的日期 | 3480 | normal | 89.9 | 0 |  | 4 |
| 5 | 指纹触碰公章 | 1965 | short | 91.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈国栋的」×6
  - narration_para_pct 19.6 低于目标 20.0
  - [observe] attr_adv_pct 28.6 > 20.0（结构塌缩）
- 第 2 章：
  - 套路句式密度 17.3/千字 > 16.0（「县粮食局」×41、「点了点头」×4、「陈国栋的」×4）
  - 单条套路句式超限：「县粮食局」×41、「点了点头」×4、「陈国栋的」×4
  - narration_para_pct 10.3 低于目标 20.0
  - attr_adv_pct 17.9 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「为什么会」×4、「“我不知道」×3、「”周美兰轻」×3
  - dialogue_chars_pct 62.9 高于目标 58.0
  - narration_para_pct 2.1 低于目标 20.0
  - dialogue_run_mean 23 高于目标 10.0
  - [observe] attr_adv_pct 20.8 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「陈国栋的」×7、「他知道这」×5
  - narration_para_pct 14.1 低于目标 20.0
  - attr_adv_pct 10.7 高于目标 10.0
  - [observe] 章内自我复读 3 句（如「你怎么会知道这个日期？…」）
- 第 5 章：
  - 单条套路句式超限：「陈国栋的」×5
  - narration_para_pct 13.2 低于目标 20.0
  - [observe] attr_adv_pct 27.3 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 14761
chapter_chars_mean: 2952
chapter_chars_median: 3308
chapter_chars_cv: 0.35
paragraphs_mean: 71
dialogue_chars_pct: 48.5
dialogue_para_pct: 83.5
interiority_para_pct: 6.0
narration_para_pct: 10.5
turn_under20_pct: 77.1
turn_over200_pct: 0.0
attr_say_pct: 30.3
attr_adv_pct: 19.5
scenes_per_chapter: 3.2
dialogue_run_mean: 8.5
turn_len_median: 11
```
