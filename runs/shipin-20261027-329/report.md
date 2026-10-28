# 指纹 生成报告

slug：`shipin-20261027-329`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5572
LLM 调用：57 次，累计 123.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 锈蚀钥匙入锁孔 | 375 | short | 37.7 | 0 |  | 1 |
| 2 | 钥匙串上的铜锈 | 1159 | normal | 37.3 | 0 |  | 2 |
| 3 | 手电筒扫过登记簿 | 806 | normal | 36.2 | 0 |  | 2 |
| 4 | 报纸边缘的指纹 | 1045 | normal | 91.5 | 0 |  | 1 |
| 5 | 对讲机里的声音 | 1314 | normal | 91.6 | 0 |  | 0 |
| 6 | 指纹覆锁孔 | 867 | normal | 36.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 334 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 27.3 低于目标 35.0
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「李建国的」×3
  - [observe] 章节过短 754 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - interiority_para_pct 6.7 高于目标 6.0
- 第 6 章：
  - [observe] 章节过短 820 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5201
chapter_chars_mean: 867
chapter_chars_median: 910
chapter_chars_cv: 0.36
paragraphs_mean: 20.5
dialogue_chars_pct: 19.4
dialogue_para_pct: 47.4
interiority_para_pct: 2.8
narration_para_pct: 49.8
turn_under20_pct: 84.8
turn_over200_pct: 0.0
attr_say_pct: 15.4
attr_adv_pct: 6.2
scenes_per_chapter: 1.3
dialogue_run_mean: 1.7
turn_len_median: 12
```
