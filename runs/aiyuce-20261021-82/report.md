# 电表指针 生成报告

slug：`aiyuce-20261021-82`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12445
LLM 调用：57 次，累计 227.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单的能耗分析 | 2190 | normal | 36.5 | 0 |  | 1 |
| 2 | 修改招聘JD的条款 | 2215 | normal | 36.3 | 0 |  | 1 |
| 3 | 调整报价单参数 | 2434 | normal | 87.0 | 0 |  | 0 |
| 4 | 折旧表的笔迹改动 | 2551 | normal | 55.7 | 0 |  | 0 |
| 5 | 核对电费单 | 1773 | normal | 88.5 | 0 |  | 0 |
| 6 | 电费单的能耗分析 | 1276 | short | 84.1 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 2 句（如「此外，我也注意到电费单中的每一笔账目都清晰地列出…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 78.8 高于目标 18.0
  - dialogue_run_mean 7 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题重复：「电费单的能耗分析」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12184
chapter_chars_mean: 2031
chapter_chars_median: 2155
chapter_chars_cv: 0.23
paragraphs_mean: 13.5
dialogue_chars_pct: 9.2
dialogue_para_pct: 19.4
interiority_para_pct: 13.6
narration_para_pct: 67.0
turn_under20_pct: 80.4
turn_over200_pct: 0.0
attr_say_pct: 8.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 3.1
turn_len_median: 17
```
