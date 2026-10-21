# 情绪灯 生成报告

slug：`aiyuce-20261021-269`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12300
LLM 调用：57 次，累计 225.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | AI质检系统测试报告 | 2060 | normal | 37.9 | 0 |  | 1 |
| 2 | 质检主管圈住68%数字 | 2200 | normal | 33.6 | 0 |  | 3 |
| 3 | 预算表 | 2394 | normal | 35.3 | 0 |  | 2 |
| 4 | 翻看客户满意度报告 | 2348 | normal | 35.5 | 0 |  | 2 |
| 5 | 翻看测试报告末页 | 2111 | normal | 35.2 | 0 |  | 3 |
| 6 | 翻看测试报告末页 | 1181 | short | 30.6 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 2 句（如「如果后续数据显示AI质检系统在实际应用中未能显著…」）
- 第 2 章：
  - dialogue_chars_pct 27.4 高于目标 18.0
  - narration_para_pct 26.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 3 章：
  - dialogue_chars_pct 19.8 高于目标 18.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 29.8 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 64.6 高于目标 18.0
  - dialogue_run_mean 7 高于目标 4.0
  - narration_para_pct 12.5 低于目标 45.0
  - [observe] 章内自我复读 5 句（如「我想你的担忧是有道理的。我打算下周开始收集更多的…」）
  - [observe] 标题重复：「翻看测试报告末页」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11979
chapter_chars_mean: 1996
chapter_chars_median: 2098
chapter_chars_cv: 0.22
paragraphs_mean: 17.3
dialogue_chars_pct: 23.4
dialogue_para_pct: 47.9
interiority_para_pct: 12.4
narration_para_pct: 39.8
turn_under20_pct: 45.7
turn_over200_pct: 0.0
attr_say_pct: 42.4
attr_adv_pct: 27.1
scenes_per_chapter: 1.2
dialogue_run_mean: 2.6
turn_len_median: 26
```
