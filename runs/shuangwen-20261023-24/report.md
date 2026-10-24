# 旧账本 生成报告

slug：`shuangwen-20261023-24`
档位：爽文　闸门模式：observe
章数：10　总字数：20520
LLM 调用：97 次，累计 450.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 灵石入掌 | 1849 | normal | 39.0 | 0 |  | 2 |
| 2 | 翻账本的指尖 | 1960 | normal | 90.8 | 0 |  | 2 |
| 3 | 折账本入掌 | 2537 | normal | 91.5 | 0 |  | 2 |
| 4 | 折账本入掌 | 1768 | normal | 92.3 | 0 |  | 2 |
| 5 | 折账本入掌 | 2124 | normal | 90.5 | 0 |  | 1 |
| 6 | 折账本入掌 | 1724 | normal | 37.4 | 0 |  | 3 |
| 7 | 折账本入掌 | 1833 | normal | 91.6 | 0 |  | 2 |
| 8 | 折账本入掌 | 2194 | normal | 93.6 | 0 |  | 4 |
| 9 | 折账本入掌 | 2122 | normal | 92.8 | 0 |  | 1 |
| 10 | 折账本入掌 | 2399 | long | 92.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李长风的」×5、「说道“我」×3
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 2 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - dialogue_run_mean 16.5 高于目标 14.0
- 第 3 章：
  - 单条套路句式超限：「说道“我」×3
  - attr_adv_pct 25.0 高于目标 12.0
- 第 4 章：
  - attr_adv_pct 15.8 高于目标 12.0
  - [observe] 标题重复：「折账本入掌」已存在
- 第 5 章：
  - [observe] 标题重复：「折账本入掌」已存在
- 第 6 章：
  - 单条套路句式超限：「”林九坚定地说」×3
  - [observe] attr_adv_pct 42.9 > 25.0（结构塌缩）
  - [observe] 标题重复：「折账本入掌」已存在
- 第 7 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 标题重复：「折账本入掌」已存在
- 第 8 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题重复：「折账本入掌」已存在
- 第 9 章：
  - [observe] 标题重复：「折账本入掌」已存在
- 第 10 章：
  - narration_para_pct 3.5 低于目标 5.0
  - [observe] 标题重复：「折账本入掌」已存在

## 整书结构指标

```
chapters: 10
total_chars: 19384
chapter_chars_mean: 1938
chapter_chars_median: 1932
chapter_chars_cv: 0.13
paragraphs_mean: 49.8
dialogue_chars_pct: 47.2
dialogue_para_pct: 83.4
interiority_para_pct: 4.0
narration_para_pct: 12.6
turn_under20_pct: 72.7
turn_over200_pct: 0.0
attr_say_pct: 19.3
attr_adv_pct: 16.1
scenes_per_chapter: 3.2
dialogue_run_mean: 7.6
turn_len_median: 14
```
