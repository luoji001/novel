# 重扫 生成报告

slug：`xuanyi-20261019-157`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14412
LLM 调用：68 次，累计 228.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 破损读取窗口 | 1731 | short | 97.9 | 0 |  | 1 |
| 2 | 扫描机器刮痕 | 4229 | normal | 91.6 | 0 |  | 3 |
| 3 | 拨弄镜头盖 | 3417 | normal | 92.0 | 0 |  | 1 |
| 4 | 摩挲咖啡杯沿 | 3224 | normal | 91.0 | 0 |  | 2 |
| 5 | 扫描设备故障 | 1806 | short | 90.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 20.0 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「周子安站在」×3、「林雪梅的」×3、「为什么会」×3
  - narration_para_pct 15.0 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「林雪梅的」×4、「周子安站在」×3
- 第 4 章：
  - 单条套路句式超限：「林雪梅的」×7、「周子安的」×6
  - narration_para_pct 4.5 低于目标 20.0
- 第 5 章：
  - narration_para_pct 6.9 低于目标 20.0
  - dialogue_run_mean 13 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13757
chapter_chars_mean: 2751
chapter_chars_median: 3076
chapter_chars_cv: 0.38
paragraphs_mean: 58.2
dialogue_chars_pct: 39.9
dialogue_para_pct: 77.7
interiority_para_pct: 7.3
narration_para_pct: 15.0
turn_under20_pct: 67.7
turn_over200_pct: 0.0
attr_say_pct: 26.4
attr_adv_pct: 9.8
scenes_per_chapter: 3.4
dialogue_run_mean: 6.8
turn_len_median: 13
```
