# 纸墨 生成报告

slug：`aiyuce-20261021-169`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12380
LLM 调用：57 次，累计 220.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 代写订单的统计表 | 1949 | normal | 97.4 | 0 |  | 2 |
| 2 | 电费单上的数字 | 2121 | normal | 89.0 | 0 |  | 0 |
| 3 | 电费单上的数字 | 2251 | normal | 89.9 | 0 |  | 3 |
| 4 | 检查订单记录表 | 2260 | normal | 36.0 | 0 |  | 2 |
| 5 | 打印机折旧表的更新 | 2673 | normal | 35.8 | 0 |  | 1 |
| 6 | 电费单上的数字 | 1120 | short | 34.5 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 18.2 高于目标 18.0
  - narration_para_pct 23.5 低于目标 45.0
- 第 3 章：
  - dialogue_chars_pct 21.3 高于目标 18.0
  - narration_para_pct 21.7 低于目标 45.0
  - [observe] 标题重复：「电费单上的数字」已存在
- 第 4 章：
  - narration_para_pct 35.0 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「他很清楚，只有这样才能确保自己不会被骗…」）
- 第 5 章：
  - [observe] 章内自我复读 3 句（如「如果未来几个月内，客户对代写服务的需求突然减少，…」）
- 第 6 章：
  - dialogue_chars_pct 60.9 高于目标 18.0
  - dialogue_run_mean 4.7 高于目标 4.0
  - narration_para_pct 12.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「电费单上的数字」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12058
chapter_chars_mean: 2010
chapter_chars_median: 2128
chapter_chars_cv: 0.26
paragraphs_mean: 18
dialogue_chars_pct: 14.7
dialogue_para_pct: 43.2
interiority_para_pct: 14.1
narration_para_pct: 42.7
turn_under20_pct: 68.6
turn_over200_pct: 0.0
attr_say_pct: 26.0
attr_adv_pct: 8.4
scenes_per_chapter: 1
dialogue_run_mean: 2.6
turn_len_median: 14
```
