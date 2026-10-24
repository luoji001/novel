# 药单 生成报告

slug：`shuangwen-20261023-126`
档位：爽文　闸门模式：observe
章数：10　总字数：19571
LLM 调用：97 次，累计 445.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 折痕里的药材清单 | 2115 | normal | 98.3 | 0 |  | 2 |
| 2 | 签字笔的重量 | 1832 | normal | 92.3 | 0 |  | 3 |
| 3 | 签字笔的重量 | 1784 | normal | 93.8 | 0 |  | 2 |
| 4 | 签字笔的重量 | 1981 | normal | 94.2 | 0 |  | 3 |
| 5 | 清单背面的日期批注 | 1561 | normal | 91.8 | 0 |  | 0 |
| 6 | 清单背面的日期批注 | 1813 | normal | 93.0 | 0 |  | 3 |
| 7 | 签字笔的重量 | 1930 | normal | 92.3 | 0 |  | 2 |
| 8 | 签字笔的重量 | 1964 | normal | 91.0 | 0 |  | 3 |
| 9 | 签字笔的重量 | 1963 | normal | 91.8 | 0 |  | 3 |
| 10 | 划掉名字的笔锋 | 2618 | long | 92.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 29.7 低于目标 30.0
  - attr_adv_pct 18.2 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「他知道这」×3
  - narration_para_pct 3.0 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
- 第 3 章：
  - narration_para_pct 2.8 低于目标 5.0
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 4 章：
  - 单条套路句式超限：「说道“我」×3
  - attr_adv_pct 14.7 高于目标 12.0
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 6 章：
  - 单条套路句式超限：「李守仁的」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「清单背面的日期批注」已存在
- 第 7 章：
  - 单条套路句式超限：「他知道这」×4
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 8 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 17.3 高于目标 14.0
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 9 章：
  - narration_para_pct 2.9 低于目标 5.0
  - dialogue_run_mean 16.5 高于目标 14.0
  - [observe] 标题重复：「签字笔的重量」已存在
- 第 10 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 25.0 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 18590
chapter_chars_mean: 1859
chapter_chars_median: 1836
chapter_chars_cv: 0.14
paragraphs_mean: 41.1
dialogue_chars_pct: 50.3
dialogue_para_pct: 85.0
interiority_para_pct: 5.9
narration_para_pct: 9.1
turn_under20_pct: 64.3
turn_over200_pct: 0.0
attr_say_pct: 25.0
attr_adv_pct: 10.9
scenes_per_chapter: 1.2
dialogue_run_mean: 8.9
turn_len_median: 14
```
