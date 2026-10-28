# 应急灯 生成报告

slug：`shipin-20261027-384`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6756
LLM 调用：57 次，累计 166.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲窗 | 692 | short | 96.2 | 0 |  | 0 |
| 2 | 折铅笔 | 992 | normal | 89.1 | 0 |  | 2 |
| 3 | 扫帚拂尘 | 1428 | normal | 92.5 | 0 |  | 2 |
| 4 | 粉笔敲窗 | 1101 | normal | 91.3 | 0 |  | 1 |
| 5 | 磨灯 | 1233 | normal | 88.7 | 0 |  | 2 |
| 6 | 擦橡皮 | 1304 | normal | 92.7 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 19.4 低于目标 35.0
  - dialogue_run_mean 6.2 高于目标 4.0
- 第 3 章：
  - 单条套路句式超限：「李秀兰站在」×3、「李秀兰的」×3
  - narration_para_pct 31.0 低于目标 35.0
- 第 4 章：
  - [observe] 标题与《敲窗》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 25.8 低于目标 35.0
  - dialogue_run_mean 5.8 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 6346
chapter_chars_mean: 1058
chapter_chars_median: 1094
chapter_chars_cv: 0.24
paragraphs_mean: 28.2
dialogue_chars_pct: 25.5
dialogue_para_pct: 65.1
interiority_para_pct: 0.0
narration_para_pct: 34.9
turn_under20_pct: 93.7
turn_over200_pct: 0.0
attr_say_pct: 62.1
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 3.3
turn_len_median: 9
```
