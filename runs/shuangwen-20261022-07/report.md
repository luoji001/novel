# 过磅单 生成报告

slug：`shuangwen-20261022-07`
档位：爽文　闸门模式：observe
章数：10　总字数：19133
LLM 调用：97 次，累计 373.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 打印机卡纸事件 | 1358 | normal | 97.2 | 0 |  | 1 |
| 2 | 监控录像显示时间差 | 1984 | normal | 95.2 | 0 |  | 2 |
| 3 | 纸屑飘入垃圾桶 | 2167 | normal | 93.5 | 0 |  | 2 |
| 4 | 打印机吞吐数据 | 1679 | normal | 36.8 | 0 |  | 1 |
| 5 | 纸币堆中露出一角单 | 1722 | normal | 93.3 | 0 |  | 1 |
| 6 | 打印纸铺满桌面 | 1682 | normal | 37.1 | 0 |  | 4 |
| 7 | 打印机吐出第二份数据 | 2101 | normal | 93.5 | 0 |  | 2 |
| 8 | 签字笔划破纸张 | 1866 | normal | 37.7 | 0 |  | 3 |
| 9 | 原始记录被撕毁 | 2319 | normal | 94.5 | 0 |  | 2 |
| 10 | 名册摊开在桌面 | 2245 | long | 91.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 14.3 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「周海峰的」×5
  - attr_adv_pct 22.2 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 16.0 高于目标 12.0
- 第 4 章：
  - [observe] attr_adv_pct 36.4 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「周海峰的」×5
- 第 6 章：
  - 单条套路句式超限：「周海峰的」×3
  - narration_para_pct 3.2 低于目标 5.0
  - dialogue_run_mean 14.5 高于目标 14.0
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 7 章：
  - 单条套路句式超限：「周海峰的」×3
  - [observe] 标题与《打印机吞吐数据》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「周海峰的」×3
  - narration_para_pct 2.9 低于目标 5.0
  - [observe] attr_adv_pct 37.5 > 25.0（结构塌缩）
- 第 9 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 14.8 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「陈志远的」×8
  - narration_para_pct 0.0 低于目标 5.0

## 整书结构指标

```
chapters: 10
total_chars: 18184
chapter_chars_mean: 1818
chapter_chars_median: 1840
chapter_chars_cv: 0.16
paragraphs_mean: 39.1
dialogue_chars_pct: 51.5
dialogue_para_pct: 87.6
interiority_para_pct: 5.2
narration_para_pct: 7.2
turn_under20_pct: 72.3
turn_over200_pct: 0.0
attr_say_pct: 21.4
attr_adv_pct: 18.9
scenes_per_chapter: 2.1
dialogue_run_mean: 8.2
turn_len_median: 13
```
