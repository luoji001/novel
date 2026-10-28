# 二维码 生成报告

slug：`shipin-20261027-339`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5976
LLM 调用：57 次，累计 124.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 二维码的银质耳环 | 250 | short | 22.6 | 0 |  | 1 |
| 2 | 绿色塑料袋的反光 | 866 | normal | 39.1 | 0 |  | 1 |
| 3 | 二维码的银质耳环 | 1265 | normal | 90.1 | 0 |  | 2 |
| 4 | 二维码的竹夹子 | 1233 | normal | 89.1 | 0 |  | 3 |
| 5 | 手机屏保的黑影 | 975 | normal | 90.8 | 0 |  | 0 |
| 6 | 二维码的银质耳环 | 1381 | normal | 91.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 214 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章节过短 792 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - narration_para_pct 30.0 低于目标 35.0
  - [observe] 标题重复：「二维码的银质耳环」已存在
- 第 4 章：
  - 单条套路句式超限：「周志远的」×3
  - narration_para_pct 28.1 低于目标 35.0
  - dialogue_run_mean 4.4 高于目标 4.0
- 第 6 章：
  - 单条套路句式超限：「陈阿婆的」×3
  - [observe] 标题重复：「二维码的银质耳环」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5556
chapter_chars_mean: 926
chapter_chars_median: 1024
chapter_chars_cv: 0.43
paragraphs_mean: 26.7
dialogue_chars_pct: 21.1
dialogue_para_pct: 54.8
interiority_para_pct: 1.8
narration_para_pct: 43.4
turn_under20_pct: 96.1
turn_over200_pct: 0.0
attr_say_pct: 16.1
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.1
turn_len_median: 10
```
