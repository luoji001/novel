# 推子 生成报告

slug：`shipin-20261027-114`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6780
LLM 调用：57 次，累计 142.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 推子与保温桶相撞 | 627 | short | 17.2 | 0 |  | 3 |
| 2 | 推子撞向镜子 | 1242 | normal | 92.2 | 0 |  | 1 |
| 3 | 推子与保温桶对峙 | 1314 | normal | 92.3 | 0 |  | 1 |
| 4 | 推子抵住记账本 | 1386 | normal | 35.9 | 0 |  | 3 |
| 5 | 推子夺回保温桶 | 1117 | normal | 54.2 | 0 |  | 1 |
| 6 | 推子抵住保温桶 | 1088 | normal | 36.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 2.3 低于目标 5.0
  - narration_para_pct 92.0 高于目标 90.0
  - [observe] 章节过短 561 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 30.8 低于目标 35.0
- 第 3 章：
  - [observe] 标题与《推子与保温桶相撞》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「“老周你」×4
  - narration_para_pct 29.0 低于目标 35.0
  - [observe] 章内自我复读 2 句（如「他忽然笑了，笑得很轻，“老周，你想留在这儿，其实…」）
- 第 5 章：
  - [observe] 标题与《推子与保温桶对峙》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「小林不甘示弱地反驳道…」）
  - [observe] 标题与《推子夺回保温桶》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6298
chapter_chars_mean: 1050
chapter_chars_median: 1094
chapter_chars_cv: 0.25
paragraphs_mean: 32
dialogue_chars_pct: 19.3
dialogue_para_pct: 50.3
interiority_para_pct: 1.1
narration_para_pct: 48.6
turn_under20_pct: 93.7
turn_over200_pct: 0.0
attr_say_pct: 15.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.5
turn_len_median: 8
```
