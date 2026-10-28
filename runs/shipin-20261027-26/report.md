# 硬币 生成报告

slug：`shipin-20261027-26`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6411
LLM 调用：57 次，累计 134.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 硬币与耳钉对望 | 629 | short | 38.0 | 0 |  | 1 |
| 2 | 硬币与耳钉对望 | 1188 | normal | 94.6 | 0 |  | 1 |
| 3 | 红笔圈出的数字 | 1145 | normal | 93.5 | 0 |  | 1 |
| 4 | 硬币与计时器对望 | 1184 | normal | 91.4 | 0 |  | 1 |
| 5 | 数字与耳钉对望 | 1183 | normal | 36.5 | 0 |  | 4 |
| 6 | 硬币与胎记对望 | 1076 | normal | 91.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 552 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 标题重复：「硬币与耳钉对望」已存在
- 第 3 章：
  - 命中套话收尾句
- 第 4 章：
  - [observe] 标题与《硬币与耳钉对望》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「林小满的」×4
  - narration_para_pct 17.4 低于目标 35.0
  - [observe] 章内自我复读 4 句（如「陈志强皱起眉头：“你是不是太在意这些数字了…」）
  - [observe] 标题与《硬币与耳钉对望》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 标题与《硬币与耳钉对望》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 5944
chapter_chars_mean: 991
chapter_chars_median: 1075
chapter_chars_cv: 0.22
paragraphs_mean: 30.8
dialogue_chars_pct: 17.9
dialogue_para_pct: 46.9
interiority_para_pct: 1.4
narration_para_pct: 51.7
turn_under20_pct: 96.4
turn_over200_pct: 0.0
attr_say_pct: 54.0
attr_adv_pct: 0.0
scenes_per_chapter: 2.3
dialogue_run_mean: 1.8
turn_len_median: 8
```
