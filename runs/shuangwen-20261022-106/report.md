# 欠条 生成报告

slug：`shuangwen-20261022-106`
档位：爽文　闸门模式：observe
章数：10　总字数：18344
LLM 调用：97 次，累计 432.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本被拍在桌上 | 2288 | normal | 98.8 | 0 |  | 2 |
| 2 | 欠条在手中颤抖 | 1858 | normal | 92.2 | 0 |  | 0 |
| 3 | 结算表被拍在桌上 | 1888 | normal | 93.7 | 0 |  | 3 |
| 4 | 签字权被推至桌面 | 1902 | normal | 36.6 | 0 |  | 2 |
| 5 | 欠条被推至桌面 | 1521 | normal | 91.1 | 0 |  | 2 |
| 6 | 欠条被推至桌面 | 1911 | normal | 92.9 | 0 |  | 3 |
| 7 | 欠条被推至桌面 | 1426 | normal | 92.7 | 0 |  | 2 |
| 8 | 欠条被推至桌面 | 1754 | normal | 92.6 | 0 |  | 1 |
| 9 | 欠条被推至桌面 | 1679 | normal | 93.9 | 0 |  | 2 |
| 10 | 欠条被推至桌面 | 2107 | long | 94.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林小满的」×4
  - attr_adv_pct 23.1 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「陈国强的」×4
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题与《账本被拍在桌上》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「林小满的」×5
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 5 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题与《签字权被推至桌面》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「林小满的」×3
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 标题重复：「欠条被推至桌面」已存在
- 第 7 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「欠条被推至桌面」已存在
- 第 8 章：
  - [observe] 标题重复：「欠条被推至桌面」已存在
- 第 9 章：
  - 单条套路句式超限：「陈国强的」×4、「林小满的」×4
  - [observe] 标题重复：「欠条被推至桌面」已存在
- 第 10 章：
  - [observe] 标题重复：「欠条被推至桌面」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17357
chapter_chars_mean: 1736
chapter_chars_median: 1770
chapter_chars_cv: 0.14
paragraphs_mean: 41.3
dialogue_chars_pct: 48.1
dialogue_para_pct: 79.9
interiority_para_pct: 5.9
narration_para_pct: 14.3
turn_under20_pct: 70.8
turn_over200_pct: 0.0
attr_say_pct: 28.2
attr_adv_pct: 13.8
scenes_per_chapter: 2
dialogue_run_mean: 5.8
turn_len_median: 14
```
