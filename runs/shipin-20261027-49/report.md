# 铜铃 生成报告

slug：`shipin-20261027-49`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6012
LLM 调用：57 次，累计 141.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 箱子上的签名 | 660 | short | 38.4 | 0 |  | 1 |
| 2 | 登记簿的裂痕 | 1178 | normal | 37.4 | 0 |  | 2 |
| 3 | 热水浇铁门 | 1024 | normal | 91.1 | 0 |  | 0 |
| 4 | 钥匙划破暮色 | 1252 | normal | 92.5 | 0 |  | 1 |
| 5 | 红绳轻晃 | 985 | normal | 37.4 | 0 |  | 1 |
| 6 | 钥匙撞击锁孔 | 907 | normal | 16.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 592 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 32.3 低于目标 35.0
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「李建国的」×4
- 第 5 章：
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「李建国站在」×3
  - dialogue_chars_pct 3.5 低于目标 5.0
  - [observe] 章节过短 855 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5531
chapter_chars_mean: 922
chapter_chars_median: 912
chapter_chars_cv: 0.22
paragraphs_mean: 32.8
dialogue_chars_pct: 20.7
dialogue_para_pct: 42.0
interiority_para_pct: 0.4
narration_para_pct: 57.7
turn_under20_pct: 98.5
turn_over200_pct: 0.0
attr_say_pct: 40.0
attr_adv_pct: 10.1
scenes_per_chapter: 1.8
dialogue_run_mean: 1.8
turn_len_median: 10
```
