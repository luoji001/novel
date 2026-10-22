# 金光 生成报告

slug：`shuangwen-20261022-32`
档位：爽文　闸门模式：observe
章数：10　总字数：19383
LLM 调用：97 次，累计 376.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 令牌上的金光 | 2256 | normal | 97.8 | 0 |  | 1 |
| 2 | 递上卷轴 | 1869 | normal | 92.0 | 0 |  | 1 |
| 3 | 交换灵石 | 1959 | normal | 92.1 | 0 |  | 1 |
| 4 | 摊开功法 | 1901 | normal | 94.2 | 0 |  | 2 |
| 5 | 灵石上的金光 | 1682 | normal | 95.3 | 0 |  | 1 |
| 6 | 递上卷轴 | 2300 | normal | 92.6 | 0 |  | 1 |
| 7 | 摊开功法 | 1793 | normal | 93.9 | 0 |  | 3 |
| 8 | 火焰凝成真元 | 1603 | normal | 36.8 | 0 |  | 1 |
| 9 | 摊开功法 | 1879 | normal | 92.6 | 0 |  | 3 |
| 10 | 摊开功法 | 2131 | long | 37.6 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「演武场」×5
- 第 2 章：
  - 单条套路句式超限：「萧长风的」×3
- 第 3 章：
  - attr_adv_pct 17.6 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「演武场」×6、「萧长风的」×4
  - attr_adv_pct 14.3 高于目标 12.0
- 第 5 章：
  - [observe] 标题与《令牌上的金光》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 标题重复：「递上卷轴」已存在
- 第 7 章：
  - 单条套路句式超限：「演武场」×4、「萧长风的」×3
  - attr_adv_pct 17.6 高于目标 12.0
  - [observe] 标题重复：「摊开功法」已存在
- 第 8 章：
  - [observe] attr_adv_pct 40.0 > 25.0（结构塌缩）
- 第 9 章：
  - 命中套话收尾句
  - 单条套路句式超限：「演武场」×4、「萧长风的」×3
  - [observe] 标题重复：「摊开功法」已存在
- 第 10 章：
  - 命中套话收尾句
  - 单条套路句式超限：「萧长风的」×6
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「摊开功法」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18311
chapter_chars_mean: 1831
chapter_chars_median: 1789
chapter_chars_cv: 0.12
paragraphs_mean: 46.8
dialogue_chars_pct: 42.3
dialogue_para_pct: 75.0
interiority_para_pct: 9.3
narration_para_pct: 15.7
turn_under20_pct: 74.5
turn_over200_pct: 0.0
attr_say_pct: 23.5
attr_adv_pct: 14.2
scenes_per_chapter: 2.2
dialogue_run_mean: 4.8
turn_len_median: 12
```
