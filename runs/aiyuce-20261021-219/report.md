# 扫描屏 生成报告

slug：`aiyuce-20261021-219`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11454
LLM 调用：57 次，累计 219.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲纸边看数字 | 1605 | normal | 95.0 | 0 |  | 1 |
| 2 | 摩挲纸边看数字 | 2258 | normal | 35.7 | 0 |  | 3 |
| 3 | 摩挲纸边看数字 | 2279 | normal | 92.2 | 0 |  | 3 |
| 4 | 摩挲纸边看数字 | 2133 | normal | 80.9 | 0 |  | 4 |
| 5 | 摩挲纸边看数字 | 1875 | normal | 88.5 | 0 |  | 1 |
| 6 | 摩挲纸边看数字 | 1298 | short | 36.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 16.7 低于目标 45.0
- 第 2 章：
  - narration_para_pct 27.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「2024年影像科医生离职率分析报告…」）
  - [observe] 标题重复：「摩挲纸边看数字」已存在
- 第 3 章：
  - dialogue_chars_pct 23.2 高于目标 18.0
  - narration_para_pct 38.1 低于目标 45.0
  - [observe] 标题重复：「摩挲纸边看数字」已存在
- 第 4 章：
  - dialogue_chars_pct 75.5 高于目标 18.0
  - dialogue_run_mean 12.5 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题重复：「摩挲纸边看数字」已存在
- 第 5 章：
  - [observe] 标题重复：「摩挲纸边看数字」已存在
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「摩挲纸边看数字」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11176
chapter_chars_mean: 1863
chapter_chars_median: 1951
chapter_chars_cv: 0.21
paragraphs_mean: 15.2
dialogue_chars_pct: 22.5
dialogue_para_pct: 50.6
interiority_para_pct: 17.0
narration_para_pct: 32.5
turn_under20_pct: 61.6
turn_over200_pct: 0.0
attr_say_pct: 16.3
attr_adv_pct: 11.9
scenes_per_chapter: 1.2
dialogue_run_mean: 3.5
turn_len_median: 17
```
