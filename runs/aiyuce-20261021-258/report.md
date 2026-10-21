# 报价单 生成报告

slug：`aiyuce-20261021-258`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11469
LLM 调用：57 次，累计 210.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 报价单上的三个数字 | 1819 | normal | 95.2 | 0 |  | 1 |
| 2 | 电费单上的数字变化 | 1893 | normal | 34.4 | 0 |  | 1 |
| 3 | 核对合同条款 | 1884 | normal | 35.8 | 0 |  | 3 |
| 4 | 招聘JD上的新要求 | 2412 | normal | 36.8 | 0 |  | 1 |
| 5 | 核对折旧表数据 | 1896 | normal | 35.4 | 0 |  | 1 |
| 6 | 价格变化触发市场反应 | 1559 | short | 36.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「杭州开源模型开发团队」×3
- 第 2 章：
  - [observe] 章内自我复读 4 句（如「如果后续数据显示用电量的增长主要来自于冷却系统的…」）
- 第 3 章：
  - dialogue_chars_pct 28.8 高于目标 18.0
  - narration_para_pct 38.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「如果在未来三个月内，公司能够通过自动化工具或流程…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - 单条套路句式超限：「杭州开源模型开发团队」×3
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 11201
chapter_chars_mean: 1867
chapter_chars_median: 1842
chapter_chars_cv: 0.15
paragraphs_mean: 13.7
dialogue_chars_pct: 5.8
dialogue_para_pct: 16.6
interiority_para_pct: 10.4
narration_para_pct: 73.1
turn_under20_pct: 37.4
turn_over200_pct: 0.0
attr_say_pct: 65.0
attr_adv_pct: 8.7
scenes_per_chapter: 1.2
dialogue_run_mean: 1.5
turn_len_median: 28
```
