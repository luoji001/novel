# 灯芯 生成报告

slug：`shipin-20261027-328`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6818
LLM 调用：57 次，累计 139.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 粉笔敲击桌面 | 663 | short | 94.8 | 0 |  | 0 |
| 2 | 石头砸向灯罩 | 952 | normal | 94.6 | 0 |  | 0 |
| 3 | 铁锹挑开木门 | 1148 | normal | 91.0 | 0 |  | 0 |
| 4 | 粉笔敲击桌面 | 1510 | normal | 93.7 | 0 |  | 2 |
| 5 | 红耳环的光芒 | 1433 | normal | 89.5 | 0 |  | 3 |
| 6 | 断铅笔的锋芒 | 1106 | normal | 36.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 4 章：
  - narration_para_pct 31.0 低于目标 35.0
  - [observe] 标题重复：「粉笔敲击桌面」已存在
- 第 5 章：
  - 单条套路句式超限：「李国栋的」×4
  - narration_para_pct 23.3 低于目标 35.0
  - dialogue_run_mean 4.4 高于目标 4.0
- 第 6 章：
  - [observe] 章内自我复读 3 句（如「夜风穿过破损的窗缝，吹起几张散落的作业纸，在昏黄…」）

## 整书结构指标

```
chapters: 6
total_chars: 6430
chapter_chars_mean: 1072
chapter_chars_median: 1065
chapter_chars_cv: 0.28
paragraphs_mean: 24.8
dialogue_chars_pct: 25.5
dialogue_para_pct: 60.9
interiority_para_pct: 1.3
narration_para_pct: 37.7
turn_under20_pct: 90.3
turn_over200_pct: 0.0
attr_say_pct: 49.5
attr_adv_pct: 0.0
scenes_per_chapter: 2.3
dialogue_run_mean: 2.4
turn_len_median: 10
```
