# 药瓶的标签 生成报告

slug：`shipin-20261027-210`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6291
LLM 调用：57 次，累计 134.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 输液椅的锈迹 | 439 | short | 21.4 | 0 |  | 1 |
| 2 | 登记本边缘翘起 | 1106 | normal | 94.0 | 0 |  | 1 |
| 3 | 药架滑动的声响 | 937 | normal | 14.4 | 0 |  | 3 |
| 4 | 药瓶的冷光 | 1298 | normal | 37.0 | 0 |  | 2 |
| 5 | 玻璃上的霜花 | 1178 | normal | 92.3 | 0 |  | 2 |
| 6 | 药瓶坠地的闷响 | 1327 | normal | 93.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 391 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「陈美玲的」×3
- 第 3 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 819 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - 单条套路句式超限：「李小红的」×3
  - [observe] attr_adv_pct 20.0 > 18.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「李小红的」×3
  - narration_para_pct 33.3 低于目标 35.0
- 第 6 章：
  - narration_para_pct 18.8 低于目标 35.0
  - dialogue_run_mean 5.2 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 5780
chapter_chars_mean: 963
chapter_chars_median: 1054
chapter_chars_cv: 0.33
paragraphs_mean: 32.5
dialogue_chars_pct: 24.9
dialogue_para_pct: 53.1
interiority_para_pct: 0.0
narration_para_pct: 46.9
turn_under20_pct: 94.3
turn_over200_pct: 0.0
attr_say_pct: 45.4
attr_adv_pct: 4.9
scenes_per_chapter: 1.2
dialogue_run_mean: 2.7
turn_len_median: 8
```
