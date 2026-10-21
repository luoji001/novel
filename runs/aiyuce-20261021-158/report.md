# 电单 生成报告

slug：`aiyuce-20261021-158`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12157
LLM 调用：57 次，累计 223.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 报价单上的数字较量 | 1427 | normal | 36.2 | 0 |  | 4 |
| 2 | 招聘JD的显卡销售主管 | 2611 | normal | 88.1 | 0 |  | 0 |
| 3 | 电费单对比分析 | 2361 | normal | 35.1 | 0 |  | 2 |
| 4 | 库存清单的显卡价格 | 2364 | normal | 34.6 | 0 |  | 1 |
| 5 | 折旧表上的剩余价值 | 2367 | normal | 35.1 | 0 |  | 1 |
| 6 | 库存清单的显卡价格 | 1021 | short | 86.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 60.3 高于目标 18.0
  - dialogue_run_mean 5.3 高于目标 4.0
  - narration_para_pct 15.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这场关于显卡和主板之争才刚刚开始…」）
- 第 3 章：
  - dialogue_run_mean 5 高于目标 4.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的数据所推翻呢…」）
- 第 6 章：
  - [observe] 标题重复：「库存清单的显卡价格」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11827
chapter_chars_mean: 1971
chapter_chars_median: 2300
chapter_chars_cv: 0.32
paragraphs_mean: 17.7
dialogue_chars_pct: 15.4
dialogue_para_pct: 31.4
interiority_para_pct: 12.5
narration_para_pct: 56.1
turn_under20_pct: 46.0
turn_over200_pct: 0.0
attr_say_pct: 38.0
attr_adv_pct: 3.2
scenes_per_chapter: 1.2
dialogue_run_mean: 3.0
turn_len_median: 24
```
