# 手表 生成报告

slug：`xuanyi-20261019-15`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14536
LLM 调用：68 次，累计 240.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 表冠转动时刻度 | 1902 | short | 94.2 | 0 |  | 1 |
| 2 | 存折上的密码 | 3796 | normal | 90.0 | 0 |  | 2 |
| 3 | 怀表与钟楼 | 3469 | normal | 88.0 | 0 |  | 3 |
| 4 | 表盘上的X-987 | 3156 | normal | 88.9 | 0 |  | 3 |
| 5 | 表盘上的X-987 | 2208 | short | 91.7 | 0 |  | 6 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 16.7 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周正阳的」×6、「他知道这」×3
  - narration_para_pct 9.3 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「“我不知道」×5、「为什么会」×5、「”林婉如轻」×4
  - narration_para_pct 9.1 低于目标 20.0
  - attr_adv_pct 16.3 高于目标 10.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×6、「“我不知道」×5、「不仅仅是」×3
  - narration_para_pct 6.8 低于目标 20.0
- 第 5 章：
  - 命中套话收尾句
  - 情节与已写章节重复 0.63 ≥ 0.62（撞上「陈师傅在冷藏室发现一具遗体手腕上的异常机械表，表盘显示1…」）
  - narration_para_pct 15.2 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「1987年12月1日…」）
  - [observe] 标题重复：「表盘上的X-987」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13859
chapter_chars_mean: 2772
chapter_chars_median: 3021
chapter_chars_cv: 0.28
paragraphs_mean: 59.6
dialogue_chars_pct: 42.6
dialogue_para_pct: 80.0
interiority_para_pct: 9.4
narration_para_pct: 10.6
turn_under20_pct: 75.7
turn_over200_pct: 0.0
attr_say_pct: 25.3
attr_adv_pct: 8.0
scenes_per_chapter: 4
dialogue_run_mean: 6.1
turn_len_median: 12
```
