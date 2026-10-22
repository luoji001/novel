# 房产证 生成报告

slug：`shuangwen-20261022-04`
档位：爽文　闸门模式：observe
章数：10　总字数：20069
LLM 调用：97 次，累计 454.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕碎的旧房产证 | 1795 | normal | 100.0 | 0 |  | 1 |
| 2 | 房产证在阳光下颤动 | 2113 | normal | 91.8 | 0 |  | 2 |
| 3 | 房产证在阳光下颤动 | 1889 | normal | 91.2 | 0 |  | 5 |
| 4 | 签字笔悬在纸面 | 1791 | normal | 90.0 | 0 |  | 0 |
| 5 | 签字笔悬在纸面 | 1922 | normal | 36.9 | 0 |  | 3 |
| 6 | 签字笔悬在纸面 | 2260 | normal | 91.2 | 0 |  | 1 |
| 7 | 房产证在阳光下颤动 | 1919 | normal | 92.5 | 0 |  | 2 |
| 8 | 房产证在铁盒中颤抖 | 1817 | normal | 37.4 | 0 |  | 4 |
| 9 | 房产证被扔在地上 | 1561 | normal | 90.1 | 0 |  | 3 |
| 10 | 签字笔悬在纸面 | 2992 | long | 91.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「王建国的」×3
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李国强的」×4、「王建国的」×4、「他知道这」×3
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李国强的」×4
  - narration_para_pct 4.9 低于目标 5.0
  - attr_adv_pct 17.4 高于目标 12.0
  - [observe] 标题重复：「房产证在阳光下颤动」已存在
- 第 5 章：
  - 单条套路句式超限：「李国强的」×5
  - [observe] attr_adv_pct 36.4 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔悬在纸面」已存在
- 第 6 章：
  - [observe] 标题重复：「签字笔悬在纸面」已存在
- 第 7 章：
  - 单条套路句式超限：「王建国的」×3
  - [observe] 标题重复：「房产证在阳光下颤动」已存在
- 第 8 章：
  - 单条套路句式超限：「王建国的」×4
  - narration_para_pct 4.2 低于目标 5.0
  - dialogue_run_mean 15 高于目标 14.0
  - [observe] attr_adv_pct 29.2 > 25.0（结构塌缩）
- 第 9 章：
  - 单条套路句式超限：「王建国的」×5
  - narration_para_pct 3.2 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「他知道这」×3、「王建国的」×3
  - [observe] 标题重复：「签字笔悬在纸面」已存在

## 整书结构指标

```
chapters: 10
total_chars: 19079
chapter_chars_mean: 1908
chapter_chars_median: 1804
chapter_chars_cv: 0.2
paragraphs_mean: 41
dialogue_chars_pct: 44.5
dialogue_para_pct: 83.5
interiority_para_pct: 6.2
narration_para_pct: 10.4
turn_under20_pct: 64.6
turn_over200_pct: 0.0
attr_say_pct: 26.0
attr_adv_pct: 11.5
scenes_per_chapter: 1.5
dialogue_run_mean: 7.5
turn_len_median: 16
```
