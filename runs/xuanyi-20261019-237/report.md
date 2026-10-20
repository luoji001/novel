# 重叠的红光 生成报告

slug：`xuanyi-20261019-237`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15247
LLM 调用：68 次，累计 230.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扫描仪的双影 | 1856 | short | 97.2 | 0 |  | 2 |
| 2 | 工牌的特殊标记 | 4165 | normal | 92.2 | 0 |  | 3 |
| 3 | 工牌的阴影倾斜 | 3873 | normal | 90.1 | 0 |  | 5 |
| 4 | 工牌的阴影倾斜 | 3731 | normal | 89.0 | 0 |  | 3 |
| 5 | 包裹的微妙触碰 | 1617 | short | 92.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈思远的」×6
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「林婉如的」×4
  - narration_para_pct 12.6 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「但我在他的身上看到了一些熟悉的迹象，就好像……他…」）
- 第 3 章：
  - 单条套路句式超限：「为什么会」×4、「南方速递集团」×4、「陈思远的」×3
  - dialogue_chars_pct 60.1 高于目标 58.0
  - narration_para_pct 5.5 低于目标 20.0
  - attr_adv_pct 17.9 高于目标 10.0
  - dialogue_run_mean 11.9 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「林婉如的」×7、「他知道自己」×3
  - narration_para_pct 13.3 低于目标 20.0
  - [observe] 标题重复：「工牌的阴影倾斜」已存在
- 第 5 章：
  - narration_para_pct 8.3 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14477
chapter_chars_mean: 2895
chapter_chars_median: 3520
chapter_chars_cv: 0.4
paragraphs_mean: 69.2
dialogue_chars_pct: 49.6
dialogue_para_pct: 81.8
interiority_para_pct: 5.7
narration_para_pct: 12.6
turn_under20_pct: 74.9
turn_over200_pct: 0.0
attr_say_pct: 42.3
attr_adv_pct: 9.2
scenes_per_chapter: 2.8
dialogue_run_mean: 6.2
turn_len_median: 12
```
