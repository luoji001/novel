# 皮重数据 生成报告

slug：`shuangwen-20261023-59`
档位：爽文　闸门模式：observe
章数：10　总字数：19149
LLM 调用：97 次，累计 413.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字权的争夺 | 1628 | normal | 97.3 | 0 |  | 3 |
| 2 | 登记本的指尖滑动 | 2187 | normal | 93.6 | 0 |  | 1 |
| 3 | 打印机吐出纸张 | 1646 | normal | 91.1 | 0 |  | 1 |
| 4 | 数据本的真相 | 2016 | normal | 93.1 | 0 |  | 0 |
| 5 | 撕碎的磅单 | 1685 | normal | 93.7 | 0 |  | 0 |
| 6 | 指纹摩擦计算器键 | 2022 | normal | 94.2 | 0 |  | 1 |
| 7 | 签字的指尖滑动 | 1768 | normal | 93.6 | 0 |  | 2 |
| 8 | 签字的手指滑动 | 1932 | normal | 94.2 | 0 |  | 4 |
| 9 | 手指摩挲纸边 | 1898 | normal | 94.2 | 0 |  | 2 |
| 10 | 手指摩挲纸边 | 2357 | long | 89.6 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×5
  - attr_adv_pct 23.1 高于目标 12.0
  - dialogue_run_mean 15.5 高于目标 14.0
- 第 2 章：
  - narration_para_pct 4.7 低于目标 5.0
- 第 3 章：
  - narration_para_pct 3.4 低于目标 5.0
- 第 6 章：
  - attr_adv_pct 20.0 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「李建国的」×6
  - [observe] 标题与《登记本的指尖滑动》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - narration_para_pct 4.3 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - dialogue_run_mean 14.3 高于目标 14.0
  - [observe] 标题与《签字的指尖滑动》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「李建国的」×4
  - attr_adv_pct 15.0 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「李建国的」×5
  - narration_para_pct 2.3 低于目标 5.0
  - attr_adv_pct 18.8 高于目标 12.0
  - dialogue_run_mean 21.5 高于目标 14.0
  - [observe] 标题重复：「手指摩挲纸边」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18197
chapter_chars_mean: 1820
chapter_chars_median: 1820
chapter_chars_cv: 0.13
paragraphs_mean: 39.7
dialogue_chars_pct: 52.6
dialogue_para_pct: 90.4
interiority_para_pct: 2.8
narration_para_pct: 6.9
turn_under20_pct: 70.1
turn_over200_pct: 0.0
attr_say_pct: 28.5
attr_adv_pct: 12.1
scenes_per_chapter: 2
dialogue_run_mean: 11.8
turn_len_median: 13
```
