# 校对钟 生成报告

slug：`aiyuce-20261021-260`
档位：AI 推演　闸门模式：observe
章数：6　总字数：10997
LLM 调用：57 次，累计 210.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅报价单 | 1907 | normal | 96.3 | 0 |  | 1 |
| 2 | 七百二十小时的校对工作 | 1908 | normal | 35.6 | 0 |  | 2 |
| 3 | 翻阅投诉记录表 | 2083 | normal | 36.5 | 0 |  | 2 |
| 4 | 校对数据对比图 | 1915 | normal | 34.0 | 0 |  | 4 |
| 5 | 翻阅满意度问卷 | 2012 | normal | 79.8 | 0 |  | 4 |
| 6 | 翻阅报价单 | 1166 | short | 34.7 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 41.7 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 20.6 高于目标 18.0
  - [observe] 章内自我复读 2 句（如「我们可以看到，这项技术目前在校对准确度方面已经取…」）
- 第 3 章：
  - narration_para_pct 43.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 48.8 高于目标 18.0
  - dialogue_run_mean 5.3 高于目标 4.0
  - narration_para_pct 15.8 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「比如说，如果有新的数据显示AI在校对某些特定领域…」）
- 第 5 章：
  - 单条套路句式超限：「点了点头」×3、「带着一丝」×3
  - dialogue_chars_pct 59.6 高于目标 18.0
  - dialogue_run_mean 9 高于目标 4.0
  - narration_para_pct 10.0 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 65.1 高于目标 18.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「翻阅报价单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 10703
chapter_chars_mean: 1784
chapter_chars_median: 1866
chapter_chars_cv: 0.18
paragraphs_mean: 16.5
dialogue_chars_pct: 31.2
dialogue_para_pct: 54.2
interiority_para_pct: 12.6
narration_para_pct: 33.2
turn_under20_pct: 53.5
turn_over200_pct: 0.0
attr_say_pct: 12.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 3.6
turn_len_median: 30
```
