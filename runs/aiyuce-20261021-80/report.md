# 校对钟 生成报告

slug：`aiyuce-20261021-80`
档位：AI 推演　闸门模式：observe
章数：6　总字数：10965
LLM 调用：57 次，累计 216.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲报价单边缘 | 1834 | normal | 95.3 | 0 |  | 1 |
| 2 | 划记报价单边缘 | 1927 | normal | 88.9 | 0 |  | 3 |
| 3 | 划记报价单边缘 | 2152 | normal | 35.8 | 0 |  | 2 |
| 4 | 摩挲反馈表边缘 | 1999 | normal | 35.5 | 0 |  | 1 |
| 5 | 摩挲财务报表边缘 | 1899 | normal | 35.0 | 0 |  | 2 |
| 6 | 摩挲反馈表边缘 | 1148 | short | 82.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 14.3 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 21.0 高于目标 18.0
  - narration_para_pct 26.7 低于目标 45.0
  - [observe] 标题与《摩挲报价单边缘》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「划记报价单边缘」已存在
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《摩挲报价单边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 52.3 高于目标 18.0
  - dialogue_run_mean 5 高于目标 4.0
  - narration_para_pct 15.4 低于目标 45.0
  - [observe] 标题重复：「摩挲反馈表边缘」已存在

## 整书结构指标

```
chapters: 6
total_chars: 10703
chapter_chars_mean: 1784
chapter_chars_median: 1870
chapter_chars_cv: 0.2
paragraphs_mean: 13.7
dialogue_chars_pct: 12.7
dialogue_para_pct: 38.3
interiority_para_pct: 21.0
narration_para_pct: 40.7
turn_under20_pct: 67.8
turn_over200_pct: 0.0
attr_say_pct: 1.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.9
turn_len_median: 13
```
