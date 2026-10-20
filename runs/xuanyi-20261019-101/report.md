# 底片 生成报告

slug：`xuanyi-20261019-101`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14393
LLM 调用：68 次，累计 233.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 触摸照片边缘 | 1704 | short | 97.9 | 0 |  | 1 |
| 2 | 触摸照片边缘 | 3465 | normal | 88.7 | 0 |  | 3 |
| 3 | 触摸照片边缘 | 3423 | normal | 89.6 | 0 |  | 4 |
| 4 | 触摸照片边缘 | 3813 | normal | 87.9 | 0 |  | 4 |
| 5 | 触摸照片边缘 | 1983 | short | 91.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 28.6 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「周玉兰的」×9、「沈国强的」×3
  - narration_para_pct 14.9 低于目标 20.0
  - [observe] 标题重复：「触摸照片边缘」已存在
- 第 3 章：
  - 单条套路句式超限：「周玉兰的」×9
  - narration_para_pct 19.3 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
  - [observe] 标题重复：「触摸照片边缘」已存在
- 第 4 章：
  - 单条套路句式超限：「周玉兰的」×10、「沈国强的」×5
  - narration_para_pct 19.5 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「图片上是一个小男孩，大概六七岁的模样，正坐在照相…」）
  - [observe] 标题重复：「触摸照片边缘」已存在
- 第 5 章：
  - 单条套路句式超限：「“我不知道」×3
  - narration_para_pct 12.5 低于目标 20.0
  - [observe] 标题重复：「触摸照片边缘」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13718
chapter_chars_mean: 2744
chapter_chars_median: 3295
chapter_chars_cv: 0.34
paragraphs_mean: 58.4
dialogue_chars_pct: 33.5
dialogue_para_pct: 72.0
interiority_para_pct: 10.6
narration_para_pct: 17.5
turn_under20_pct: 79.4
turn_over200_pct: 0.0
attr_say_pct: 27.7
attr_adv_pct: 7.1
scenes_per_chapter: 3.2
dialogue_run_mean: 4.5
turn_len_median: 12
```
