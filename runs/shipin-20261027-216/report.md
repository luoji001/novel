# 应急灯 生成报告

slug：`shipin-20261027-216`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7451
LLM 调用：57 次，累计 144.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 应急灯坠落 | 636 | short | 38.4 | 0 |  | 1 |
| 2 | 应急灯闪烁 | 1323 | normal | 36.5 | 0 |  | 2 |
| 3 | 钢笔轻点纸面 | 1429 | normal | 94.8 | 0 |  | 2 |
| 4 | 蓝色手背的伤痕 | 1565 | normal | 35.8 | 0 |  | 3 |
| 5 | 应急灯与笔记本 | 1198 | normal | 89.9 | 0 |  | 3 |
| 6 | 蓝色纹身浮现 | 1294 | normal | 91.7 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 585 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章内自我复读 6 句（如「李国强望着他消失的身影，轻轻叹了口气，目光落在墙…」）
  - [observe] 标题与《应急灯坠落》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「王小明的」×4
  - narration_para_pct 34.5 低于目标 35.0
- 第 4 章：
  - 单条套路句式超限：「李国强站在」×3、「王小明的」×3、「李国强的」×3
  - interiority_para_pct 7.3 高于目标 6.0
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「李国强的」×3
  - narration_para_pct 21.7 低于目标 35.0
  - dialogue_run_mean 4.5 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 6990
chapter_chars_mean: 1165
chapter_chars_median: 1222
chapter_chars_cv: 0.26
paragraphs_mean: 30.2
dialogue_chars_pct: 25.1
dialogue_para_pct: 58.7
interiority_para_pct: 1.5
narration_para_pct: 39.8
turn_under20_pct: 94.3
turn_over200_pct: 0.0
attr_say_pct: 34.3
attr_adv_pct: 12.7
scenes_per_chapter: 1.8
dialogue_run_mean: 2.2
turn_len_median: 8
```
