# 雨靴的归属 生成报告

slug：`shipin-20261027-327`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6918
LLM 调用：57 次，累计 137.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 雨靴的归属 | 830 | short | 39.0 | 0 |  | 1 |
| 2 | 钥匙与雨靴的对峙 | 1150 | normal | 94.1 | 0 |  | 1 |
| 3 | 拖把与报纸的对峙 | 1166 | normal | 57.2 | 0 |  | 0 |
| 4 | 雨靴的破洞 | 1159 | normal | 90.9 | 0 |  | 3 |
| 5 | 钥匙与水渍对峙 | 1406 | normal | 88.0 | 0 |  | 3 |
| 6 | 雨靴与钥匙的对峙 | 1201 | normal | 91.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 100.0 > 18.0（结构塌缩）
- 第 2 章：
  - dialogue_run_mean 4.2 高于目标 4.0
- 第 4 章：
  - narration_para_pct 19.4 低于目标 35.0
  - dialogue_run_mean 4.2 高于目标 4.0
  - [observe] 标题与《雨靴的归属》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「陈玉兰站在」×3
  - interiority_para_pct 6.2 高于目标 6.0
  - [observe] 标题与《钥匙与雨靴的对峙》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 47.4 高于目标 45.0
  - narration_para_pct 18.2 低于目标 35.0
  - dialogue_run_mean 5.4 高于目标 4.0
  - [observe] 标题与《钥匙与雨靴的对峙》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6492
chapter_chars_mean: 1082
chapter_chars_median: 1099
chapter_chars_cv: 0.16
paragraphs_mean: 27.5
dialogue_chars_pct: 26.1
dialogue_para_pct: 56.3
interiority_para_pct: 2.7
narration_para_pct: 41.0
turn_under20_pct: 92.5
turn_over200_pct: 0.0
attr_say_pct: 58.6
attr_adv_pct: 12.1
scenes_per_chapter: 1.7
dialogue_run_mean: 3.6
turn_len_median: 10
```
