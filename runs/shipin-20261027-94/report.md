# 铜匙 生成报告

slug：`shipin-20261027-94`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5564
LLM 调用：57 次，累计 124.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙与地图的对峙 | 270 | short | 37.8 | 0 |  | 1 |
| 2 | 钥匙的低语 | 997 | normal | 37.3 | 0 |  | 2 |
| 3 | 钥匙上的裂痕 | 962 | normal | 35.4 | 0 |  | 1 |
| 4 | 玻璃瓶里的贝壳 | 1215 | normal | 91.9 | 0 |  | 0 |
| 5 | 玻璃罐的刻痕 | 1143 | normal | 89.8 | 0 |  | 0 |
| 6 | 钥匙与红绳对峙 | 971 | normal | 91.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 232 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 21.1 低于目标 35.0
  - [observe] 章内自我复读 4 句（如「因为你不是第一个发现它的人…」）
- 第 3 章：
  - [observe] 章内自我复读 5 句（如「林晓阳慢慢抬起头，透过门缝望向走廊尽头，那里站着…」）
- 第 6 章：
  - 单条套路句式超限：「周德昌的」×5
  - [observe] 标题与《钥匙与地图的对峙》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5162
chapter_chars_mean: 860
chapter_chars_median: 912
chapter_chars_cv: 0.38
paragraphs_mean: 24.5
dialogue_chars_pct: 15.5
dialogue_para_pct: 39.0
interiority_para_pct: 0.6
narration_para_pct: 60.4
turn_under20_pct: 98.5
turn_over200_pct: 0.0
attr_say_pct: 36.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.7
turn_len_median: 10
```
