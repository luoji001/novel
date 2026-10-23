# 合同复印件 生成报告

slug：`shuangwen-20261022-102`
档位：爽文　闸门模式：observe
章数：10　总字数：18787
LLM 调用：97 次，累计 422.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔的余温 | 1955 | normal | 40.0 | 0 |  | 2 |
| 2 | 碎纸机的嗡鸣 | 1934 | normal | 91.6 | 0 |  | 1 |
| 3 | 签字笔的较量 | 1710 | normal | 90.8 | 0 |  | 2 |
| 4 | 签字笔的余温 | 1701 | normal | 92.9 | 0 |  | 3 |
| 5 | 合同复印件的现身 | 1858 | normal | 89.8 | 0 |  | 2 |
| 6 | 现金袋的重量 | 1863 | normal | 94.1 | 0 |  | 1 |
| 7 | 签字笔的触碰 | 2032 | normal | 92.7 | 0 |  | 1 |
| 8 | 签字笔的较量 | 1656 | normal | 37.8 | 0 |  | 2 |
| 9 | 合同复印件的现身 | 1811 | normal | 89.6 | 0 |  | 3 |
| 10 | 账本上的三处数据 | 2257 | long | 91.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李振国的」×6
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「李振国的」×4
- 第 3 章：
  - 单条套路句式超限：「李振国的」×3
  - [observe] 标题与《签字笔的余温》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 命中套话收尾句
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「签字笔的余温」已存在
- 第 5 章：
  - 单条套路句式超限：「周晓芸的」×3
  - attr_adv_pct 12.5 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「点了点头」×3
- 第 7 章：
  - [observe] 标题与《签字笔的余温》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔的较量」已存在
- 第 9 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 23 高于目标 14.0
  - [observe] 标题重复：「合同复印件的现身」已存在
- 第 10 章：
  - 单条套路句式超限：「李振国的」×4、「周晓芸的」×3
  - attr_adv_pct 22.2 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 17927
chapter_chars_mean: 1793
chapter_chars_median: 1780
chapter_chars_cv: 0.1
paragraphs_mean: 35.2
dialogue_chars_pct: 49.4
dialogue_para_pct: 84.9
interiority_para_pct: 5.3
narration_para_pct: 9.8
turn_under20_pct: 61.0
turn_over200_pct: 0.0
attr_say_pct: 16.2
attr_adv_pct: 12.7
scenes_per_chapter: 1.6
dialogue_run_mean: 7.8
turn_len_median: 16
```
