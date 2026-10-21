# 性能单 生成报告

slug：`aiyuce-20261021-27`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11651
LLM 调用：57 次，累计 207.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指滑动评估表 | 1713 | normal | 96.1 | 0 |  | 1 |
| 2 | 手指滑动评估表 | 2093 | normal | 35.8 | 0 |  | 2 |
| 3 | 手指滑动统计表 | 2177 | normal | 35.8 | 0 |  | 2 |
| 4 | 手指敲打桌面 | 2468 | normal | 34.2 | 0 |  | 3 |
| 5 | 手指摩挲纸页边缘 | 1917 | normal | 36.3 | 0 |  | 2 |
| 6 | 手指敲击桌面 | 1277 | short | 84.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 30.8 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「然而，这条推论可能会被什么推翻呢…」）
  - [observe] 标题重复：「手指滑动评估表」已存在
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的实际结果推翻呢…」）
  - [observe] 标题与《手指滑动评估表》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - dialogue_chars_pct 33.5 高于目标 18.0
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 26.7 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「这条推论会被什么推翻？…」）
- 第 6 章：
  - dialogue_chars_pct 35.9 高于目标 18.0
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 标题与《手指敲打桌面》近似 0.83 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11364
chapter_chars_mean: 1894
chapter_chars_median: 1952
chapter_chars_cv: 0.22
paragraphs_mean: 15.3
dialogue_chars_pct: 16.7
dialogue_para_pct: 41.7
interiority_para_pct: 9.1
narration_para_pct: 49.3
turn_under20_pct: 48.4
turn_over200_pct: 0.0
attr_say_pct: 36.4
attr_adv_pct: 16.4
scenes_per_chapter: 1.3
dialogue_run_mean: 2.1
turn_len_median: 25
```
