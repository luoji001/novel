# 焚单 生成报告

slug：`shuangwen-20261023-104`
档位：爽文　闸门模式：observe
章数：10　总字数：19032
LLM 调用：97 次，累计 437.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 掀开泛黄供奉单 | 1644 | normal | 38.8 | 0 |  | 2 |
| 2 | 摊开泛黄供奉单 | 2248 | normal | 91.5 | 0 |  | 3 |
| 3 | 摊开泛黄供奉单 | 1765 | normal | 93.1 | 0 |  | 3 |
| 4 | 签字笔的重量 | 1780 | normal | 94.1 | 0 |  | 1 |
| 5 | 摊开泛黄供奉单 | 1822 | normal | 92.1 | 0 |  | 3 |
| 6 | 摊开泛黄供奉单 | 1733 | normal | 93.0 | 0 |  | 1 |
| 7 | 摊开泛黄供奉单 | 1747 | normal | 94.4 | 0 |  | 2 |
| 8 | 供奉单的重量 | 1689 | normal | 36.5 | 0 |  | 2 |
| 9 | 摊开泛黄供奉单 | 2224 | normal | 37.2 | 0 |  | 3 |
| 10 | 碎纸入掌 | 2370 | long | 93.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「苏怀远的」×4
  - [observe] attr_adv_pct 40.0 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「苏怀远的」×6
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 标题与《掀开泛黄供奉单》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - narration_para_pct 3.1 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「摊开泛黄供奉单」已存在
- 第 4 章：
  - 命中套话收尾句
- 第 5 章：
  - 单条套路句式超限：「点了点头“」×3、「林秋站在」×3
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「摊开泛黄供奉单」已存在
- 第 6 章：
  - [observe] 标题重复：「摊开泛黄供奉单」已存在
- 第 7 章：
  - narration_para_pct 4.4 低于目标 5.0
  - [observe] 标题重复：「摊开泛黄供奉单」已存在
- 第 8 章：
  - 命中套话收尾句
  - [observe] 章内自我复读 1 句（如「所以你不能拿着过去的记录来要求我现在给你好处…」）
- 第 9 章：
  - attr_adv_pct 15.2 高于目标 12.0
  - [observe] 章内自我复读 2 句（如「因为你的供奉期限到了…」）
  - [observe] 标题重复：「摊开泛黄供奉单」已存在
- 第 10 章：
  - 命中套话收尾句
  - 单条套路句式超限：「苏怀远的」×3、「他知道这」×3

## 整书结构指标

```
chapters: 10
total_chars: 18035
chapter_chars_mean: 1804
chapter_chars_median: 1671
chapter_chars_cv: 0.14
paragraphs_mean: 42
dialogue_chars_pct: 45.4
dialogue_para_pct: 82.2
interiority_para_pct: 6.8
narration_para_pct: 11.0
turn_under20_pct: 73.7
turn_over200_pct: 0.0
attr_say_pct: 35.2
attr_adv_pct: 11.8
scenes_per_chapter: 2.6
dialogue_run_mean: 6.9
turn_len_median: 14
```
