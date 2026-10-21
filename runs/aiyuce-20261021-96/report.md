# 电表转得更快 生成报告

slug：`aiyuce-20261021-96`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11395
LLM 调用：57 次，累计 212.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的用电量增长 | 1937 | normal | 35.7 | 0 |  | 4 |
| 2 | 模拟机使用记录 | 2282 | normal | 35.9 | 0 |  | 2 |
| 3 | 核对课程报价细节 | 1961 | normal | 34.6 | 0 |  | 3 |
| 4 | 折旧表边缘的120W标注 | 2252 | normal | 35.3 | 0 |  | 3 |
| 5 | 翻看电费单 | 1795 | normal | 85.1 | 0 |  | 2 |
| 6 | 翻看折旧表 | 1162 | short | 34.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「带着一丝」×3
  - dialogue_chars_pct 35.3 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 18.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 31.4 高于目标 18.0
  - narration_para_pct 35.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 22.0 高于目标 18.0
  - narration_para_pct 15.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 44.8 高于目标 18.0
  - narration_para_pct 11.1 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 41.4 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 11076
chapter_chars_mean: 1846
chapter_chars_median: 1891
chapter_chars_cv: 0.22
paragraphs_mean: 18.2
dialogue_chars_pct: 29.6
dialogue_para_pct: 62.2
interiority_para_pct: 14.1
narration_para_pct: 23.7
turn_under20_pct: 36.3
turn_over200_pct: 0.0
attr_say_pct: 18.5
attr_adv_pct: 14.7
scenes_per_chapter: 1.8
dialogue_run_mean: 3.0
turn_len_median: 26
```
