# 听音 生成报告

slug：`aiyuce-20261021-113`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12559
LLM 调用：57 次，累计 226.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 抚摸报表边缘 | 2087 | normal | 37.8 | 0 |  | 2 |
| 2 | 审阅报表边缘 | 2367 | normal | 34.9 | 0 |  | 2 |
| 3 | 审阅报表边缘 | 2025 | normal | 34.8 | 0 |  | 2 |
| 4 | 手指抚过报表边缘 | 2283 | normal | 90.3 | 0 |  | 3 |
| 5 | 手指抚过报表边缘 | 2657 | normal | 34.2 | 0 |  | 3 |
| 6 | 手指抚过报表边缘 | 1134 | short | 81.6 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 26.7 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「如果AI质检系统的测试报告显示其准确率达到或超过…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《抚摸报表边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「审阅报表边缘」已存在
- 第 4 章：
  - dialogue_chars_pct 21.1 高于目标 18.0
  - narration_para_pct 35.0 低于目标 45.0
  - [observe] 标题与《抚摸报表边缘》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 35.0 低于目标 45.0
  - [observe] 章内自我复读 5 句（如「一方面，他知道任何变革都伴随着阵痛期；另一方面他…」）
  - [observe] 标题重复：「手指抚过报表边缘」已存在
- 第 6 章：
  - 情节与已写章节重复 0.73 ≥ 0.72（撞上「技术部经理与质检主管讨论AI质检系统的测试结果及是否替代…」）
  - dialogue_chars_pct 74.1 高于目标 18.0
  - dialogue_run_mean 13 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题重复：「手指抚过报表边缘」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12273
chapter_chars_mean: 2046
chapter_chars_median: 2135
chapter_chars_cv: 0.25
paragraphs_mean: 15.8
dialogue_chars_pct: 14.0
dialogue_para_pct: 37.0
interiority_para_pct: 25.2
narration_para_pct: 37.9
turn_under20_pct: 66.4
turn_over200_pct: 0.0
attr_say_pct: 28.0
attr_adv_pct: 5.2
scenes_per_chapter: 1
dialogue_run_mean: 4.0
turn_len_median: 21
```
