# 盖章 生成报告

slug：`shuangwen-20261023-35`
档位：爽文　闸门模式：observe
章数：10　总字数：18641
LLM 调用：97 次，累计 410.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔的最后一页 | 1540 | normal | 99.6 | 0 |  | 1 |
| 2 | 签字笔的最后一页 | 2499 | normal | 37.3 | 0 |  | 3 |
| 3 | 签字笔的最后一页 | 1834 | normal | 37.3 | 0 |  | 3 |
| 4 | 签字笔的最后一页 | 1853 | normal | 92.7 | 0 |  | 3 |
| 5 | 签字笔的最后一页 | 1770 | normal | 90.9 | 0 |  | 3 |
| 6 | 签字笔的最后一页 | 1929 | normal | 87.5 | 0 |  | 5 |
| 7 | 签字笔的最后一页 | 1721 | normal | 93.2 | 0 |  | 2 |
| 8 | 签字笔的最后一页 | 1626 | normal | 37.1 | 0 |  | 4 |
| 9 | 签字笔的较量 | 1650 | normal | 94.0 | 0 |  | 1 |
| 10 | 签字笔的最后一页 | 2209 | long | 93.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
- 第 2 章：
  - 单条套路句式超限：「李国强的」×3
  - [observe] attr_adv_pct 26.7 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔的最后一页」已存在
- 第 3 章：
  - 单条套路句式超限：「李国强的」×3
  - [observe] attr_adv_pct 44.4 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔的最后一页」已存在
- 第 4 章：
  - narration_para_pct 2.9 低于目标 5.0
  - dialogue_run_mean 17 高于目标 14.0
  - [observe] 标题重复：「签字笔的最后一页」已存在
- 第 5 章：
  - 单条套路句式超限：「李国强的」×5
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「签字笔的最后一页」已存在
- 第 6 章：
  - 情节与已写章节重复 0.91 ≥ 0.7（撞上「张磊发现并拿出内部审计报告揭露李国强虚报采购价格的问题，…」）
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 15.0 高于目标 12.0
  - dialogue_run_mean 44 高于目标 14.0
  - [observe] 标题重复：「签字笔的最后一页」已存在
- 第 7 章：
  - 单条套路句式超限：「李国强的」×3
  - [observe] 标题重复：「签字笔的最后一页」已存在
- 第 8 章：
  - 单条套路句式超限：「李国强的」×3、「他知道这」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「好吧，我陪你去做一次审查…」）
  - [observe] 标题重复：「签字笔的最后一页」已存在
- 第 9 章：
  - narration_para_pct 3.3 低于目标 5.0
- 第 10 章：
  - 单条套路句式超限：「李国强的」×5
  - [observe] 标题重复：「签字笔的最后一页」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17712
chapter_chars_mean: 1771
chapter_chars_median: 1724
chapter_chars_cv: 0.16
paragraphs_mean: 38.1
dialogue_chars_pct: 51.8
dialogue_para_pct: 85.6
interiority_para_pct: 3.2
narration_para_pct: 11.2
turn_under20_pct: 68.4
turn_over200_pct: 0.0
attr_say_pct: 31.0
attr_adv_pct: 13.8
scenes_per_chapter: 1.5
dialogue_run_mean: 10.7
turn_len_median: 13
```
