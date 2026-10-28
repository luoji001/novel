# 红带 生成报告

slug：`shipin-20261027-135`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6623
LLM 调用：57 次，累计 134.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 抓录像带的手 | 697 | short | 97.2 | 0 |  | 0 |
| 2 | 抢夺录像带的对决 | 1209 | normal | 90.4 | 0 |  | 1 |
| 3 | 撕破购物袋的瞬间 | 1289 | normal | 92.7 | 0 |  | 0 |
| 4 | 收银机上的指纹 | 872 | normal | 23.9 | 0 |  | 3 |
| 5 | 钥匙划过绷带 | 1094 | normal | 93.4 | 0 |  | 1 |
| 6 | 耳钉与钥匙相碰 | 1456 | normal | 93.7 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「陈志远的」×3
- 第 4 章：
  - 单条套路句式超限：「小林站在」×3
  - dialogue_chars_pct 3.6 低于目标 5.0
  - [observe] 章节过短 813 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - 单条套路句式超限：「陈志远的」×4

## 整书结构指标

```
chapters: 6
total_chars: 6197
chapter_chars_mean: 1033
chapter_chars_median: 1078
chapter_chars_cv: 0.26
paragraphs_mean: 27.5
dialogue_chars_pct: 16.5
dialogue_para_pct: 41.1
interiority_para_pct: 1.7
narration_para_pct: 57.2
turn_under20_pct: 99.1
turn_over200_pct: 0.0
attr_say_pct: 49.3
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 1.4
turn_len_median: 9
```
