# 应急灯的光 生成报告

slug：`shipin-20261027-300`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6410
LLM 调用：57 次，累计 140.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 应急灯的光圈 | 665 | short | 93.8 | 0 |  | 0 |
| 2 | 铅笔盒的裂痕 | 1200 | normal | 93.2 | 0 |  | 0 |
| 3 | 擦灯罩的手势 | 1280 | normal | 91.3 | 0 |  | 3 |
| 4 | 铅笔划破试卷 | 1142 | normal | 92.9 | 0 |  | 2 |
| 5 | 铅笔划过课本 | 1091 | normal | 92.2 | 0 |  | 0 |
| 6 | 应急灯的开关 | 1026 | normal | 37.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - 单条套路句式超限：「李国强站在」×3
  - narration_para_pct 23.3 低于目标 35.0
  - dialogue_run_mean 5.8 高于目标 4.0
- 第 4 章：
  - 单条套路句式超限：「李国强站在」×3
  - narration_para_pct 28.6 低于目标 35.0
- 第 6 章：
  - 单条套路句式超限：「李国强的」×4
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
  - [observe] 标题与《应急灯的光圈》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5880
chapter_chars_mean: 980
chapter_chars_median: 1004
chapter_chars_cv: 0.21
paragraphs_mean: 34.8
dialogue_chars_pct: 22.4
dialogue_para_pct: 50.5
interiority_para_pct: 1.6
narration_para_pct: 47.9
turn_under20_pct: 99.2
turn_over200_pct: 0.0
attr_say_pct: 60.7
attr_adv_pct: 6.5
scenes_per_chapter: 1.2
dialogue_run_mean: 2.5
turn_len_median: 8
```
