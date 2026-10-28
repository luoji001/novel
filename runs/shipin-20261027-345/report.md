# 储油区的锁 生成报告

slug：`shipin-20261027-345`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5814
LLM 调用：57 次，累计 142.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 储油区的锁 | 545 | short | 22.0 | 0 |  | 3 |
| 2 | 摄像头的雪花点 | 1077 | normal | 93.6 | 0 |  | 0 |
| 3 | 警示牌的裂痕 | 882 | normal | 23.4 | 0 |  | 3 |
| 4 | 加油枪的对峙 | 846 | normal | 37.6 | 0 |  | 1 |
| 5 | 钥匙与撬棍的较量 | 1078 | normal | 93.0 | 0 |  | 1 |
| 6 | 钥匙与撬棍的较量 | 1380 | normal | 91.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 516 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - dialogue_chars_pct 3.3 低于目标 5.0
  - narration_para_pct 90.9 高于目标 90.0
  - [observe] 章节过短 780 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - [observe] 章节过短 792 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - narration_para_pct 28.0 低于目标 35.0
- 第 6 章：
  - 单条套路句式超限：「他知道这」×3、「小林站在」×3
  - [observe] 标题重复：「钥匙与撬棍的较量」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5410
chapter_chars_mean: 902
chapter_chars_median: 895
chapter_chars_cv: 0.3
paragraphs_mean: 25.8
dialogue_chars_pct: 15.2
dialogue_para_pct: 39.2
interiority_para_pct: 1.8
narration_para_pct: 58.9
turn_under20_pct: 94.9
turn_over200_pct: 0.0
attr_say_pct: 38.6
attr_adv_pct: 0.0
scenes_per_chapter: 3.3
dialogue_run_mean: 1.6
turn_len_median: 9
```
