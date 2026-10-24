# 机油渍 生成报告

slug：`shuangwen-20261023-138`
档位：爽文　闸门模式：observe
章数：10　总字数：18409
LLM 调用：97 次，累计 423.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔的使用权 | 1739 | normal | 99.5 | 0 |  | 0 |
| 2 | 账本复印件的重量 | 1712 | normal | 90.9 | 0 |  | 2 |
| 3 | 账本边缘的机油印 | 1754 | normal | 94.1 | 0 |  | 0 |
| 4 | 签字笔划破纸张 | 1894 | normal | 92.9 | 0 |  | 1 |
| 5 | 手电筒照亮日期 | 1859 | normal | 93.0 | 0 |  | 1 |
| 6 | 机油印的重量 | 1443 | normal | 37.2 | 0 |  | 2 |
| 7 | 机油印的重量 | 1743 | normal | 91.1 | 0 |  | 4 |
| 8 | 机油印的重量 | 1827 | normal | 92.0 | 0 |  | 2 |
| 9 | 账本边缘的机油印 | 2027 | normal | 91.0 | 0 |  | 3 |
| 10 | 账本边缘的机油印 | 2401 | long | 37.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「林小满的」×3
  - narration_para_pct 3.8 低于目标 5.0
- 第 4 章：
  - attr_adv_pct 14.3 高于目标 12.0
- 第 5 章：
  - narration_para_pct 3.4 低于目标 5.0
- 第 6 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 章内自我复读 1 句（如「他知道，这场较量才刚刚开始…」）
- 第 7 章：
  - 单条套路句式超限：「陈国强的」×5、「林小满的」×3
  - narration_para_pct 2.9 低于目标 5.0
  - dialogue_run_mean 16.5 高于目标 14.0
  - [observe] 标题重复：「机油印的重量」已存在
- 第 8 章：
  - 单条套路句式超限：「陈国强的」×7、「林小满的」×3
  - [observe] 标题重复：「机油印的重量」已存在
- 第 9 章：
  - 单条套路句式超限：「陈国强的」×4
  - dialogue_run_mean 17.5 高于目标 14.0
  - [observe] 标题重复：「账本边缘的机油印」已存在
- 第 10 章：
  - 单条套路句式超限：「陈国强的」×3
  - [observe] attr_adv_pct 38.1 > 25.0（结构塌缩）
  - [observe] 标题重复：「账本边缘的机油印」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17494
chapter_chars_mean: 1749
chapter_chars_median: 1698
chapter_chars_cv: 0.14
paragraphs_mean: 37.7
dialogue_chars_pct: 47.1
dialogue_para_pct: 86.5
interiority_para_pct: 5.0
narration_para_pct: 8.6
turn_under20_pct: 69.6
turn_over200_pct: 0.0
attr_say_pct: 25.4
attr_adv_pct: 7.7
scenes_per_chapter: 2.2
dialogue_run_mean: 8.8
turn_len_median: 14
```
