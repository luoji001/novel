# 红绳 生成报告

slug：`shipin-20261027-253`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6679
LLM 调用：57 次，累计 139.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铁钳擦出火星 | 594 | short | 39.0 | 0 |  | 1 |
| 2 | 钥匙串敲击 | 1100 | normal | 94.4 | 0 |  | 1 |
| 3 | 铁钳与车票 | 1214 | normal | 91.2 | 0 |  | 1 |
| 4 | 红绳缠蛇皮袋 | 1284 | normal | 92.4 | 0 |  | 0 |
| 5 | 证件落地声 | 1158 | normal | 15.6 | 0 |  | 2 |
| 6 | 手电筒照蛇皮袋 | 1323 | normal | 92.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 532 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 33.3 低于目标 35.0
- 第 3 章：
  - narration_para_pct 34.3 低于目标 35.0
- 第 5 章：
  - interiority_para_pct 13.6 高于目标 6.0
  - narration_para_pct 31.8 低于目标 35.0
- 第 6 章：
  - 单条套路句式超限：「王小兰的」×4、「李建国的」×4

## 整书结构指标

```
chapters: 6
total_chars: 6243
chapter_chars_mean: 1040
chapter_chars_median: 1116
chapter_chars_cv: 0.25
paragraphs_mean: 28.7
dialogue_chars_pct: 22.7
dialogue_para_pct: 53.6
interiority_para_pct: 3.0
narration_para_pct: 43.4
turn_under20_pct: 94.0
turn_over200_pct: 0.0
attr_say_pct: 9.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 2.4
turn_len_median: 10
```
