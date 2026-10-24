# 签单 生成报告

slug：`shuangwen-20261023-97`
档位：爽文　闸门模式：observe
章数：10　总字数：19617
LLM 调用：97 次，累计 423.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲纸缘 | 1756 | normal | 100.0 | 0 |  | 2 |
| 2 | 文件夹较量 | 1977 | normal | 86.2 | 0 |  | 4 |
| 3 | 摩挲纸缘 | 1738 | normal | 36.7 | 0 |  | 4 |
| 4 | 争夺请假条 | 2005 | normal | 90.7 | 0 |  | 1 |
| 5 | 摩挲纸缘 | 1863 | normal | 92.6 | 0 |  | 3 |
| 6 | 摩挲纸缘 | 1845 | normal | 93.8 | 0 |  | 2 |
| 7 | 摩挲纸缘 | 1848 | normal | 92.5 | 0 |  | 3 |
| 8 | 摩挲纸缘 | 1823 | normal | 94.0 | 0 |  | 2 |
| 9 | 摩挲纸缘 | 2203 | normal | 37.3 | 0 |  | 4 |
| 10 | 摩挲纸缘 | 2549 | long | 37.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈国强的」×4
  - attr_adv_pct 16.7 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「陈国强的」×3、「微微一笑」×3
  - narration_para_pct 2.4 低于目标 5.0
  - attr_adv_pct 13.6 高于目标 12.0
  - dialogue_run_mean 41 高于目标 14.0
- 第 3 章：
  - 单条套路句式超限：「林婉秋的」×3
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「因为我的学生都在这儿…」）
  - [observe] 标题重复：「摩挲纸缘」已存在
- 第 4 章：
  - 单条套路句式超限：「陈国强的」×4
- 第 5 章：
  - 单条套路句式超限：「陈国强的」×5
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题重复：「摩挲纸缘」已存在
- 第 6 章：
  - 单条套路句式超限：「陈国强的」×6
  - [observe] 标题重复：「摩挲纸缘」已存在
- 第 7 章：
  - 单条套路句式超限：「陈国强的」×4
  - dialogue_run_mean 16 高于目标 14.0
  - [observe] 标题重复：「摩挲纸缘」已存在
- 第 8 章：
  - 命中套话收尾句
  - [observe] 标题重复：「摩挲纸缘」已存在
- 第 9 章：
  - 单条套路句式超限：「林婉秋的」×3
  - dialogue_run_mean 15.3 高于目标 14.0
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「摩挲纸缘」已存在
- 第 10 章：
  - 单条套路句式超限：「陈国强的」×5
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「摩挲纸缘」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18662
chapter_chars_mean: 1866
chapter_chars_median: 1774
chapter_chars_cv: 0.13
paragraphs_mean: 41.1
dialogue_chars_pct: 51.5
dialogue_para_pct: 86.1
interiority_para_pct: 4.3
narration_para_pct: 9.6
turn_under20_pct: 69.3
turn_over200_pct: 0.0
attr_say_pct: 24.1
attr_adv_pct: 17.6
scenes_per_chapter: 1.9
dialogue_run_mean: 11.1
turn_len_median: 14
```
