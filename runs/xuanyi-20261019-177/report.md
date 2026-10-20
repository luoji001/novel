# 双扫 生成报告

slug：`xuanyi-20261019-177`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14124
LLM 调用：68 次，累计 227.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扫描枪重复读数 | 1675 | short | 86.7 | 0 |  | 1 |
| 2 | 扫描枪误读编号牌 | 3740 | normal | 91.0 | 0 |  | 4 |
| 3 | 扫描枪误读编号牌 | 3446 | normal | 88.0 | 0 |  | 5 |
| 4 | 扫描枪误读编号牌 | 3526 | normal | 87.3 | 0 |  | 5 |
| 5 | 扫描枪误读编号牌 | 1732 | short | 92.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 11.5 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周雪梅的」×5、「为什么会」×3
  - narration_para_pct 8.6 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「那你为什么不告诉别人？…」）
  - [observe] attr_adv_pct 26.1 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「陈启明的」×5、「为什么会」×3
  - narration_para_pct 6.3 低于目标 20.0
  - dialogue_run_mean 14.2 高于目标 10.0
  - [observe] 与历史章节逐字重复 3 句（如「他知道，这件事远比表面看起来复杂得多…」）
  - [observe] 标题重复：「扫描枪误读编号牌」已存在
- 第 4 章：
  - 单条套路句式超限：「周雪梅的」×4、「“我不知道」×3
  - dialogue_chars_pct 62.0 高于目标 58.0
  - narration_para_pct 1.4 低于目标 20.0
  - dialogue_run_mean 16 高于目标 10.0
  - [observe] 标题重复：「扫描枪误读编号牌」已存在
- 第 5 章：
  - narration_para_pct 9.5 低于目标 20.0
  - [observe] 标题重复：「扫描枪误读编号牌」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13430
chapter_chars_mean: 2686
chapter_chars_median: 3272
chapter_chars_cv: 0.36
paragraphs_mean: 61
dialogue_chars_pct: 49.2
dialogue_para_pct: 84.3
interiority_para_pct: 6.0
narration_para_pct: 9.7
turn_under20_pct: 71.5
turn_over200_pct: 0.0
attr_say_pct: 28.6
attr_adv_pct: 9.2
scenes_per_chapter: 2
dialogue_run_mean: 9.4
turn_len_median: 13
```
