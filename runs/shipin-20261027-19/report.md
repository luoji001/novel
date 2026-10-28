# 雨靴 生成报告

slug：`shipin-20261027-19`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6277
LLM 调用：57 次，累计 133.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扫帚与拐杖 | 481 | short | 39.6 | 0 |  | 1 |
| 2 | 钥匙与锁孔 | 908 | normal | 20.1 | 0 |  | 3 |
| 3 | 报纸的折痕 | 880 | normal | 23.5 | 0 |  | 2 |
| 4 | 雨靴与拐杖 | 1412 | normal | 93.6 | 0 |  | 1 |
| 5 | 保温杯与烧伤疤痕 | 1403 | normal | 94.5 | 0 |  | 1 |
| 6 | 雨靴与耳环 | 1187 | normal | 92.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 438 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - dialogue_chars_pct 1.2 低于目标 5.0
  - interiority_para_pct 6.7 高于目标 6.0
  - [observe] 章节过短 810 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - [observe] 章内自我复读 9 句（如「她站起身，拿起对讲机，报纸随着她的动作飘落到地上…」）
  - [observe] 章节过短 794 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - [observe] 标题与《扫帚与拐杖》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 31.0 低于目标 35.0
- 第 6 章：
  - narration_para_pct 30.4 低于目标 35.0
  - [observe] 标题与《雨靴与拐杖》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5814
chapter_chars_mean: 969
chapter_chars_median: 969
chapter_chars_cv: 0.36
paragraphs_mean: 28
dialogue_chars_pct: 19.0
dialogue_para_pct: 46.5
interiority_para_pct: 2.5
narration_para_pct: 50.9
turn_under20_pct: 94.2
turn_over200_pct: 0.0
attr_say_pct: 23.9
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 1.9
turn_len_median: 10
```
