# 雨靴上的泥渍 生成报告

slug：`shipin-20261027-145`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6758
LLM 调用：57 次，累计 146.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 拐杖与雨靴相碰 | 613 | short | 38.4 | 0 |  | 1 |
| 2 | 钥匙与拐杖相触 | 995 | normal | 86.8 | 0 |  | 1 |
| 3 | 钥匙与工具箱相撞 | 1176 | normal | 92.8 | 0 |  | 0 |
| 4 | 电费单与雨靴共眠 | 1143 | normal | 90.2 | 0 |  | 2 |
| 5 | 钥匙与银镯相映 | 1358 | normal | 90.8 | 0 |  | 2 |
| 6 | 雨靴与钥匙相争 | 1467 | normal | 85.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 562 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - interiority_para_pct 9.5 高于目标 6.0
- 第 4 章：
  - narration_para_pct 8.3 低于目标 35.0
  - dialogue_run_mean 7.3 高于目标 4.0
- 第 5 章：
  - 单条套路句式超限：「李秀兰的」×3
  - narration_para_pct 29.2 低于目标 35.0
- 第 6 章：
  - narration_para_pct 20.0 低于目标 35.0
  - dialogue_run_mean 6.7 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 6396
chapter_chars_mean: 1066
chapter_chars_median: 1100
chapter_chars_cv: 0.28
paragraphs_mean: 22
dialogue_chars_pct: 22.6
dialogue_para_pct: 67.6
interiority_para_pct: 1.4
narration_para_pct: 31.0
turn_under20_pct: 90.5
turn_over200_pct: 0.0
attr_say_pct: 20.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 3.7
turn_len_median: 10
```
