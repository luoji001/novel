# 刻痕 生成报告

slug：`shuangwen-20261022-15`
档位：爽文　闸门模式：observe
章数：10　总字数：19400
LLM 调用：97 次，累计 383.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 玉牌上的刻痕 | 1906 | normal | 96.8 | 0 |  | 2 |
| 2 | 玉牌上的刻痕 | 1972 | normal | 91.4 | 0 |  | 2 |
| 3 | 玉牌上的刻痕 | 1740 | normal | 37.3 | 0 |  | 4 |
| 4 | 玉牌显现古老符咒 | 2051 | normal | 37.2 | 0 |  | 2 |
| 5 | 玉牌轻磕桌面 | 1630 | normal | 92.4 | 0 |  | 1 |
| 6 | 玉牌裂痕现古纹 | 1777 | normal | 89.9 | 0 |  | 2 |
| 7 | 玉牌轻磕桌面 | 2044 | normal | 91.9 | 0 |  | 3 |
| 8 | 玉牌轻磕桌面 | 1911 | normal | 91.4 | 0 |  | 3 |
| 9 | 玉牌裂痕现古纹 | 1748 | normal | 89.1 | 0 |  | 4 |
| 10 | 玉牌轻磕桌面 | 2611 | long | 36.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道自己」×3、「李怀远的」×3
  - attr_adv_pct 16.7 高于目标 12.0
- 第 2 章：
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「玉牌上的刻痕」已存在
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李怀远的」×8
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「玉牌上的刻痕」已存在
- 第 4 章：
  - 单条套路句式超限：「验货台」×7
  - [observe] attr_adv_pct 30.4 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「李怀远的」×4
- 第 6 章：
  - 单条套路句式超限：「李怀远的」×6
  - attr_adv_pct 21.4 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「李怀远的」×8
  - attr_adv_pct 21.1 高于目标 12.0
  - [observe] 标题重复：「玉牌轻磕桌面」已存在
- 第 8 章：
  - 单条套路句式超限：「李怀远的」×4
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「玉牌轻磕桌面」已存在
- 第 9 章：
  - narration_para_pct 2.7 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
  - dialogue_run_mean 18 高于目标 14.0
  - [observe] 标题重复：「玉牌裂痕现古纹」已存在
- 第 10 章：
  - 单条套路句式超限：「李怀远的」×8、「青云坊市」×3
  - [observe] 章内自我复读 2 句（如「因为我父亲就是这么教我的…」）
  - [observe] 标题重复：「玉牌轻磕桌面」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18372
chapter_chars_mean: 1837
chapter_chars_median: 1818
chapter_chars_cv: 0.15
paragraphs_mean: 43.7
dialogue_chars_pct: 45.4
dialogue_para_pct: 82.0
interiority_para_pct: 6.4
narration_para_pct: 11.7
turn_under20_pct: 76.7
turn_over200_pct: 0.0
attr_say_pct: 24.8
attr_adv_pct: 19.4
scenes_per_chapter: 1.3
dialogue_run_mean: 6.9
turn_len_median: 13
```
