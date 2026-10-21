# 数据镜 生成报告

slug：`aiyuce-20261021-257`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12066
LLM 调用：57 次，累计 217.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击桌面 | 2369 | normal | 38.0 | 0 |  | 1 |
| 2 | 核对招聘JD条款 | 2221 | normal | 89.3 | 0 |  | 0 |
| 3 | 核对考勤记录 | 2103 | normal | 35.6 | 0 |  | 1 |
| 4 | 敲击桌面 | 2051 | normal | 35.2 | 0 |  | 4 |
| 5 | 敲击键盘 | 1965 | normal | 85.9 | 0 |  | 2 |
| 6 | 敲击键盘 | 1351 | short | 36.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「一条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 30.6 高于目标 18.0
  - narration_para_pct 17.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻？…」）
  - [observe] 标题重复：「敲击桌面」已存在
- 第 5 章：
  - dialogue_chars_pct 32.6 高于目标 18.0
  - narration_para_pct 11.8 低于目标 45.0
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「不过，目前的数据确实还存在一些偏差…」）
  - [observe] 标题重复：「敲击键盘」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11802
chapter_chars_mean: 1967
chapter_chars_median: 2031
chapter_chars_cv: 0.18
paragraphs_mean: 15
dialogue_chars_pct: 13.5
dialogue_para_pct: 38.1
interiority_para_pct: 13.2
narration_para_pct: 48.7
turn_under20_pct: 71.7
turn_over200_pct: 0.0
attr_say_pct: 5.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 2.1
turn_len_median: 12
```
