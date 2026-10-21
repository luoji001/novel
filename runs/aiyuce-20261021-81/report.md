# 改卷 生成报告

slug：`aiyuce-20261021-81`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12208
LLM 调用：57 次，累计 221.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 点击听课记录 | 1869 | normal | 86.6 | 0 |  | 3 |
| 2 | 核对听课记录表 | 2041 | normal | 89.0 | 0 |  | 2 |
| 3 | 分析系统运行日志 | 2127 | normal | 35.5 | 0 |  | 1 |
| 4 | 记录表的细微变化 | 2343 | normal | 35.8 | 0 |  | 1 |
| 5 | 分析系统运行日志 | 2535 | normal | 34.6 | 0 |  | 2 |
| 6 | 核对听课记录表 | 1287 | short | 78.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 73.1 高于目标 18.0
  - dialogue_run_mean 16 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
- 第 2 章：
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 标题与《点击听课记录》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「分析系统运行日志」已存在
- 第 6 章：
  - dialogue_chars_pct 69.5 高于目标 18.0
  - dialogue_run_mean 10 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题重复：「核对听课记录表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11936
chapter_chars_mean: 1989
chapter_chars_median: 2038
chapter_chars_cv: 0.22
paragraphs_mean: 14.5
dialogue_chars_pct: 22.1
dialogue_para_pct: 42.1
interiority_para_pct: 11.1
narration_para_pct: 46.8
turn_under20_pct: 48.7
turn_over200_pct: 0.0
attr_say_pct: 21.5
attr_adv_pct: 2.7
scenes_per_chapter: 1.2
dialogue_run_mean: 5.2
turn_len_median: 21
```
