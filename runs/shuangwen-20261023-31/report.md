# 旧本子 生成报告

slug：`shuangwen-20261023-31`
档位：爽文　闸门模式：observe
章数：10　总字数：18756
LLM 调用：97 次，累计 424.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 工具摆上桌面 | 2101 | normal | 97.8 | 0 |  | 0 |
| 2 | 钢笔划过纸面 | 1812 | normal | 91.7 | 0 |  | 1 |
| 3 | 签字笔的重量 | 1910 | normal | 91.8 | 0 |  | 2 |
| 4 | 钢笔悬空 | 1653 | normal | 92.2 | 0 |  | 0 |
| 5 | 印章压纸 | 1938 | normal | 37.2 | 0 |  | 1 |
| 6 | 旧本子上的日期 | 1682 | normal | 90.9 | 0 |  | 0 |
| 7 | 墨痕压住旧细则 | 1823 | normal | 90.6 | 0 |  | 1 |
| 8 | 旧本子上的反光 | 1546 | normal | 91.5 | 0 |  | 1 |
| 9 | 墨迹覆盖旧细则 | 1831 | normal | 92.2 | 0 |  | 1 |
| 10 | 签字笔悬空 | 2450 | long | 93.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - attr_adv_pct 16.7 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「沈德昌的」×4
  - dialogue_chars_pct 29.5 低于目标 30.0
- 第 5 章：
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 7 章：
  - 单条套路句式超限：「周启明的」×5
- 第 8 章：
  - [observe] 标题与《旧本子上的日期》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「沈德昌的」×5、「周启明的」×4
- 第 10 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 标题与《钢笔悬空》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 10
total_chars: 17925
chapter_chars_mean: 1792
chapter_chars_median: 1748
chapter_chars_cv: 0.14
paragraphs_mean: 34.1
dialogue_chars_pct: 40.8
dialogue_para_pct: 79.3
interiority_para_pct: 7.2
narration_para_pct: 13.6
turn_under20_pct: 65.9
turn_over200_pct: 0.0
attr_say_pct: 26.0
attr_adv_pct: 6.7
scenes_per_chapter: 1.5
dialogue_run_mean: 5.4
turn_len_median: 16
```
