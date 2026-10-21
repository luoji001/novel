# 数据镜 生成报告

slug：`aiyuce-20261021-53`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12944
LLM 调用：57 次，累计 232.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击桌面 | 2820 | normal | 95.2 | 0 |  | 1 |
| 2 | 摩挲桌面边缘 | 2676 | normal | 89.4 | 0 |  | 1 |
| 3 | 扫描评分表 | 1693 | normal | 84.4 | 0 |  | 2 |
| 4 | 扫描评分表 | 2453 | normal | 79.2 | 0 |  | 4 |
| 5 | 翻阅评分表 | 2198 | normal | 85.2 | 0 |  | 4 |
| 6 | 签署审批单 | 1098 | short | 33.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现。

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 35.7 低于目标 45.0
- 第 2 章：
  - narration_para_pct 44.4 低于目标 45.0
- 第 3 章：
  - dialogue_chars_pct 43.5 高于目标 18.0
  - narration_para_pct 26.7 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 69.2 高于目标 18.0
  - dialogue_run_mean 23 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题重复：「扫描评分表」已存在
- 第 5 章：
  - dialogue_chars_pct 23.5 高于目标 18.0
  - dialogue_run_mean 5 高于目标 4.0
  - narration_para_pct 16.7 低于目标 45.0
  - [observe] 标题与《扫描评分表》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 38.9 高于目标 18.0
  - narration_para_pct 30.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12676
chapter_chars_mean: 2113
chapter_chars_median: 2278
chapter_chars_cv: 0.31
paragraphs_mean: 15.3
dialogue_chars_pct: 29.9
dialogue_para_pct: 69.4
interiority_para_pct: 4.7
narration_para_pct: 25.9
turn_under20_pct: 51.3
turn_over200_pct: 0.0
attr_say_pct: 17.8
attr_adv_pct: 6.9
scenes_per_chapter: 1.8
dialogue_run_mean: 6.4
turn_len_median: 27
```
