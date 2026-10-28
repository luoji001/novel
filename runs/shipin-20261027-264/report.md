# 硬币密码 生成报告

slug：`shipin-20261027-264`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5820
LLM 调用：57 次，累计 118.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 擦座椅遇见硬币 | 588 | short | 36.6 | 0 |  | 3 |
| 2 | 触碰硬币的瞬间 | 1141 | normal | 94.5 | 0 |  | 2 |
| 3 | 擦拭警示牌的瞬间 | 1097 | normal | 91.7 | 0 |  | 0 |
| 4 | 记账本上的折痕 | 1200 | normal | 91.5 | 0 |  | 1 |
| 5 | 绕红绳的时刻 | 964 | normal | 92.3 | 0 |  | 0 |
| 6 | 擦拭座椅边缘 | 824 | normal | 36.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 3.1 低于目标 5.0
  - narration_para_pct 93.5 高于目标 90.0
  - [observe] 章节过短 511 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「李建国的」×4
  - attr_adv_pct 16.7 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「李建国的」×3
- 第 6 章：
  - [observe] 章节过短 740 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5397
chapter_chars_mean: 900
chapter_chars_median: 976
chapter_chars_cv: 0.26
paragraphs_mean: 27.3
dialogue_chars_pct: 16.4
dialogue_para_pct: 36.6
interiority_para_pct: 1.1
narration_para_pct: 62.4
turn_under20_pct: 90.9
turn_over200_pct: 0.0
attr_say_pct: 54.3
attr_adv_pct: 3.2
scenes_per_chapter: 2
dialogue_run_mean: 1.5
turn_len_median: 10
```
