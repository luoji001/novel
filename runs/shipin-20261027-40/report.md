# 硬币记 生成报告

slug：`shipin-20261027-40`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6423
LLM 调用：57 次，累计 129.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙与耳钉的对视 | 478 | short | 38.2 | 0 |  | 1 |
| 2 | 计时器裂痕 | 1134 | normal | 93.1 | 0 |  | 0 |
| 3 | 硬币与登记簿的对视 | 1272 | normal | 93.1 | 0 |  | 0 |
| 4 | 钥匙与硬币的对视 | 1127 | normal | 89.6 | 0 |  | 1 |
| 5 | 硬币与纸角的触碰 | 1337 | normal | 90.4 | 0 |  | 0 |
| 6 | 硬币与方向盘的触碰 | 1069 | normal | 89.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 418 < 597（本章目标 1087 字的 55%）
- 第 4 章：
  - [observe] 标题与《钥匙与耳钉的对视》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 标题与《硬币与纸角的触碰》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5896
chapter_chars_mean: 983
chapter_chars_median: 1037
chapter_chars_cv: 0.31
paragraphs_mean: 35.3
dialogue_chars_pct: 15.0
dialogue_para_pct: 38.8
interiority_para_pct: 1.0
narration_para_pct: 60.2
turn_under20_pct: 96.5
turn_over200_pct: 0.0
attr_say_pct: 39.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.7
turn_len_median: 8
```
