# 模型拆分 生成报告

slug：`aiyuce-20261021-47`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12119
LLM 调用：57 次，累计 210.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 检查案件检索报告 | 2689 | normal | 94.2 | 0 |  | 1 |
| 2 | 模型推理报价单 | 2110 | normal | 35.1 | 0 |  | 3 |
| 3 | 复核页数统计表 | 2272 | normal | 36.2 | 0 |  | 1 |
| 4 | 审查案件检索报告 | 1902 | normal | 90.2 | 0 |  | 3 |
| 5 | 检查案件检索报告 | 1765 | normal | 89.2 | 0 |  | 2 |
| 6 | 核对复核页数 | 1375 | short | 33.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 35.3 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 31.7 高于目标 18.0
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 18.4 高于目标 18.0
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 标题与《检查案件检索报告》近似 0.88 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 标题重复：「检查案件检索报告」已存在
- 第 6 章：
  - dialogue_chars_pct 39.5 高于目标 18.0
  - narration_para_pct 27.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《复核页数统计表》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11833
chapter_chars_mean: 1972
chapter_chars_median: 1954
chapter_chars_cv: 0.23
paragraphs_mean: 15.7
dialogue_chars_pct: 16.5
dialogue_para_pct: 49.2
interiority_para_pct: 15.4
narration_para_pct: 35.4
turn_under20_pct: 53.4
turn_over200_pct: 0.0
attr_say_pct: 14.3
attr_adv_pct: 3.6
scenes_per_chapter: 2.2
dialogue_run_mean: 2.6
turn_len_median: 22
```
