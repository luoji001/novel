# 登录记录 生成报告

slug：`xuanyi-20261019-72`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15022
LLM 调用：68 次，累计 234.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 擦拭主机外壳 | 1899 | short | 95.3 | 0 |  | 0 |
| 2 | 撕碎的账单残片 | 4143 | normal | 89.0 | 0 |  | 4 |
| 3 | 摩挲皱褶的账单 | 3414 | normal | 91.1 | 0 |  | 2 |
| 4 | 摩挲皱褶的账单 | 3647 | normal | 89.8 | 0 |  | 3 |
| 5 | 刮痕背后的秘密 | 1914 | short | 93.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「林志远的」×6、「“我不知道」×5、「陈雪梅的」×4
  - narration_para_pct 10.2 低于目标 20.0
  - dialogue_run_mean 11 高于目标 10.0
  - [observe] 章内自我复读 19 句（如「照片上是一个年轻男人的脸庞，那是很久以前的某个夜…」）
- 第 3 章：
  - 单条套路句式超限：「林志远的」×5、「陈雪梅的」×4、「他知道这」×3
  - narration_para_pct 10.7 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「林志远的」×5
  - narration_para_pct 10.9 低于目标 20.0
  - [observe] 标题重复：「摩挲皱褶的账单」已存在
- 第 5 章：
  - narration_para_pct 13.3 低于目标 20.0
  - [observe] attr_adv_pct 50.0 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 14213
chapter_chars_mean: 2843
chapter_chars_median: 3249
chapter_chars_cv: 0.35
paragraphs_mean: 73
dialogue_chars_pct: 37.7
dialogue_para_pct: 78.3
interiority_para_pct: 6.7
narration_para_pct: 15.0
turn_under20_pct: 81.6
turn_over200_pct: 0.0
attr_say_pct: 29.5
attr_adv_pct: 11.5
scenes_per_chapter: 3.2
dialogue_run_mean: 6.6
turn_len_median: 11
```
