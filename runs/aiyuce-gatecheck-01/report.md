# 听评课本 生成报告

slug：`aiyuce-gatecheck-01`
档位：AI 推演　闸门模式：defect
章数：6　总字数：9081
LLM 调用：109 次，累计 538.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 听课记录表的更新 | 1393 | normal | 93.5 | 1 |  | 0 |
| 2 | 作文样本的实时比对 | 1942 | normal | 36.7 | 3 | 是 | 1 |
| 3 | 检查写作教学时间变化 | 1678 | normal | 36.3 | 3 | 是 | 2 |
| 4 | 预算明细的改动 | 1531 | normal | 86.2 | 0 |  | 2 |
| 5 | 作文样本集的更新 | 1661 | normal | 33.8 | 3 | 是 | 4 |
| 6 | 翻看泛黄听课记录表 | 870 | short | 89.0 | 1 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [degraded] 章内自我复读 1 句（如「这条推论会被什么样的情况推翻…」）
- 第 3 章：
  - narration_para_pct 33.3 低于目标 45.0
  - [degraded] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 29.3 高于目标 18.0
  - narration_para_pct 30.8 低于目标 45.0
- 第 5 章：
  - dialogue_chars_pct 49.0 高于目标 18.0
  - dialogue_run_mean 4.7 高于目标 4.0
  - narration_para_pct 22.2 低于目标 45.0
  - [degraded] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - narration_para_pct 33.3 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 8834
chapter_chars_mean: 1472
chapter_chars_median: 1550
chapter_chars_cv: 0.24
paragraphs_mean: 11.8
dialogue_chars_pct: 16.3
dialogue_para_pct: 42.4
interiority_para_pct: 12.4
narration_para_pct: 45.2
turn_under20_pct: 55.5
turn_over200_pct: 0.0
attr_say_pct: 10.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.7
turn_len_median: 22
```
