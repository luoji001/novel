# 铜钥 生成报告

slug：`xuanyi-20261019-13`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：12933
LLM 调用：68 次，累计 225.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钥匙与老地图 | 1591 | short | 96.8 | 0 |  | 3 |
| 2 | 钥匙触碰凹槽 | 3286 | normal | 91.3 | 0 |  | 3 |
| 3 | 玉镯与账本对望 | 3495 | normal | 90.3 | 0 |  | 3 |
| 4 | 算盘与账本对话 | 3173 | normal | 88.6 | 0 |  | 4 |
| 5 | 钥匙触碰凹槽 | 1383 | short | 91.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周文渊的」×3
  - narration_para_pct 5.3 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「沈怀瑾的」×5
  - narration_para_pct 10.9 低于目标 20.0
  - attr_adv_pct 17.6 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「周文渊的」×5、「周文渊点」×4、「沈怀瑾的」×3
  - narration_para_pct 14.1 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「沈怀瑾没有立刻回答，而是转头看向墙上的那幅地图，…」）
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周文渊的」×4、「他知道这」×4、「沈怀瑾的」×4
  - narration_para_pct 15.9 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「他知道自己的时间不多了，而且他也越来越清楚一件事…」）
- 第 5 章：
  - narration_para_pct 11.5 低于目标 20.0
  - [observe] 标题重复：「钥匙触碰凹槽」已存在

## 整书结构指标

```
chapters: 5
total_chars: 12350
chapter_chars_mean: 2470
chapter_chars_median: 3032
chapter_chars_cv: 0.4
paragraphs_mean: 50.6
dialogue_chars_pct: 37.0
dialogue_para_pct: 77.2
interiority_para_pct: 10.4
narration_para_pct: 12.4
turn_under20_pct: 66.9
turn_over200_pct: 0.0
attr_say_pct: 14.1
attr_adv_pct: 10.0
scenes_per_chapter: 2
dialogue_run_mean: 4.3
turn_len_median: 15
```
