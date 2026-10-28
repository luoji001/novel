# 手电筒 生成报告

slug：`shipin-20261027-146`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6458
LLM 调用：57 次，累计 130.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 应急灯的光斑 | 457 | short | 15.5 | 0 |  | 3 |
| 2 | 铅笔划破纸面 | 1184 | normal | 90.9 | 0 |  | 1 |
| 3 | 手电筒的光斑 | 1185 | normal | 89.2 | 0 |  | 3 |
| 4 | 试卷上的红圈痕迹 | 1349 | normal | 89.3 | 0 |  | 1 |
| 5 | 笔记本的折痕秘密 | 1060 | normal | 88.9 | 0 |  | 1 |
| 6 | 应急灯滚落瞬间 | 1217 | normal | 52.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 413 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - interiority_para_pct 6.1 高于目标 6.0
- 第 3 章：
  - 单条套路句式超限：「李国强的」×3
  - narration_para_pct 26.9 低于目标 35.0
  - dialogue_run_mean 4.8 高于目标 4.0
- 第 4 章：
  - interiority_para_pct 6.5 高于目标 6.0
- 第 5 章：
  - 单条套路句式超限：「王小明点」×3、「王小明的」×3
- 第 6 章：
  - interiority_para_pct 10.3 高于目标 6.0

## 整书结构指标

```
chapters: 6
total_chars: 5997
chapter_chars_mean: 1000
chapter_chars_median: 1112
chapter_chars_cv: 0.31
paragraphs_mean: 30.5
dialogue_chars_pct: 18.4
dialogue_para_pct: 41.5
interiority_para_pct: 4.5
narration_para_pct: 54.1
turn_under20_pct: 93.1
turn_over200_pct: 0.0
attr_say_pct: 34.1
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.1
turn_len_median: 10
```
