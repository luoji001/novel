# 硬币的重量 生成报告

slug：`shipin-20261027-166`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7162
LLM 调用：57 次，累计 139.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 金属反光闪过 | 278 | short | 23.8 | 0 |  | 2 |
| 2 | 保温杯里的名字 | 1904 | normal | 24.4 | 0 |  | 1 |
| 3 | 硬币落进掌心 | 1240 | normal | 35.5 | 0 |  | 2 |
| 4 | 保温杯底部的纸条 | 1326 | normal | 91.3 | 0 |  | 1 |
| 5 | 钥匙别在工装外套上 | 1074 | normal | 85.6 | 0 |  | 2 |
| 6 | 硬币与保温杯的对峙 | 1334 | normal | 92.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 4.1 低于目标 5.0
  - [observe] 章节过短 244 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - interiority_para_pct 12.8 高于目标 6.0
- 第 3 章：
  - dialogue_chars_pct 3.7 低于目标 5.0
  - [observe] 章内自我复读 2 句（如「他知道，今天的训练肯定比平时更辛苦一些…」）
- 第 4 章：
  - interiority_para_pct 6.2 高于目标 6.0
- 第 5 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
- 第 6 章：
  - interiority_para_pct 6.2 高于目标 6.0

## 整书结构指标

```
chapters: 6
total_chars: 6581
chapter_chars_mean: 1097
chapter_chars_median: 1200
chapter_chars_cv: 0.47
paragraphs_mean: 36
dialogue_chars_pct: 11.4
dialogue_para_pct: 36.7
interiority_para_pct: 6.3
narration_para_pct: 56.9
turn_under20_pct: 98.6
turn_over200_pct: 0.0
attr_say_pct: 19.0
attr_adv_pct: 0.0
scenes_per_chapter: 2.3
dialogue_run_mean: 1.5
turn_len_median: 7
```
