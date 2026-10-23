# 校准证书 生成报告

slug：`shuangwen-20261022-107`
档位：爽文　闸门模式：observe
章数：10　总字数：19490
LLM 调用：97 次，累计 415.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔的重量 | 1708 | normal | 99.4 | 0 |  | 0 |
| 2 | 拍桌子的回响 | 1813 | normal | 37.0 | 0 |  | 1 |
| 3 | 校准证书的失效 | 2019 | normal | 93.5 | 0 |  | 1 |
| 4 | 校准证书的失效 | 2095 | normal | 36.4 | 0 |  | 2 |
| 5 | 签字笔的重量 | 1738 | normal | 91.4 | 0 |  | 2 |
| 6 | 签字笔的重量 | 1808 | normal | 92.1 | 0 |  | 3 |
| 7 | 校准证书的失效 | 1905 | normal | 36.4 | 0 |  | 2 |
| 8 | 签字笔的重量 | 2044 | normal | 90.1 | 0 |  | 3 |
| 9 | 签字本的重量 | 1728 | normal | 93.7 | 0 |  | 1 |
| 10 | 签字本的重量 | 2622 | long | 91.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] attr_adv_pct 37.5 > 25.0（结构塌缩）
- 第 3 章：
  - attr_adv_pct 22.2 高于目标 12.0
- 第 4 章：
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「校准证书的失效」已存在
- 第 5 章：
  - 单条套路句式超限：「李建国的」×6
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 6 章：
  - 单条套路句式超限：「李建国的」×5
  - attr_adv_pct 15.4 高于目标 12.0
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 7 章：
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「校准证书的失效」已存在
- 第 8 章：
  - narration_para_pct 2.4 低于目标 5.0
  - dialogue_run_mean 20 高于目标 14.0
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 9 章：
  - [observe] 标题与《签字笔的重量》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - [observe] 标题重复：「签字本的重量」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18525
chapter_chars_mean: 1852
chapter_chars_median: 1766
chapter_chars_cv: 0.14
paragraphs_mean: 40.6
dialogue_chars_pct: 51.1
dialogue_para_pct: 85.4
interiority_para_pct: 4.1
narration_para_pct: 10.5
turn_under20_pct: 64.9
turn_over200_pct: 0.0
attr_say_pct: 28.8
attr_adv_pct: 15.1
scenes_per_chapter: 2.2
dialogue_run_mean: 8.1
turn_len_median: 15
```
