# 铁皮盒 生成报告

slug：`xuanyi-20261019-226`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13607
LLM 调用：68 次，累计 218.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 窥探木门的钥匙声 | 1644 | short | 97.2 | 0 |  | 1 |
| 2 | 值班表上的日期 | 3402 | normal | 91.0 | 0 |  | 3 |
| 3 | 掀开铁皮盒的瞬间 | 3403 | normal | 92.2 | 0 |  | 2 |
| 4 | 摩挲铁皮盒边缘 | 3254 | normal | 89.0 | 0 |  | 2 |
| 5 | 摩挲笔记本封面 | 1899 | short | 90.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 13.3 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈素芬的」×4、「周正阳站在」×3、「”陈素芬轻」×3
  - narration_para_pct 9.8 低于目标 20.0
  - [observe] attr_adv_pct 36.4 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「陈素芬的」×6、「周正阳的」×6
  - narration_para_pct 16.9 低于目标 20.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周正阳站在」×3、「陈素芬的」×3
- 第 5 章：
  - 单条套路句式超限：「陈素芬的」×4
  - narration_para_pct 14.3 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13043
chapter_chars_mean: 2609
chapter_chars_median: 3119
chapter_chars_cv: 0.32
paragraphs_mean: 48.2
dialogue_chars_pct: 28.3
dialogue_para_pct: 71.0
interiority_para_pct: 12.4
narration_para_pct: 16.7
turn_under20_pct: 76.6
turn_over200_pct: 0.0
attr_say_pct: 16.6
attr_adv_pct: 11.1
scenes_per_chapter: 5
dialogue_run_mean: 4.6
turn_len_median: 12
```
