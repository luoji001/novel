# 笔记 生成报告

slug：`shuangwen-20261023-77`
档位：爽文　闸门模式：observe
章数：10　总字数：19265
LLM 调用：97 次，累计 418.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指轻叩桌面 | 2155 | normal | 39.6 | 0 |  | 2 |
| 2 | 翻开教学笔记 | 2345 | normal | 37.7 | 0 |  | 1 |
| 3 | 手指轻触审批栏 | 1562 | normal | 90.5 | 0 |  | 0 |
| 4 | 手指轻压审批栏 | 1574 | normal | 93.2 | 0 |  | 1 |
| 5 | 手指轻抚评分表 | 2044 | normal | 91.7 | 0 |  | 0 |
| 6 | 手指轻敲桌面 | 1623 | normal | 91.5 | 0 |  | 3 |
| 7 | 手指轻抚评分表 | 1890 | normal | 36.7 | 0 |  | 3 |
| 8 | 手指轻抚银行卡 | 1835 | normal | 36.7 | 0 |  | 3 |
| 9 | 文件轻落桌面 | 1733 | normal | 92.9 | 0 |  | 0 |
| 10 | 手指轻抚教学笔记 | 2494 | long | 93.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×3
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 2 章：
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 4 章：
  - [observe] 标题与《手指轻触审批栏》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 命中套话收尾句
  - narration_para_pct 3.3 低于目标 5.0
  - [observe] 标题与《手指轻叩桌面》近似 0.83 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「林小雨的」×4
  - [observe] attr_adv_pct 50.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「手指轻抚评分表」已存在
- 第 8 章：
  - 单条套路句式超限：「林小雨的」×3
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 与历史章节逐字重复 3 句（如「好吧，我可以给你一次机会…」）
- 第 10 章：
  - 单条套路句式超限：「李国强的」×4、「林小雨的」×4

## 整书结构指标

```
chapters: 10
total_chars: 18381
chapter_chars_mean: 1838
chapter_chars_median: 1780
chapter_chars_cv: 0.17
paragraphs_mean: 36.4
dialogue_chars_pct: 46.7
dialogue_para_pct: 79.7
interiority_para_pct: 7.6
narration_para_pct: 12.7
turn_under20_pct: 64.3
turn_over200_pct: 0.0
attr_say_pct: 28.8
attr_adv_pct: 17.2
scenes_per_chapter: 2.4
dialogue_run_mean: 6.0
turn_len_median: 15
```
