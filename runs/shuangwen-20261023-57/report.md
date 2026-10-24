# 碎纸机 生成报告

slug：`shuangwen-20261023-57`
档位：爽文　闸门模式：observe
章数：10　总字数：18617
LLM 调用：97 次，累计 406.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一纸教学记录本 | 1769 | normal | 40.0 | 0 |  | 1 |
| 2 | 一张旧教案 | 1985 | normal | 93.9 | 0 |  | 1 |
| 3 | 摩挲封面边缘 | 1826 | normal | 92.2 | 0 |  | 0 |
| 4 | 摩挲封面边缘 | 1938 | normal | 93.6 | 0 |  | 2 |
| 5 | 摩挲封面边缘 | 1649 | normal | 92.4 | 0 |  | 3 |
| 6 | 摩挲封面边缘 | 1833 | normal | 92.6 | 0 |  | 3 |
| 7 | 摩挲封面边缘 | 1801 | normal | 93.4 | 0 |  | 2 |
| 8 | 摩挲封面边缘 | 1957 | normal | 92.7 | 0 |  | 2 |
| 9 | 摩挲纸张边缘 | 1751 | normal | 91.4 | 0 |  | 1 |
| 10 | 摩挲纸张边缘 | 2098 | long | 90.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 57.1 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「林婉秋的」×4
- 第 4 章：
  - 单条套路句式超限：「周振邦的」×4
  - [observe] 标题重复：「摩挲封面边缘」已存在
- 第 5 章：
  - 单条套路句式超限：「林婉秋的」×3
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「摩挲封面边缘」已存在
- 第 6 章：
  - 单条套路句式超限：「带着一丝」×3、「周振邦的」×3
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「摩挲封面边缘」已存在
- 第 7 章：
  - narration_para_pct 0.0 低于目标 5.0
  - [observe] 标题重复：「摩挲封面边缘」已存在
- 第 8 章：
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「摩挲封面边缘」已存在
- 第 9 章：
  - [observe] 标题与《摩挲封面边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「周振邦的」×6
  - narration_para_pct 2.5 低于目标 5.0
  - dialogue_run_mean 19 高于目标 14.0
  - [observe] 标题重复：「摩挲纸张边缘」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17795
chapter_chars_mean: 1780
chapter_chars_median: 1758
chapter_chars_cv: 0.07
paragraphs_mean: 33.6
dialogue_chars_pct: 51.6
dialogue_para_pct: 85.6
interiority_para_pct: 6.1
narration_para_pct: 8.3
turn_under20_pct: 60.1
turn_over200_pct: 0.0
attr_say_pct: 19.1
attr_adv_pct: 15.1
scenes_per_chapter: 1.6
dialogue_run_mean: 8.6
turn_len_median: 15
```
