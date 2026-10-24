# 账本 生成报告

slug：`shuangwen-20261023-81`
档位：爽文　闸门模式：observe
章数：10　总字数：18884
LLM 调用：97 次，累计 420.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本的塑料封皮 | 1748 | normal | 100.0 | 0 |  | 1 |
| 2 | 敲击账本的节奏 | 2162 | normal | 92.2 | 0 |  | 2 |
| 3 | 指纹覆盖的账页 | 1797 | normal | 89.5 | 0 |  | 2 |
| 4 | 签字笔的颤抖 | 1687 | normal | 92.6 | 0 |  | 2 |
| 5 | 敲击计算器的节奏 | 1858 | normal | 94.9 | 0 |  | 1 |
| 6 | 计算器的确认键 | 1993 | normal | 37.0 | 0 |  | 2 |
| 7 | 敲击计算器的节奏 | 1515 | normal | 93.3 | 0 |  | 3 |
| 8 | 计算器的确认键 | 1816 | normal | 94.3 | 0 |  | 3 |
| 9 | 签字笔的颤抖 | 1955 | normal | 94.0 | 0 |  | 2 |
| 10 | 敲击计算器的节奏 | 2343 | long | 94.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国点」×3、「李建国的」×3
- 第 2 章：
  - 单条套路句式超限：「李建国的」×4
  - narration_para_pct 3.3 低于目标 5.0
- 第 3 章：
  - 单条套路句式超限：「李建国的」×4
  - narration_para_pct 0.0 低于目标 5.0
- 第 4 章：
  - 单条套路句式超限：「李建国的」×7、「了自己的」×3
  - attr_adv_pct 20.0 高于目标 12.0
- 第 5 章：
  - [observe] 标题与《敲击账本的节奏》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「点了点头」×3、「他知道这」×3
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 7 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×4、「说道“我」×3
  - [observe] 标题重复：「敲击计算器的节奏」已存在
- 第 8 章：
  - 单条套路句式超限：「李建国的」×3
  - narration_para_pct 2.8 低于目标 5.0
  - [observe] 标题重复：「计算器的确认键」已存在
- 第 9 章：
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 标题重复：「签字笔的颤抖」已存在
- 第 10 章：
  - attr_adv_pct 20.6 高于目标 12.0
  - [observe] 标题重复：「敲击计算器的节奏」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17947
chapter_chars_mean: 1795
chapter_chars_median: 1750
chapter_chars_cv: 0.13
paragraphs_mean: 38.6
dialogue_chars_pct: 49.4
dialogue_para_pct: 86.3
interiority_para_pct: 4.1
narration_para_pct: 9.6
turn_under20_pct: 70.4
turn_over200_pct: 0.0
attr_say_pct: 27.4
attr_adv_pct: 11.1
scenes_per_chapter: 1.4
dialogue_run_mean: 8.3
turn_len_median: 14
```
