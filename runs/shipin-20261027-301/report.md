# 锁孔的裂痕 生成报告

slug：`shipin-20261027-301`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6431
LLM 调用：57 次，累计 137.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红绳缠绕登记簿 | 576 | short | 37.6 | 0 |  | 1 |
| 2 | 钥匙与锁孔的对峙 | 1257 | normal | 91.4 | 0 |  | 1 |
| 3 | 指纹与登记簿的对峙 | 1440 | normal | 90.8 | 0 |  | 1 |
| 4 | 红绳与火车票 | 1131 | normal | 91.8 | 0 |  | 1 |
| 5 | 红绳里的车票 | 1019 | normal | 93.2 | 0 |  | 2 |
| 6 | 钥匙坠入尘埃 | 1002 | normal | 92.8 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 533 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「陈志强的」×4
- 第 3 章：
  - 单条套路句式超限：「陈志强的」×3
- 第 4 章：
  - narration_para_pct 25.7 低于目标 35.0
- 第 5 章：
  - narration_para_pct 34.8 低于目标 35.0
  - [observe] 标题与《红绳与火车票》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6014
chapter_chars_mean: 1002
chapter_chars_median: 1002
chapter_chars_cv: 0.29
paragraphs_mean: 26.7
dialogue_chars_pct: 24.8
dialogue_para_pct: 58.3
interiority_para_pct: 1.3
narration_para_pct: 40.4
turn_under20_pct: 92.7
turn_over200_pct: 0.0
attr_say_pct: 20.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 2.1
turn_len_median: 10
```
