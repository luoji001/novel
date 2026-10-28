# 药瓶碎光 生成报告

slug：`shipin-20261027-280`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5991
LLM 调用：57 次，累计 130.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药瓶在两人之间摇晃 | 507 | short | 38.9 | 0 |  | 1 |
| 2 | 药瓶坠地碎裂 | 988 | normal | 91.8 | 0 |  | 1 |
| 3 | 药盒与红绳交缠 | 1224 | normal | 36.5 | 0 |  | 1 |
| 4 | 红绳绕过工牌 | 1204 | normal | 90.0 | 0 |  | 1 |
| 5 | 红绳缠绕药瓶 | 1166 | normal | 90.1 | 0 |  | 0 |
| 6 | 红绳绕过输液椅 | 896 | normal | 35.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 460 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「周雪梅的」×4
- 第 3 章：
  - [observe] 章内自我复读 2 句（如「医生说只有这个能救他…」）
- 第 4 章：
  - attr_adv_pct 14.3 高于目标 10.0
- 第 6 章：
  - 单条套路句式超限：「周雪梅的」×4
  - [observe] 章节过短 831 < 870（本章目标 1582 字的 55%）
  - [observe] 标题与《红绳绕过工牌》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5545
chapter_chars_mean: 924
chapter_chars_median: 1003
chapter_chars_cv: 0.28
paragraphs_mean: 29.2
dialogue_chars_pct: 26.3
dialogue_para_pct: 57.1
interiority_para_pct: 0.0
narration_para_pct: 42.9
turn_under20_pct: 91.2
turn_over200_pct: 0.0
attr_say_pct: 59.2
attr_adv_pct: 3.3
scenes_per_chapter: 1.3
dialogue_run_mean: 2.2
turn_len_median: 10
```
