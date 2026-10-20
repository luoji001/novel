# 粮票 生成报告

slug：`xuanyi-20261019-24`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14219
LLM 调用：68 次，累计 228.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻动账本的手指 | 1787 | short | 94.4 | 0 |  | 2 |
| 2 | 钥匙敲响铁门 | 3291 | normal | 91.4 | 0 |  | 2 |
| 3 | 翻开旧粮票的秘密 | 3729 | normal | 89.8 | 0 |  | 2 |
| 4 | 摩挲纸边的手指 | 3490 | normal | 90.6 | 0 |  | 3 |
| 5 | 触碰账本的指尖 | 1917 | short | 92.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 章内自我复读 17 句（如「周淑兰走到桌子旁，看着他在那里翻来覆去的动作，眉…」）
- 第 2 章：
  - 单条套路句式超限：「周淑兰的」×7、「陈志远的」×6
  - narration_para_pct 15.1 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「陈志远的」×7、「周淑兰的」×5、「”周淑兰轻」×4
  - narration_para_pct 11.3 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「陈志远的」×4、「”周淑兰轻」×3
  - narration_para_pct 12.3 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「周淑兰的」×4、「陈志远的」×3
  - 情节与已写章节重复 0.64 ≥ 0.62（撞上「陈志远发现每月亏空与自己工资一致，并发现一盒与入职日期相…」）
  - narration_para_pct 7.9 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13607
chapter_chars_mean: 2721
chapter_chars_median: 3171
chapter_chars_cv: 0.33
paragraphs_mean: 53.2
dialogue_chars_pct: 37.9
dialogue_para_pct: 75.4
interiority_para_pct: 11.5
narration_para_pct: 13.1
turn_under20_pct: 74.1
turn_over200_pct: 0.0
attr_say_pct: 22.7
attr_adv_pct: 4.5
scenes_per_chapter: 1.8
dialogue_run_mean: 4.4
turn_len_median: 14
```
