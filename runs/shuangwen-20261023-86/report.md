# 药方本背面的批注 生成报告

slug：`shuangwen-20261023-86`
档位：爽文　闸门模式：observe
章数：10　总字数：19388
LLM 调用：97 次，累计 427.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙开启库房门 | 1789 | normal | 39.8 | 0 |  | 2 |
| 2 | 核对清单 | 1968 | normal | 95.9 | 0 |  | 2 |
| 3 | 划破药方本 | 1979 | normal | 37.7 | 0 |  | 3 |
| 4 | 揭开药方本秘密 | 2240 | normal | 93.0 | 0 |  | 1 |
| 5 | 红墨水笔划线 | 1733 | normal | 93.4 | 0 |  | 2 |
| 6 | 记录新配方 | 1830 | normal | 91.2 | 0 |  | 3 |
| 7 | 红墨水笔划线 | 1923 | normal | 91.1 | 0 |  | 3 |
| 8 | 签名笔落 | 1814 | normal | 37.6 | 0 |  | 1 |
| 9 | 红墨水笔划线 | 2070 | normal | 37.3 | 0 |  | 3 |
| 10 | 揭开药方本秘密 | 2032 | long | 37.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈德昌的」×5
  - [observe] attr_adv_pct 60.0 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「陈德昌的」×4
  - attr_adv_pct 20.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「陈德昌的」×6
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 章内自我复读 2 句（如「但我至少可以让自己不再受制于它…」）
- 第 4 章：
  - 单条套路句式超限：「陈德昌的」×4
- 第 5 章：
  - 单条套路句式超限：「林小满的」×4、「带着一丝」×3
  - attr_adv_pct 15.4 高于目标 12.0
- 第 6 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈德昌的」×3
  - attr_adv_pct 15.4 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「陈德昌的」×4、「他知道这」×3、「林小满的」×3
  - attr_adv_pct 23.5 高于目标 12.0
  - [observe] 标题重复：「红墨水笔划线」已存在
- 第 8 章：
  - [observe] attr_adv_pct 35.3 > 25.0（结构塌缩）
- 第 9 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「红墨水笔划线」已存在
- 第 10 章：
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「揭开药方本秘密」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18358
chapter_chars_mean: 1836
chapter_chars_median: 1852
chapter_chars_cv: 0.08
paragraphs_mean: 44.1
dialogue_chars_pct: 41.0
dialogue_para_pct: 79.6
interiority_para_pct: 6.1
narration_para_pct: 14.3
turn_under20_pct: 78.1
turn_over200_pct: 0.0
attr_say_pct: 22.5
attr_adv_pct: 25.0
scenes_per_chapter: 2.3
dialogue_run_mean: 4.8
turn_len_median: 12
```
