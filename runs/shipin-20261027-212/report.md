# 铜镜风波 生成报告

slug：`shipin-20261027-212`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6482
LLM 调用：57 次，累计 140.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜质推子震颤 | 474 | short | 37.8 | 0 |  | 3 |
| 2 | 铜推子轻颤 | 1317 | normal | 89.3 | 0 |  | 4 |
| 3 | 铜质推子争夺 | 1080 | normal | 90.0 | 0 |  | 1 |
| 4 | 铜推子争夺 | 1237 | normal | 92.9 | 0 |  | 1 |
| 5 | 镜子裂痕映心肠 | 1170 | normal | 90.0 | 0 |  | 0 |
| 6 | 镜子裂痕 | 1198 | normal | 89.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 4.5 低于目标 5.0
  - narration_para_pct 90.5 高于目标 90.0
  - [observe] 章节过短 418 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「李师傅的」×4、「老张站在」×3
  - narration_para_pct 16.1 低于目标 35.0
  - dialogue_run_mean 6.5 高于目标 4.0
  - [observe] 标题与《铜质推子震颤》近似 0.73 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 标题与《铜质推子震颤》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - [observe] 标题与《铜质推子争夺》近似 0.91 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 标题与《镜子裂痕映心肠》近似 0.73 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6022
chapter_chars_mean: 1004
chapter_chars_median: 1106
chapter_chars_cv: 0.29
paragraphs_mean: 31
dialogue_chars_pct: 20.8
dialogue_para_pct: 48.4
interiority_para_pct: 1.0
narration_para_pct: 50.6
turn_under20_pct: 95.4
turn_over200_pct: 0.0
attr_say_pct: 23.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 2.4
turn_len_median: 9
```
