# 电改 生成报告

slug：`aiyuce-20261021-232`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13044
LLM 调用：57 次，累计 220.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电费单数字 | 2326 | normal | 59.8 | 0 |  | 0 |
| 2 | 核对电费单数字 | 2141 | normal | 36.1 | 0 |  | 2 |
| 3 | 核对服务器折旧表 | 2185 | normal | 90.8 | 0 |  | 2 |
| 4 | 核对服务器性能报告 | 2397 | normal | 35.9 | 0 |  | 3 |
| 5 | 摩挲电费单边缘 | 2394 | normal | 35.6 | 0 |  | 3 |
| 6 | 核对电费单数字 | 1595 | short | 36.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对电费单数字」已存在
- 第 3 章：
  - dialogue_chars_pct 22.8 高于目标 18.0
  - narration_para_pct 18.8 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 22.7 高于目标 18.0
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 22.5 高于目标 18.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对电费单数字」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12725
chapter_chars_mean: 2121
chapter_chars_median: 2205
chapter_chars_cv: 0.14
paragraphs_mean: 17.8
dialogue_chars_pct: 12.7
dialogue_para_pct: 37.3
interiority_para_pct: 17.7
narration_para_pct: 45.0
turn_under20_pct: 61.5
turn_over200_pct: 0.0
attr_say_pct: 15.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 2.1
turn_len_median: 19
```
