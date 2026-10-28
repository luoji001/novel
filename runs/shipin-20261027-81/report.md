# 胶片与放映机 生成报告

slug：`shipin-20261027-81`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6549
LLM 调用：57 次，累计 132.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 擦拭胶片的手指 | 630 | short | 18.8 | 0 |  | 3 |
| 2 | 钥匙与锈迹 | 1255 | normal | 94.5 | 0 |  | 0 |
| 3 | 测量与红绳 | 1329 | normal | 36.7 | 0 |  | 1 |
| 4 | 藏票于胶片盒 | 1295 | normal | 89.5 | 0 |  | 0 |
| 5 | 红绳沿手腕滑落 | 917 | normal | 36.0 | 0 |  | 2 |
| 6 | 放映机轻推胶片 | 1117 | normal | 89.3 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 563 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - [observe] 章内自我复读 4 句（如「他知道那是他的父亲留下的…」）
- 第 5 章：
  - 单条套路句式超限：「周镇长的」×5
  - [observe] 章节过短 848 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 6088
chapter_chars_mean: 1015
chapter_chars_median: 1100
chapter_chars_cv: 0.26
paragraphs_mean: 30.8
dialogue_chars_pct: 18.1
dialogue_para_pct: 34.9
interiority_para_pct: 2.7
narration_para_pct: 62.4
turn_under20_pct: 90.5
turn_over200_pct: 0.0
attr_say_pct: 62.0
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 1.3
turn_len_median: 13
```
