# 数据镜 生成报告

slug：`aiyuce-20261021-29`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12885
LLM 调用：57 次，累计 229.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲统计表 | 2190 | normal | 38.5 | 0 |  | 2 |
| 2 | 勾画柱状图 | 2402 | normal | 37.2 | 0 |  | 1 |
| 3 | 手指滑动屏幕 | 2107 | normal | 79.8 | 0 |  | 3 |
| 4 | 普通话等级考试成绩单 | 2387 | normal | 34.4 | 0 |  | 1 |
| 5 | 手指滑动屏幕 | 2499 | normal | 35.6 | 0 |  | 2 |
| 6 | 手指滑动屏幕 | 1294 | short | 32.9 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「不仅仅是」×3
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 63.1 高于目标 18.0
  - dialogue_run_mean 11.5 高于目标 4.0
  - narration_para_pct 4.2 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「手指滑动屏幕」已存在
- 第 6 章：
  - dialogue_chars_pct 45.3 高于目标 18.0
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「手指滑动屏幕」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12599
chapter_chars_mean: 2100
chapter_chars_median: 2244
chapter_chars_cv: 0.21
paragraphs_mean: 16.2
dialogue_chars_pct: 16.2
dialogue_para_pct: 30.9
interiority_para_pct: 9.4
narration_para_pct: 59.7
turn_under20_pct: 54.7
turn_over200_pct: 0.0
attr_say_pct: 2.6
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 3.7
turn_len_median: 24
```
