# 药瓶 生成报告

slug：`shipin-20261027-112`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6388
LLM 调用：57 次，累计 135.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 体温计砸向扶手 | 570 | short | 38.5 | 0 |  | 1 |
| 2 | 注射器逼近手腕 | 1179 | normal | 36.0 | 0 |  | 1 |
| 3 | 药瓶与耳钉的对峙 | 1168 | normal | 93.2 | 0 |  | 2 |
| 4 | 体温计砸向药瓶 | 1080 | normal | 89.1 | 0 |  | 2 |
| 5 | 药瓶滚落地 | 1100 | normal | 90.9 | 0 |  | 0 |
| 6 | 体温计坠地瞬间 | 1285 | normal | 88.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 511 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章内自我复读 3 句（如「李娟的手指开始发抖，体温计从掌心滑落，在地上发出…」）
- 第 3 章：
  - 单条套路句式超限：「李娟站在」×3
  - narration_para_pct 16.7 低于目标 35.0
- 第 4 章：
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 标题与《体温计砸向扶手》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - 单条套路句式超限：「李娟站在」×3

## 整书结构指标

```
chapters: 6
total_chars: 5997
chapter_chars_mean: 1000
chapter_chars_median: 1070
chapter_chars_cv: 0.25
paragraphs_mean: 24.7
dialogue_chars_pct: 20.0
dialogue_para_pct: 59.0
interiority_para_pct: 0.0
narration_para_pct: 41.0
turn_under20_pct: 97.9
turn_over200_pct: 0.0
attr_say_pct: 44.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 2.0
turn_len_median: 10
```
