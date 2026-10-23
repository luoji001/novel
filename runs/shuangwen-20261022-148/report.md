# 旧账本页码 生成报告

slug：`shuangwen-20261022-148`
档位：爽文　闸门模式：observe
章数：10　总字数：19409
LLM 调用：97 次，累计 454.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 拨动地钉密码 | 1790 | normal | 99.0 | 0 |  | 1 |
| 2 | 翻动旧账本页码 | 1848 | normal | 92.8 | 0 |  | 3 |
| 3 | 翻动旧账本页码 | 2065 | normal | 93.0 | 0 |  | 3 |
| 4 | 翻动账本页码 | 1901 | normal | 94.9 | 0 |  | 3 |
| 5 | 翻动账本页码 | 1836 | normal | 35.0 | 0 |  | 5 |
| 6 | 翻动账本页码 | 1748 | normal | 94.4 | 0 |  | 2 |
| 7 | 翻动账本页码 | 1891 | normal | 91.5 | 0 |  | 4 |
| 8 | 翻动账本页码 | 1821 | normal | 92.8 | 0 |  | 3 |
| 9 | 翻动账本页码 | 1965 | normal | 93.5 | 0 |  | 2 |
| 10 | 翻动账本页码 | 2534 | long | 93.8 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 3.4 低于目标 5.0
- 第 2 章：
  - 单条套路句式超限：「李国强的」×3、「林小满的」×3
  - narration_para_pct 4.8 低于目标 5.0
  - attr_adv_pct 15.4 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「李国强的」×7
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「翻动旧账本页码」已存在
- 第 4 章：
  - 单条套路句式超限：「县革委会」×4
  - attr_adv_pct 18.5 高于目标 12.0
  - [observe] 标题与《翻动旧账本页码》近似 0.92 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「李国强的」×3
  - narration_para_pct 2.6 低于目标 5.0
  - dialogue_run_mean 38 高于目标 14.0
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「翻动账本页码」已存在
- 第 6 章：
  - 单条套路句式超限：「林小满的」×6
  - [observe] 标题重复：「翻动账本页码」已存在
- 第 7 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李国强的」×5
  - attr_adv_pct 18.8 高于目标 12.0
  - [observe] 标题重复：「翻动账本页码」已存在
- 第 8 章：
  - 单条套路句式超限：「点了点头」×3
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「翻动账本页码」已存在
- 第 9 章：
  - narration_para_pct 4.7 低于目标 5.0
  - [observe] 标题重复：「翻动账本页码」已存在
- 第 10 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林小满的」×5
  - narration_para_pct 3.6 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「翻动账本页码」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18457
chapter_chars_mean: 1846
chapter_chars_median: 1773
chapter_chars_cv: 0.12
paragraphs_mean: 40
dialogue_chars_pct: 49.0
dialogue_para_pct: 87.5
interiority_para_pct: 5.9
narration_para_pct: 6.6
turn_under20_pct: 70.7
turn_over200_pct: 0.0
attr_say_pct: 22.9
attr_adv_pct: 14.6
scenes_per_chapter: 2.7
dialogue_run_mean: 11.0
turn_len_median: 13
```
