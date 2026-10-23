# 旧账本 生成报告

slug：`shuangwen-20261022-84`
档位：爽文　闸门模式：observe
章数：10　总字数：18891
LLM 调用：97 次，累计 434.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本揭开尘封往事 | 1779 | normal | 97.4 | 0 |  | 1 |
| 2 | 账本撕裂的瞬间 | 1657 | normal | 92.4 | 0 |  | 2 |
| 3 | 旧房产证的亮相 | 1850 | normal | 36.6 | 0 |  | 2 |
| 4 | 登记簿的质疑 | 1887 | normal | 37.3 | 0 |  | 2 |
| 5 | 账本砸落桌面 | 2316 | normal | 93.4 | 0 |  | 2 |
| 6 | 签字笔的震颤 | 1753 | normal | 93.0 | 0 |  | 1 |
| 7 | 账本撕裂的瞬间 | 1714 | normal | 92.4 | 0 |  | 4 |
| 8 | 账本砸落桌面 | 1781 | normal | 93.3 | 0 |  | 2 |
| 9 | 账本掀开尘封往事 | 1770 | normal | 92.7 | 0 |  | 2 |
| 10 | 账本摊开的瞬间 | 2374 | long | 93.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×7、「林小满的」×3
- 第 2 章：
  - 单条套路句式超限：「李建国的」×4
  - attr_adv_pct 12.5 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「李建国的」×3
  - [observe] attr_adv_pct 26.7 > 25.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「街道办事处」×3
  - [observe] attr_adv_pct 44.4 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「李建国的」×4
  - attr_adv_pct 25.0 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「李建国的」×5
- 第 7 章：
  - 单条套路句式超限：「李建国的」×6
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「账本撕裂的瞬间」已存在
- 第 8 章：
  - narration_para_pct 4.0 低于目标 5.0
  - [observe] 标题重复：「账本砸落桌面」已存在
- 第 9 章：
  - 单条套路句式超限：「李建国的」×4、「林小满的」×3
  - [observe] 标题与《账本揭开尘封往事》近似 0.88 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题与《账本撕裂的瞬间》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 17997
chapter_chars_mean: 1800
chapter_chars_median: 1696
chapter_chars_cv: 0.14
paragraphs_mean: 36.8
dialogue_chars_pct: 46.7
dialogue_para_pct: 84.6
interiority_para_pct: 7.2
narration_para_pct: 8.2
turn_under20_pct: 64.6
turn_over200_pct: 0.0
attr_say_pct: 21.1
attr_adv_pct: 17.1
scenes_per_chapter: 1.4
dialogue_run_mean: 6.2
turn_len_median: 16
```
