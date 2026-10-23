# 签字笔 生成报告

slug：`shuangwen-20261022-42`
档位：爽文　闸门模式：observe
章数：10　总字数：18792
LLM 调用：97 次，累计 337.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔的裂痕 | 1741 | normal | 99.6 | 0 |  | 1 |
| 2 | 旧清单的重现 | 1920 | normal | 37.5 | 0 |  | 2 |
| 3 | 签字笔的裂痕 | 1846 | normal | 90.5 | 0 |  | 1 |
| 4 | 旧清单的重现 | 1821 | normal | 91.1 | 0 |  | 3 |
| 5 | 旧清单的重现 | 1719 | normal | 91.0 | 0 |  | 1 |
| 6 | 签字笔的指纹 | 1634 | normal | 91.9 | 0 |  | 2 |
| 7 | 签字笔的指纹 | 1908 | normal | 90.7 | 0 |  | 2 |
| 8 | 签字笔的指纹 | 1816 | normal | 90.6 | 0 |  | 1 |
| 9 | 签字笔的指纹 | 2033 | normal | 85.5 | 0 |  | 3 |
| 10 | 清单的指纹 | 2344 | long | 90.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 25.0 高于目标 12.0
- 第 2 章：
  - narration_para_pct 4.0 低于目标 5.0
  - [observe] attr_adv_pct 29.2 > 25.0（结构塌缩）
- 第 3 章：
  - [observe] 标题重复：「签字笔的裂痕」已存在
- 第 4 章：
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「旧清单的重现」已存在
- 第 5 章：
  - [observe] 标题重复：「旧清单的重现」已存在
- 第 6 章：
  - attr_adv_pct 15.8 高于目标 12.0
  - [observe] 标题与《签字笔的裂痕》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - dialogue_run_mean 18.5 高于目标 14.0
  - [observe] 标题重复：「签字笔的指纹」已存在
- 第 8 章：
  - [observe] 标题重复：「签字笔的指纹」已存在
- 第 9 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 34 高于目标 14.0
  - [observe] 标题重复：「签字笔的指纹」已存在
- 第 10 章：
  - attr_adv_pct 16.7 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 17759
chapter_chars_mean: 1776
chapter_chars_median: 1744
chapter_chars_cv: 0.11
paragraphs_mean: 44.2
dialogue_chars_pct: 53.1
dialogue_para_pct: 89.0
interiority_para_pct: 4.3
narration_para_pct: 6.6
turn_under20_pct: 70.4
turn_over200_pct: 0.0
attr_say_pct: 21.6
attr_adv_pct: 12.4
scenes_per_chapter: 1.4
dialogue_run_mean: 12.1
turn_len_median: 12
```
