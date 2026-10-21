# 显卡标价本 生成报告

slug：`aiyuce-20261021-50`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12220
LLM 调用：57 次，累计 234.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 计算器上的折旧计算 | 2448 | normal | 96.5 | 0 |  | 0 |
| 2 | 手指划过泛黄纸页 | 2245 | normal | 36.5 | 0 |  | 4 |
| 3 | 手指划过报价单 | 2225 | normal | 90.5 | 0 |  | 0 |
| 4 | 计算器上的折旧计算 | 1984 | normal | 35.8 | 0 |  | 2 |
| 5 | 手指划过电费账单 | 2037 | normal | 35.8 | 0 |  | 2 |
| 6 | 调整显卡标价 | 1275 | short | 91.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - dialogue_chars_pct 24.1 高于目标 18.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - narration_para_pct 22.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 4 句（如「如果实际使用过程中显卡的磨损速度加快，或者由于技…」）
  - [observe] 标题重复：「计算器上的折旧计算」已存在
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《手指划过报价单》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 30.0 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11909
chapter_chars_mean: 1985
chapter_chars_median: 2082
chapter_chars_cv: 0.2
paragraphs_mean: 17.5
dialogue_chars_pct: 9.4
dialogue_para_pct: 38.8
interiority_para_pct: 13.4
narration_para_pct: 47.7
turn_under20_pct: 76.5
turn_over200_pct: 0.0
attr_say_pct: 4.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 2.4
turn_len_median: 12
```
