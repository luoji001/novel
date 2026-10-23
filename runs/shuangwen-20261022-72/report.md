# 旧令牌 生成报告

slug：`shuangwen-20261022-72`
档位：爽文　闸门模式：observe
章数：10　总字数：18032
LLM 调用：97 次，累计 418.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧令牌的踪迹 | 1700 | normal | 97.4 | 0 |  | 2 |
| 2 | 借阅记录的对比 | 1591 | normal | 94.2 | 0 |  | 3 |
| 3 | 玉佩与令牌对峙 | 1747 | normal | 93.0 | 0 |  | 1 |
| 4 | 令牌吻玉佩 | 1753 | normal | 90.2 | 0 |  | 2 |
| 5 | 令牌入火燃证身 | 1696 | normal | 36.6 | 0 |  | 2 |
| 6 | 令牌叩玉佩 | 2023 | normal | 92.6 | 0 |  | 5 |
| 7 | 令牌裂痕照旧信 | 1837 | normal | 93.8 | 0 |  | 1 |
| 8 | 令牌吻玉佩 | 1798 | normal | 90.7 | 0 |  | 2 |
| 9 | 令牌吻玉佩 | 1809 | normal | 93.7 | 0 |  | 3 |
| 10 | 令牌吻玉佩 | 2068 | long | 89.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「藏书阁第三层」×3
  - narration_para_pct 2.6 低于目标 5.0
- 第 2 章：
  - 命中套话收尾句
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「萧怀远的」×8
- 第 4 章：
  - 单条套路句式超限：「萧怀远的」×7
  - attr_adv_pct 25.0 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「萧怀远的」×3、「他知道这」×3
  - [observe] attr_adv_pct 44.4 > 25.0（结构塌缩）
- 第 6 章：
  - 命中套话收尾句
  - 单条套路句式超限：「萧怀远的」×5
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 17 高于目标 14.0
  - [observe] 标题与《令牌吻玉佩》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「萧怀远的」×5
- 第 8 章：
  - 单条套路句式超限：「萧怀远的」×9
  - [observe] 标题重复：「令牌吻玉佩」已存在
- 第 9 章：
  - 单条套路句式超限：「萧怀远的」×3
  - attr_adv_pct 21.7 高于目标 12.0
  - [observe] 标题重复：「令牌吻玉佩」已存在
- 第 10 章：
  - 单条套路句式超限：「萧怀远的」×7
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「令牌吻玉佩」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17142
chapter_chars_mean: 1714
chapter_chars_median: 1695
chapter_chars_cv: 0.09
paragraphs_mean: 37.2
dialogue_chars_pct: 47.7
dialogue_para_pct: 84.6
interiority_para_pct: 6.9
narration_para_pct: 8.6
turn_under20_pct: 69.0
turn_over200_pct: 0.0
attr_say_pct: 26.5
attr_adv_pct: 14.6
scenes_per_chapter: 1.1
dialogue_run_mean: 7.7
turn_len_median: 14
```
