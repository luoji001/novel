# 代码审查 生成报告

slug：`aiyuce-20261021-163`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12262
LLM 调用：57 次，累计 221.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 代码审查流程手册 | 1903 | normal | 38.3 | 0 |  | 2 |
| 2 | 签到表上的重复签名 | 2345 | normal | 35.8 | 0 |  | 1 |
| 3 | 便签纸上的两行字 | 2215 | normal | 35.5 | 0 |  | 1 |
| 4 | 翻阅绩效评估表 | 2070 | normal | 88.2 | 0 |  | 1 |
| 5 | 代码审查流程手册 | 2342 | normal | 36.4 | 0 |  | 2 |
| 6 | 手指滑动手册 | 1381 | short | 84.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 40.0 低于目标 45.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「代码审查流程手册」已存在
- 第 6 章：
  - dialogue_chars_pct 58.2 高于目标 18.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - narration_para_pct 9.1 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11988
chapter_chars_mean: 1998
chapter_chars_median: 2096
chapter_chars_cv: 0.18
paragraphs_mean: 14.5
dialogue_chars_pct: 12.4
dialogue_para_pct: 39.9
interiority_para_pct: 12.1
narration_para_pct: 48.0
turn_under20_pct: 57.1
turn_over200_pct: 0.0
attr_say_pct: 1.8
attr_adv_pct: 1.8
scenes_per_chapter: 1.8
dialogue_run_mean: 2.1
turn_len_median: 18
```
