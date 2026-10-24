# 欠条 生成报告

slug：`shuangwen-20261023-38`
档位：爽文　闸门模式：observe
章数：10　总字数：18647
LLM 调用：97 次，累计 413.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 机油桶藏身角落 | 1837 | normal | 98.3 | 0 |  | 0 |
| 2 | 账本末页未填部分 | 1914 | normal | 89.1 | 0 |  | 1 |
| 3 | 签字本上的指纹 | 1658 | normal | 95.0 | 0 |  | 0 |
| 4 | 指缝间的欠条 | 1975 | normal | 90.0 | 0 |  | 0 |
| 5 | 欠条背面的指纹 | 1947 | normal | 91.1 | 0 |  | 1 |
| 6 | 欠条背面的指纹 | 1874 | normal | 92.3 | 0 |  | 2 |
| 7 | 签字本上的指纹 | 1864 | normal | 93.4 | 0 |  | 2 |
| 8 | 欠条背面的数字 | 1660 | normal | 37.0 | 0 |  | 2 |
| 9 | 欠条背面的数字 | 1554 | normal | 90.6 | 0 |  | 2 |
| 10 | 欠条背面的数字 | 2354 | long | 92.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - attr_adv_pct 16.7 高于目标 12.0
- 第 5 章：
  - attr_adv_pct 16.7 高于目标 12.0
- 第 6 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「欠条背面的指纹」已存在
- 第 7 章：
  - dialogue_chars_pct 70.1 高于目标 70.0
  - [observe] 标题重复：「签字本上的指纹」已存在
- 第 8 章：
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题与《欠条背面的指纹》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 标题重复：「欠条背面的数字」已存在
- 第 10 章：
  - narration_para_pct 3.6 低于目标 5.0
  - [observe] 标题重复：「欠条背面的数字」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17637
chapter_chars_mean: 1764
chapter_chars_median: 1757
chapter_chars_cv: 0.12
paragraphs_mean: 42.5
dialogue_chars_pct: 50.8
dialogue_para_pct: 84.8
interiority_para_pct: 3.9
narration_para_pct: 11.3
turn_under20_pct: 70.4
turn_over200_pct: 0.0
attr_say_pct: 26.4
attr_adv_pct: 12.1
scenes_per_chapter: 2.4
dialogue_run_mean: 7.5
turn_len_median: 13
```
