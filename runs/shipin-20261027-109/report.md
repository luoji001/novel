# 胶片标签 生成报告

slug：`shipin-20261027-109`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6421
LLM 调用：57 次，累计 133.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 胶片盒上的指纹 | 654 | short | 97.4 | 0 |  | 0 |
| 2 | 摩挲公文包边缘 | 1223 | normal | 39.2 | 0 |  | 1 |
| 3 | 摩挲电影票根 | 1077 | normal | 92.0 | 0 |  | 0 |
| 4 | 摩挲胶片盒边缘 | 1008 | normal | 90.6 | 0 |  | 0 |
| 5 | 摩挲银质耳环 | 1193 | normal | 86.4 | 0 |  | 3 |
| 6 | 摩挲胶片盒边缘 | 1260 | normal | 89.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - dialogue_chars_pct 4.7 低于目标 5.0
- 第 5 章：
  - narration_para_pct 17.9 低于目标 35.0
  - attr_adv_pct 15.8 高于目标 10.0
  - dialogue_run_mean 5.8 高于目标 4.0
- 第 6 章：
  - [observe] 标题重复：「摩挲胶片盒边缘」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6031
chapter_chars_mean: 1005
chapter_chars_median: 1062
chapter_chars_cv: 0.21
paragraphs_mean: 23.2
dialogue_chars_pct: 16.8
dialogue_para_pct: 44.1
interiority_para_pct: 2.2
narration_para_pct: 53.7
turn_under20_pct: 90.6
turn_over200_pct: 0.0
attr_say_pct: 45.5
attr_adv_pct: 2.9
scenes_per_chapter: 1.8
dialogue_run_mean: 2.4
turn_len_median: 10
```
