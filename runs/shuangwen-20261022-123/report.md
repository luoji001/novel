# 签字笔 生成报告

slug：`shuangwen-20261022-123`
档位：爽文　闸门模式：observe
章数：10　总字数：18846
LLM 调用：97 次，累计 418.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔 | 1539 | normal | 96.8 | 0 |  | 3 |
| 2 | 一张验收单 | 1858 | normal | 91.5 | 0 |  | 0 |
| 3 | 一张旧文件 | 2153 | normal | 91.9 | 0 |  | 3 |
| 4 | 文件夹展开 | 1835 | normal | 93.3 | 0 |  | 1 |
| 5 | 一份旧文件 | 1764 | normal | 91.7 | 0 |  | 4 |
| 6 | 撕纸一角 | 2124 | normal | 91.4 | 0 |  | 1 |
| 7 | 签字笔 | 1777 | normal | 93.1 | 0 |  | 1 |
| 8 | 签字笔 | 1660 | normal | 91.5 | 0 |  | 3 |
| 9 | 签字笔 | 2013 | normal | 93.7 | 0 |  | 1 |
| 10 | 撕纸一角 | 2113 | long | 93.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 18.2 高于目标 12.0
- 第 3 章：
  - 命中套话收尾句
  - narration_para_pct 3.7 低于目标 5.0
  - dialogue_run_mean 17 高于目标 14.0
- 第 4 章：
  - attr_adv_pct 20.0 高于目标 12.0
- 第 5 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
  - dialogue_run_mean 18 高于目标 14.0
  - [observe] 标题与《一张旧文件》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「李晨站在」×3
- 第 7 章：
  - [observe] 标题重复：「签字笔」已存在
- 第 8 章：
  - 命中套话收尾句
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题重复：「签字笔」已存在
- 第 9 章：
  - [observe] 标题重复：「签字笔」已存在
- 第 10 章：
  - [observe] 标题重复：「撕纸一角」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17844
chapter_chars_mean: 1784
chapter_chars_median: 1766
chapter_chars_cv: 0.11
paragraphs_mean: 42.6
dialogue_chars_pct: 47.7
dialogue_para_pct: 86.4
interiority_para_pct: 5.0
narration_para_pct: 8.6
turn_under20_pct: 73.0
turn_over200_pct: 0.0
attr_say_pct: 30.1
attr_adv_pct: 11.9
scenes_per_chapter: 2.2
dialogue_run_mean: 8.7
turn_len_median: 14
```
