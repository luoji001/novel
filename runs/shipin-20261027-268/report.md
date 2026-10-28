# 推子 生成报告

slug：`shipin-20261027-268`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6674
LLM 调用：57 次，累计 132.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 抚摸推子纹路 | 452 | short | 23.8 | 0 |  | 2 |
| 2 | 推子与账本对话 | 1282 | normal | 91.3 | 0 |  | 1 |
| 3 | 铅笔点数账本 | 1099 | normal | 91.2 | 0 |  | 0 |
| 4 | 擦镜裂痕 | 1079 | normal | 89.2 | 0 |  | 0 |
| 5 | 推子与老式推子对话 | 1344 | normal | 88.4 | 0 |  | 1 |
| 6 | 擦拭推子柄纹路 | 1412 | normal | 93.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 25.0 低于目标 35.0
  - [observe] 章节过短 422 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 32.4 低于目标 35.0
- 第 5 章：
  - [observe] 标题与《推子与账本对话》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 34.5 低于目标 35.0
  - [observe] 标题与《抚摸推子纹路》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6250
chapter_chars_mean: 1042
chapter_chars_median: 1114
chapter_chars_cv: 0.32
paragraphs_mean: 27.5
dialogue_chars_pct: 28.6
dialogue_para_pct: 58.5
interiority_para_pct: 0.6
narration_para_pct: 40.8
turn_under20_pct: 90.2
turn_over200_pct: 0.0
attr_say_pct: 37.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 2.3
turn_len_median: 10
```
