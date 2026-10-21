# 执照 生成报告

slug：`aiyuce-20261021-238`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12934
LLM 调用：57 次，累计 229.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对工资结算单 | 2040 | normal | 59.4 | 0 |  | 0 |
| 2 | 核对客户订单明细表 | 2559 | normal | 35.7 | 0 |  | 2 |
| 3 | 核对客户订单明细表 | 2483 | normal | 88.0 | 0 |  | 1 |
| 4 | 核对客户订单明细表 | 2432 | normal | 34.7 | 0 |  | 3 |
| 5 | 核对客户订单明细表 | 2098 | normal | 86.3 | 0 |  | 3 |
| 6 | 核对客户订单明细表 | 1316 | short | 82.4 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 标题重复：「核对客户订单明细表」已存在
- 第 4 章：
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对客户订单明细表」已存在
- 第 5 章：
  - interiority_para_pct 43.8 高于目标 40.0
  - narration_para_pct 31.2 低于目标 45.0
  - [observe] 标题重复：「核对客户订单明细表」已存在
- 第 6 章：
  - dialogue_chars_pct 73.1 高于目标 18.0
  - dialogue_run_mean 10.5 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题重复：「核对客户订单明细表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12634
chapter_chars_mean: 2106
chapter_chars_median: 2218
chapter_chars_cv: 0.22
paragraphs_mean: 16.2
dialogue_chars_pct: 10.7
dialogue_para_pct: 31.7
interiority_para_pct: 27.7
narration_para_pct: 40.6
turn_under20_pct: 67.8
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 2.9
turn_len_median: 13
```
