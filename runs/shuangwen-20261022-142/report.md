# 一本名册 生成报告

slug：`shuangwen-20261022-142`
档位：爽文　闸门模式：observe
章数：10　总字数：19096
LLM 调用：97 次，累计 414.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一张客户名单 | 1774 | normal | 99.8 | 0 |  | 0 |
| 2 | 签字笔 | 2019 | normal | 93.1 | 0 |  | 1 |
| 3 | 签字笔 | 1890 | normal | 94.0 | 0 |  | 1 |
| 4 | 推名单 | 1858 | normal | 36.9 | 0 |  | 1 |
| 5 | 推名单 | 2001 | normal | 94.5 | 0 |  | 3 |
| 6 | 推名单 | 1910 | normal | 94.0 | 0 |  | 1 |
| 7 | 推名单 | 1540 | normal | 91.3 | 0 |  | 2 |
| 8 | 推名单 | 2070 | normal | 91.8 | 0 |  | 4 |
| 9 | 推名单 | 1675 | normal | 94.1 | 0 |  | 2 |
| 10 | 推名单 | 2349 | long | 37.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - attr_adv_pct 18.2 高于目标 12.0
- 第 3 章：
  - [observe] 标题重复：「签字笔」已存在
- 第 4 章：
  - [observe] attr_adv_pct 42.9 > 25.0（结构塌缩）
- 第 5 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「推名单」已存在
- 第 6 章：
  - [observe] 标题重复：「推名单」已存在
- 第 7 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「推名单」已存在
- 第 8 章：
  - 命中套话收尾句
  - narration_para_pct 2.4 低于目标 5.0
  - dialogue_run_mean 20 高于目标 14.0
  - [observe] 标题重复：「推名单」已存在
- 第 9 章：
  - narration_para_pct 3.3 低于目标 5.0
  - [observe] 标题重复：「推名单」已存在
- 第 10 章：
  - narration_para_pct 3.8 低于目标 5.0
  - [observe] 章内自我复读 2 句（如「我知道，但我相信，只有这样，才能真正改变我们公司…」）
  - [observe] 标题重复：「推名单」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18233
chapter_chars_mean: 1823
chapter_chars_median: 1815
chapter_chars_cv: 0.12
paragraphs_mean: 36.7
dialogue_chars_pct: 53.2
dialogue_para_pct: 86.1
interiority_para_pct: 6.9
narration_para_pct: 7.0
turn_under20_pct: 60.0
turn_over200_pct: 0.0
attr_say_pct: 22.1
attr_adv_pct: 12.7
scenes_per_chapter: 1.9
dialogue_run_mean: 9.3
turn_len_median: 17
```
