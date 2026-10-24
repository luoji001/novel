# 红章 生成报告

slug：`shuangwen-20261023-136`
档位：爽文　闸门模式：observe
章数：10　总字数：18308
LLM 调用：97 次，累计 397.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 房产证递上 | 2223 | normal | 98.8 | 0 |  | 1 |
| 2 | 房产证举高 | 1834 | normal | 91.8 | 0 |  | 2 |
| 3 | 房产证递上 | 1632 | normal | 94.0 | 0 |  | 1 |
| 4 | 旧证摊开 | 1575 | normal | 93.4 | 0 |  | 1 |
| 5 | 房产证摊开 | 1830 | normal | 92.7 | 0 |  | 1 |
| 6 | 房产证举高 | 1829 | normal | 90.9 | 0 |  | 3 |
| 7 | 房产证摊开 | 1765 | normal | 94.4 | 0 |  | 1 |
| 8 | 房产证摊开 | 1902 | normal | 90.9 | 0 |  | 2 |
| 9 | 房产证摊开 | 1734 | normal | 88.5 | 0 |  | 3 |
| 10 | 房产证摊开 | 1974 | long | 36.0 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×3
- 第 2 章：
  - 单条套路句式超限：「李国强的」×5
  - [observe] 标题与《房产证递上》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 标题重复：「房产证递上」已存在
- 第 4 章：
  - attr_adv_pct 16.7 高于目标 12.0
- 第 5 章：
  - [observe] 标题与《旧证摊开》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「李国强的」×7、「王建国的」×4
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「房产证举高」已存在
- 第 7 章：
  - [observe] 标题重复：「房产证摊开」已存在
- 第 8 章：
  - 单条套路句式超限：「王建国的」×7
  - [observe] 标题重复：「房产证摊开」已存在
- 第 9 章：
  - narration_para_pct 3.3 低于目标 5.0
  - dialogue_run_mean 29 高于目标 14.0
  - [observe] 标题重复：「房产证摊开」已存在
- 第 10 章：
  - 单条套路句式超限：「他知道这」×5
  - attr_adv_pct 17.6 高于目标 12.0
  - [observe] 章内自我复读 2 句（如「李国强看着王建国，心中暗自思忖…」）
  - [observe] 标题重复：「房产证摊开」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17423
chapter_chars_mean: 1742
chapter_chars_median: 1738
chapter_chars_cv: 0.1
paragraphs_mean: 37.3
dialogue_chars_pct: 47.2
dialogue_para_pct: 85.1
interiority_para_pct: 4.4
narration_para_pct: 10.5
turn_under20_pct: 65.8
turn_over200_pct: 0.0
attr_say_pct: 16.6
attr_adv_pct: 8.7
scenes_per_chapter: 2
dialogue_run_mean: 8.2
turn_len_median: 16
```
