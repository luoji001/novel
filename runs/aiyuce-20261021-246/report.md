# 报价单 生成报告

slug：`aiyuce-20261021-246`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12905
LLM 调用：57 次，累计 231.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 拨通A公司电话 | 2424 | normal | 95.7 | 0 |  | 1 |
| 2 | 核对报价单与成本报告 | 2466 | normal | 88.6 | 0 |  | 0 |
| 3 | 核对账户明细 | 2071 | normal | 36.3 | 0 |  | 1 |
| 4 | 核对报价单与成本报告 | 2199 | normal | 86.9 | 0 |  | 2 |
| 5 | 核对报价单与成本报告 | 2287 | normal | 35.0 | 0 |  | 2 |
| 6 | 核对成本报告细节 | 1452 | short | 88.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 26.7 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 标题重复：「核对报价单与成本报告」已存在
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对报价单与成本报告」已存在
- 第 6 章：
  - [observe] 标题与《核对报价单与成本报告》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 12622
chapter_chars_mean: 2104
chapter_chars_median: 2189
chapter_chars_cv: 0.17
paragraphs_mean: 14.8
dialogue_chars_pct: 5.4
dialogue_para_pct: 26.0
interiority_para_pct: 17.3
narration_para_pct: 56.7
turn_under20_pct: 67.8
turn_over200_pct: 0.0
attr_say_pct: 25.3
attr_adv_pct: 4.9
scenes_per_chapter: 2.3
dialogue_run_mean: 1.3
turn_len_median: 14
```
