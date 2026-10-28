# 车票 生成报告

slug：`shipin-20261027-309`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7383
LLM 调用：57 次，累计 183.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 袋子的重量 | 1023 | short | 96.4 | 0 |  | 0 |
| 2 | 撕开蛇皮袋 | 1140 | normal | 90.3 | 0 |  | 0 |
| 3 | 帽子的重量 | 1404 | normal | 92.8 | 0 |  | 3 |
| 4 | 车票的边缘 | 1358 | normal | 91.6 | 0 |  | 0 |
| 5 | 指纹的温度 | 1187 | normal | 90.6 | 0 |  | 1 |
| 6 | 车票的体温 | 1265 | normal | 94.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「王德福的」×6
  - [observe] 标题与《袋子的重量》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「王德福的」×4
- 第 6 章：
  - 单条套路句式超限：「李建军的」×4、「李建军站在」×3
  - narration_para_pct 34.1 低于目标 35.0
  - [observe] 标题与《车票的边缘》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6817
chapter_chars_mean: 1136
chapter_chars_median: 1128
chapter_chars_cv: 0.12
paragraphs_mean: 40.2
dialogue_chars_pct: 27.6
dialogue_para_pct: 48.1
interiority_para_pct: 0.4
narration_para_pct: 51.5
turn_under20_pct: 90.7
turn_over200_pct: 0.0
attr_say_pct: 38.3
attr_adv_pct: 0.0
scenes_per_chapter: 2
dialogue_run_mean: 1.7
turn_len_median: 9
```
