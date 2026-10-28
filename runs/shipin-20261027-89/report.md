# 雨靴 生成报告

slug：`shipin-20261027-89`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5493
LLM 调用：57 次，累计 142.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 报纸与通风口 | 604 | short | 38.7 | 0 |  | 1 |
| 2 | 钥匙与便条 | 809 | normal | 22.6 | 0 |  | 1 |
| 3 | 镜子与钥匙 | 1118 | normal | 91.4 | 0 |  | 0 |
| 4 | 塑料袋与碎纸 | 1010 | normal | 52.9 | 0 |  | 0 |
| 5 | 塞报纸 | 993 | normal | 90.6 | 0 |  | 0 |
| 6 | 钥匙与靴子 | 953 | normal | 92.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 554 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章节过短 758 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - [observe] 标题与《钥匙与便条》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5112
chapter_chars_mean: 852
chapter_chars_median: 890
chapter_chars_cv: 0.21
paragraphs_mean: 21.3
dialogue_chars_pct: 17.0
dialogue_para_pct: 44.2
interiority_para_pct: 0.0
narration_para_pct: 55.8
turn_under20_pct: 94.4
turn_over200_pct: 0.0
attr_say_pct: 50.0
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 1.8
turn_len_median: 10
```
