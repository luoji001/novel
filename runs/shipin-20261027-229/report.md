# 雨靴 生成报告

slug：`shipin-20261027-229`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6362
LLM 调用：57 次，累计 136.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 争夺雨靴 | 702 | short | 96.9 | 0 |  | 0 |
| 2 | 钥匙与雨靴之争 | 1211 | normal | 91.0 | 0 |  | 1 |
| 3 | 电费单上的姓名 | 1159 | normal | 88.7 | 0 |  | 2 |
| 4 | 红布条的温度 | 1079 | normal | 37.5 | 0 |  | 2 |
| 5 | 蹬鞋的动作 | 1320 | normal | 93.7 | 0 |  | 1 |
| 6 | 抱靴入怀 | 885 | normal | 17.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「张素芬站在」×3
- 第 3 章：
  - narration_para_pct 10.5 低于目标 35.0
  - dialogue_run_mean 8.5 高于目标 4.0
- 第 4 章：
  - 单条套路句式超限：「李建国的」×4
  - [observe] 章内自我复读 1 句（如「你……你怎么知道的？…」）
- 第 5 章：
  - 单条套路句式超限：「李建国的」×3
- 第 6 章：
  - [observe] 章内自我复读 4 句（如「靴子边缘有些磨损，却格外干净…」）
  - [observe] 章节过短 726 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5910
chapter_chars_mean: 985
chapter_chars_median: 1060
chapter_chars_cv: 0.25
paragraphs_mean: 27.2
dialogue_chars_pct: 21.1
dialogue_para_pct: 55.2
interiority_para_pct: 2.1
narration_para_pct: 42.6
turn_under20_pct: 80.8
turn_over200_pct: 0.0
attr_say_pct: 22.8
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 3.1
turn_len_median: 10
```
