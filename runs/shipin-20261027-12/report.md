# 硬币的重量 生成报告

slug：`shipin-20261027-12`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6377
LLM 调用：57 次，累计 126.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 硬币在风中飘荡 | 843 | short | 93.5 | 0 |  | 0 |
| 2 | 硬币与手机的对望 | 1319 | normal | 90.3 | 0 |  | 0 |
| 3 | 手机的倒影 | 990 | normal | 91.6 | 0 |  | 1 |
| 4 | 硬币与露水的触碰 | 1322 | normal | 90.8 | 0 |  | 0 |
| 5 | 红绳的重量 | 1016 | normal | 35.6 | 0 |  | 1 |
| 6 | 手机的微光 | 881 | normal | 35.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - narration_para_pct 30.8 低于目标 35.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「他说着，用手轻轻拨弄了一下红绳，让它随着手臂的动…」）
- 第 6 章：
  - [observe] 章节过短 832 < 870（本章目标 1582 字的 55%）
  - [observe] 标题与《手机的倒影》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5957
chapter_chars_mean: 993
chapter_chars_median: 939
chapter_chars_cv: 0.2
paragraphs_mean: 27.3
dialogue_chars_pct: 18.6
dialogue_para_pct: 49.7
interiority_para_pct: 1.7
narration_para_pct: 48.6
turn_under20_pct: 98.2
turn_over200_pct: 0.0
attr_say_pct: 39.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.2
turn_len_median: 10
```
