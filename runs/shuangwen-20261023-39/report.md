# 旧磅单 生成报告

slug：`shuangwen-20261023-39`
档位：爽文　闸门模式：observe
章数：10　总字数：18815
LLM 调用：97 次，累计 414.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔的重量 | 1794 | normal | 38.6 | 0 |  | 1 |
| 2 | 旧磅单与电子秤之争 | 2191 | normal | 93.4 | 0 |  | 0 |
| 3 | 记录表的重量 | 1677 | normal | 91.1 | 0 |  | 0 |
| 4 | 抹布擦过磅单的痕迹 | 1568 | normal | 94.2 | 0 |  | 0 |
| 5 | 摩挲记录表边缘 | 1806 | normal | 92.7 | 0 |  | 2 |
| 6 | 签字笔的重量 | 1993 | normal | 92.2 | 0 |  | 1 |
| 7 | 摩挲记录表边缘 | 1932 | normal | 92.3 | 0 |  | 3 |
| 8 | 摩挲记录表边缘 | 1828 | normal | 89.7 | 0 |  | 2 |
| 9 | 摩挲证书边缘 | 1777 | normal | 93.0 | 0 |  | 2 |
| 10 | 摩挲旧磅单边缘 | 2239 | long | 88.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
- 第 6 章：
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 7 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
  - [observe] 标题重复：「摩挲记录表边缘」已存在
- 第 8 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「摩挲记录表边缘」已存在
- 第 9 章：
  - 单条套路句式超限：「点了点头」×4
  - [observe] 标题与《摩挲记录表边缘》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「过磅房」×3
  - [observe] 标题与《摩挲证书边缘》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 17793
chapter_chars_mean: 1779
chapter_chars_median: 1726
chapter_chars_cv: 0.12
paragraphs_mean: 43.1
dialogue_chars_pct: 44.6
dialogue_para_pct: 78.6
interiority_para_pct: 5.7
narration_para_pct: 15.7
turn_under20_pct: 74.9
turn_over200_pct: 0.0
attr_say_pct: 23.7
attr_adv_pct: 8.3
scenes_per_chapter: 1.4
dialogue_run_mean: 5.3
turn_len_median: 14
```
