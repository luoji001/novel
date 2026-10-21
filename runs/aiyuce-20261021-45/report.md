# 批改笔 生成报告

slug：`aiyuce-20261021-45`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11185
LLM 调用：57 次，累计 207.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻开听课记录本 | 1972 | normal | 83.9 | 0 |  | 3 |
| 2 | 翻开批改时间统计表 | 1627 | normal | 86.0 | 0 |  | 2 |
| 3 | 翻开费用明细表 | 2118 | normal | 33.3 | 0 |  | 3 |
| 4 | 翻开作文批改对比表 | 2240 | normal | 83.9 | 0 |  | 2 |
| 5 | 翻开满意度调查问卷 | 1975 | normal | 34.2 | 0 |  | 3 |
| 6 | 翻开听课记录本 | 1247 | short | 34.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 45.4 高于目标 18.0
  - dialogue_run_mean 7.5 高于目标 4.0
  - narration_para_pct 10.5 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 38.1 高于目标 18.0
  - narration_para_pct 31.2 低于目标 45.0
- 第 3 章：
  - dialogue_chars_pct 41.6 高于目标 18.0
  - narration_para_pct 35.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 31.7 高于目标 18.0
  - narration_para_pct 21.7 低于目标 45.0
- 第 5 章：
  - dialogue_chars_pct 32.8 高于目标 18.0
  - narration_para_pct 22.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 23.7 高于目标 18.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「翻开听课记录本」已存在

## 整书结构指标

```
chapters: 6
total_chars: 10877
chapter_chars_mean: 1813
chapter_chars_median: 1920
chapter_chars_cv: 0.2
paragraphs_mean: 17.2
dialogue_chars_pct: 36.2
dialogue_para_pct: 62.8
interiority_para_pct: 10.2
narration_para_pct: 26.9
turn_under20_pct: 28.4
turn_over200_pct: 0.0
attr_say_pct: 20.6
attr_adv_pct: 6.1
scenes_per_chapter: 1.3
dialogue_run_mean: 3.3
turn_len_median: 31
```
