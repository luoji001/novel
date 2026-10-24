# 笔记 生成报告

slug：`shuangwen-20261023-111`
档位：爽文　闸门模式：observe
章数：10　总字数：18318
LLM 调用：97 次，累计 410.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 釉面触碰放大镜 | 1796 | normal | 99.8 | 0 |  | 0 |
| 2 | 釉面触碰放大镜 | 1828 | normal | 94.7 | 0 |  | 2 |
| 3 | 釉面触碰放大镜 | 1591 | normal | 94.4 | 0 |  | 3 |
| 4 | 备案单出现 | 1684 | normal | 93.6 | 0 |  | 3 |
| 5 | 签字笔夺回 | 1755 | normal | 93.6 | 0 |  | 1 |
| 6 | 备案单消失 | 1912 | normal | 93.4 | 0 |  | 2 |
| 7 | 签字笔夺回 | 1859 | normal | 93.7 | 0 |  | 1 |
| 8 | 备案单浮现 | 2126 | normal | 93.6 | 0 |  | 2 |
| 9 | 签字笔夺回 | 1701 | normal | 93.9 | 0 |  | 1 |
| 10 | 签字笔夺回 | 2056 | long | 92.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「釉面触碰放大镜」已存在
- 第 3 章：
  - 单条套路句式超限：「镇工艺协会」×3
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「釉面触碰放大镜」已存在
- 第 4 章：
  - 单条套路句式超限：「陈启明的」×3
  - attr_adv_pct 16.7 高于目标 12.0
  - dialogue_run_mean 17.5 高于目标 14.0
- 第 5 章：
  - attr_adv_pct 20.0 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「他知道这」×5
  - [observe] 标题与《备案单出现》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - [observe] 标题重复：「签字笔夺回」已存在
- 第 8 章：
  - 命中套话收尾句
  - [observe] 标题与《备案单出现》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - [observe] 标题重复：「签字笔夺回」已存在
- 第 10 章：
  - 单条套路句式超限：「陈启明的」×3
  - [observe] 标题重复：「签字笔夺回」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17390
chapter_chars_mean: 1739
chapter_chars_median: 1721
chapter_chars_cv: 0.09
paragraphs_mean: 39.1
dialogue_chars_pct: 48.5
dialogue_para_pct: 85.7
interiority_para_pct: 5.3
narration_para_pct: 9.0
turn_under20_pct: 75.3
turn_over200_pct: 0.0
attr_say_pct: 24.7
attr_adv_pct: 10.5
scenes_per_chapter: 2.1
dialogue_run_mean: 7.7
turn_len_median: 12
```
