# 数据镜 生成报告

slug：`aiyuce-20261021-125`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12428
LLM 调用：57 次，累计 230.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅质检报表 | 1740 | normal | 96.8 | 0 |  | 1 |
| 2 | 核对预算分配表 | 2485 | normal | 33.0 | 0 |  | 4 |
| 3 | 翻阅测试报告 | 2222 | normal | 85.9 | 0 |  | 2 |
| 4 | 翻阅考勤记录表 | 2696 | normal | 35.8 | 0 |  | 1 |
| 5 | 翻阅客户投诉报表 | 2147 | normal | 31.8 | 0 |  | 4 |
| 6 | 翻阅质检报表 | 1132 | short | 80.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 36.4 低于目标 45.0
- 第 2 章：
  - 命中套话收尾句
  - dialogue_chars_pct 66.6 高于目标 18.0
  - narration_para_pct 12.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 22.2 高于目标 18.0
  - narration_para_pct 42.9 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 65.8 高于目标 18.0
  - dialogue_run_mean 5.7 高于目标 4.0
  - narration_para_pct 10.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 68.8 高于目标 18.0
  - dialogue_run_mean 10 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题重复：「翻阅质检报表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12110
chapter_chars_mean: 2018
chapter_chars_median: 2120
chapter_chars_cv: 0.27
paragraphs_mean: 17.2
dialogue_chars_pct: 38.1
dialogue_para_pct: 57.0
interiority_para_pct: 11.9
narration_para_pct: 31.1
turn_under20_pct: 32.7
turn_over200_pct: 0.0
attr_say_pct: 25.8
attr_adv_pct: 3.9
scenes_per_chapter: 1.2
dialogue_run_mean: 4.0
turn_len_median: 36
```
