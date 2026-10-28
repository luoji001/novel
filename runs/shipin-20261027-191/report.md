# 裂纹 生成报告

slug：`shipin-20261027-191`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5996
LLM 调用：57 次，累计 127.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击收银机的节奏 | 637 | short | 37.6 | 0 |  | 1 |
| 2 | 铁锹插进警示牌 | 866 | normal | 37.8 | 0 |  | 1 |
| 3 | 自动门上的冰霜 | 787 | normal | 22.6 | 0 |  | 2 |
| 4 | 钥匙串上的裂痕 | 1181 | normal | 89.5 | 0 |  | 2 |
| 5 | 手指触碰收银机边缘 | 1205 | normal | 91.5 | 0 |  | 1 |
| 6 | 手指触碰屏幕裂痕 | 1314 | normal | 91.4 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 555 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章节过短 751 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - dialogue_chars_pct 4.1 低于目标 5.0
  - [observe] 章节过短 736 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - dialogue_chars_pct 4.4 低于目标 5.0
  - interiority_para_pct 6.2 高于目标 6.0
- 第 5 章：
  - dialogue_chars_pct 4.8 低于目标 5.0

## 整书结构指标

```
chapters: 6
total_chars: 5553
chapter_chars_mean: 926
chapter_chars_median: 942
chapter_chars_cv: 0.3
paragraphs_mean: 28.3
dialogue_chars_pct: 6.1
dialogue_para_pct: 26.8
interiority_para_pct: 2.9
narration_para_pct: 70.2
turn_under20_pct: 100.0
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.1
turn_len_median: 6
```
