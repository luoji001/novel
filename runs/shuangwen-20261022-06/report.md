# 红印 生成报告

slug：`shuangwen-20261022-06`
档位：爽文　闸门模式：observe
章数：10　总字数：19838
LLM 调用：97 次，累计 385.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本的第一页 | 1953 | normal | 99.4 | 0 |  | 3 |
| 2 | 手指摩挲纸边 | 2317 | normal | 92.5 | 0 |  | 1 |
| 3 | 签字笔的较量 | 1950 | normal | 35.1 | 0 |  | 4 |
| 4 | 财务章的重量 | 1849 | normal | 37.8 | 0 |  | 2 |
| 5 | 撕下的账本一角 | 1731 | normal | 92.4 | 0 |  | 0 |
| 6 | 签字笔的较量 | 2093 | normal | 91.5 | 0 |  | 4 |
| 7 | 账本掀开的瞬间 | 1737 | normal | 37.8 | 0 |  | 2 |
| 8 | 摩挲账本边缘的手指 | 1819 | normal | 86.6 | 0 |  | 4 |
| 9 | 印章与账本的对峙 | 1935 | normal | 95.1 | 0 |  | 1 |
| 10 | 签字笔的较量 | 2444 | long | 94.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈国强的」×4
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 13.3 高于目标 12.0
- 第 2 章：
  - narration_para_pct 4.7 低于目标 5.0
- 第 3 章：
  - 单条套路句式超限：「陈国强的」×7
  - narration_para_pct 2.0 低于目标 5.0
  - dialogue_run_mean 48 高于目标 14.0
  - [observe] attr_adv_pct 29.4 > 25.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「陈国强的」×4
  - [observe] attr_adv_pct 44.4 > 25.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「陈国强的」×6
  - narration_para_pct 2.2 低于目标 5.0
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题重复：「签字笔的较量」已存在
- 第 7 章：
  - 单条套路句式超限：「陈国强的」×3
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
- 第 8 章：
  - 单条套路句式超限：「陈国强的」×4
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
  - dialogue_run_mean 42 高于目标 14.0
- 第 9 章：
  - 单条套路句式超限：「县财政局」×5
- 第 10 章：
  - 单条套路句式超限：「县财政局」×7、「林小满的」×6、「陈国强的」×3
  - attr_adv_pct 13.6 高于目标 12.0
  - [observe] 标题重复：「签字笔的较量」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18773
chapter_chars_mean: 1877
chapter_chars_median: 1838
chapter_chars_cv: 0.12
paragraphs_mean: 45.4
dialogue_chars_pct: 52.7
dialogue_para_pct: 88.8
interiority_para_pct: 3.8
narration_para_pct: 7.4
turn_under20_pct: 75.9
turn_over200_pct: 0.0
attr_say_pct: 36.4
attr_adv_pct: 19.5
scenes_per_chapter: 2.2
dialogue_run_mean: 16.5
turn_len_median: 12
```
