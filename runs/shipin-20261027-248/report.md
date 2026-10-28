# 红绳 生成报告

slug：`shipin-20261027-248`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5738
LLM 调用：57 次，累计 121.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙板上的划痕 | 502 | short | 37.4 | 0 |  | 1 |
| 2 | 钥匙扣的对峙 | 1098 | normal | 90.7 | 0 |  | 1 |
| 3 | 钥匙板上的裂痕 | 1117 | normal | 89.6 | 0 |  | 1 |
| 4 | 墨汁晕染的疑问 | 800 | normal | 21.7 | 0 |  | 1 |
| 5 | 钥匙板上的红绳 | 1231 | normal | 88.8 | 0 |  | 2 |
| 6 | 印章的温度 | 984 | normal | 37.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 455 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 32.4 低于目标 35.0
- 第 3 章：
  - [observe] 标题与《钥匙板上的划痕》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] 章节过短 595 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - narration_para_pct 27.3 低于目标 35.0
  - [observe] 标题与《钥匙板上的划痕》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 47.2 高于目标 45.0
  - narration_para_pct 22.2 低于目标 35.0
  - [observe] 章内自我复读 3 句（如「刚才你说过，我就是因为它才找到你这里的…」）

## 整书结构指标

```
chapters: 6
total_chars: 5163
chapter_chars_mean: 860
chapter_chars_median: 962
chapter_chars_cv: 0.32
paragraphs_mean: 35.5
dialogue_chars_pct: 26.8
dialogue_para_pct: 56.9
interiority_para_pct: 1.6
narration_para_pct: 41.6
turn_under20_pct: 94.2
turn_over200_pct: 0.0
attr_say_pct: 49.1
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 1.9
turn_len_median: 10
```
