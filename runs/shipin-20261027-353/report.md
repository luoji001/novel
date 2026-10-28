# 二维码 生成报告

slug：`shipin-20261027-353`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6718
LLM 调用：57 次，累计 143.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 二维码贴纸风波 | 985 | short | 96.7 | 0 |  | 2 |
| 2 | 捏皱的香烟包装 | 1150 | normal | 93.4 | 0 |  | 2 |
| 3 | 二维码贴纸风波 | 1114 | normal | 90.1 | 0 |  | 2 |
| 4 | 二维码贴纸风波 | 950 | normal | 23.8 | 0 |  | 3 |
| 5 | 二维码贴纸风波 | 1070 | normal | 94.2 | 0 |  | 3 |
| 6 | 贴纸压不住菜刀 | 1443 | normal | 91.9 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 21.9 低于目标 35.0
  - dialogue_run_mean 6 高于目标 4.0
- 第 2 章：
  - 单条套路句式超限：「陈阿婆的」×4
  - narration_para_pct 33.3 低于目标 35.0
- 第 3 章：
  - narration_para_pct 21.1 低于目标 35.0
  - [observe] 标题重复：「二维码贴纸风波」已存在
- 第 4 章：
  - narration_para_pct 93.7 高于目标 90.0
  - [observe] 章节过短 725 < 870（本章目标 1582 字的 55%）
  - [observe] 标题重复：「二维码贴纸风波」已存在
- 第 5 章：
  - 单条套路句式超限：「陈阿婆的」×3
  - narration_para_pct 32.1 低于目标 35.0
  - [observe] 标题重复：「二维码贴纸风波」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6069
chapter_chars_mean: 1012
chapter_chars_median: 1030
chapter_chars_cv: 0.19
paragraphs_mean: 40.3
dialogue_chars_pct: 28.3
dialogue_para_pct: 60.0
interiority_para_pct: 0.5
narration_para_pct: 39.5
turn_under20_pct: 88.6
turn_over200_pct: 0.0
attr_say_pct: 4.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 3.1
turn_len_median: 10
```
