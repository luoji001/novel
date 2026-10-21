# 电表 生成报告

slug：`aiyuce-20261021-124`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12898
LLM 调用：57 次，累计 231.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指轻抚电费单 | 2222 | normal | 96.2 | 0 |  | 0 |
| 2 | 手指轻抚折旧表 | 2532 | normal | 35.9 | 0 |  | 2 |
| 3 | 手指轻抚招聘JD | 2541 | normal | 90.5 | 0 |  | 0 |
| 4 | 比对电价走势 | 2240 | normal | 23.6 | 0 |  | 2 |
| 5 | 核对电费单数据 | 1916 | normal | 35.2 | 0 |  | 1 |
| 6 | 核对电费单数据 | 1441 | short | 88.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 44.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - interiority_para_pct 46.2 高于目标 40.0
  - [observe] 章内自我复读 1 句（如「这条推论会被电网调度异常导致的生产延误所推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_run_mean 5 高于目标 4.0
  - narration_para_pct 30.0 低于目标 45.0
  - [observe] 标题重复：「核对电费单数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12632
chapter_chars_mean: 2105
chapter_chars_median: 2184
chapter_chars_cv: 0.2
paragraphs_mean: 14.2
dialogue_chars_pct: 5.5
dialogue_para_pct: 26.0
interiority_para_pct: 21.5
narration_para_pct: 52.5
turn_under20_pct: 69.5
turn_over200_pct: 0.0
attr_say_pct: 12.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.9
turn_len_median: 14
```
