# 老式推子 生成报告

slug：`shipin-20261027-254`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5863
LLM 调用：57 次，累计 125.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 擦拭账本的手指 | 523 | short | 21.2 | 0 |  | 3 |
| 2 | 触摸箱沿的指尖 | 1185 | normal | 36.7 | 0 |  | 1 |
| 3 | 抚摸镜框的指尖 | 991 | normal | 36.3 | 0 |  | 1 |
| 4 | 擦拭账本的手指 | 1375 | normal | 89.7 | 0 |  | 1 |
| 5 | 触碰账本的指尖 | 934 | normal | 36.6 | 0 |  | 1 |
| 6 | 触摸箱沿的指尖 | 849 | normal | 35.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.8 低于目标 5.0
  - narration_para_pct 92.9 高于目标 90.0
  - [observe] 章节过短 480 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章内自我复读 2 句（如「师父，我想把箱子收起来…」）
- 第 3 章：
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
- 第 4 章：
  - [observe] 标题重复：「擦拭账本的手指」已存在
- 第 5 章：
  - [observe] 章节过短 867 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - [observe] 章节过短 772 < 870（本章目标 1582 字的 55%）
  - [observe] 标题重复：「触摸箱沿的指尖」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5417
chapter_chars_mean: 903
chapter_chars_median: 896
chapter_chars_cv: 0.3
paragraphs_mean: 27.7
dialogue_chars_pct: 18.6
dialogue_para_pct: 38.9
interiority_para_pct: 1.0
narration_para_pct: 60.1
turn_under20_pct: 93.4
turn_over200_pct: 0.0
attr_say_pct: 28.7
attr_adv_pct: 7.6
scenes_per_chapter: 1.3
dialogue_run_mean: 1.5
turn_len_median: 10
```
