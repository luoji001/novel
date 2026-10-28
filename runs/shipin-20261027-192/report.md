# 铜钥匙 生成报告

slug：`shipin-20261027-192`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5646
LLM 调用：57 次，累计 120.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙板的新凹痕 | 868 | short | 96.0 | 0 |  | 3 |
| 2 | 钥匙与血痕 | 1023 | normal | 91.3 | 0 |  | 0 |
| 3 | 笔记本上的空白页 | 1116 | normal | 92.8 | 0 |  | 0 |
| 4 | 水杯边缘的圆圈 | 674 | normal | 19.4 | 0 |  | 2 |
| 5 | 钥匙敲击门框声 | 897 | normal | 36.3 | 0 |  | 1 |
| 6 | 钥匙板与墙缝数字 | 1062 | normal | 90.6 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林晓雨的」×3
  - narration_para_pct 25.0 低于目标 35.0
  - dialogue_run_mean 6 高于目标 4.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「几滴水珠顺着杯壁滑落，在灯光下折射出细碎的光斑…」）
  - [observe] 章节过短 631 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - [observe] 章节过短 844 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5310
chapter_chars_mean: 885
chapter_chars_median: 899
chapter_chars_cv: 0.17
paragraphs_mean: 20
dialogue_chars_pct: 19.7
dialogue_para_pct: 49.5
interiority_para_pct: 0.6
narration_para_pct: 49.9
turn_under20_pct: 90.9
turn_over200_pct: 0.0
attr_say_pct: 47.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.3
turn_len_median: 10
```
