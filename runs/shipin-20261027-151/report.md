# 胶片的终点 生成报告

slug：`shipin-20261027-151`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5544
LLM 调用：57 次，累计 115.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 胶片边缘的标签 | 477 | short | 37.9 | 0 |  | 1 |
| 2 | 钥匙的第三颗齿轮 | 1017 | normal | 94.1 | 0 |  | 0 |
| 3 | 放大镜的光圈 | 1131 | normal | 93.5 | 0 |  | 0 |
| 4 | 耳钉与窗帘的触碰 | 726 | normal | 19.8 | 0 |  | 3 |
| 5 | 胶片缓缓拉出 | 1171 | normal | 86.9 | 0 |  | 2 |
| 6 | 胶片缓缓拉出 | 1016 | normal | 91.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 422 < 597（本章目标 1087 字的 55%）
- 第 4 章：
  - dialogue_chars_pct 0.7 低于目标 5.0
  - narration_para_pct 96.5 高于目标 90.0
  - [observe] 章节过短 543 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - 单条套路句式超限：「老张站在」×3
  - interiority_para_pct 8.3 高于目标 6.0
- 第 6 章：
  - [observe] 标题重复：「胶片缓缓拉出」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5068
chapter_chars_mean: 845
chapter_chars_median: 962
chapter_chars_cv: 0.34
paragraphs_mean: 27.3
dialogue_chars_pct: 15.1
dialogue_para_pct: 39.0
interiority_para_pct: 3.6
narration_para_pct: 57.4
turn_under20_pct: 98.5
turn_over200_pct: 0.0
attr_say_pct: 52.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.5
turn_len_median: 9
```
