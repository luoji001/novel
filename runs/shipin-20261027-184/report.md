# 铜质推子 生成报告

slug：`shipin-20261027-184`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6002
LLM 调用：57 次，累计 130.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜质推子的年轮 | 561 | short | 38.1 | 0 |  | 1 |
| 2 | 推子与磨刀石对峙 | 1012 | normal | 88.2 | 0 |  | 0 |
| 3 | 推子与账本对峙 | 1249 | normal | 91.9 | 0 |  | 1 |
| 4 | 推子与红绳对峙 | 1103 | normal | 90.8 | 0 |  | 1 |
| 5 | 铜质推子的温度 | 1067 | normal | 35.6 | 0 |  | 2 |
| 6 | 推子与铁盒对峙 | 1004 | normal | 38.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 520 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - [observe] 标题与《推子与磨刀石对峙》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] 标题与《推子与账本对峙》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 章内自我复读 5 句（如「他顿了一下，望向墙上挂着的老照片，“你爸还在用呢…」）
  - [observe] 标题与《铜质推子的年轮》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 1.2 低于目标 5.0
  - narration_para_pct 97.7 高于目标 90.0
  - [observe] 标题与《推子与红绳对峙》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5563
chapter_chars_mean: 927
chapter_chars_median: 977
chapter_chars_cv: 0.24
paragraphs_mean: 28.5
dialogue_chars_pct: 19.8
dialogue_para_pct: 44.8
interiority_para_pct: 0.0
narration_para_pct: 55.2
turn_under20_pct: 94.6
turn_over200_pct: 0.0
attr_say_pct: 55.4
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 1.8
turn_len_median: 9
```
