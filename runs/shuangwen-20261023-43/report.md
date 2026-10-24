# 旧合同 生成报告

slug：`shuangwen-20261023-43`
档位：爽文　闸门模式：observe
章数：10　总字数：20725
LLM 调用：97 次，累计 438.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 合同上的签字日期 | 1988 | normal | 98.8 | 0 |  | 1 |
| 2 | 合同上的折痕 | 2023 | normal | 91.9 | 0 |  | 2 |
| 3 | 签字日期的对决 | 1899 | normal | 86.7 | 0 |  | 3 |
| 4 | 印章与旧合同的对峙 | 2258 | normal | 89.7 | 0 |  | 1 |
| 5 | 签名的手指 | 1992 | normal | 93.6 | 0 |  | 2 |
| 6 | 签字日期的较量 | 1845 | normal | 36.5 | 0 |  | 4 |
| 7 | 签字日期的较量 | 1950 | normal | 36.8 | 0 |  | 3 |
| 8 | 签字日期的对决 | 2019 | normal | 91.9 | 0 |  | 3 |
| 9 | 签字日期的对决 | 1931 | normal | 91.4 | 0 |  | 3 |
| 10 | 签字日期的较量 | 2810 | long | 91.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周振华的」×6
- 第 2 章：
  - 单条套路句式超限：「周振华的」×6、「陈志远的」×3
  - attr_adv_pct 19.0 高于目标 12.0
- 第 3 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
  - dialogue_run_mean 43 高于目标 14.0
- 第 4 章：
  - 单条套路句式超限：「周振华的」×3
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周振华的」×7
- 第 6 章：
  - 单条套路句式超限：「周振华的」×4
  - narration_para_pct 3.0 低于目标 5.0
  - [observe] attr_adv_pct 36.4 > 25.0（结构塌缩）
  - [observe] 标题与《签字日期的对决》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「周振华的」×5
  - [observe] attr_adv_pct 46.7 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字日期的较量」已存在
- 第 8 章：
  - 单条套路句式超限：「周振华的」×7
  - attr_adv_pct 13.2 高于目标 12.0
  - [observe] 标题重复：「签字日期的对决」已存在
- 第 9 章：
  - 单条套路句式超限：「周振华的」×6
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题重复：「签字日期的对决」已存在
- 第 10 章：
  - 单条套路句式超限：「周振华的」×4、「说道“我」×3
  - [observe] 标题重复：「签字日期的较量」已存在

## 整书结构指标

```
chapters: 10
total_chars: 19575
chapter_chars_mean: 1958
chapter_chars_median: 1874
chapter_chars_cv: 0.14
paragraphs_mean: 49.5
dialogue_chars_pct: 51.3
dialogue_para_pct: 84.8
interiority_para_pct: 5.8
narration_para_pct: 9.5
turn_under20_pct: 73.1
turn_over200_pct: 0.0
attr_say_pct: 35.9
attr_adv_pct: 19.2
scenes_per_chapter: 2.6
dialogue_run_mean: 10.5
turn_len_median: 12
```
