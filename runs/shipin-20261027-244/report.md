# 红灯 生成报告

slug：`shipin-20261027-244`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6188
LLM 调用：57 次，累计 138.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 应急灯的红光 | 456 | short | 37.8 | 0 |  | 1 |
| 2 | 铅笔的痕迹 | 1051 | normal | 36.1 | 0 |  | 2 |
| 3 | 保温杯的刻痕 | 1125 | normal | 94.1 | 0 |  | 1 |
| 4 | 书包的裂痕 | 994 | normal | 92.5 | 0 |  | 0 |
| 5 | 铅笔的断口 | 1138 | normal | 92.6 | 0 |  | 2 |
| 6 | 应急灯的摇晃 | 1418 | normal | 94.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 414 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「”王小明低」×3
  - [observe] 章内自我复读 2 句（如「王小明抬起头，眼中满是委屈与慌乱…」）
- 第 3 章：
  - narration_para_pct 34.6 低于目标 35.0
- 第 5 章：
  - 单条套路句式超限：「王小明的」×4
  - [observe] 标题与《铅笔的痕迹》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 命中套话收尾句
  - 单条套路句式超限：「王小明的」×3
  - [observe] 标题与《应急灯的红光》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5732
chapter_chars_mean: 955
chapter_chars_median: 997
chapter_chars_cv: 0.31
paragraphs_mean: 28.3
dialogue_chars_pct: 26.1
dialogue_para_pct: 56.0
interiority_para_pct: 1.0
narration_para_pct: 43.0
turn_under20_pct: 91.2
turn_over200_pct: 0.0
attr_say_pct: 24.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.1
turn_len_median: 9
```
