# 水表 生成报告

slug：`xuanyi-20261019-08`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15413
LLM 调用：68 次，累计 234.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 水龙头滴水声 | 1712 | short | 97.6 | 0 |  | 0 |
| 2 | 水表指针的秘密 | 4438 | normal | 89.6 | 0 |  | 3 |
| 3 | 钥匙上的刻痕 | 3722 | normal | 88.9 | 0 |  | 2 |
| 4 | 电费单上的名字 | 3617 | normal | 89.5 | 0 |  | 2 |
| 5 | 身份证背面的照片 | 1919 | short | 65.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈志远的」×5、「“我不知道」×4、「林晓梅的」×4
  - narration_para_pct 7.8 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「陈志远的」×8、「林晓梅的」×7、「陈志远站在」×3
  - narration_para_pct 11.8 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「林晓梅的」×9、「陈志远的」×5、「”林晓梅低」×4
  - narration_para_pct 7.7 低于目标 20.0
- 第 5 章：
  - dialogue_chars_pct 10.6 低于目标 20.0
  - interiority_para_pct 43.3 高于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14742
chapter_chars_mean: 2948
chapter_chars_median: 3446
chapter_chars_cv: 0.39
paragraphs_mean: 59.2
dialogue_chars_pct: 34.4
dialogue_para_pct: 71.1
interiority_para_pct: 16.6
narration_para_pct: 12.4
turn_under20_pct: 76.1
turn_over200_pct: 0.0
attr_say_pct: 16.8
attr_adv_pct: 5.7
scenes_per_chapter: 5
dialogue_run_mean: 4.2
turn_len_median: 12
```
