# 底款 生成报告

slug：`shuangwen-20261022-118`
档位：爽文　闸门模式：observe
章数：10　总字数：18330
LLM 调用：97 次，累计 412.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 传递编号印章 | 1799 | normal | 99.9 | 0 |  | 1 |
| 2 | 摩挲纸页边缘 | 1662 | normal | 91.9 | 0 |  | 0 |
| 3 | 摩挲纸页边缘 | 1661 | normal | 90.7 | 0 |  | 3 |
| 4 | 摩挲纸页边缘 | 1520 | normal | 92.8 | 0 |  | 3 |
| 5 | 摩挲纸页边缘 | 1928 | normal | 94.2 | 0 |  | 3 |
| 6 | 摩挲纸页边缘 | 1832 | normal | 94.0 | 0 |  | 3 |
| 7 | 摩挲瓷器底款编号 | 1997 | normal | 92.5 | 0 |  | 1 |
| 8 | 摩挲瓷器底款编号 | 1928 | normal | 37.6 | 0 |  | 2 |
| 9 | 摩挲纸页边缘 | 1996 | normal | 92.4 | 0 |  | 3 |
| 10 | 摩挲纸页边缘 | 1997 | long | 91.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 20.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「周振国的」×3
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「摩挲纸页边缘」已存在
- 第 4 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「摩挲纸页边缘」已存在
- 第 5 章：
  - 命中套话收尾句
  - narration_para_pct 2.9 低于目标 5.0
  - [observe] 标题重复：「摩挲纸页边缘」已存在
- 第 6 章：
  - narration_para_pct 2.5 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「摩挲纸页边缘」已存在
- 第 7 章：
  - narration_para_pct 0.0 低于目标 5.0
- 第 8 章：
  - [observe] 章内自我复读 1 句（如「在这场小小的会议上，陈文远终于做出了自己多年的抉…」）
  - [observe] 标题重复：「摩挲瓷器底款编号」已存在
- 第 9 章：
  - 单条套路句式超限：「沈玉兰的」×4
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「摩挲纸页边缘」已存在
- 第 10 章：
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题重复：「摩挲纸页边缘」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17442
chapter_chars_mean: 1744
chapter_chars_median: 1777
chapter_chars_cv: 0.09
paragraphs_mean: 36.7
dialogue_chars_pct: 48.3
dialogue_para_pct: 86.4
interiority_para_pct: 6.4
narration_para_pct: 7.2
turn_under20_pct: 61.7
turn_over200_pct: 0.0
attr_say_pct: 19.3
attr_adv_pct: 12.0
scenes_per_chapter: 1.9
dialogue_run_mean: 7.3
turn_len_median: 16
```
