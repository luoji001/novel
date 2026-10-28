# 药瓶上的名字 生成报告

slug：`shipin-20261027-14`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6646
LLM 调用：57 次，累计 140.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红绳缠绕药瓶 | 785 | short | 97.9 | 0 |  | 1 |
| 2 | 红绳缠绕药瓶 | 917 | normal | 36.2 | 0 |  | 5 |
| 3 | 红绳缠绕药瓶 | 1299 | normal | 90.7 | 0 |  | 1 |
| 4 | 红绳缠绕药瓶 | 1309 | normal | 88.4 | 0 |  | 1 |
| 5 | 红绳缠绕药瓶 | 1187 | normal | 91.4 | 0 |  | 2 |
| 6 | 红绳缠绕药瓶 | 1143 | normal | 93.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李娟站在」×3
- 第 2 章：
  - 单条套路句式超限：「陈雪梅的」×3
  - narration_para_pct 31.6 低于目标 35.0
  - dialogue_run_mean 4.3 高于目标 4.0
  - [observe] 章节过短 865 < 870（本章目标 1582 字的 55%）
  - [observe] 标题重复：「红绳缠绕药瓶」已存在
- 第 3 章：
  - [observe] 标题重复：「红绳缠绕药瓶」已存在
- 第 4 章：
  - [observe] 标题重复：「红绳缠绕药瓶」已存在
- 第 5 章：
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 标题重复：「红绳缠绕药瓶」已存在
- 第 6 章：
  - [observe] 标题重复：「红绳缠绕药瓶」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6207
chapter_chars_mean: 1034
chapter_chars_median: 1092
chapter_chars_cv: 0.19
paragraphs_mean: 29
dialogue_chars_pct: 24.5
dialogue_para_pct: 60.6
interiority_para_pct: 1.5
narration_para_pct: 37.9
turn_under20_pct: 97.0
turn_over200_pct: 0.0
attr_say_pct: 44.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.5
turn_len_median: 10
```
