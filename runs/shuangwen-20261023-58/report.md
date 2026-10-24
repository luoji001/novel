# 旧账单 生成报告

slug：`shuangwen-20261023-58`
档位：爽文　闸门模式：observe
章数：10　总字数：19595
LLM 调用：97 次，累计 442.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字权的缺失 | 1981 | normal | 99.2 | 0 |  | 2 |
| 2 | 账本一角的旧账单 | 2376 | normal | 92.8 | 0 |  | 3 |
| 3 | 签字笔的重量 | 1926 | normal | 92.5 | 0 |  | 0 |
| 4 | 欠条上的指纹痕迹 | 1545 | normal | 93.7 | 0 |  | 3 |
| 5 | 账本一角的旧账单 | 2116 | normal | 88.2 | 0 |  | 3 |
| 6 | 账本一角的旧账单 | 1466 | normal | 92.8 | 0 |  | 2 |
| 7 | 旧账单的角落 | 1771 | normal | 35.4 | 0 |  | 3 |
| 8 | 账本一角的旧账单 | 1848 | normal | 92.0 | 0 |  | 3 |
| 9 | 账本一角的缺页 | 1875 | normal | 93.8 | 0 |  | 2 |
| 10 | 账本一角的旧账单 | 2681 | long | 86.6 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈国强的」×4
  - attr_adv_pct 25.0 高于目标 12.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈国强的」×3
  - attr_adv_pct 13.0 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「陈国强的」×4
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
- 第 5 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 39 高于目标 14.0
  - [observe] 标题重复：「账本一角的旧账单」已存在
- 第 6 章：
  - 单条套路句式超限：「陈国强的」×3
  - [observe] 标题重复：「账本一角的旧账单」已存在
- 第 7 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 35 高于目标 14.0
  - [observe] attr_adv_pct 42.9 > 25.0（结构塌缩）
- 第 8 章：
  - 命中套话收尾句
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「账本一角的旧账单」已存在
- 第 9 章：
  - narration_para_pct 4.4 低于目标 5.0
  - [observe] 标题与《账本一角的旧账单》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「陈国强的」×5、「林小满的」×4
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 17.4 高于目标 12.0
  - dialogue_run_mean 27 高于目标 14.0
  - [observe] 标题重复：「账本一角的旧账单」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18566
chapter_chars_mean: 1857
chapter_chars_median: 1806
chapter_chars_cv: 0.19
paragraphs_mean: 43.3
dialogue_chars_pct: 51.8
dialogue_para_pct: 88.5
interiority_para_pct: 3.7
narration_para_pct: 7.8
turn_under20_pct: 73.2
turn_over200_pct: 0.0
attr_say_pct: 26.9
attr_adv_pct: 14.9
scenes_per_chapter: 2.1
dialogue_run_mean: 15.2
turn_len_median: 12
```
