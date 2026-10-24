# 旧版验收单 生成报告

slug：`shuangwen-20261023-55`
档位：爽文　闸门模式：observe
章数：10　总字数：18602
LLM 调用：97 次，累计 409.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指抚过纸页 | 1577 | normal | 97.1 | 0 |  | 0 |
| 2 | 签字笔压痕 | 1874 | normal | 37.4 | 0 |  | 1 |
| 3 | 手指抚过纸页 | 1644 | normal | 36.9 | 0 |  | 3 |
| 4 | 撕碎的验货单 | 1902 | normal | 92.8 | 0 |  | 0 |
| 5 | 签字笔压痕 | 2005 | normal | 37.3 | 0 |  | 3 |
| 6 | 纸页边缘的褐色污渍 | 1784 | normal | 94.7 | 0 |  | 0 |
| 7 | 旧版验收单边缘的褐色污渍 | 1720 | normal | 90.7 | 0 |  | 2 |
| 8 | 手指抚过纸页 | 1791 | normal | 93.2 | 0 |  | 2 |
| 9 | 签字笔压痕 | 2009 | normal | 92.1 | 0 |  | 3 |
| 10 | 签字笔压痕 | 2286 | long | 92.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] attr_adv_pct 35.7 > 25.0（结构塌缩）
- 第 3 章：
  - 命中套话收尾句
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「手指抚过纸页」已存在
- 第 5 章：
  - narration_para_pct 4.0 低于目标 5.0
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔压痕」已存在
- 第 7 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题与《纸页边缘的褐色污渍》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - narration_para_pct 2.8 低于目标 5.0
  - [observe] 标题重复：「手指抚过纸页」已存在
- 第 9 章：
  - narration_para_pct 4.9 低于目标 5.0
  - attr_adv_pct 17.6 高于目标 12.0
  - [observe] 标题重复：「签字笔压痕」已存在
- 第 10 章：
  - [observe] 标题重复：「签字笔压痕」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17701
chapter_chars_mean: 1770
chapter_chars_median: 1742
chapter_chars_cv: 0.11
paragraphs_mean: 37.3
dialogue_chars_pct: 50.5
dialogue_para_pct: 84.0
interiority_para_pct: 5.2
narration_para_pct: 10.9
turn_under20_pct: 67.1
turn_over200_pct: 0.0
attr_say_pct: 22.7
attr_adv_pct: 16.1
scenes_per_chapter: 1.8
dialogue_run_mean: 7.2
turn_len_median: 14
```
