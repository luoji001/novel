# 校对小时 生成报告

slug：`aiyuce-20261021-140`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11810
LLM 调用：57 次，累计 217.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 校对主管拨通电话 | 2147 | normal | 38.6 | 0 |  | 2 |
| 2 | 拨打电话核实工时 | 1982 | normal | 34.8 | 0 |  | 3 |
| 3 | 使用记录表的数字变化 | 1969 | normal | 35.0 | 0 |  | 1 |
| 4 | 屏幕上的数据流 | 2270 | normal | 35.4 | 0 |  | 1 |
| 5 | 检查问卷中的异常数据 | 2119 | normal | 90.1 | 0 |  | 3 |
| 6 | 核对错误率的对比数据 | 1317 | short | 34.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 18.3 高于目标 18.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - dialogue_chars_pct 24.7 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「如果我们继续按小时收费的话，在同等条件下会不会更…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 19.5 高于目标 18.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - narration_para_pct 13.3 低于目标 45.0
- 第 6 章：
  - [observe] 章内自我复读 2 句（如「这让校对主管更加确信，当前的计价模式并不是简单的…」）

## 整书结构指标

```
chapters: 6
total_chars: 11529
chapter_chars_mean: 1922
chapter_chars_median: 2000
chapter_chars_cv: 0.17
paragraphs_mean: 14
dialogue_chars_pct: 12.6
dialogue_para_pct: 37.3
interiority_para_pct: 11.0
narration_para_pct: 51.7
turn_under20_pct: 29.8
turn_over200_pct: 0.0
attr_say_pct: 25.2
attr_adv_pct: 2.6
scenes_per_chapter: 1.3
dialogue_run_mean: 2.8
turn_len_median: 26
```
