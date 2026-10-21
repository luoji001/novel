# 电表 生成报告

slug：`aiyuce-20261021-28`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12369
LLM 调用：53 次，累计 228.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 查看机房用电明细表 | 1398 | normal | 94.6 | 0 |  | 1 |
| 2 | 勾画电价基准值 | 2390 | normal | 88.5 | 0 |  | 0 |
| 3 | 手指划过电价涨幅数字 | 2396 | normal | 88.1 | 0 |  | 0 |
| 4 | 手指划过电价涨幅数字 | 2281 | normal | 34.8 | 0 |  | 2 |
| 5 | 核对电费明细表 | 2371 | normal | 87.9 | 0 |  | 0 |
| 6 | 手指划过电价涨幅数字 | 1527 | short | 34.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 44.4 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「手指划过电价涨幅数字」已存在
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「手指划过电价涨幅数字」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12090
chapter_chars_mean: 2015
chapter_chars_median: 2280
chapter_chars_cv: 0.23
paragraphs_mean: 13.8
dialogue_chars_pct: 3.6
dialogue_para_pct: 22.9
interiority_para_pct: 18.1
narration_para_pct: 59.0
turn_under20_pct: 75.7
turn_over200_pct: 0.0
attr_say_pct: 18.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.2
turn_len_median: 6
```
