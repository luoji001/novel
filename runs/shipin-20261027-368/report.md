# 铜铃 生成报告

slug：`shipin-20261027-368`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5985
LLM 调用：57 次，累计 128.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 纸片映出红袖章 | 593 | short | 37.7 | 0 |  | 1 |
| 2 | 铜钥匙敲击桌面 | 1110 | normal | 93.7 | 0 |  | 0 |
| 3 | 木箱底泛黄纸条 | 841 | normal | 36.8 | 0 |  | 1 |
| 4 | 银质耳钉坠入账本 | 1076 | normal | 91.7 | 0 |  | 1 |
| 5 | 铜铃敲击桌面三下 | 1173 | normal | 35.0 | 0 |  | 2 |
| 6 | 船票贴胸 | 1186 | normal | 92.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 532 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - [observe] 章节过短 776 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - 单条套路句式超限：「林小满的」×4
- 第 5 章：
  - [observe] 章内自我复读 9 句（如「他缓缓合上了账本，低声说道：“等会儿我去看看，是…」）
  - [observe] 标题与《铜钥匙敲击桌面》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 34.5 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 5535
chapter_chars_mean: 922
chapter_chars_median: 1008
chapter_chars_cv: 0.25
paragraphs_mean: 29
dialogue_chars_pct: 26.5
dialogue_para_pct: 56.5
interiority_para_pct: 0.4
narration_para_pct: 43.1
turn_under20_pct: 87.7
turn_over200_pct: 0.0
attr_say_pct: 40.9
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 2.2
turn_len_median: 10
```
