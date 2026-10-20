# 行李箱 生成报告

slug：`xuanyi-20261019-103`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15107
LLM 调用：68 次，累计 245.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 行李箱的踪迹 | 1888 | short | 97.7 | 0 |  | 2 |
| 2 | 登记簿的折痕 | 4748 | normal | 86.2 | 0 |  | 4 |
| 3 | 摩挲工牌裂痕 | 3194 | normal | 91.3 | 0 |  | 2 |
| 4 | 摩挲工资单边缘 | 3608 | normal | 89.3 | 0 |  | 2 |
| 5 | 摩挲指纹痕迹 | 1664 | short | 93.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林志远的」×3
  - narration_para_pct 16.2 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×9、「陈美玲的」×9、「林志远的」×4
  - narration_para_pct 8.1 低于目标 20.0
  - attr_adv_pct 13.0 高于目标 10.0
  - [observe] 章内自我复读 31 句（如「可是在第二天早上，所有人都发现了那只沉重的行李箱…」）
- 第 3 章：
  - 单条套路句式超限：「林志远站在」×4、「林志远的」×3
  - narration_para_pct 11.0 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「“我不知道」×5、「林志远站在」×4、「林志远点点」×4
  - narration_para_pct 13.7 低于目标 20.0
- 第 5 章：
  - narration_para_pct 12.2 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14281
chapter_chars_mean: 2856
chapter_chars_median: 3034
chapter_chars_cv: 0.42
paragraphs_mean: 69.4
dialogue_chars_pct: 39.9
dialogue_para_pct: 79.9
interiority_para_pct: 8.5
narration_para_pct: 11.5
turn_under20_pct: 80.1
turn_over200_pct: 0.0
attr_say_pct: 23.3
attr_adv_pct: 7.8
scenes_per_chapter: 6
dialogue_run_mean: 5.0
turn_len_median: 11
```
