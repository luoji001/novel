# 电费单 生成报告

slug：`aiyuce-20261021-222`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12139
LLM 调用：57 次，累计 220.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲打桌面 | 1741 | normal | 93.1 | 0 |  | 2 |
| 2 | 电费单增长数据 | 2164 | normal | 90.0 | 0 |  | 0 |
| 3 | 核对折旧表数据 | 2348 | normal | 59.5 | 0 |  | 0 |
| 4 | 敲击键盘 | 2055 | normal | 89.2 | 0 |  | 2 |
| 5 | 敲开玻璃窗 | 2485 | normal | 36.4 | 0 |  | 3 |
| 6 | 核对报价单涨幅 | 1340 | short | 89.7 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 28.5 高于目标 18.0
  - narration_para_pct 18.8 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 18.5 高于目标 18.0
  - narration_para_pct 25.0 低于目标 45.0
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3
  - narration_para_pct 43.8 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「如果不尽快处理这个问题，不仅会影响到招聘进度，还…」）

## 整书结构指标

```
chapters: 6
total_chars: 11877
chapter_chars_mean: 1980
chapter_chars_median: 2064
chapter_chars_cv: 0.21
paragraphs_mean: 14.5
dialogue_chars_pct: 8.8
dialogue_para_pct: 27.2
interiority_para_pct: 19.2
narration_para_pct: 53.6
turn_under20_pct: 66.8
turn_over200_pct: 0.0
attr_say_pct: 10.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.4
turn_len_median: 11
```
