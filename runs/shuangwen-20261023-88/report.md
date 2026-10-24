# 铜尺 生成报告

slug：`shuangwen-20261023-88`
档位：爽文　闸门模式：observe
章数：10　总字数：19849
LLM 调用：97 次，累计 450.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜尺划破凭据 | 1585 | normal | 99.0 | 0 |  | 0 |
| 2 | 铜尺敲响 | 2216 | normal | 94.9 | 0 |  | 0 |
| 3 | 铜尺敲响 | 1779 | normal | 93.2 | 0 |  | 1 |
| 4 | 铜尺敲响 | 2202 | normal | 93.8 | 0 |  | 1 |
| 5 | 暗纹成金尘 | 1793 | normal | 94.8 | 0 |  | 0 |
| 6 | 签字笔的重量 | 1916 | normal | 95.4 | 0 |  | 1 |
| 7 | 铜尺划破凭据 | 2116 | normal | 90.9 | 0 |  | 3 |
| 8 | 撕碎的凭据 | 1964 | normal | 93.6 | 0 |  | 3 |
| 9 | 撕碎的凭据 | 1803 | normal | 94.3 | 0 |  | 2 |
| 10 | 签字笔的重量 | 2465 | long | 92.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - [observe] 标题重复：「铜尺敲响」已存在
- 第 4 章：
  - [observe] 标题重复：「铜尺敲响」已存在
- 第 6 章：
  - attr_adv_pct 15.4 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「说道“我」×3
  - attr_adv_pct 14.8 高于目标 12.0
  - [observe] 标题重复：「铜尺划破凭据」已存在
- 第 8 章：
  - narration_para_pct 3.8 低于目标 5.0
  - attr_adv_pct 18.2 高于目标 12.0
  - dialogue_run_mean 16.3 高于目标 14.0
- 第 9 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「撕碎的凭据」已存在
- 第 10 章：
  - 单条套路句式超限：「点了点头」×3
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「签字笔的重量」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18730
chapter_chars_mean: 1873
chapter_chars_median: 1822
chapter_chars_cv: 0.13
paragraphs_mean: 48.8
dialogue_chars_pct: 47.6
dialogue_para_pct: 81.8
interiority_para_pct: 4.1
narration_para_pct: 14.1
turn_under20_pct: 74.0
turn_over200_pct: 0.0
attr_say_pct: 25.7
attr_adv_pct: 11.6
scenes_per_chapter: 2.6
dialogue_run_mean: 6.6
turn_len_median: 12
```
