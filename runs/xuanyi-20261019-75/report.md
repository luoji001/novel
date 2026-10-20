# 表停时 生成报告

slug：`xuanyi-20261019-75`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14065
LLM 调用：68 次，累计 222.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 微波炉里的液体痕迹 | 1848 | short | 93.3 | 0 |  | 1 |
| 2 | 撕掉的登记簿页 | 3371 | normal | 93.4 | 0 |  | 2 |
| 3 | 病历卡边缘的褶皱 | 3224 | normal | 89.0 | 0 |  | 2 |
| 4 | 手表与登记簿的秘密 | 3651 | normal | 89.6 | 0 |  | 0 |
| 5 | 手表与病历卡的谜题 | 1966 | short | 90.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 18.6 低于目标 20.0
- 第 2 章：
  - narration_para_pct 11.8 低于目标 20.0
  - attr_adv_pct 19.0 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「林婉如的」×6、「“我不知道」×3
  - narration_para_pct 10.7 低于目标 20.0
- 第 5 章：
  - narration_para_pct 8.3 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13410
chapter_chars_mean: 2682
chapter_chars_median: 3096
chapter_chars_cv: 0.3
paragraphs_mean: 56.8
dialogue_chars_pct: 34.5
dialogue_para_pct: 71.6
interiority_para_pct: 13.0
narration_para_pct: 15.3
turn_under20_pct: 73.7
turn_over200_pct: 0.0
attr_say_pct: 26.6
attr_adv_pct: 7.4
scenes_per_chapter: 4.6
dialogue_run_mean: 4.0
turn_len_median: 11
```
