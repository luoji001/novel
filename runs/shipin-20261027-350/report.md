# 药瓶的温度 生成报告

slug：`shipin-20261027-350`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5933
LLM 调用：57 次，累计 130.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 输液架的吱呀声 | 648 | short | 98.1 | 0 |  | 1 |
| 2 | 药瓶与手腕的纠缠 | 1196 | normal | 87.2 | 0 |  | 1 |
| 3 | 药瓶与手腕的纠缠 | 1073 | normal | 91.9 | 0 |  | 2 |
| 4 | 耳钉与病历纸摩擦 | 909 | normal | 36.4 | 0 |  | 2 |
| 5 | 胸牌的十字架闪烁 | 1044 | normal | 91.7 | 0 |  | 1 |
| 6 | 药瓶与手腕的纠缠 | 1057 | normal | 37.0 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林小满的」×4
- 第 2 章：
  - 单条套路句式超限：「林小满的」×5
- 第 3 章：
  - 单条套路句式超限：「林小满的」×3
  - [observe] 标题重复：「药瓶与手腕的纠缠」已存在
- 第 4 章：
  - [observe] 章节过短 837 < 870（本章目标 1582 字的 55%）
  - [observe] attr_adv_pct 100.0 > 18.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「林小满的」×3
- 第 6 章：
  - 单条套路句式超限：「林小满的」×5
  - narration_para_pct 28.6 低于目标 35.0
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）
  - [observe] 标题重复：「药瓶与手腕的纠缠」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5416
chapter_chars_mean: 903
chapter_chars_median: 958
chapter_chars_cv: 0.19
paragraphs_mean: 33.8
dialogue_chars_pct: 21.1
dialogue_para_pct: 47.2
interiority_para_pct: 0.4
narration_para_pct: 52.4
turn_under20_pct: 95.9
turn_over200_pct: 0.0
attr_say_pct: 59.7
attr_adv_pct: 27.6
scenes_per_chapter: 1.8
dialogue_run_mean: 2.4
turn_len_median: 8
```
