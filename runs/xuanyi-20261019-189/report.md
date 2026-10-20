# 药瓶上的名字 生成报告

slug：`xuanyi-20261019-189`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14153
LLM 调用：68 次，累计 228.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药瓶上的名字 | 1631 | short | 98.6 | 0 |  | 3 |
| 2 | 登记簿的裂痕 | 3577 | normal | 86.3 | 0 |  | 3 |
| 3 | 病历卡上的签名 | 3358 | normal | 88.2 | 0 |  | 2 |
| 4 | 抽屉边缘的墨水痕迹 | 3713 | normal | 88.7 | 0 |  | 2 |
| 5 | 药瓶上的名字 | 1869 | short | 91.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周怀远的」×4
  - narration_para_pct 5.6 低于目标 20.0
  - dialogue_run_mean 10.3 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「周怀远的」×9、「沈秋实的」×5、「沈秋实点了点头」×3
  - narration_para_pct 2.9 低于目标 20.0
  - dialogue_run_mean 15.2 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「周怀远的」×6、「沈秋实的」×6
  - narration_para_pct 10.8 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周怀远的」×12、「沈秋实的」×5
  - narration_para_pct 10.4 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「周怀远的」×3
  - narration_para_pct 5.4 低于目标 20.0
  - [observe] attr_adv_pct 30.0 > 20.0（结构塌缩）
  - [observe] 标题重复：「药瓶上的名字」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13527
chapter_chars_mean: 2705
chapter_chars_median: 3213
chapter_chars_cv: 0.36
paragraphs_mean: 54.8
dialogue_chars_pct: 41.8
dialogue_para_pct: 83.9
interiority_para_pct: 8.7
narration_para_pct: 7.4
turn_under20_pct: 70.5
turn_over200_pct: 0.0
attr_say_pct: 21.0
attr_adv_pct: 7.2
scenes_per_chapter: 2.6
dialogue_run_mean: 8.7
turn_len_median: 14
```
