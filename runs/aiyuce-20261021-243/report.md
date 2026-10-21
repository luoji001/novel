# 屏光 生成报告

slug：`aiyuce-20261021-243`
档位：AI 推演　闸门模式：observe
章数：6　总字数：10974
LLM 调用：53 次，累计 195.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 报表上的平均时间 | 1801 | normal | 36.5 | 0 |  | 3 |
| 2 | 查看招聘JD | 2338 | normal | 34.2 | 0 |  | 3 |
| 3 | 核对预算与离职率 | 2195 | normal | 32.0 | 0 |  | 4 |
| 4 | 核对预算与离职率 | 1099 | normal | 91.2 | 0 |  | 2 |
| 5 | 核对预算与离职率 | 2006 | normal | 88.7 | 0 |  | 1 |
| 6 | 核对报表与离职率 | 1529 | short | 85.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 31.0 高于目标 18.0
  - narration_para_pct 31.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - dialogue_chars_pct 36.3 高于目标 18.0
  - narration_para_pct 25.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 41.1 高于目标 18.0
  - dialogue_run_mean 8.5 高于目标 4.0
  - narration_para_pct 18.2 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「我们相信，只要预算安排合理，这项投资将会带来显著…」）
- 第 4 章：
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 标题重复：「核对预算与离职率」已存在
- 第 5 章：
  - [observe] 标题重复：「核对预算与离职率」已存在
- 第 6 章：
  - dialogue_chars_pct 43.6 高于目标 18.0
  - narration_para_pct 7.7 低于目标 45.0
  - [observe] 标题与《核对预算与离职率》近似 0.75 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 10660
chapter_chars_mean: 1777
chapter_chars_median: 1856
chapter_chars_cv: 0.25
paragraphs_mean: 17
dialogue_chars_pct: 28.3
dialogue_para_pct: 57.2
interiority_para_pct: 10.6
narration_para_pct: 32.1
turn_under20_pct: 46.4
turn_over200_pct: 0.0
attr_say_pct: 31.2
attr_adv_pct: 5.7
scenes_per_chapter: 1.5
dialogue_run_mean: 3.5
turn_len_median: 24
```
