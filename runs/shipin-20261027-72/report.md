# 裂镜 生成报告

slug：`shipin-20261027-72`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6621
LLM 调用：57 次，累计 138.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 修镜 | 519 | short | 38.3 | 0 |  | 1 |
| 2 | 撕布条 | 974 | normal | 93.5 | 0 |  | 1 |
| 3 | 削账本 | 1073 | normal | 90.3 | 0 |  | 1 |
| 4 | 抚镜之手 | 1453 | normal | 94.0 | 0 |  | 0 |
| 5 | 调频与盐包 | 1176 | normal | 37.6 | 0 |  | 1 |
| 6 | 削镜 | 1420 | normal | 36.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 479 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 34.8 低于目标 35.0
- 第 3 章：
  - narration_para_pct 33.3 低于目标 35.0
- 第 5 章：
  - [observe] 章内自我复读 4 句（如「收音机的电流声变得稳定了一些，她伸手摸了摸自己的…」）
- 第 6 章：
  - [observe] 章内自我复读 3 句（如「你想带出去也好，留在这儿也罢，但别让它再碎一次…」）

## 整书结构指标

```
chapters: 6
total_chars: 6147
chapter_chars_mean: 1024
chapter_chars_median: 1054
chapter_chars_cv: 0.31
paragraphs_mean: 32.3
dialogue_chars_pct: 32.6
dialogue_para_pct: 61.3
interiority_para_pct: 0.0
narration_para_pct: 38.7
turn_under20_pct: 89.7
turn_over200_pct: 0.0
attr_say_pct: 64.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.1
turn_len_median: 10
```
