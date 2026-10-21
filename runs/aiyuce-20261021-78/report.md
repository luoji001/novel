# 报价单上的数字 生成报告

slug：`aiyuce-20261021-78`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12716
LLM 调用：57 次，累计 218.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击桌面确认数字 | 1985 | normal | 95.1 | 0 |  | 0 |
| 2 | 核对财务报表数字 | 2025 | normal | 36.9 | 0 |  | 1 |
| 3 | 翻阅合同条款 | 2117 | normal | 36.4 | 0 |  | 2 |
| 4 | 核对费用明细 | 2469 | normal | 87.6 | 0 |  | 1 |
| 5 | 核对许可证条款 | 2500 | normal | 36.2 | 0 |  | 1 |
| 6 | 核对成本清单数据 | 1614 | short | 35.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 3 章：
  - 单条套路句式超限：「杭州开源模型项目组」×4
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - interiority_para_pct 41.2 高于目标 40.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12431
chapter_chars_mean: 2072
chapter_chars_median: 2025
chapter_chars_cv: 0.16
paragraphs_mean: 15.5
dialogue_chars_pct: 2.9
dialogue_para_pct: 15.5
interiority_para_pct: 21.5
narration_para_pct: 63.0
turn_under20_pct: 74.5
turn_over200_pct: 0.0
attr_say_pct: 44.2
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 1.5
turn_len_median: 7
```
