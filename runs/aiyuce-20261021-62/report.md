# 电表 生成报告

slug：`aiyuce-20261021-62`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12667
LLM 调用：57 次，累计 224.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电表读数 | 1833 | normal | 94.3 | 0 |  | 1 |
| 2 | 核对订单记录 | 2277 | normal | 35.9 | 0 |  | 1 |
| 3 | 核对价格表数据 | 2701 | normal | 35.2 | 0 |  | 2 |
| 4 | 核对测试机参数 | 2439 | normal | 36.4 | 0 |  | 1 |
| 5 | 核对折旧计算表 | 2106 | normal | 91.6 | 0 |  | 0 |
| 6 | 核对显卡用电数据 | 1305 | short | 85.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 16.7 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《核对电表读数》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - interiority_para_pct 44.4 高于目标 40.0

## 整书结构指标

```
chapters: 6
total_chars: 12398
chapter_chars_mean: 2066
chapter_chars_median: 2146
chapter_chars_cv: 0.24
paragraphs_mean: 14.5
dialogue_chars_pct: 6.0
dialogue_para_pct: 27.6
interiority_para_pct: 17.5
narration_para_pct: 54.9
turn_under20_pct: 69.2
turn_over200_pct: 0.0
attr_say_pct: 33.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.5
turn_len_median: 19
```
