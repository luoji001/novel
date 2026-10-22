# 账本 生成报告

slug：`shuangwen-20261022-28`
档位：爽文　闸门模式：observe
章数：10　总字数：20254
LLM 调用：97 次，累计 380.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本上的指纹痕迹 | 1776 | normal | 99.9 | 0 |  | 1 |
| 2 | 账本上的签名框 | 2168 | normal | 37.2 | 0 |  | 3 |
| 3 | 签字笔的重量 | 1706 | normal | 93.5 | 0 |  | 1 |
| 4 | 账本上的签名框 | 1884 | normal | 92.9 | 0 |  | 2 |
| 5 | 账本上的签名框 | 2178 | normal | 93.0 | 0 |  | 3 |
| 6 | 签字笔的重量 | 1717 | normal | 93.3 | 0 |  | 1 |
| 7 | 账本上的签名框 | 1914 | normal | 91.3 | 0 |  | 4 |
| 8 | 账本上的签名框 | 1848 | normal | 93.5 | 0 |  | 2 |
| 9 | 账本上的签名框 | 2767 | normal | 34.8 | 0 |  | 6 |
| 10 | 账本上的签名框 | 2286 | long | 93.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「张局长的」×10
- 第 2 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「你知道这意味着什么吗…」）
- 第 3 章：
  - 命中套话收尾句
- 第 4 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「账本上的签名框」已存在
- 第 5 章：
  - 单条套路句式超限：「张局长的」×5
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「账本上的签名框」已存在
- 第 6 章：
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 7 章：
  - 单条套路句式超限：「王小满的」×3
  - narration_para_pct 3.0 低于目标 5.0
  - attr_adv_pct 18.8 高于目标 12.0
  - [observe] 标题重复：「账本上的签名框」已存在
- 第 8 章：
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题重复：「账本上的签名框」已存在
- 第 9 章：
  - 单条套路句式超限：「张局长的」×3
  - 情节与已写章节重复 0.86 ≥ 0.7（撞上「王小满拿出父亲遗留的账本，揭露张局长多年前以他人名义借款…」）
  - narration_para_pct 4.9 低于目标 5.0
  - dialogue_run_mean 19.2 高于目标 14.0
  - [observe] 章内自我复读 2 句（如「那你觉得自己还有能力还多少？…」）
  - [observe] 标题重复：「账本上的签名框」已存在
- 第 10 章：
  - 单条套路句式超限：「张局长的」×5
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「账本上的签名框」已存在

## 整书结构指标

```
chapters: 10
total_chars: 19166
chapter_chars_mean: 1917
chapter_chars_median: 1806
chapter_chars_cv: 0.16
paragraphs_mean: 46.3
dialogue_chars_pct: 49.5
dialogue_para_pct: 83.4
interiority_para_pct: 5.2
narration_para_pct: 11.4
turn_under20_pct: 77.2
turn_over200_pct: 0.0
attr_say_pct: 35.6
attr_adv_pct: 11.3
scenes_per_chapter: 1.6
dialogue_run_mean: 6.8
turn_len_median: 13
```
