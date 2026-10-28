# 钥匙的归宿 生成报告

slug：`shipin-20261027-318`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5381
LLM 调用：57 次，累计 125.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲钥匙的指尖 | 712 | short | 90.7 | 0 |  | 1 |
| 2 | 钥匙卡入锁孔 | 1190 | normal | 92.0 | 0 |  | 1 |
| 3 | 账本坠入床底 | 415 | normal | 16.8 | 0 |  | 3 |
| 4 | 茶渍晕染的登记表 | 1130 | normal | 92.9 | 0 |  | 1 |
| 5 | 徽章贴胸的瞬间 | 880 | normal | 36.4 | 0 |  | 1 |
| 6 | 钥匙环坠地声 | 1048 | normal | 92.5 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 8.3 高于目标 6.0
- 第 2 章：
  - 单条套路句式超限：「沈国强的」×3
- 第 3 章：
  - dialogue_chars_pct 1.7 低于目标 5.0
  - narration_para_pct 94.7 高于目标 90.0
  - [observe] 章节过短 363 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - narration_para_pct 25.0 低于目标 35.0
- 第 5 章：
  - [observe] 章节过短 780 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 4994
chapter_chars_mean: 832
chapter_chars_median: 882
chapter_chars_cv: 0.35
paragraphs_mean: 23.5
dialogue_chars_pct: 18.2
dialogue_para_pct: 49.2
interiority_para_pct: 1.1
narration_para_pct: 49.6
turn_under20_pct: 96.7
turn_over200_pct: 0.0
attr_say_pct: 42.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.8
turn_len_median: 10
```
