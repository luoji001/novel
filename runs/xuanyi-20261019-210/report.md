# 空档 生成报告

slug：`xuanyi-20261019-210`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15889
LLM 调用：68 次，累计 235.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 查看GPS记录 | 1790 | short | 97.2 | 0 |  | 2 |
| 2 | 核对手机截图 | 4331 | normal | 84.9 | 0 |  | 2 |
| 3 | 查看支付凭证 | 3625 | normal | 88.9 | 0 |  | 3 |
| 4 | 查看车载导航 | 4023 | normal | 83.5 | 0 |  | 4 |
| 5 | 翻看燃油费单据 | 2115 | short | 77.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周晓芸的」×3
  - attr_adv_pct 20.0 高于目标 10.0
- 第 2 章：
  - dialogue_chars_pct 17.1 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「车子正在驶入城北新区的路上，这里比城南更安静一些…」）
- 第 3 章：
  - 单条套路句式超限：「深吸一口气」×3
  - narration_para_pct 12.9 低于目标 20.0
  - [observe] 章内自我复读 15 句（如「李明停顿了几秒，深吸一口气，压低音量说道，“但我…」）
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「为什么会」×3
  - dialogue_chars_pct 15.8 低于目标 20.0
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）
- 第 5 章：
  - dialogue_chars_pct 15.2 低于目标 20.0
  - interiority_para_pct 25.8 高于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 15275
chapter_chars_mean: 3055
chapter_chars_median: 3488
chapter_chars_cv: 0.36
paragraphs_mean: 53.8
dialogue_chars_pct: 22.5
dialogue_para_pct: 55.8
interiority_para_pct: 15.5
narration_para_pct: 28.7
turn_under20_pct: 70.9
turn_over200_pct: 0.0
attr_say_pct: 15.1
attr_adv_pct: 16.2
scenes_per_chapter: 3.6
dialogue_run_mean: 3.1
turn_len_median: 11
```
