# 破卷 生成报告

slug：`shuangwen-20261023-148`
档位：爽文　闸门模式：observe
章数：10　总字数：19548
LLM 调用：97 次，累计 441.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 半张纸上的真相 | 1839 | normal | 39.1 | 0 |  | 1 |
| 2 | 半张纸上的痕迹 | 2010 | normal | 37.9 | 0 |  | 3 |
| 3 | 半张纸上的真相 | 1821 | normal | 93.1 | 0 |  | 3 |
| 4 | 油灯下的影子 | 1938 | normal | 91.7 | 0 |  | 0 |
| 5 | 半张纸上的真相 | 1938 | normal | 90.3 | 0 |  | 2 |
| 6 | 半张纸上的真相 | 1786 | normal | 93.5 | 0 |  | 2 |
| 7 | 半张纸上的真相 | 1793 | normal | 91.0 | 0 |  | 2 |
| 8 | 半张纸上的真相 | 1741 | normal | 93.9 | 0 |  | 2 |
| 9 | 半张纸上的真相 | 2170 | normal | 92.5 | 0 |  | 1 |
| 10 | 半张纸上的真相 | 2502 | long | 90.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 53.3 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] attr_adv_pct 26.3 > 25.0（结构塌缩）
  - [observe] 标题与《半张纸上的真相》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - attr_adv_pct 15.0 高于目标 12.0
  - dialogue_run_mean 15 高于目标 14.0
  - [observe] 标题重复：「半张纸上的真相」已存在
- 第 5 章：
  - 单条套路句式超限：「点了点头“」×3、「验货台」×3
  - [observe] 标题重复：「半张纸上的真相」已存在
- 第 6 章：
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「半张纸上的真相」已存在
- 第 7 章：
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「半张纸上的真相」已存在
- 第 8 章：
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题重复：「半张纸上的真相」已存在
- 第 9 章：
  - [observe] 标题重复：「半张纸上的真相」已存在
- 第 10 章：
  - [observe] 标题重复：「半张纸上的真相」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18381
chapter_chars_mean: 1838
chapter_chars_median: 1761
chapter_chars_cv: 0.12
paragraphs_mean: 50.4
dialogue_chars_pct: 47.3
dialogue_para_pct: 80.5
interiority_para_pct: 6.2
narration_para_pct: 13.3
turn_under20_pct: 72.1
turn_over200_pct: 0.0
attr_say_pct: 31.8
attr_adv_pct: 18.5
scenes_per_chapter: 1.4
dialogue_run_mean: 6.0
turn_len_median: 14
```
