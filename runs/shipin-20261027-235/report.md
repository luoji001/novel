# 胶片盒 生成报告

slug：`shipin-20261027-235`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6335
LLM 调用：57 次，累计 133.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 胶片盒的温度 | 588 | short | 13.8 | 0 |  | 3 |
| 2 | 公文包的暗红裂痕 | 1347 | normal | 37.0 | 0 |  | 2 |
| 3 | 拾起电影票 | 960 | normal | 91.3 | 0 |  | 0 |
| 4 | 手指抚过胶片盒 | 1177 | normal | 91.6 | 0 |  | 0 |
| 5 | 解开最后一颗纽扣 | 1161 | normal | 57.9 | 0 |  | 2 |
| 6 | 解开发光纽扣 | 1096 | normal | 59.8 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 526 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 34.6 低于目标 35.0
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
- 第 5 章：
  - dialogue_chars_pct 4.8 低于目标 5.0
  - narration_para_pct 91.2 高于目标 90.0

## 整书结构指标

```
chapters: 6
total_chars: 5899
chapter_chars_mean: 983
chapter_chars_median: 1040
chapter_chars_cv: 0.26
paragraphs_mean: 28.5
dialogue_chars_pct: 13.2
dialogue_para_pct: 37.2
interiority_para_pct: 0.6
narration_para_pct: 62.2
turn_under20_pct: 93.9
turn_over200_pct: 0.0
attr_say_pct: 53.0
attr_adv_pct: 7.9
scenes_per_chapter: 2.5
dialogue_run_mean: 1.8
turn_len_median: 8
```
