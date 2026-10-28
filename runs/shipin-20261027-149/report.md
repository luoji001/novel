# 红灯按钮 生成报告

slug：`shipin-20261027-149`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5807
LLM 调用：57 次，累计 119.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红色警报按钮 | 522 | short | 20.1 | 0 |  | 3 |
| 2 | 机械表切锁 | 744 | normal | 36.7 | 0 |  | 1 |
| 3 | 钥匙转动声 | 1183 | normal | 90.7 | 0 |  | 1 |
| 4 | 红色警报按钮按下 | 1010 | normal | 90.4 | 0 |  | 1 |
| 5 | 钥匙转动声 | 1178 | normal | 93.4 | 0 |  | 1 |
| 6 | 钥匙转动声 | 1164 | normal | 92.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 1.9 低于目标 5.0
  - narration_para_pct 90.5 高于目标 90.0
  - [observe] 章节过短 466 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章节过短 683 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - 单条套路句式超限：「带着一丝」×3
- 第 4 章：
  - [observe] 标题与《红色警报按钮》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 标题重复：「钥匙转动声」已存在
- 第 6 章：
  - narration_para_pct 32.3 低于目标 35.0
  - [observe] 标题重复：「钥匙转动声」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5467
chapter_chars_mean: 911
chapter_chars_median: 1020
chapter_chars_cv: 0.31
paragraphs_mean: 21
dialogue_chars_pct: 12.9
dialogue_para_pct: 44.6
interiority_para_pct: 0.4
narration_para_pct: 55.0
turn_under20_pct: 98.4
turn_over200_pct: 0.0
attr_say_pct: 23.8
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.7
turn_len_median: 9
```
