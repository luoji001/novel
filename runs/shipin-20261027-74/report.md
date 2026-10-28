# 硬币的重量 生成报告

slug：`shipin-20261027-74`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6250
LLM 调用：57 次，累计 131.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 纸片的边缘 | 584 | short | 21.8 | 0 |  | 4 |
| 2 | 手机的光 | 918 | normal | 53.7 | 0 |  | 2 |
| 3 | 铁锹的余温 | 1095 | normal | 91.7 | 0 |  | 0 |
| 4 | 硬币的温度 | 849 | normal | 37.1 | 0 |  | 1 |
| 5 | 木炭的余温 | 1297 | normal | 93.2 | 0 |  | 2 |
| 6 | 纸片的边缘 | 1501 | normal | 95.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 4.6 低于目标 5.0
  - narration_para_pct 90.9 高于目标 90.0
  - [observe] 章内自我复读 2 句（如「纸面上，“2013年6月15日”几个字清晰可见，…」）
  - [observe] 章节过短 518 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - dialogue_chars_pct 3.9 低于目标 5.0
  - narration_para_pct 0.0 低于目标 35.0
- 第 4 章：
  - [observe] 章节过短 758 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 标题与《铁锹的余温》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 34.4 低于目标 35.0
  - [observe] 标题重复：「纸片的边缘」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5818
chapter_chars_mean: 970
chapter_chars_median: 963
chapter_chars_cv: 0.33
paragraphs_mean: 26.3
dialogue_chars_pct: 17.1
dialogue_para_pct: 56.4
interiority_para_pct: 0.0
narration_para_pct: 43.6
turn_under20_pct: 98.2
turn_over200_pct: 0.0
attr_say_pct: 64.2
attr_adv_pct: 3.3
scenes_per_chapter: 2.2
dialogue_run_mean: 2.1
turn_len_median: 10
```
