# 充电枪 生成报告

slug：`shipin-20261027-335`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6812
LLM 调用：57 次，累计 140.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 雪铲与充电桩的争执 | 722 | short | 97.8 | 0 |  | 1 |
| 2 | 红色停车牌的争夺 | 1075 | normal | 93.9 | 0 |  | 0 |
| 3 | 防滑链与充电枪的对峙 | 1397 | normal | 93.8 | 0 |  | 0 |
| 4 | 对讲机的警告 | 1304 | normal | 35.3 | 0 |  | 5 |
| 5 | 警示锥的边界 | 1174 | normal | 36.7 | 0 |  | 2 |
| 6 | 雪铲与充电枪的较量 | 1134 | normal | 35.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 33.3 低于目标 35.0
- 第 4 章：
  - 单条套路句式超限：「说道“我」×4
  - narration_para_pct 25.8 低于目标 35.0
  - attr_adv_pct 11.1 高于目标 10.0
  - dialogue_run_mean 7.3 高于目标 4.0
  - [observe] 章内自我复读 2 句（如「刘建国没有理会他的挑衅，继续说道：“我给你们五分…」）
- 第 5 章：
  - [observe] 章内自我复读 2 句（如「你要是敢动它，我就报警…」）
  - [observe] attr_adv_pct 20.0 > 18.0（结构塌缩）
- 第 6 章：
  - [observe] 章内自我复读 2 句（如「等等！你不能这么做！…」）
  - [observe] 标题与《雪铲与充电桩的争执》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6208
chapter_chars_mean: 1035
chapter_chars_median: 1020
chapter_chars_cv: 0.23
paragraphs_mean: 40.2
dialogue_chars_pct: 27.7
dialogue_para_pct: 56.1
interiority_para_pct: 1.6
narration_para_pct: 42.3
turn_under20_pct: 92.7
turn_over200_pct: 0.0
attr_say_pct: 20.0
attr_adv_pct: 5.6
scenes_per_chapter: 1
dialogue_run_mean: 2.9
turn_len_median: 9
```
