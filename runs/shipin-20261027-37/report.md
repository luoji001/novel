# 饮料箱的重量 生成报告

slug：`shipin-20261027-37`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6066
LLM 调用：57 次，累计 119.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 监控屏幕的裂痕 | 632 | short | 17.3 | 0 |  | 3 |
| 2 | 触摸冷藏柜的裂痕 | 1190 | normal | 93.0 | 0 |  | 0 |
| 3 | 触碰冷藏柜的凹陷 | 1426 | normal | 36.2 | 0 |  | 3 |
| 4 | 触碰绷带的指尖 | 844 | normal | 37.4 | 0 |  | 2 |
| 5 | 对讲机的电流声 | 972 | normal | 92.1 | 0 |  | 0 |
| 6 | 紧握饮料箱的手 | 996 | normal | 91.4 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 97.7 高于目标 90.0
  - [observe] 章节过短 486 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - 单条套路句式超限：「小林站在」×3
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
  - [observe] 标题与《触摸冷藏柜的裂痕》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] 章节过短 757 < 870（本章目标 1582 字的 55%）
  - [observe] attr_adv_pct 20.0 > 18.0（结构塌缩）

## 整书结构指标

```
chapters: 6
total_chars: 5535
chapter_chars_mean: 922
chapter_chars_median: 900
chapter_chars_cv: 0.33
paragraphs_mean: 32.3
dialogue_chars_pct: 15.1
dialogue_para_pct: 44.7
interiority_para_pct: 1.1
narration_para_pct: 54.2
turn_under20_pct: 99.0
turn_over200_pct: 0.0
attr_say_pct: 32.7
attr_adv_pct: 12.1
scenes_per_chapter: 2.7
dialogue_run_mean: 1.4
turn_len_median: 8
```
