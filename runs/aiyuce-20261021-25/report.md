# 代写价签 生成报告

slug：`aiyuce-20261021-25`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12121
LLM 调用：57 次，累计 206.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 营业额报表对比分析 | 2157 | normal | 38.2 | 0 |  | 1 |
| 2 | 核对电费单数字 | 2204 | normal | 36.0 | 0 |  | 1 |
| 3 | 核对工资明细表 | 2176 | normal | 91.5 | 0 |  | 1 |
| 4 | 核对AI报价单数字 | 1739 | normal | 87.3 | 0 |  | 3 |
| 5 | 核对用户反馈记录 | 2362 | normal | 91.5 | 0 |  | 0 |
| 6 | 核对营业额报表数据 | 1477 | short | 91.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「不过总体来说，眼下看来似乎仍然面临着不小的困难…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 26.7 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 42.6 高于目标 18.0
  - narration_para_pct 14.3 低于目标 45.0
  - [observe] 标题与《核对电费单数字》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 33.3 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11828
chapter_chars_mean: 1971
chapter_chars_median: 2120
chapter_chars_cv: 0.17
paragraphs_mean: 15.8
dialogue_chars_pct: 8.1
dialogue_para_pct: 27.6
interiority_para_pct: 21.3
narration_para_pct: 51.0
turn_under20_pct: 85.1
turn_over200_pct: 0.0
attr_say_pct: 6.3
attr_adv_pct: 2.1
scenes_per_chapter: 1.2
dialogue_run_mean: 1.7
turn_len_median: 8
```
