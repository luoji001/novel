# 数据钟摆 生成报告

slug：`aiyuce-20261021-185`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12165
LLM 调用：57 次，累计 221.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对报表 | 2037 | normal | 37.8 | 0 |  | 1 |
| 2 | 摩挲预算表 | 2293 | normal | 89.7 | 0 |  | 0 |
| 3 | 摩挲预算表 | 1879 | normal | 35.8 | 0 |  | 2 |
| 4 | 摩挲考勤表 | 2596 | normal | 89.1 | 0 |  | 2 |
| 5 | 摩挲招聘JD | 2080 | normal | 35.2 | 0 |  | 1 |
| 6 | 摩挲预算表 | 1274 | short | 78.6 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「摩挲预算表」已存在
- 第 4 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 标题与《摩挲预算表》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 67.6 高于目标 18.0
  - dialogue_run_mean 11 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题重复：「摩挲预算表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11919
chapter_chars_mean: 1986
chapter_chars_median: 2020
chapter_chars_cv: 0.22
paragraphs_mean: 13.5
dialogue_chars_pct: 10.4
dialogue_para_pct: 26.6
interiority_para_pct: 23.3
narration_para_pct: 50.1
turn_under20_pct: 66.9
turn_over200_pct: 0.0
attr_say_pct: 6.1
attr_adv_pct: 46.8
scenes_per_chapter: 1.3
dialogue_run_mean: 2.7
turn_len_median: 16
```
