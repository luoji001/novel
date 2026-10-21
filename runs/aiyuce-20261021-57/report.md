# 作文样本分析 生成报告

slug：`aiyuce-20261021-57`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11946
LLM 调用：57 次，累计 219.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 修改听课安排 | 1955 | normal | 37.8 | 0 |  | 1 |
| 2 | AI反馈报告 | 2434 | normal | 33.8 | 0 |  | 4 |
| 3 | 预算报表 | 2118 | normal | 88.7 | 0 |  | 2 |
| 4 | AI反馈报告 | 2152 | normal | 35.4 | 0 |  | 3 |
| 5 | 工作量统计表 | 1928 | normal | 36.9 | 0 |  | 2 |
| 6 | 翻看作文样本集 | 1353 | short | 89.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - dialogue_chars_pct 25.2 高于目标 18.0
  - dialogue_run_mean 7 高于目标 4.0
  - narration_para_pct 17.6 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「但他很快意识到，仅仅依靠经济因素还不足以说服所有…」）
- 第 3 章：
  - dialogue_chars_pct 27.2 高于目标 18.0
  - narration_para_pct 23.5 低于目标 45.0
- 第 4 章：
  - narration_para_pct 29.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「AI反馈报告」已存在
- 第 5 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - narration_para_pct 25.0 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11675
chapter_chars_mean: 1946
chapter_chars_median: 1990
chapter_chars_cv: 0.18
paragraphs_mean: 15.2
dialogue_chars_pct: 16.6
dialogue_para_pct: 54.9
interiority_para_pct: 15.0
narration_para_pct: 30.0
turn_under20_pct: 42.1
turn_over200_pct: 0.0
attr_say_pct: 9.5
attr_adv_pct: 8.5
scenes_per_chapter: 1.5
dialogue_run_mean: 3.0
turn_len_median: 20
```
