# 信笺 生成报告

slug：`aiyuce-20261021-174`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11784
LLM 调用：53 次，累计 205.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 会议桌上的合同签署 | 1266 | normal | 93.6 | 0 |  | 0 |
| 2 | 核对技术服务费明细 | 2177 | normal | 37.6 | 0 |  | 2 |
| 3 | 核对报价单金额变化 | 2251 | normal | 36.0 | 0 |  | 3 |
| 4 | 核对合同条款差异 | 2308 | normal | 35.5 | 0 |  | 2 |
| 5 | 核对芯片价格涨幅 | 2539 | normal | 34.7 | 0 |  | 2 |
| 6 | 核对合同条款差异 | 1237 | short | 35.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 35.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - interiority_para_pct 42.9 高于目标 40.0
  - narration_para_pct 21.4 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「不过，他也清楚地知道，这条推论会被什么推翻——如…」）
- 第 4 章：
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被具体的合同样本以及最终执行结果所验证…」）
- 第 5 章：
  - 单条套路句式超限：「上海开源模型开发公司」×3
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对合同条款差异」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11531
chapter_chars_mean: 1922
chapter_chars_median: 2169
chapter_chars_cv: 0.29
paragraphs_mean: 12.3
dialogue_chars_pct: 5.8
dialogue_para_pct: 36.4
interiority_para_pct: 21.7
narration_para_pct: 41.9
turn_under20_pct: 69.5
turn_over200_pct: 0.0
attr_say_pct: 10.6
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 1.4
turn_len_median: 12
```
