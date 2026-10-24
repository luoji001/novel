# 旧工牌 生成报告

slug：`shuangwen-20261023-110`
档位：爽文　闸门模式：observe
章数：10　总字数：18226
LLM 调用：97 次，累计 415.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 登记簿上的名字 | 1557 | normal | 97.0 | 0 |  | 0 |
| 2 | 旧工牌被反复端详 | 2303 | normal | 94.5 | 0 |  | 0 |
| 3 | 旧工牌被反复端详 | 1540 | normal | 94.1 | 0 |  | 1 |
| 4 | 旧工牌被反复端详 | 1993 | normal | 93.3 | 0 |  | 2 |
| 5 | 旧工牌被反复端详 | 1688 | normal | 92.9 | 0 |  | 1 |
| 6 | 旧工牌被反复端详 | 1864 | normal | 93.5 | 0 |  | 1 |
| 7 | 旧工牌被反复端详 | 1467 | normal | 93.3 | 0 |  | 1 |
| 8 | 旧工牌碎屑中的编号 | 1887 | normal | 91.6 | 0 |  | 1 |
| 9 | 旧工牌被反复端详 | 1805 | normal | 37.1 | 0 |  | 3 |
| 10 | 旧工牌被反复端详 | 2112 | long | 92.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - [observe] 标题重复：「旧工牌被反复端详」已存在
- 第 4 章：
  - attr_adv_pct 15.0 高于目标 12.0
  - [observe] 标题重复：「旧工牌被反复端详」已存在
- 第 5 章：
  - [observe] 标题重复：「旧工牌被反复端详」已存在
- 第 6 章：
  - [observe] 标题重复：「旧工牌被反复端详」已存在
- 第 7 章：
  - [observe] 标题重复：「旧工牌被反复端详」已存在
- 第 8 章：
  - 单条套路句式超限：「张德强的」×3
- 第 9 章：
  - 单条套路句式超限：「张德强的」×4
  - [observe] 章内自我复读 2 句（如「我不需要别人替我做决定，只需要确认一件事——我已…」）
  - [observe] 标题重复：「旧工牌被反复端详」已存在
- 第 10 章：
  - [observe] 标题重复：「旧工牌被反复端详」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17170
chapter_chars_mean: 1717
chapter_chars_median: 1742
chapter_chars_cv: 0.15
paragraphs_mean: 44.3
dialogue_chars_pct: 50.1
dialogue_para_pct: 85.0
interiority_para_pct: 4.3
narration_para_pct: 10.7
turn_under20_pct: 77.0
turn_over200_pct: 0.0
attr_say_pct: 41.9
attr_adv_pct: 4.6
scenes_per_chapter: 1.9
dialogue_run_mean: 6.9
turn_len_median: 12
```
