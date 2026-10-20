# 刻痕 生成报告

slug：`xuanyi-20261019-247`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13613
LLM 调用：68 次，累计 236.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 算盘拨动的瞬间 | 1795 | short | 97.1 | 0 |  | 1 |
| 2 | 拓印图的凹陷 | 3421 | normal | 90.0 | 0 |  | 2 |
| 3 | 地契上的指纹 | 2953 | normal | 90.8 | 0 |  | 3 |
| 4 | 砚台上的刻痕 | 3579 | normal | 89.6 | 0 |  | 2 |
| 5 | 砚台凹陷现旧踪 | 1860 | short | 92.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 12.9 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「沈子安点」×3
  - narration_para_pct 8.8 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「陆怀远的」×3、「微微一笑」×3
  - narration_para_pct 11.8 低于目标 20.0
  - attr_adv_pct 15.8 高于目标 10.0
- 第 4 章：
  - narration_para_pct 8.0 低于目标 20.0
  - attr_adv_pct 11.4 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「说道“我」×3
  - narration_para_pct 14.3 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 12968
chapter_chars_mean: 2594
chapter_chars_median: 2803
chapter_chars_cv: 0.31
paragraphs_mean: 56.8
dialogue_chars_pct: 42.4
dialogue_para_pct: 81.5
interiority_para_pct: 7.9
narration_para_pct: 10.5
turn_under20_pct: 70.7
turn_over200_pct: 0.0
attr_say_pct: 30.0
attr_adv_pct: 7.7
scenes_per_chapter: 1.8
dialogue_run_mean: 5.0
turn_len_median: 14
```
