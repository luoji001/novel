# 推子 生成报告

slug：`shipin-20261027-366`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6430
LLM 调用：57 次，累计 130.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 擦推子的手指 | 714 | short | 93.9 | 0 |  | 0 |
| 2 | 摩挲病历单的指尖 | 1177 | normal | 36.4 | 0 |  | 2 |
| 3 | 摩挲推子的手指 | 1393 | normal | 92.1 | 0 |  | 1 |
| 4 | 擦镜子的裂口 | 1020 | normal | 59.6 | 0 |  | 0 |
| 5 | 割裂镜面的剪刀 | 1261 | normal | 90.8 | 0 |  | 1 |
| 6 | 推子与账本的对话 | 859 | normal | 22.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 25.9 低于目标 35.0
  - [observe] 章内自我复读 2 句（如「我爸爸做手术那天，这上面写的日期…」）
- 第 3 章：
  - [observe] 标题与《擦推子的手指》近似 0.77 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「”小李低」×3
- 第 6 章：
  - dialogue_chars_pct 4.7 低于目标 5.0
  - [observe] 章节过短 827 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 6014
chapter_chars_mean: 1002
chapter_chars_median: 1030
chapter_chars_cv: 0.23
paragraphs_mean: 26.7
dialogue_chars_pct: 27.6
dialogue_para_pct: 55.1
interiority_para_pct: 2.0
narration_para_pct: 42.9
turn_under20_pct: 89.1
turn_over200_pct: 0.0
attr_say_pct: 78.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.9
turn_len_median: 11
```
