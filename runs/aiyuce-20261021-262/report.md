# 单价钟 生成报告

slug：`aiyuce-20261021-262`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11817
LLM 调用：57 次，累计 212.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单的核对过程 | 1803 | normal | 37.1 | 0 |  | 1 |
| 2 | 招聘JD的修改 | 2329 | normal | 92.0 | 0 |  | 0 |
| 3 | 绩效考核表的修改 | 2113 | normal | 36.2 | 0 |  | 2 |
| 4 | 报价单的反复确认 | 2044 | normal | 36.2 | 0 |  | 1 |
| 5 | 供应商评估报告的分析 | 2221 | normal | 88.1 | 0 |  | 1 |
| 6 | 折旧表的凝视时刻 | 1301 | short | 89.6 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 33.3 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11564
chapter_chars_mean: 1927
chapter_chars_median: 2036
chapter_chars_cv: 0.19
paragraphs_mean: 12.5
dialogue_chars_pct: 3.2
dialogue_para_pct: 24.9
interiority_para_pct: 16.4
narration_para_pct: 58.7
turn_under20_pct: 78.4
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.4
turn_len_median: 10
```
