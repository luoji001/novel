# 雨靴的归属 生成报告

slug：`shipin-20261027-355`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6049
LLM 调用：57 次，累计 129.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 报纸的争夺战 | 419 | short | 38.1 | 0 |  | 1 |
| 2 | 钥匙与锈迹 | 1229 | normal | 37.8 | 0 |  | 2 |
| 3 | 保温杯的敲击声 | 1101 | normal | 37.7 | 0 |  | 2 |
| 4 | 红笔记的记录 | 1448 | normal | 91.9 | 0 |  | 1 |
| 5 | 房产证的裂痕 | 813 | normal | 37.1 | 0 |  | 2 |
| 6 | 系鞋带的手势 | 1033 | normal | 91.4 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 365 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 34.4 低于目标 35.0
  - [observe] 章内自我复读 5 句（如「周建国终于停下动作，转过身来，目光直视对方：“这…」）
- 第 3 章：
  - narration_para_pct 26.1 低于目标 35.0
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）
- 第 4 章：
  - narration_para_pct 32.1 低于目标 35.0
- 第 5 章：
  - [observe] 章节过短 745 < 870（本章目标 1582 字的 55%）
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）

## 整书结构指标

```
chapters: 6
total_chars: 5657
chapter_chars_mean: 943
chapter_chars_median: 1008
chapter_chars_cv: 0.37
paragraphs_mean: 25.2
dialogue_chars_pct: 34.0
dialogue_para_pct: 62.2
interiority_para_pct: 0.9
narration_para_pct: 36.9
turn_under20_pct: 83.8
turn_over200_pct: 0.0
attr_say_pct: 11.1
attr_adv_pct: 19.1
scenes_per_chapter: 1.7
dialogue_run_mean: 2.5
turn_len_median: 12
```
