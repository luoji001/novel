# 批改本 生成报告

slug：`aiyuce-20261021-261`
档位：AI 推演　闸门模式：observe
章数：6　总字数：10750
LLM 调用：53 次，累计 189.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅听课记录本 | 1971 | normal | 96.3 | 0 |  | 1 |
| 2 | AI作文批改系统 | 1396 | normal | 89.5 | 0 |  | 0 |
| 3 | 核对预算表 | 2024 | normal | 35.9 | 0 |  | 1 |
| 4 | 核对预算表 | 1825 | normal | 34.0 | 0 |  | 4 |
| 5 | 核对听课记录本 | 2140 | normal | 35.6 | 0 |  | 2 |
| 6 | 手指滑过图表边缘 | 1388 | short | 80.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 30.0 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 32.9 高于目标 18.0
  - narration_para_pct 31.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对预算表」已存在
- 第 5 章：
  - [observe] 章内自我复读 2 句（如「比如说在未来某个季度内，若出现大量因忽略个别细节…」）
  - [observe] 标题与《翻阅听课记录本》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 42.5 高于目标 18.0
  - dialogue_run_mean 11 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 10485
chapter_chars_mean: 1748
chapter_chars_median: 1848
chapter_chars_cv: 0.18
paragraphs_mean: 14.3
dialogue_chars_pct: 15.7
dialogue_para_pct: 44.7
interiority_para_pct: 13.2
narration_para_pct: 42.1
turn_under20_pct: 52.4
turn_over200_pct: 0.0
attr_say_pct: 21.7
attr_adv_pct: 2.8
scenes_per_chapter: 1.5
dialogue_run_mean: 3.9
turn_len_median: 17
```
