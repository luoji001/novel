# 电表 生成报告

slug：`aiyuce-20261021-256`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12945
LLM 调用：57 次，累计 218.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻看电费单数据 | 2225 | normal | 37.2 | 0 |  | 1 |
| 2 | 核对折旧表数据 | 2870 | normal | 34.6 | 0 |  | 1 |
| 3 | 核对折旧表数据 | 2130 | normal | 34.9 | 0 |  | 5 |
| 4 | 核对生产日志数据 | 2273 | normal | 88.8 | 0 |  | 1 |
| 5 | 核对折旧表数据 | 2117 | normal | 35.0 | 0 |  | 3 |
| 6 | 调整生产计划 | 1324 | short | 36.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
  - dialogue_chars_pct 28.9 高于目标 18.0
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对折旧表数据」已存在
- 第 4 章：
  - narration_para_pct 43.8 低于目标 45.0
- 第 5 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的证据推翻…」）
  - [observe] 标题重复：「核对折旧表数据」已存在
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12649
chapter_chars_mean: 2108
chapter_chars_median: 2126
chapter_chars_cv: 0.23
paragraphs_mean: 16
dialogue_chars_pct: 8.7
dialogue_para_pct: 27.0
interiority_para_pct: 22.5
narration_para_pct: 50.6
turn_under20_pct: 61.6
turn_over200_pct: 0.0
attr_say_pct: 23.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.7
turn_len_median: 20
```
