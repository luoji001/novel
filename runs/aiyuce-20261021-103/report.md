# 代码复查 生成报告

slug：`aiyuce-20261021-103`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13211
LLM 调用：57 次，累计 232.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 调整任务分配方案 | 2681 | normal | 94.2 | 0 |  | 2 |
| 2 | 重新标注数据集 | 2310 | normal | 35.6 | 0 |  | 2 |
| 3 | 对比两份项目进度表 | 2449 | normal | 34.6 | 0 |  | 1 |
| 4 | 画折线图 | 2133 | normal | 87.5 | 0 |  | 2 |
| 5 | 检查代码审核报告 | 2240 | normal | 34.8 | 0 |  | 1 |
| 6 | 检查代码审核报告 | 1392 | short | 34.1 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 19.2 高于目标 18.0
  - narration_para_pct 31.6 低于目标 45.0
- 第 2 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 23.3 高于目标 18.0
  - narration_para_pct 27.8 低于目标 45.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 30.7 高于目标 18.0
  - narration_para_pct 35.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「检查代码审核报告」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12915
chapter_chars_mean: 2152
chapter_chars_median: 2228
chapter_chars_cv: 0.2
paragraphs_mean: 16.5
dialogue_chars_pct: 12.9
dialogue_para_pct: 37.8
interiority_para_pct: 13.5
narration_para_pct: 48.7
turn_under20_pct: 49.1
turn_over200_pct: 0.0
attr_say_pct: 16.5
attr_adv_pct: 1.6
scenes_per_chapter: 1.2
dialogue_run_mean: 1.9
turn_len_median: 22
```
