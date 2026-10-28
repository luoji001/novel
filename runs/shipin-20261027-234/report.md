# 铜钥 生成报告

slug：`shipin-20261027-234`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5429
LLM 调用：57 次，累计 128.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙震动的瞬间 | 540 | short | 37.8 | 0 |  | 1 |
| 2 | 钥匙震颤的刹那 | 634 | normal | 23.7 | 0 |  | 1 |
| 3 | 钥匙按在登记本上 | 1003 | normal | 36.2 | 0 |  | 1 |
| 4 | 钥匙与耳钉相触 | 761 | normal | 36.1 | 0 |  | 1 |
| 5 | 钥匙敲击桌面 | 1341 | normal | 34.8 | 0 |  | 4 |
| 6 | 钥匙划破纸面 | 1144 | normal | 89.6 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 485 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章节过短 589 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - [observe] 章内自我复读 6 句（如「她没有回头，只是把记号笔收回口袋，轻声道：“我只…」）
- 第 4 章：
  - [observe] 章节过短 700 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - narration_para_pct 17.4 低于目标 35.0
  - attr_adv_pct 16.7 高于目标 10.0
  - dialogue_run_mean 4.8 高于目标 4.0
  - [observe] 章内自我复读 3 句（如「当时有个男人，拿着把和你现在一样的钥匙来找我…」）

## 整书结构指标

```
chapters: 6
total_chars: 5072
chapter_chars_mean: 845
chapter_chars_median: 818
chapter_chars_cv: 0.36
paragraphs_mean: 21.2
dialogue_chars_pct: 22.8
dialogue_para_pct: 56.8
interiority_para_pct: 0.0
narration_para_pct: 43.2
turn_under20_pct: 90.0
turn_over200_pct: 0.0
attr_say_pct: 43.5
attr_adv_pct: 5.4
scenes_per_chapter: 1.7
dialogue_run_mean: 2.1
turn_len_median: 10
```
