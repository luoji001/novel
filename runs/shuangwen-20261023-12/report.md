# 旧卡 生成报告

slug：`shuangwen-20261023-12`
档位：爽文　闸门模式：observe
章数：10　总字数：18596
LLM 调用：97 次，累计 418.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钱的重量 | 1709 | normal | 98.2 | 0 |  | 1 |
| 2 | 借书卡的年代 | 2143 | normal | 94.4 | 0 |  | 0 |
| 3 | 借书卡的边缘 | 1650 | normal | 93.6 | 0 |  | 1 |
| 4 | 铜牌的共鸣 | 1973 | normal | 93.9 | 0 |  | 0 |
| 5 | 铜牌与章程的对峙 | 1666 | normal | 36.5 | 0 |  | 1 |
| 6 | 铜牌与旧卡的对峙 | 1704 | normal | 92.4 | 0 |  | 5 |
| 7 | 旧卡的磨损 | 1922 | normal | 93.7 | 0 |  | 0 |
| 8 | 旧卡的归还 | 1508 | normal | 91.8 | 0 |  | 1 |
| 9 | 章程的边缘 | 1792 | normal | 94.0 | 0 |  | 1 |
| 10 | 青铜手令的封印 | 2519 | long | 91.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 3.3 低于目标 5.0
- 第 3 章：
  - [observe] 标题与《借书卡的年代》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「陆怀瑾的」×4
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - dialogue_run_mean 17 高于目标 14.0
  - [observe] 标题与《铜牌与章程的对峙》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - [observe] 标题与《旧卡的磨损》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「陆怀瑾的」×6
- 第 10 章：
  - 单条套路句式超限：「陆怀瑾的」×7、「沈知远的」×3
  - attr_adv_pct 18.5 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 17599
chapter_chars_mean: 1760
chapter_chars_median: 1670
chapter_chars_cv: 0.15
paragraphs_mean: 40.9
dialogue_chars_pct: 46.1
dialogue_para_pct: 84.0
interiority_para_pct: 7.0
narration_para_pct: 9.0
turn_under20_pct: 76.3
turn_over200_pct: 0.0
attr_say_pct: 29.8
attr_adv_pct: 9.3
scenes_per_chapter: 1.5
dialogue_run_mean: 6.8
turn_len_median: 12
```
