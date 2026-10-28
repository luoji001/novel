# 蛇皮袋 生成报告

slug：`shipin-20261027-127`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6271
LLM 调用：57 次，累计 188.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 蛇皮袋的破口 | 414 | short | 38.2 | 0 |  | 1 |
| 2 | 身份证的重量 | 1252 | normal | 37.3 | 0 |  | 1 |
| 3 | 钥匙的断裂 | 1347 | normal | 90.8 | 0 |  | 1 |
| 4 | 手机的震动 | 893 | normal | 36.6 | 0 |  | 1 |
| 5 | 钞票的温度 | 1195 | normal | 93.3 | 0 |  | 1 |
| 6 | 红绳的温度 | 1164 | normal | 93.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 382 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「王秀兰的」×3
- 第 4 章：
  - [observe] 章节过短 808 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - 单条套路句式超限：「王秀兰的」×3
- 第 6 章：
  - narration_para_pct 31.2 低于目标 35.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 标题与《钞票的温度》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5809
chapter_chars_mean: 968
chapter_chars_median: 1092
chapter_chars_cv: 0.34
paragraphs_mean: 31.3
dialogue_chars_pct: 23.1
dialogue_para_pct: 50.1
interiority_para_pct: 0.8
narration_para_pct: 49.1
turn_under20_pct: 99.3
turn_over200_pct: 0.0
attr_say_pct: 56.4
attr_adv_pct: 7.9
scenes_per_chapter: 1.8
dialogue_run_mean: 1.6
turn_len_median: 10
```
