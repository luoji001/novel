# 排产表 生成报告

slug：`aiyuce-20261021-88`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12296
LLM 调用：57 次，累计 222.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 统计图揭示用电新趋势 | 2306 | normal | 95.8 | 0 |  | 0 |
| 2 | 指尖划过电费单 | 2017 | normal | 88.3 | 0 |  | 1 |
| 3 | 指尖划过数据线条 | 2660 | normal | 90.9 | 0 |  | 1 |
| 4 | 指尖划过数据线条 | 2263 | normal | 34.8 | 0 |  | 2 |
| 5 | 目光停留于12千瓦数据 | 1825 | normal | 36.2 | 0 |  | 2 |
| 6 | 指尖划过数据线条 | 1219 | short | 84.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 43.8 低于目标 45.0
- 第 3 章：
  - narration_para_pct 33.3 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「指尖划过数据线条」已存在
- 第 5 章：
  - narration_para_pct 41.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这个数字让他皱起了眉头…」）
- 第 6 章：
  - [observe] 标题重复：「指尖划过数据线条」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12012
chapter_chars_mean: 2002
chapter_chars_median: 2088
chapter_chars_cv: 0.24
paragraphs_mean: 14
dialogue_chars_pct: 8.0
dialogue_para_pct: 32.9
interiority_para_pct: 16.8
narration_para_pct: 50.3
turn_under20_pct: 39.5
turn_over200_pct: 0.0
attr_say_pct: 12.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.8
turn_len_median: 21
```
