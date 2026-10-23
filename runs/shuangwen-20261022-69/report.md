# 账本 生成报告

slug：`shuangwen-20261022-69`
档位：爽文　闸门模式：observe
章数：10　总字数：18470
LLM 调用：97 次，累计 427.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕碎的纸片 | 1472 | normal | 98.4 | 0 |  | 0 |
| 2 | 签字的钢笔 | 2286 | normal | 94.3 | 0 |  | 1 |
| 3 | 签到的账本 | 1912 | normal | 91.1 | 0 |  | 0 |
| 4 | 指认的日期 | 1742 | normal | 95.0 | 0 |  | 0 |
| 5 | 账本上的订金收据 | 1964 | normal | 37.0 | 0 |  | 1 |
| 6 | 钢笔划破合同 | 1674 | normal | 36.1 | 0 |  | 1 |
| 7 | 账本上的订金收据 | 1761 | normal | 37.6 | 0 |  | 2 |
| 8 | 账本上的订金收据 | 1634 | normal | 37.2 | 0 |  | 4 |
| 9 | 账本上的订金收据 | 1606 | normal | 37.1 | 0 |  | 3 |
| 10 | 账本上的订金收据 | 2409 | long | 93.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - attr_adv_pct 16.0 高于目标 12.0
- 第 5 章：
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
- 第 6 章：
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 7 章：
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「账本上的订金收据」已存在
- 第 8 章：
  - 单条套路句式超限：「带着一丝」×3
  - narration_para_pct 0.0 低于目标 5.0
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
  - [observe] 标题重复：「账本上的订金收据」已存在
- 第 9 章：
  - narration_para_pct 3.7 低于目标 5.0
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
  - [observe] 标题重复：「账本上的订金收据」已存在
- 第 10 章：
  - 单条套路句式超限：「市文化局」×3
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 标题重复：「账本上的订金收据」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17628
chapter_chars_mean: 1763
chapter_chars_median: 1652
chapter_chars_cv: 0.16
paragraphs_mean: 34.3
dialogue_chars_pct: 44.0
dialogue_para_pct: 82.1
interiority_para_pct: 9.4
narration_para_pct: 8.4
turn_under20_pct: 61.1
turn_over200_pct: 0.0
attr_say_pct: 19.5
attr_adv_pct: 18.7
scenes_per_chapter: 1.9
dialogue_run_mean: 5.7
turn_len_median: 17
```
