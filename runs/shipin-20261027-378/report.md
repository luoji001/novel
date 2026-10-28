# 药瓶 生成报告

slug：`shipin-20261027-378`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6046
LLM 调用：57 次，累计 123.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 紧握药瓶的颤抖 | 383 | short | 23.3 | 0 |  | 1 |
| 2 | 红色胸牌的压制 | 1030 | normal | 37.6 | 0 |  | 1 |
| 3 | 保温杯与药瓶相碰 | 1013 | normal | 36.9 | 0 |  | 1 |
| 4 | 银环与电子秤的碰撞 | 1123 | normal | 36.5 | 0 |  | 2 |
| 5 | 红绳与胸牌的对峙 | 1233 | normal | 56.0 | 0 |  | 0 |
| 6 | 保温杯撞向药瓶 | 1258 | normal | 92.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 344 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）
- 第 3 章：
  - [observe] 章内自我复读 2 句（如「你现在这个样子，比那时候还糟糕…」）
- 第 4 章：
  - narration_para_pct 32.1 低于目标 35.0
  - [observe] 章内自我复读 1 句（如「女人攥着围裙边缘，脸色发白…」）
- 第 6 章：
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 标题与《保温杯与药瓶相碰》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5598
chapter_chars_mean: 933
chapter_chars_median: 1008
chapter_chars_cv: 0.32
paragraphs_mean: 29
dialogue_chars_pct: 21.0
dialogue_para_pct: 52.3
interiority_para_pct: 0.9
narration_para_pct: 46.8
turn_under20_pct: 97.8
turn_over200_pct: 0.0
attr_say_pct: 49.2
attr_adv_pct: 8.6
scenes_per_chapter: 2
dialogue_run_mean: 2.0
turn_len_median: 8
```
