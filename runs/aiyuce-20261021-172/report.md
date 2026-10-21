# 电表指针 生成报告

slug：`aiyuce-20261021-172`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13762
LLM 调用：57 次，累计 236.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电费单 | 2347 | normal | 95.7 | 0 |  | 0 |
| 2 | 招聘JD的打印通知 | 2514 | normal | 92.4 | 0 |  | 1 |
| 3 | 核对报价单 | 2418 | normal | 91.9 | 0 |  | 1 |
| 4 | 核对折旧表数据 | 2338 | normal | 90.7 | 0 |  | 1 |
| 5 | 核对电费单 | 2642 | normal | 35.0 | 0 |  | 2 |
| 6 | 核对报价单 | 1497 | short | 35.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 30.8 低于目标 45.0
- 第 3 章：
  - [observe] 标题与《核对电费单》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - narration_para_pct 35.3 低于目标 45.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对电费单」已存在
- 第 6 章：
  - dialogue_chars_pct 19.8 高于目标 18.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对报价单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 13468
chapter_chars_mean: 2245
chapter_chars_median: 2326
chapter_chars_cv: 0.18
paragraphs_mean: 16.2
dialogue_chars_pct: 8.9
dialogue_para_pct: 29.2
interiority_para_pct: 18.2
narration_para_pct: 52.6
turn_under20_pct: 42.6
turn_over200_pct: 0.0
attr_say_pct: 14.2
attr_adv_pct: 4.3
scenes_per_chapter: 1.5
dialogue_run_mean: 1.7
turn_len_median: 22
```
