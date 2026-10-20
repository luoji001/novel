# 旧账单 生成报告

slug：`xuanyi-20261019-17`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15249
LLM 调用：68 次，累计 234.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 编号的双影 | 1821 | short | 98.5 | 0 |  | 1 |
| 2 | 纸箱的异样痕迹 | 4048 | normal | 88.5 | 0 |  | 3 |
| 3 | 电子秤的校准异常 | 3892 | normal | 88.2 | 0 |  | 3 |
| 4 | 纸箱的双重编号 | 3605 | normal | 88.6 | 0 |  | 2 |
| 5 | 纸箱的双重日期 | 1878 | short | 91.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈志强的」×5
- 第 2 章：
  - 单条套路句式超限：「周慧玲的」×4、「他知道这」×4
  - narration_para_pct 11.0 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「小李没有立刻回答，而是指着快递单上的地址部分说道…」）
- 第 3 章：
  - narration_para_pct 3.9 低于目标 20.0
  - attr_adv_pct 12.7 高于目标 10.0
  - dialogue_run_mean 10.2 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「点了点头」×4、「周慧玲点」×3、「为什么会」×3
  - narration_para_pct 9.1 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「点了点头」×3
  - narration_para_pct 5.9 低于目标 20.0
  - [observe] 标题与《纸箱的双重编号》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 14509
chapter_chars_mean: 2902
chapter_chars_median: 3459
chapter_chars_cv: 0.36
paragraphs_mean: 66.2
dialogue_chars_pct: 41.0
dialogue_para_pct: 81.9
interiority_para_pct: 8.0
narration_para_pct: 10.1
turn_under20_pct: 73.0
turn_over200_pct: 0.0
attr_say_pct: 20.5
attr_adv_pct: 5.2
scenes_per_chapter: 1.8
dialogue_run_mean: 6.2
turn_len_median: 12
```
