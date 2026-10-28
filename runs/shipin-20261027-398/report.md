# 灯芯 生成报告

slug：`shipin-20261027-398`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7214
LLM 调用：57 次，累计 140.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 灯光的争夺 | 815 | short | 94.2 | 0 |  | 1 |
| 2 | 铅笔与折痕 | 1306 | normal | 36.8 | 0 |  | 1 |
| 3 | 应急灯的争夺 | 1515 | normal | 91.3 | 0 |  | 4 |
| 4 | 书包的拉链声 | 1356 | normal | 93.9 | 0 |  | 1 |
| 5 | 矿泉水瓶的裂痕 | 882 | normal | 37.4 | 0 |  | 1 |
| 6 | 铅笔的折痕 | 1334 | normal | 92.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「”王小明低」×3
- 第 2 章：
  - [observe] 章内自我复读 4 句（如「那只断了笔芯的铅笔，此刻正在纸上刻出一道深深的痕…」）
- 第 3 章：
  - 单条套路句式超限：「李国强站在」×3、「王小明的」×3、「李国强的」×3
  - narration_para_pct 22.6 低于目标 35.0
  - dialogue_run_mean 4.8 高于目标 4.0
  - [observe] 标题与《灯光的争夺》近似 0.73 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「王小明的」×3
- 第 5 章：
  - [observe] 章节过短 817 < 870（本章目标 1582 字的 55%）
- 第 6 章：
  - [observe] 标题与《铅笔与折痕》近似 0.80 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 6742
chapter_chars_mean: 1124
chapter_chars_median: 1242
chapter_chars_cv: 0.24
paragraphs_mean: 31.8
dialogue_chars_pct: 22.9
dialogue_para_pct: 57.8
interiority_para_pct: 1.1
narration_para_pct: 41.0
turn_under20_pct: 93.8
turn_over200_pct: 0.0
attr_say_pct: 29.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 2.8
turn_len_median: 10
```
