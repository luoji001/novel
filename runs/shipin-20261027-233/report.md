# 加油枪 生成报告

slug：`shipin-20261027-233`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5885
LLM 调用：57 次，累计 135.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲钥匙卡 | 541 | short | 39.4 | 0 |  | 1 |
| 2 | 顶货架 | 924 | normal | 91.5 | 0 |  | 1 |
| 3 | 遮挡监控屏 | 1078 | normal | 90.0 | 0 |  | 0 |
| 4 | 红色纽扣失踪 | 939 | normal | 36.0 | 0 |  | 2 |
| 5 | 甩加油枪 | 1095 | normal | 92.3 | 0 |  | 2 |
| 6 | 摩挲红色耳钉 | 1302 | normal | 89.8 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

1. 第二章提到周浩使用“黑色加油枪”撬开货架，但第五章中周浩却“甩出加油枪”，暗示加油枪是其作案工具，前后逻辑不一致。

2. 第四章提到“红色影子”出现在监控画面中，而第六章提到“红色耳钉”，两者均为红色物品，但未明确关联，存在未交代的物件线索。

3. 第三章提到小林用保温箱遮挡监控，但第一章提到小林用钥匙卡挡住监控屏幕的视线，两种遮挡方式不一致，存在人名/称呼不一致及行为矛盾。

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 500 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - dialogue_chars_pct 4.1 低于目标 5.0
- 第 4 章：
  - interiority_para_pct 6.5 高于目标 6.0
  - [observe] 章节过短 863 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - narration_para_pct 26.7 低于目标 35.0
  - dialogue_run_mean 4.4 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 5367
chapter_chars_mean: 894
chapter_chars_median: 946
chapter_chars_cv: 0.24
paragraphs_mean: 31
dialogue_chars_pct: 11.7
dialogue_para_pct: 32.3
interiority_para_pct: 1.3
narration_para_pct: 66.4
turn_under20_pct: 99.2
turn_over200_pct: 0.0
attr_say_pct: 45.8
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.6
turn_len_median: 8
```
