# 争码 生成报告

slug：`shipin-20261027-297`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6961
LLM 调用：57 次，累计 138.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扫码之争 | 903 | short | 98.3 | 0 |  | 3 |
| 2 | 撕二维码 | 1236 | normal | 90.6 | 0 |  | 0 |
| 3 | 拍打车筐 | 1655 | normal | 93.1 | 0 |  | 1 |
| 4 | 撕二维码 | 1385 | normal | 91.9 | 0 |  | 2 |
| 5 | 撕二维码 | 1074 | normal | 90.1 | 0 |  | 1 |
| 6 | 警报响起时 | 702 | normal | 36.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈阿婆的」×4
  - narration_para_pct 24.1 低于目标 35.0
  - dialogue_run_mean 4.2 高于目标 4.0
- 第 3 章：
  - attr_adv_pct 16.7 高于目标 10.0
- 第 4 章：
  - narration_para_pct 27.0 低于目标 35.0
  - [observe] 标题重复：「撕二维码」已存在
- 第 5 章：
  - [observe] 标题重复：「撕二维码」已存在
- 第 6 章：
  - [observe] 章节过短 659 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 6503
chapter_chars_mean: 1084
chapter_chars_median: 1061
chapter_chars_cv: 0.31
paragraphs_mean: 31.5
dialogue_chars_pct: 21.6
dialogue_para_pct: 53.7
interiority_para_pct: 1.6
narration_para_pct: 44.6
turn_under20_pct: 91.4
turn_over200_pct: 0.0
attr_say_pct: 35.8
attr_adv_pct: 4.1
scenes_per_chapter: 2.2
dialogue_run_mean: 2.4
turn_len_median: 10
```
