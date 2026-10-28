# 粉笔划光 生成报告

slug：`shipin-20261027-104`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6788
LLM 调用：57 次，累计 138.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铅笔盒闪光 | 665 | short | 22.6 | 0 |  | 1 |
| 2 | 铅笔盒藏匿 | 1420 | normal | 92.0 | 0 |  | 1 |
| 3 | 粉笔划光 | 972 | normal | 36.3 | 0 |  | 2 |
| 4 | 橡皮裂痕 | 1261 | normal | 35.4 | 0 |  | 1 |
| 5 | 手机电筒闪烁 | 1097 | normal | 89.8 | 0 |  | 1 |
| 6 | 粉笔划光 | 1367 | normal | 91.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 590 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 标题与《铅笔盒闪光》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - narration_para_pct 92.2 高于目标 90.0
  - [observe] 章节过短 744 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - [observe] 章内自我复读 5 句（如「他站起身，慢慢走到王小明面前，影子投在地上，像一…」）
- 第 5 章：
  - interiority_para_pct 7.4 高于目标 6.0
- 第 6 章：
  - [observe] 标题重复：「粉笔划光」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6202
chapter_chars_mean: 1034
chapter_chars_median: 1115
chapter_chars_cv: 0.3
paragraphs_mean: 36.8
dialogue_chars_pct: 17.4
dialogue_para_pct: 35.8
interiority_para_pct: 2.4
narration_para_pct: 61.8
turn_under20_pct: 94.1
turn_over200_pct: 0.0
attr_say_pct: 33.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.4
turn_len_median: 9
```
