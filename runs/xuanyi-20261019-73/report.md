# 铜钱裂纹 生成报告

slug：`xuanyi-20261019-73`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13556
LLM 调用：68 次，累计 227.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本的缺口 | 1673 | short | 97.7 | 0 |  | 2 |
| 2 | 铜锁换三次 | 3365 | normal | 90.7 | 0 |  | 3 |
| 3 | 碗底裂痕 | 3576 | normal | 91.4 | 0 |  | 2 |
| 4 | 铜钱的凹痕 | 3181 | normal | 85.8 | 0 |  | 3 |
| 5 | 铜钱消失的瞬间 | 1756 | short | 92.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈砚秋的」×4
  - narration_para_pct 15.4 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「沈砚秋的」×9、「周云舟的」×6、「学徒房」×4
  - narration_para_pct 8.5 低于目标 20.0
  - [observe] attr_adv_pct 30.8 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「”周云舟低」×4、「沈砚秋的」×4、「周云舟的」×3
  - narration_para_pct 9.5 低于目标 20.0
- 第 4 章：
  - interiority_para_pct 23.1 高于目标 20.0
  - narration_para_pct 11.5 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「沈砚秋的」×11
  - narration_para_pct 6.5 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 12901
chapter_chars_mean: 2580
chapter_chars_median: 3064
chapter_chars_cv: 0.34
paragraphs_mean: 56.4
dialogue_chars_pct: 41.8
dialogue_para_pct: 78.2
interiority_para_pct: 11.8
narration_para_pct: 10.1
turn_under20_pct: 67.9
turn_over200_pct: 0.0
attr_say_pct: 17.7
attr_adv_pct: 13.6
scenes_per_chapter: 3.2
dialogue_run_mean: 5.6
turn_len_median: 13
```
