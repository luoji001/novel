# 铜印 生成报告

slug：`xuanyi-20261019-267`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13592
LLM 调用：68 次，累计 233.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 砚台上的铭文疑云 | 1664 | short | 93.3 | 0 |  | 2 |
| 2 | 砚台上的归期未定 | 3618 | normal | 88.6 | 0 |  | 3 |
| 3 | 铜印与地图对峙 | 3121 | normal | 88.4 | 0 |  | 5 |
| 4 | 画轴上的裂痕之谜 | 3446 | normal | 90.9 | 0 |  | 3 |
| 5 | 砚台上的归期未定 | 1738 | short | 89.7 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 0.0 低于目标 20.0
  - dialogue_run_mean 34 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「他知道这」×5、「点了点头」×4
  - narration_para_pct 14.1 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「沈文渊抬起头看着李怀远，“但我记得你父亲曾经提起…」）
- 第 3 章：
  - 单条套路句式超限：「周慕云点」×4、「为什么会」×3
  - dialogue_chars_pct 58.1 高于目标 58.0
  - narration_para_pct 3.9 低于目标 20.0
  - attr_adv_pct 18.6 高于目标 10.0
  - dialogue_run_mean 11.7 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3
  - narration_para_pct 5.3 低于目标 20.0
  - attr_adv_pct 12.0 高于目标 10.0
- 第 5 章：
  - narration_para_pct 11.4 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「李怀远的心跳加快了几分…」）
  - [observe] attr_adv_pct 50.0 > 20.0（结构塌缩）
  - [observe] 标题重复：「砚台上的归期未定」已存在

## 整书结构指标

```
chapters: 5
total_chars: 12888
chapter_chars_mean: 2578
chapter_chars_median: 2954
chapter_chars_cv: 0.35
paragraphs_mean: 59.6
dialogue_chars_pct: 50.0
dialogue_para_pct: 85.7
interiority_para_pct: 6.7
narration_para_pct: 7.4
turn_under20_pct: 69.5
turn_over200_pct: 0.0
attr_say_pct: 19.0
attr_adv_pct: 15.6
scenes_per_chapter: 2.4
dialogue_run_mean: 11.7
turn_len_median: 14
```
