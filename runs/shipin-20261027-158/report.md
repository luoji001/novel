# 船票 生成报告

slug：`shipin-20261027-158`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5888
LLM 调用：57 次，累计 134.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 船票贴在玻璃上 | 532 | short | 37.7 | 0 |  | 1 |
| 2 | 抚摸铁皮钱箱 | 1127 | normal | 37.7 | 0 |  | 1 |
| 3 | 船票与红绳交织 | 1193 | normal | 89.9 | 0 |  | 2 |
| 4 | 钥匙与硬币 | 1041 | normal | 94.2 | 0 |  | 0 |
| 5 | 触摸船票的指尖 | 707 | normal | 36.7 | 0 |  | 1 |
| 6 | 钥匙落入硬币罐 | 1282 | normal | 92.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 479 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] attr_adv_pct 33.3 > 18.0（结构塌缩）
- 第 3 章：
  - narration_para_pct 17.4 低于目标 35.0
  - dialogue_run_mean 9.5 高于目标 4.0
- 第 5 章：
  - [observe] 章节过短 630 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - [observe] 标题与《钥匙与硬币》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5475
chapter_chars_mean: 912
chapter_chars_median: 1016
chapter_chars_cv: 0.32
paragraphs_mean: 25.8
dialogue_chars_pct: 27.7
dialogue_para_pct: 58.7
interiority_para_pct: 1.3
narration_para_pct: 40.0
turn_under20_pct: 89.9
turn_over200_pct: 0.0
attr_say_pct: 17.1
attr_adv_pct: 6.5
scenes_per_chapter: 1.8
dialogue_run_mean: 3.2
turn_len_median: 10
```
