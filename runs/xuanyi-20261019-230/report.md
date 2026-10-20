# 铁盒 生成报告

slug：`xuanyi-20261019-230`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14744
LLM 调用：68 次，累计 229.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 充电器自燃记 | 2011 | short | 60.2 | 0 |  | 4 |
| 2 | 监控摄像头的视线 | 3246 | normal | 47.1 | 0 |  | 3 |
| 3 | 铁盒的锈迹 | 3685 | normal | 58.6 | 0 |  | 5 |
| 4 | 发票的背面暗语 | 3838 | normal | 89.1 | 0 |  | 3 |
| 5 | 手表与监控屏 | 1959 | short | 91.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 6.9 低于目标 20.0
  - interiority_para_pct 29.0 高于目标 20.0
  - dialogue_run_mean 1.2 低于目标 1.5
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「深吸一口气」×4、「他知道这」×4、「他知道自己」×3
  - dialogue_chars_pct 12.6 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「他想起那天夜里，在那家小卖部买水时，收银员说过的…」）
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「城南老街区」×3
  - dialogue_chars_pct 14.2 低于目标 20.0
  - dialogue_run_mean 1.3 低于目标 1.5
  - [observe] 章内自我复读 15 句（如「随着最后一张照片被完全展现在他面前，一种奇怪的感…」）
- 第 4 章：
  - 单条套路句式超限：「为什么会」×5、「“我不知道」×4、「城南老街区」×3
  - narration_para_pct 19.7 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「他深吸了一口气，努力让自己冷静下来…」）
- 第 5 章：
  - dialogue_chars_pct 19.9 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「李志的心跳加快了几分…」）

## 整书结构指标

```
chapters: 5
total_chars: 14107
chapter_chars_mean: 2821
chapter_chars_median: 3092
chapter_chars_cv: 0.31
paragraphs_mean: 56
dialogue_chars_pct: 15.6
dialogue_para_pct: 47.1
interiority_para_pct: 19.1
narration_para_pct: 33.8
turn_under20_pct: 90.1
turn_over200_pct: 0.0
attr_say_pct: 18.7
attr_adv_pct: 6.2
scenes_per_chapter: 2.6
dialogue_run_mean: 1.8
turn_len_median: 10
```
