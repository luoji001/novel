# 合同副本 生成报告

slug：`shuangwen-20261022-09`
档位：爽文　闸门模式：observe
章数：10　总字数：19656
LLM 调用：97 次，累计 348.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 递上旧证 | 1770 | normal | 39.9 | 0 |  | 1 |
| 2 | 递上旧证 | 1767 | normal | 95.1 | 0 |  | 1 |
| 3 | 递出泛黄合同 | 2012 | normal | 37.3 | 0 |  | 2 |
| 4 | 递出泛黄合同 | 1968 | normal | 36.0 | 0 |  | 3 |
| 5 | 递交泛黄合同 | 2139 | normal | 93.0 | 0 |  | 4 |
| 6 | 递上旧证 | 2074 | normal | 93.7 | 0 |  | 3 |
| 7 | 手机屏幕的倒影 | 2271 | normal | 37.2 | 0 |  | 1 |
| 8 | 签下旧合同 | 1790 | normal | 92.1 | 0 |  | 2 |
| 9 | 递出泛黄合同 | 1768 | normal | 36.6 | 0 |  | 2 |
| 10 | 递出泛黄合同 | 2087 | long | 85.2 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 60.0 > 25.0（结构塌缩）
- 第 2 章：
  - [observe] 标题重复：「递上旧证」已存在
- 第 3 章：
  - 命中套话收尾句
  - [observe] attr_adv_pct 35.7 > 25.0（结构塌缩）
- 第 4 章：
  - narration_para_pct 2.6 低于目标 5.0
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「递出泛黄合同」已存在
- 第 5 章：
  - narration_para_pct 2.1 低于目标 5.0
  - attr_adv_pct 14.8 高于目标 12.0
  - dialogue_run_mean 14.7 高于目标 14.0
  - [observe] 标题与《递出泛黄合同》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 2.0 低于目标 5.0
  - attr_adv_pct 13.9 高于目标 12.0
  - [observe] 标题重复：「递上旧证」已存在
- 第 7 章：
  - [observe] attr_adv_pct 26.9 > 25.0（结构塌缩）
- 第 8 章：
  - 单条套路句式超限：「带着一丝」×3
  - attr_adv_pct 14.3 高于目标 12.0
- 第 9 章：
  - [observe] attr_adv_pct 26.7 > 25.0（结构塌缩）
  - [observe] 标题重复：「递出泛黄合同」已存在
- 第 10 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 34 高于目标 14.0
  - [observe] 标题重复：「递出泛黄合同」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18646
chapter_chars_mean: 1865
chapter_chars_median: 1894
chapter_chars_cv: 0.1
paragraphs_mean: 43.3
dialogue_chars_pct: 50.8
dialogue_para_pct: 88.8
interiority_para_pct: 4.3
narration_para_pct: 6.9
turn_under20_pct: 74.1
turn_over200_pct: 0.0
attr_say_pct: 32.0
attr_adv_pct: 24.3
scenes_per_chapter: 1.4
dialogue_run_mean: 11.6
turn_len_median: 12
```
