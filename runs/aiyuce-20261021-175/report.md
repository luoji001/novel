# 验码台 生成报告

slug：`aiyuce-20261021-175`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12148
LLM 调用：57 次，累计 208.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击键盘 | 2249 | normal | 95.9 | 0 |  | 1 |
| 2 | 敲击键盘 | 2204 | normal | 88.6 | 0 |  | 2 |
| 3 | 代码验收流程调整方案 | 2498 | normal | 35.1 | 0 |  | 1 |
| 4 | 敲击键盘 | 2122 | normal | 86.1 | 0 |  | 3 |
| 5 | 敲击桌面 | 1797 | normal | 82.7 | 0 |  | 3 |
| 6 | 敲击桌面 | 1272 | short | 85.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 31.6 低于目标 45.0
- 第 2 章：
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 标题重复：「敲击键盘」已存在
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 29.4 高于目标 18.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 标题重复：「敲击键盘」已存在
- 第 5 章：
  - dialogue_chars_pct 64.6 高于目标 18.0
  - dialogue_run_mean 6.5 高于目标 4.0
  - narration_para_pct 6.2 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 32.1 高于目标 18.0
  - narration_para_pct 16.7 低于目标 45.0
  - [observe] 标题重复：「敲击桌面」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11861
chapter_chars_mean: 1977
chapter_chars_median: 2114
chapter_chars_cv: 0.22
paragraphs_mean: 16.8
dialogue_chars_pct: 22.5
dialogue_para_pct: 47.2
interiority_para_pct: 16.0
narration_para_pct: 36.9
turn_under20_pct: 55.3
turn_over200_pct: 0.0
attr_say_pct: 8.5
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 3.0
turn_len_median: 20
```
