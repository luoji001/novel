# 定价尺 生成报告

slug：`aiyuce-20261021-90`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13500
LLM 调用：57 次，累计 228.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻看报价单细节 | 2099 | normal | 37.4 | 0 |  | 1 |
| 2 | 核对合规成本明细 | 2637 | normal | 89.6 | 0 |  | 1 |
| 3 | 翻看财务报表细节 | 2420 | normal | 88.4 | 0 |  | 1 |
| 4 | 翻看市场调研报告 | 2555 | normal | 35.0 | 0 |  | 1 |
| 5 | 敲击桌面思考 | 2484 | normal | 35.7 | 0 |  | 1 |
| 6 | 核对财务报表细节 | 1299 | short | 35.3 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被哪些实际的数据所推翻…」）
- 第 2 章：
  - narration_para_pct 35.3 低于目标 45.0
- 第 3 章：
  - [observe] 标题与《翻看报价单细节》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「这条推论会被什么样的证据推翻呢…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - interiority_para_pct 42.9 高于目标 40.0
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
  - [observe] 标题与《翻看财务报表细节》近似 0.75 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 13221
chapter_chars_mean: 2204
chapter_chars_median: 2402
chapter_chars_cv: 0.22
paragraphs_mean: 15
dialogue_chars_pct: 3.8
dialogue_para_pct: 28.1
interiority_para_pct: 15.3
narration_para_pct: 56.7
turn_under20_pct: 84.2
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 1.2
turn_len_median: 7
```
