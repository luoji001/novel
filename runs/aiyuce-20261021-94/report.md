# 标尺 生成报告

slug：`aiyuce-20261021-94`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12764
LLM 调用：57 次，累计 214.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 工资单核对 | 2487 | normal | 95.0 | 0 |  | 0 |
| 2 | 报价单核对 | 2414 | normal | 88.3 | 0 |  | 1 |
| 3 | 核对工资单 | 1868 | normal | 89.4 | 0 |  | 3 |
| 4 | 折旧表核对 | 2247 | normal | 36.7 | 0 |  | 1 |
| 5 | 薪资标准调整 | 2356 | normal | 23.7 | 0 |  | 1 |
| 6 | 查看证书发放记录 | 1386 | short | 87.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 标题与《工资单核对》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
  - narration_para_pct 30.8 低于目标 45.0
  - [observe] 标题与《工资单核对》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - interiority_para_pct 63.6 高于目标 40.0
  - narration_para_pct 27.3 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 12508
chapter_chars_mean: 2085
chapter_chars_median: 2258
chapter_chars_cv: 0.2
paragraphs_mean: 14
dialogue_chars_pct: 3.0
dialogue_para_pct: 16.6
interiority_para_pct: 19.0
narration_para_pct: 64.4
turn_under20_pct: 67.8
turn_over200_pct: 0.0
attr_say_pct: 28.6
attr_adv_pct: 28.6
scenes_per_chapter: 1.3
dialogue_run_mean: 1.2
turn_len_median: 19
```
