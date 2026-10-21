# 报表 生成报告

slug：`aiyuce-20261021-173`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11794
LLM 调用：57 次，累计 223.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击键盘 | 1862 | normal | 93.8 | 0 |  | 2 |
| 2 | 敲击键盘 | 2301 | normal | 85.5 | 0 |  | 3 |
| 3 | 测试报告 | 2130 | normal | 31.1 | 0 |  | 4 |
| 4 | 手指滑动名单 | 2265 | normal | 34.0 | 0 |  | 1 |
| 5 | 翻阅预算表 | 1789 | normal | 80.1 | 0 |  | 3 |
| 6 | 手指敲击键盘 | 1441 | short | 33.8 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 42.9 高于目标 40.0
  - narration_para_pct 21.4 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 32.3 高于目标 18.0
  - narration_para_pct 35.0 低于目标 45.0
  - [observe] 标题重复：「敲击键盘」已存在
- 第 3 章：
  - dialogue_chars_pct 69.4 高于目标 18.0
  - dialogue_run_mean 9.5 高于目标 4.0
  - narration_para_pct 13.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么呢推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「一条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 48.4 高于目标 18.0
  - dialogue_run_mean 6.7 高于目标 4.0
  - narration_para_pct 16.7 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 23.9 高于目标 18.0
  - dialogue_run_mean 5 高于目标 4.0
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《敲击键盘》近似 0.80 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11503
chapter_chars_mean: 1917
chapter_chars_median: 1948
chapter_chars_cv: 0.17
paragraphs_mean: 17.3
dialogue_chars_pct: 30.9
dialogue_para_pct: 50.6
interiority_para_pct: 12.7
narration_para_pct: 36.6
turn_under20_pct: 25.8
turn_over200_pct: 0.0
attr_say_pct: 26.5
attr_adv_pct: 1.6
scenes_per_chapter: 1.2
dialogue_run_mean: 4.9
turn_len_median: 36
```
