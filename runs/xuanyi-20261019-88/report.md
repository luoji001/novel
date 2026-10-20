# 水箱密语 生成报告

slug：`xuanyi-20261019-88`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15735
LLM 调用：68 次，累计 234.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 水表刻度 | 2075 | short | 94.6 | 0 |  | 1 |
| 2 | 撬开水箱底板 | 4538 | normal | 47.1 | 0 |  | 2 |
| 3 | 收音机重复播报 | 3973 | normal | 91.9 | 0 |  | 3 |
| 4 | 摩挲合同边缘 | 3453 | normal | 90.1 | 0 |  | 3 |
| 5 | 摩挲水表灰尘 | 1691 | short | 94.0 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 18.0 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「苏婉秋的」×3
  - dialogue_chars_pct 12.6 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「苏婉秋的」×5、「林振邦的」×3、「为什么会」×3
  - narration_para_pct 12.0 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「苏婉秋的」×7、「林振邦的」×4
  - interiority_para_pct 20.3 高于目标 20.0
  - narration_para_pct 17.2 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 15046
chapter_chars_mean: 3009
chapter_chars_median: 3311
chapter_chars_cv: 0.4
paragraphs_mean: 61.4
dialogue_chars_pct: 21.7
dialogue_para_pct: 55.8
interiority_para_pct: 18.5
narration_para_pct: 25.7
turn_under20_pct: 81.7
turn_over200_pct: 0.0
attr_say_pct: 24.6
attr_adv_pct: 7.3
scenes_per_chapter: 5
dialogue_run_mean: 3.0
turn_len_median: 11
```
