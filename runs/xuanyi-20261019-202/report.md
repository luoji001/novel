# 当票 生成报告

slug：`xuanyi-20261019-202`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14033
LLM 调用：68 次，累计 233.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 玉扳指上的裂痕 | 2289 | short | 95.3 | 0 |  | 2 |
| 2 | 怀表停在三点 | 3218 | normal | 92.3 | 0 |  | 2 |
| 3 | 铜锁上的雕花纹样 | 3132 | normal | 93.2 | 0 |  | 2 |
| 4 | 当票与怀表相遇 | 3617 | normal | 89.7 | 0 |  | 2 |
| 5 | 烛光下的铜锁秘密 | 1772 | short | 92.2 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 18.9 低于目标 20.0
  - attr_adv_pct 18.2 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「陆文渊的」×4、「他知道这」×3
  - attr_adv_pct 15.4 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「沈砚秋的」×5
  - narration_para_pct 7.2 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「沈砚秋点点」×3
  - narration_para_pct 14.8 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13375
chapter_chars_mean: 2675
chapter_chars_median: 2978
chapter_chars_cv: 0.27
paragraphs_mean: 57.8
dialogue_chars_pct: 37.8
dialogue_para_pct: 71.4
interiority_para_pct: 7.9
narration_para_pct: 20.7
turn_under20_pct: 66.7
turn_over200_pct: 0.0
attr_say_pct: 14.0
attr_adv_pct: 8.6
scenes_per_chapter: 2.8
dialogue_run_mean: 4.4
turn_len_median: 13
```
