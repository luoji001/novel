# 断笔 生成报告

slug：`xuanyi-20261019-273`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13630
LLM 调用：68 次，累计 230.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 算盘珠的凹痕 | 1781 | short | 95.5 | 0 |  | 1 |
| 2 | 触摸账页的指尖 | 3830 | normal | 91.5 | 0 |  | 3 |
| 3 | 触碰丝绸腰带的指尖 | 3121 | normal | 90.7 | 0 |  | 2 |
| 4 | 凝视钢笔的余光 | 3124 | normal | 91.6 | 0 |  | 2 |
| 5 | 拾起残纸的指尖 | 1769 | short | 93.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈怀瑾的」×4
- 第 2 章：
  - 单条套路句式超限：「沈怀瑾的」×6、「周文渊的」×5
  - narration_para_pct 8.3 低于目标 20.0
  - attr_adv_pct 15.8 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「沈怀瑾站在」×4、「沈怀瑾的」×4
  - narration_para_pct 14.3 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周文渊的」×6、「沈怀瑾的」×5
  - narration_para_pct 9.8 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「周文渊的」×5、「沈怀瑾的」×3
  - narration_para_pct 8.8 低于目标 20.0
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 13034
chapter_chars_mean: 2607
chapter_chars_median: 2978
chapter_chars_cv: 0.34
paragraphs_mean: 50.4
dialogue_chars_pct: 34.4
dialogue_para_pct: 75.6
interiority_para_pct: 11.8
narration_para_pct: 12.7
turn_under20_pct: 74.7
turn_over200_pct: 0.0
attr_say_pct: 12.1
attr_adv_pct: 10.5
scenes_per_chapter: 2.2
dialogue_run_mean: 5.0
turn_len_median: 13
```
