# 模型盒 生成报告

slug：`aiyuce-20261021-168`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12799
LLM 调用：57 次，累计 217.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摸模型清单 | 2373 | normal | 96.9 | 0 |  | 0 |
| 2 | 敲击桌面 | 2573 | normal | 36.0 | 0 |  | 2 |
| 3 | 核对模型清单 | 2206 | normal | 87.5 | 0 |  | 1 |
| 4 | 翻查工作日志 | 1970 | normal | 34.8 | 0 |  | 1 |
| 5 | 模型教学推广员巡查 | 2496 | normal | 34.6 | 0 |  | 1 |
| 6 | 翻查工作日志 | 1175 | short | 87.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 标题与《摸模型清单》近似 0.73 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 标题重复：「翻查工作日志」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12527
chapter_chars_mean: 2088
chapter_chars_median: 2245
chapter_chars_cv: 0.24
paragraphs_mean: 15.2
dialogue_chars_pct: 5.5
dialogue_para_pct: 25.3
interiority_para_pct: 20.3
narration_para_pct: 54.4
turn_under20_pct: 72.4
turn_over200_pct: 0.0
attr_say_pct: 14.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.1
turn_len_median: 12
```
