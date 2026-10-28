# 药瓶 生成报告

slug：`shipin-20261027-140`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6913
LLM 调用：57 次，累计 139.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 碰触药瓶的指尖 | 478 | short | 37.6 | 0 |  | 2 |
| 2 | 药瓶与病历本的对峙 | 1426 | normal | 93.2 | 0 |  | 1 |
| 3 | 棉球拂过的药瓶 | 1345 | normal | 35.6 | 0 |  | 4 |
| 4 | 药瓶与诊断书的对峙 | 1110 | normal | 89.4 | 0 |  | 1 |
| 5 | 药瓶滑向托盘边缘 | 1376 | normal | 89.7 | 0 |  | 1 |
| 6 | 药瓶坠落瞬间 | 1172 | normal | 35.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李秀兰的」×3
  - [observe] 章节过短 447 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「周玉兰的」×3、「李秀兰的」×3
- 第 3 章：
  - 单条套路句式超限：「李秀兰的」×3
  - narration_para_pct 16.7 低于目标 35.0
  - dialogue_run_mean 4.8 高于目标 4.0
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）
- 第 4 章：
  - [observe] 标题与《药瓶与病历本的对峙》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「李秀兰站在」×3、「李秀兰的」×3
- 第 6 章：
  - 单条套路句式超限：「李秀兰站在」×3、「周玉兰的」×3
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）

## 整书结构指标

```
chapters: 6
total_chars: 6463
chapter_chars_mean: 1077
chapter_chars_median: 1176
chapter_chars_cv: 0.31
paragraphs_mean: 29.2
dialogue_chars_pct: 21.7
dialogue_para_pct: 61.0
interiority_para_pct: 2.3
narration_para_pct: 36.7
turn_under20_pct: 98.5
turn_over200_pct: 0.0
attr_say_pct: 58.2
attr_adv_pct: 18.2
scenes_per_chapter: 1.8
dialogue_run_mean: 2.5
turn_len_median: 8
```
