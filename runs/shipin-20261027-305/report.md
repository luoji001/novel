# 胶片上的标签 生成报告

slug：`shipin-20261027-305`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5465
LLM 调用：57 次，累计 126.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 剪刀与胶片 | 378 | short | 37.4 | 0 |  | 1 |
| 2 | 钥匙踢门声 | 943 | normal | 91.6 | 0 |  | 0 |
| 3 | 茶壶嘴上的票根 | 753 | normal | 37.5 | 0 |  | 3 |
| 4 | 胶片缓缓转动 | 1190 | normal | 93.5 | 0 |  | 2 |
| 5 | 钥匙卡锁孔 | 762 | normal | 19.2 | 0 |  | 3 |
| 6 | 胶片边缘的指纹 | 1433 | normal | 91.5 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 347 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 26.7 低于目标 35.0
  - [observe] 章内自我复读 2 句（如「阿婆，今天的茶还跟昨天一样苦…」）
  - [observe] 章节过短 708 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - interiority_para_pct 6.7 高于目标 6.0
  - narration_para_pct 20.0 低于目标 35.0
- 第 5 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 97.1 高于目标 90.0
  - [observe] 章节过短 681 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5100
chapter_chars_mean: 850
chapter_chars_median: 800
chapter_chars_cv: 0.42
paragraphs_mean: 23
dialogue_chars_pct: 16.7
dialogue_para_pct: 47.0
interiority_para_pct: 1.9
narration_para_pct: 51.2
turn_under20_pct: 98.9
turn_over200_pct: 0.0
attr_say_pct: 71.7
attr_adv_pct: 2.3
scenes_per_chapter: 1.5
dialogue_run_mean: 2.2
turn_len_median: 9
```
