# 行李箱 生成报告

slug：`xuanyi-20261019-43`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14264
LLM 调用：68 次，累计 243.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 照片的浮现 | 1762 | short | 100.0 | 0 |  | 0 |
| 2 | 指纹的痕迹 | 3272 | normal | 92.2 | 0 |  | 2 |
| 3 | 口香糖的出现 | 3791 | normal | 84.2 | 0 |  | 4 |
| 4 | 行李箱的秘密 | 3539 | normal | 86.6 | 0 |  | 4 |
| 5 | 木牌的裂痕 | 1895 | short | 92.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「周慧玲的」×4、「陈思远的」×4、「“我不知道」×3
  - narration_para_pct 5.9 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×5、「”周慧玲低」×3
  - narration_para_pct 3.8 低于目标 20.0
  - attr_adv_pct 10.9 高于目标 10.0
  - dialogue_run_mean 24.5 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「陈思远的」×7、「”周慧玲轻」×4、「陈思远站在」×3
  - dialogue_chars_pct 62.1 高于目标 58.0
  - narration_para_pct 3.6 低于目标 20.0
  - dialogue_run_mean 16 高于目标 10.0
- 第 5 章：
  - narration_para_pct 5.1 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13510
chapter_chars_mean: 2702
chapter_chars_median: 3123
chapter_chars_cv: 0.33
paragraphs_mean: 68.2
dialogue_chars_pct: 54.5
dialogue_para_pct: 89.6
interiority_para_pct: 3.7
narration_para_pct: 6.6
turn_under20_pct: 77.7
turn_over200_pct: 0.0
attr_say_pct: 25.5
attr_adv_pct: 6.7
scenes_per_chapter: 5.8
dialogue_run_mean: 12.9
turn_len_median: 12
```
