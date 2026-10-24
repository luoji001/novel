# 旧卷轴 生成报告

slug：`shuangwen-20261023-49`
档位：爽文　闸门模式：observe
章数：10　总字数：19050
LLM 调用：97 次，累计 443.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 卷轴与旧册对峙 | 1587 | normal | 97.5 | 0 |  | 2 |
| 2 | 纸币验证卷轴真伪 | 1657 | normal | 93.8 | 0 |  | 0 |
| 3 | 墨笔盖印之争 | 1821 | normal | 92.5 | 0 |  | 2 |
| 4 | 墨笔撕裂卷轴 | 1942 | normal | 93.5 | 0 |  | 0 |
| 5 | 卷轴与存折对峙 | 1854 | normal | 92.9 | 0 |  | 1 |
| 6 | 墨笔划开旧卷轴 | 2021 | normal | 90.0 | 0 |  | 2 |
| 7 | 墨笔划破旧卷轴 | 1855 | normal | 36.8 | 0 |  | 2 |
| 8 | 墨笔划破旧卷轴 | 1509 | normal | 91.3 | 0 |  | 2 |
| 9 | 卷轴摊开在案几上 | 2094 | normal | 91.9 | 0 |  | 2 |
| 10 | 卷轴摊开在案几上 | 2700 | long | 92.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「赵文远的」×3
  - attr_adv_pct 20.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「赵文远的」×5
  - attr_adv_pct 25.0 高于目标 12.0
- 第 5 章：
  - [observe] 标题与《卷轴与旧册对峙》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「赵文远的」×7
  - [observe] 标题与《墨笔撕裂卷轴》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题与《墨笔划开旧卷轴》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题重复：「墨笔划破旧卷轴」已存在
- 第 9 章：
  - 单条套路句式超限：「赵文远的」×6
  - narration_para_pct 4.3 低于目标 5.0
- 第 10 章：
  - 单条套路句式超限：「赵文远的」×8
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「卷轴摊开在案几上」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18085
chapter_chars_mean: 1808
chapter_chars_median: 1756
chapter_chars_cv: 0.18
paragraphs_mean: 40.2
dialogue_chars_pct: 46.8
dialogue_para_pct: 81.1
interiority_para_pct: 6.1
narration_para_pct: 12.8
turn_under20_pct: 66.8
turn_over200_pct: 0.0
attr_say_pct: 19.0
attr_adv_pct: 13.6
scenes_per_chapter: 1.7
dialogue_run_mean: 6.3
turn_len_median: 13
```
