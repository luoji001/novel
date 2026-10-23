# 资格证 生成报告

slug：`shuangwen-20261022-65`
档位：爽文　闸门模式：observe
章数：10　总字数：20031
LLM 调用：97 次，累计 443.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字权的争夺 | 1826 | normal | 99.2 | 0 |  | 2 |
| 2 | 工资单的核对 | 1966 | normal | 91.7 | 0 |  | 1 |
| 3 | 证件的摊开 | 2170 | normal | 37.7 | 0 |  | 2 |
| 4 | 证件的摊开 | 1875 | normal | 90.1 | 0 |  | 2 |
| 5 | 证件的摊开 | 1916 | normal | 91.3 | 0 |  | 5 |
| 6 | 工资单的摊开 | 1864 | normal | 36.6 | 0 |  | 5 |
| 7 | 证件的摊开 | 1988 | normal | 93.4 | 0 |  | 2 |
| 8 | 证件的摊开 | 1940 | normal | 91.6 | 0 |  | 2 |
| 9 | 证件的摊开 | 2000 | normal | 92.5 | 0 |  | 4 |
| 10 | 签字的笔尖落下 | 2476 | long | 93.5 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周振国的」×4、「他知道这」×3
  - attr_adv_pct 15.4 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「带着一丝」×3、「他知道这」×3
- 第 3 章：
  - 单条套路句式超限：「周振国的」×8、「林秋实的」×3
  - [observe] attr_adv_pct 50.0 > 25.0（结构塌缩）
- 第 4 章：
  - dialogue_run_mean 18 高于目标 14.0
  - [observe] 标题重复：「证件的摊开」已存在
- 第 5 章：
  - 单条套路句式超限：「周振国的」×7
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 21 高于目标 14.0
  - [observe] 标题重复：「证件的摊开」已存在
- 第 6 章：
  - 单条套路句式超限：「周振国的」×10
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 16.5 高于目标 14.0
  - [observe] attr_adv_pct 50.0 > 25.0（结构塌缩）
  - [observe] 标题与《工资单的核对》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「周振国的」×7、「林秋实的」×3
  - [observe] 标题重复：「证件的摊开」已存在
- 第 8 章：
  - dialogue_run_mean 18.5 高于目标 14.0
  - [observe] 标题重复：「证件的摊开」已存在
- 第 9 章：
  - 单条套路句式超限：「周振国的」×4
  - narration_para_pct 4.8 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「证件的摊开」已存在

## 整书结构指标

```
chapters: 10
total_chars: 19072
chapter_chars_mean: 1907
chapter_chars_median: 1866
chapter_chars_cv: 0.1
paragraphs_mean: 40.7
dialogue_chars_pct: 52.9
dialogue_para_pct: 88.4
interiority_para_pct: 3.0
narration_para_pct: 8.6
turn_under20_pct: 70.2
turn_over200_pct: 0.0
attr_say_pct: 23.2
attr_adv_pct: 15.3
scenes_per_chapter: 1.9
dialogue_run_mean: 12.1
turn_len_median: 14
```
