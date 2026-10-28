# 胶片的余光 生成报告

slug：`shipin-20261027-333`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6531
LLM 调用：57 次，累计 139.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 胶片盒的微光 | 511 | short | 37.8 | 0 |  | 1 |
| 2 | 公文包敲击放映机 | 1408 | normal | 90.8 | 0 |  | 2 |
| 3 | 电影票的裂痕 | 1205 | normal | 92.4 | 0 |  | 0 |
| 4 | 红袖章的震颤 | 932 | normal | 35.9 | 0 |  | 1 |
| 5 | 银质耳环的反光 | 1016 | normal | 91.4 | 0 |  | 0 |
| 6 | 胶片盒的微光 | 1453 | normal | 91.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 473 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「周国强的」×3
  - narration_para_pct 32.0 低于目标 35.0
- 第 4 章：
  - [observe] 章节过短 858 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - interiority_para_pct 6.2 高于目标 6.0
  - narration_para_pct 34.4 低于目标 35.0
  - [observe] 标题重复：「胶片盒的微光」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6043
chapter_chars_mean: 1007
chapter_chars_median: 1010
chapter_chars_cv: 0.33
paragraphs_mean: 30.8
dialogue_chars_pct: 25.4
dialogue_para_pct: 54.7
interiority_para_pct: 1.9
narration_para_pct: 43.3
turn_under20_pct: 94.5
turn_over200_pct: 0.0
attr_say_pct: 53.2
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 1.7
turn_len_median: 10
```
