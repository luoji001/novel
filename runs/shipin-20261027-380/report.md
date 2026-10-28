# 铜推子 生成报告

slug：`shipin-20261027-380`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6713
LLM 调用：57 次，累计 137.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜推子落地声 | 622 | short | 38.8 | 0 |  | 1 |
| 2 | 铜推子划过镜面 | 1453 | normal | 91.8 | 0 |  | 1 |
| 3 | 铜推子轻触地面 | 1272 | normal | 36.2 | 0 |  | 2 |
| 4 | 纸币在床底翻滚 | 1283 | normal | 55.9 | 0 |  | 2 |
| 5 | 铜推子碰桌角 | 1121 | normal | 93.9 | 0 |  | 0 |
| 6 | 纸片落满青砖地 | 956 | normal | 36.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 570 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 31.8 低于目标 35.0
- 第 3 章：
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
  - [observe] 标题与《铜推子落地声》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - dialogue_chars_pct 3.4 低于目标 5.0
  - narration_para_pct 94.4 高于目标 90.0
- 第 6 章：
  - 单条套路句式超限：「老张站在」×3
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 章内自我复读 1 句（如「老张的声音低沉，带着压抑的怒火…」）

## 整书结构指标

```
chapters: 6
total_chars: 6321
chapter_chars_mean: 1054
chapter_chars_median: 1113
chapter_chars_cv: 0.28
paragraphs_mean: 24.8
dialogue_chars_pct: 21.8
dialogue_para_pct: 46.4
interiority_para_pct: 1.0
narration_para_pct: 52.5
turn_under20_pct: 78.0
turn_over200_pct: 0.0
attr_say_pct: 59.9
attr_adv_pct: 4.7
scenes_per_chapter: 1.7
dialogue_run_mean: 1.9
turn_len_median: 10
```
