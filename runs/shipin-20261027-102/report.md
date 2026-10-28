# 铜铃 生成报告

slug：`shipin-20261027-102`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6889
LLM 调用：57 次，累计 142.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 纸片上的水渍 | 567 | short | 38.6 | 0 |  | 1 |
| 2 | 皮夹坠入铁皮柜 | 1320 | normal | 92.2 | 0 |  | 0 |
| 3 | 铁皮柜的裂痕 | 1219 | normal | 36.9 | 0 |  | 2 |
| 4 | 红色印章的印记 | 1570 | normal | 92.9 | 0 |  | 1 |
| 5 | 帆布包的重量 | 1015 | normal | 52.1 | 0 |  | 2 |
| 6 | 铜铃铛的凹陷 | 1192 | normal | 91.7 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 511 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 23.8 低于目标 35.0
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）
- 第 4 章：
  - narration_para_pct 23.1 低于目标 35.0
- 第 5 章：
  - dialogue_chars_pct 0.6 低于目标 5.0
  - interiority_para_pct 7.7 高于目标 6.0

## 整书结构指标

```
chapters: 6
total_chars: 6509
chapter_chars_mean: 1085
chapter_chars_median: 1146
chapter_chars_cv: 0.3
paragraphs_mean: 23.8
dialogue_chars_pct: 15.7
dialogue_para_pct: 48.7
interiority_para_pct: 2.3
narration_para_pct: 49.0
turn_under20_pct: 95.3
turn_over200_pct: 0.0
attr_say_pct: 55.7
attr_adv_pct: 13.2
scenes_per_chapter: 2
dialogue_run_mean: 2.1
turn_len_median: 8
```
