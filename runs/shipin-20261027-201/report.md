# 雨靴与电梯 生成报告

slug：`shipin-20261027-201`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6179
LLM 调用：53 次，累计 194.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 伞骨折痕 | 750 | short | 94.8 | 0 |  | 1 |
| 2 | 黑色橡胶的低语 | 1197 | normal | 37.3 | 0 |  | 1 |
| 3 | 雨靴坠落时刻 | 858 | normal | 37.8 | 0 |  | 2 |
| 4 | 徽章嵌入凹槽 | 1053 | normal | 93.1 | 0 |  | 0 |
| 5 | 钥匙撞击声响起 | 1112 | normal | 91.5 | 0 |  | 0 |
| 6 | 雨靴与钥匙碰撞 | 1203 | normal | 88.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 25.9 低于目标 35.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「周志远迅速上前按下紧急制动按钮，同时抬手拦住即将…」）
- 第 3 章：
  - narration_para_pct 23.8 低于目标 35.0
  - [observe] 章节过短 802 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - narration_para_pct 22.6 低于目标 35.0
  - dialogue_run_mean 5 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 5737
chapter_chars_mean: 956
chapter_chars_median: 1020
chapter_chars_cv: 0.18
paragraphs_mean: 27.5
dialogue_chars_pct: 26.5
dialogue_para_pct: 58.1
interiority_para_pct: 1.0
narration_para_pct: 40.9
turn_under20_pct: 90.7
turn_over200_pct: 0.0
attr_say_pct: 40.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 2.5
turn_len_median: 9
```
