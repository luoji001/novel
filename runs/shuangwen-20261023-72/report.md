# 借阅证 生成报告

slug：`shuangwen-20261023-72`
档位：爽文　闸门模式：observe
章数：10　总字数：17247
LLM 调用：97 次，累计 418.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 借阅证编号风波 | 1663 | normal | 99.9 | 0 |  | 1 |
| 2 | 撕碎登记簿一角 | 2124 | normal | 93.2 | 0 |  | 1 |
| 3 | 按红印 | 1956 | normal | 36.5 | 0 |  | 2 |
| 4 | 挑战借阅证编号 | 1466 | normal | 91.8 | 0 |  | 4 |
| 5 | 触碰铜令牌 | 1575 | normal | 92.8 | 0 |  | 1 |
| 6 | 签上姓名 | 1425 | normal | 92.6 | 0 |  | 1 |
| 7 | 按红印 | 1447 | normal | 93.9 | 0 |  | 1 |
| 8 | 按下红印 | 1743 | normal | 94.0 | 0 |  | 3 |
| 9 | 签下姓名 | 1603 | normal | 92.2 | 0 |  | 3 |
| 10 | 签下姓名 | 2235 | long | 88.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「方守仁的」×3
- 第 2 章：
  - 单条套路句式超限：「李怀远站在」×3、「带着一丝」×3、「李怀远的」×3
- 第 3 章：
  - dialogue_run_mean 16.7 高于目标 14.0
  - [observe] attr_adv_pct 36.0 > 25.0（结构塌缩）
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「方守仁的」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题与《借阅证编号风波》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「方守仁的」×7、「李怀远的」×3
- 第 6 章：
  - narration_para_pct 4.9 低于目标 5.0
- 第 7 章：
  - [observe] 标题重复：「按红印」已存在
- 第 8 章：
  - attr_adv_pct 18.2 高于目标 12.0
  - dialogue_run_mean 15.5 高于目标 14.0
  - [observe] 标题与《按红印》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「方守仁的」×3
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题与《签上姓名》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「方守仁的」×6
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 52 高于目标 14.0
  - [observe] 标题重复：「签下姓名」已存在

## 整书结构指标

```
chapters: 10
total_chars: 16297
chapter_chars_mean: 1630
chapter_chars_median: 1546
chapter_chars_cv: 0.17
paragraphs_mean: 40.6
dialogue_chars_pct: 50.3
dialogue_para_pct: 86.2
interiority_para_pct: 4.7
narration_para_pct: 9.1
turn_under20_pct: 74.9
turn_over200_pct: 0.0
attr_say_pct: 32.9
attr_adv_pct: 12.3
scenes_per_chapter: 1.6
dialogue_run_mean: 13.3
turn_len_median: 12
```
