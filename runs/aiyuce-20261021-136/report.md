# 电网维护预算表 生成报告

slug：`aiyuce-20261021-136`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13748
LLM 调用：57 次，累计 237.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 三张电费单 | 2047 | normal | 38.0 | 0 |  | 1 |
| 2 | 一通调度中心电话 | 2801 | normal | 92.1 | 0 |  | 1 |
| 3 | 报价单被转发至技术组 | 2427 | normal | 35.7 | 0 |  | 1 |
| 4 | 设备老化讨论会 | 2427 | normal | 35.5 | 0 |  | 1 |
| 5 | 线路改造费用明细 | 2490 | normal | 34.7 | 0 |  | 1 |
| 6 | 新增监控节点 | 1550 | short | 88.4 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 2 句（如「因此对于现状来说，至少可以确定的是现行制度确实造…」）
- 第 2 章：
  - narration_para_pct 42.9 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 2 句（如「这些补充材料最终被供电局采纳，并作为后续审批的重…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 13456
chapter_chars_mean: 2243
chapter_chars_median: 2376
chapter_chars_cv: 0.19
paragraphs_mean: 16.2
dialogue_chars_pct: 4.5
dialogue_para_pct: 19.2
interiority_para_pct: 12.1
narration_para_pct: 68.7
turn_under20_pct: 58.1
turn_over200_pct: 0.0
attr_say_pct: 15.5
attr_adv_pct: 53.5
scenes_per_chapter: 1
dialogue_run_mean: 1.4
turn_len_median: 18
```
