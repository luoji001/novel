# 算力账本 生成报告

slug：`aiyuce-20261021-42`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12704
LLM 调用：57 次，累计 219.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对报价单 | 2356 | normal | 38.1 | 0 |  | 1 |
| 2 | 核对许可证变更通知 | 2036 | normal | 86.5 | 0 |  | 3 |
| 3 | 核对电费账单 | 2412 | normal | 36.4 | 0 |  | 1 |
| 4 | 核对电费账单 | 2254 | normal | 88.4 | 0 |  | 1 |
| 5 | 敲击桌面 | 2095 | normal | 81.3 | 0 |  | 3 |
| 6 | 敲击桌面 | 1545 | short | 89.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - dialogue_chars_pct 27.5 高于目标 18.0
  - dialogue_run_mean 4.3 高于目标 4.0
  - narration_para_pct 31.8 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 标题重复：「核对电费账单」已存在
- 第 5 章：
  - dialogue_chars_pct 37.3 高于目标 18.0
  - dialogue_run_mean 6.5 高于目标 4.0
  - narration_para_pct 31.6 低于目标 45.0
- 第 6 章：
  - narration_para_pct 30.0 低于目标 45.0
  - [observe] 标题重复：「敲击桌面」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12420
chapter_chars_mean: 2070
chapter_chars_median: 2130
chapter_chars_cv: 0.15
paragraphs_mean: 16.3
dialogue_chars_pct: 15.4
dialogue_para_pct: 39.2
interiority_para_pct: 17.2
narration_para_pct: 43.6
turn_under20_pct: 49.3
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.7
turn_len_median: 24
```
