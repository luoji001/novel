# AI扫描仪 生成报告

slug：`aiyuce-20261021-75`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11987
LLM 调用：57 次，累计 228.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对招聘JD数据 | 2130 | normal | 96.3 | 0 |  | 0 |
| 2 | 核对年度报告数据 | 2127 | normal | 36.4 | 0 |  | 2 |
| 3 | 敲击电费单 | 2242 | normal | 35.2 | 0 |  | 1 |
| 4 | 展开报价单 | 2081 | normal | 34.6 | 0 |  | 3 |
| 5 | 核对折旧表数据 | 2027 | normal | 32.8 | 0 |  | 4 |
| 6 | 核对招聘JD数据 | 1374 | short | 90.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 62.9 高于目标 18.0
  - narration_para_pct 16.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 34.9 高于目标 18.0
  - dialogue_run_mean 5 高于目标 4.0
  - narration_para_pct 22.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 标题重复：「核对招聘JD数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11694
chapter_chars_mean: 1949
chapter_chars_median: 2050
chapter_chars_cv: 0.16
paragraphs_mean: 16.5
dialogue_chars_pct: 21.3
dialogue_para_pct: 47.5
interiority_para_pct: 9.7
narration_para_pct: 42.8
turn_under20_pct: 43.3
turn_over200_pct: 0.0
attr_say_pct: 9.1
attr_adv_pct: 2.6
scenes_per_chapter: 1.5
dialogue_run_mean: 2.5
turn_len_median: 24
```
