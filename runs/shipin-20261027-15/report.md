# 蛇皮袋 生成报告

slug：`shipin-20261027-15`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6176
LLM 调用：57 次，累计 134.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 紧握蛇皮袋的手 | 584 | short | 37.0 | 0 |  | 2 |
| 2 | 红水壶的撞击 | 1036 | normal | 93.8 | 0 |  | 1 |
| 3 | 摩挲工牌的夜晚 | 1022 | normal | 94.1 | 0 |  | 0 |
| 4 | 摩挲手电筒的瞬间 | 1429 | normal | 91.8 | 0 |  | 2 |
| 5 | 耳环坠入掌心 | 1062 | normal | 91.9 | 0 |  | 1 |
| 6 | 撕开蛇皮袋的一瞬 | 1037 | normal | 90.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 7.1 高于目标 6.0
  - [observe] 章节过短 541 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「王春梅的」×3
- 第 4 章：
  - 单条套路句式超限：「李建军的」×5
  - narration_para_pct 30.8 低于目标 35.0
- 第 5 章：
  - 单条套路句式超限：「王春梅的」×3
- 第 6 章：
  - 单条套路句式超限：「王春梅的」×4

## 整书结构指标

```
chapters: 6
total_chars: 5738
chapter_chars_mean: 956
chapter_chars_median: 970
chapter_chars_cv: 0.26
paragraphs_mean: 28.3
dialogue_chars_pct: 19.5
dialogue_para_pct: 49.2
interiority_para_pct: 1.9
narration_para_pct: 49.0
turn_under20_pct: 97.0
turn_over200_pct: 0.0
attr_say_pct: 46.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.5
turn_len_median: 8
```
