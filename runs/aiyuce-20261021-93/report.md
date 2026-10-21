# 听课笔记 生成报告

slug：`aiyuce-20261021-93`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11461
LLM 调用：57 次，累计 213.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 听课记录本的减页调整 | 1850 | normal | 38.2 | 0 |  | 2 |
| 2 | AI作文批改报告核查 | 2165 | normal | 36.1 | 0 |  | 1 |
| 3 | 批改作文时间缩短 | 2107 | normal | 35.7 | 0 |  | 1 |
| 4 | AI作文样本的字数争议 | 1919 | normal | 34.0 | 0 |  | 4 |
| 5 | AI批改报告核查 | 1894 | normal | 89.2 | 0 |  | 1 |
| 6 | 听课记录本的边缘痕迹 | 1520 | short | 90.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 30.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - 单条套路句式超限：「智教科技的」×4
  - dialogue_chars_pct 36.0 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 标题与《AI作文批改报告核查》近似 0.89 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 标题与《听课记录本的减页调整》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11194
chapter_chars_mean: 1866
chapter_chars_median: 1865
chapter_chars_cv: 0.12
paragraphs_mean: 13
dialogue_chars_pct: 11.7
dialogue_para_pct: 36.5
interiority_para_pct: 12.0
narration_para_pct: 51.5
turn_under20_pct: 54.7
turn_over200_pct: 0.0
attr_say_pct: 33.9
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 1.9
turn_len_median: 20
```
