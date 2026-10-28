# 铜钥匙 生成报告

slug：`shipin-20261027-396`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5269
LLM 调用：57 次，累计 131.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 纸条上的墨迹 | 565 | short | 39.1 | 0 |  | 1 |
| 2 | 钥匙划破铁皮 | 869 | normal | 38.1 | 0 |  | 1 |
| 3 | 碗底的裂痕 | 1165 | normal | 36.6 | 0 |  | 3 |
| 4 | 帆布包的破洞 | 865 | normal | 37.0 | 0 |  | 1 |
| 5 | 伞骨的重量 | 902 | normal | 36.9 | 0 |  | 1 |
| 6 | 纸条上的日期 | 897 | normal | 36.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 523 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章节过短 781 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - narration_para_pct 17.4 低于目标 35.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - [observe] 章内自我复读 2 句（如「你们都在找答案，可答案就在眼前…」）
- 第 4 章：
  - [observe] 章节过短 785 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - [observe] 章节过短 861 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - [observe] 章节过短 841 < 870（本章目标 1582 字的 55%）
  - [observe] 标题与《纸条上的墨迹》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 4897
chapter_chars_mean: 816
chapter_chars_median: 813
chapter_chars_cv: 0.23
paragraphs_mean: 22.8
dialogue_chars_pct: 22.3
dialogue_para_pct: 52.2
interiority_para_pct: 1.0
narration_para_pct: 46.9
turn_under20_pct: 90.4
turn_over200_pct: 0.0
attr_say_pct: 45.7
attr_adv_pct: 0.0
scenes_per_chapter: 2.5
dialogue_run_mean: 2.1
turn_len_median: 10
```
