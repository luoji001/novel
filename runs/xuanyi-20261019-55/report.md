# 时光刻度 生成报告

slug：`xuanyi-20261019-55`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14255
LLM 调用：68 次，累计 236.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 开关上的字条 | 1537 | short | 100.0 | 0 |  | 3 |
| 2 | 表盘上的裂痕 | 4110 | normal | 89.2 | 0 |  | 4 |
| 3 | 表盘上的裂痕 | 3336 | normal | 87.4 | 0 |  | 4 |
| 4 | 摩挲存折封面 | 3378 | normal | 89.7 | 0 |  | 2 |
| 5 | 摩挲钢笔外壳 | 1889 | short | 89.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈文远的」×6
  - narration_para_pct 14.7 低于目标 20.0
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×4、「点了点头」×3、「周雪梅的」×3
  - narration_para_pct 12.1 低于目标 20.0
  - [observe] 章内自我复读 9 句（如「周雪梅笑着摇头，“不过，如果你能证明这一点的话，…」）
  - [observe] attr_adv_pct 22.7 > 20.0（结构塌缩）
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈文远的」×5、「点了点头」×3、「他知道这」×3
  - narration_para_pct 12.7 低于目标 20.0
  - [observe] 标题重复：「表盘上的裂痕」已存在
- 第 4 章：
  - 单条套路句式超限：「“我不知道」×3、「点了点头」×3、「他知道这」×3
  - narration_para_pct 9.4 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3、「浦东新区殡仪馆」×3
  - attr_adv_pct 16.7 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13593
chapter_chars_mean: 2719
chapter_chars_median: 3196
chapter_chars_cv: 0.38
paragraphs_mean: 58.8
dialogue_chars_pct: 42.8
dialogue_para_pct: 79.2
interiority_para_pct: 5.9
narration_para_pct: 15.0
turn_under20_pct: 70.1
turn_over200_pct: 0.0
attr_say_pct: 23.8
attr_adv_pct: 14.2
scenes_per_chapter: 3.2
dialogue_run_mean: 5.6
turn_len_median: 13
```
