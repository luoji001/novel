# 显影液 生成报告

slug：`xuanyi-20261019-241`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14487
LLM 调用：68 次，累计 221.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 显影机的异响 | 1789 | short | 73.1 | 0 |  | 2 |
| 2 | 登记簿的折痕 | 3612 | normal | 84.7 | 0 |  | 4 |
| 3 | 显影机的纸屑 | 3672 | normal | 17.1 | 0 |  | 6 |
| 4 | 档案袋的指纹 | 3694 | normal | 90.9 | 0 |  | 3 |
| 5 | 显影机的裂痕 | 1715 | short | 66.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 4.0 低于目标 20.0
  - dialogue_run_mean 1.3 低于目标 1.5
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈国强的」×5、「带着一丝」×3
  - dialogue_chars_pct 15.7 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「之后，他抬头看了看窗外，仿佛在等待什么人或者事情…」）
- 第 3 章：
  - 单条套路句式超限：「陈国强的」×9
  - dialogue_chars_pct 8.4 低于目标 20.0
  - interiority_para_pct 29.2 高于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 章内自我复读 2 句（如「今天下午，有人来找我要了一张照片…」）
  - [observe] 标题与《显影机的异响》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「周雪梅的」×3、「为什么会」×3
  - narration_para_pct 12.0 低于目标 20.0
  - attr_adv_pct 15.2 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「陈国强的」×3
  - dialogue_chars_pct 7.1 低于目标 20.0
  - interiority_para_pct 28.0 高于目标 20.0
  - [observe] 标题与《显影机的异响》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13916
chapter_chars_mean: 2783
chapter_chars_median: 3460
chapter_chars_cv: 0.36
paragraphs_mean: 49.6
dialogue_chars_pct: 17.8
dialogue_para_pct: 48.1
interiority_para_pct: 17.8
narration_para_pct: 34.1
turn_under20_pct: 88.2
turn_over200_pct: 0.0
attr_say_pct: 34.4
attr_adv_pct: 9.0
scenes_per_chapter: 4.4
dialogue_run_mean: 2.8
turn_len_median: 10
```
