# 铜铃 生成报告

slug：`xuanyi-20261019-53`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14122
LLM 调用：68 次，累计 233.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕裂的账页一角 | 1493 | short | 90.8 | 0 |  | 2 |
| 2 | 铜铃应声 | 3756 | normal | 87.9 | 0 |  | 3 |
| 3 | 铜钥匙的低语 | 3761 | normal | 89.3 | 0 |  | 3 |
| 4 | 铜铃应声 | 3446 | normal | 90.0 | 0 |  | 4 |
| 5 | 纸条上的符号 | 1661 | short | 92.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 18.7 低于目标 20.0
  - interiority_para_pct 21.7 高于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周怀瑾的」×4、「他知道这」×4
  - dialogue_chars_pct 19.1 低于目标 20.0
  - interiority_para_pct 22.6 高于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「沈文渊的」×9、「他知道自己」×4、「“你是谁」×3
  - narration_para_pct 15.6 低于目标 20.0
  - attr_adv_pct 16.0 高于目标 10.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈文渊的」×5、「他知道这」×4
  - attr_adv_pct 10.5 高于目标 10.0
  - [observe] 标题重复：「铜铃应声」已存在
- 第 5 章：
  - 单条套路句式超限：「绍兴当铺」×11、「周怀瑾的」×3
  - narration_para_pct 8.1 低于目标 20.0
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 13508
chapter_chars_mean: 2702
chapter_chars_median: 3290
chapter_chars_cv: 0.41
paragraphs_mean: 54.2
dialogue_chars_pct: 24.5
dialogue_para_pct: 60.7
interiority_para_pct: 17.8
narration_para_pct: 21.5
turn_under20_pct: 79.5
turn_over200_pct: 0.0
attr_say_pct: 22.1
attr_adv_pct: 10.7
scenes_per_chapter: 3.2
dialogue_run_mean: 3.9
turn_len_median: 12
```
