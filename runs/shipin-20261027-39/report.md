# 铜铃 生成报告

slug：`shipin-20261027-39`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5826
LLM 调用：57 次，累计 130.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 胶片袋上的铅笔字 | 551 | short | 36.4 | 0 |  | 2 |
| 2 | 钥匙落锁 | 847 | normal | 21.8 | 0 |  | 1 |
| 3 | 胶片盒在摇晃 | 873 | normal | 36.9 | 0 |  | 1 |
| 4 | 铜铃在摇晃 | 1082 | normal | 93.8 | 0 |  | 1 |
| 5 | 胶片盒在摇晃 | 1288 | normal | 91.8 | 0 |  | 3 |
| 6 | 铜铃静止 | 1179 | normal | 55.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 5 句（如「老李转过头，看着风中摇摆的铜铃，手指不自觉地摩挲…」）
  - [observe] 章节过短 500 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章节过短 811 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - [observe] 章节过短 835 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - dialogue_chars_pct 4.9 低于目标 5.0
- 第 5 章：
  - 单条套路句式超限：「周正国的」×3
  - narration_para_pct 26.5 低于目标 35.0
  - [observe] 标题重复：「胶片盒在摇晃」已存在
- 第 6 章：
  - 单条套路句式超限：「老李站在」×3
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 95.8 高于目标 90.0

## 整书结构指标

```
chapters: 6
total_chars: 5435
chapter_chars_mean: 906
chapter_chars_median: 900
chapter_chars_cv: 0.28
paragraphs_mean: 23.2
dialogue_chars_pct: 10.8
dialogue_para_pct: 32.8
interiority_para_pct: 1.5
narration_para_pct: 65.7
turn_under20_pct: 92.7
turn_over200_pct: 0.0
attr_say_pct: 62.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.7
turn_len_median: 9
```
