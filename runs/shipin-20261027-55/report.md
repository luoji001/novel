# 钥匙落雪 生成报告

slug：`shipin-20261027-55`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6527
LLM 调用：57 次，累计 139.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙的重量 | 932 | short | 99.7 | 0 |  | 0 |
| 2 | 保温杯的霜花 | 792 | normal | 37.0 | 0 |  | 1 |
| 3 | 钥匙坠入雪地 | 1392 | normal | 35.9 | 0 |  | 1 |
| 4 | 钥匙划破雪地 | 1140 | normal | 88.9 | 0 |  | 1 |
| 5 | 手机的闪光灯 | 1004 | normal | 89.2 | 0 |  | 0 |
| 6 | 钥匙与保温杯的对话 | 1261 | normal | 88.8 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章节过短 702 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
- 第 4 章：
  - [observe] 标题与《钥匙坠入雪地》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5876
chapter_chars_mean: 979
chapter_chars_median: 982
chapter_chars_cv: 0.21
paragraphs_mean: 41.3
dialogue_chars_pct: 20.5
dialogue_para_pct: 41.1
interiority_para_pct: 0.0
narration_para_pct: 58.9
turn_under20_pct: 98.6
turn_over200_pct: 0.0
attr_say_pct: 61.7
attr_adv_pct: 5.6
scenes_per_chapter: 1
dialogue_run_mean: 1.3
turn_len_median: 9
```
