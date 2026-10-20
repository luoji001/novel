# 铜钥匙 生成报告

slug：`xuanyi-20261019-219`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14050
LLM 调用：68 次，累计 243.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲汇款单 | 1420 | short | 92.3 | 0 |  | 2 |
| 2 | 摩挲汇款单 | 3792 | normal | 91.1 | 0 |  | 3 |
| 3 | 摩挲账本边缘 | 3816 | normal | 86.6 | 0 |  | 4 |
| 4 | 摩挲算盘木壳 | 3352 | normal | 90.8 | 0 |  | 3 |
| 5 | 摩挲信纸折痕 | 1665 | short | 92.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「信用社」×5、「他知道这」×3
  - dialogue_chars_pct 16.6 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林秋实的」×6、「信用社」×3
  - narration_para_pct 11.8 低于目标 20.0
  - [observe] 标题重复：「摩挲汇款单」已存在
- 第 3 章：
  - 单条套路句式超限：「陈大勇的」×7、「带着一丝」×4、「林秋实的」×4
  - narration_para_pct 13.4 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 章内自我复读 18 句（如「这本账本似乎比记忆中还要古老一些，纸页泛黄得仿佛…」）
- 第 4 章：
  - 单条套路句式超限：「陈大勇的」×7、「林秋实的」×6、「“我不知道」×3
  - narration_para_pct 13.0 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「信用社」×5
  - narration_para_pct 16.7 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13429
chapter_chars_mean: 2686
chapter_chars_median: 3184
chapter_chars_cv: 0.42
paragraphs_mean: 54.6
dialogue_chars_pct: 37.9
dialogue_para_pct: 74.6
interiority_para_pct: 10.4
narration_para_pct: 15.0
turn_under20_pct: 77.1
turn_over200_pct: 0.0
attr_say_pct: 22.2
attr_adv_pct: 8.5
scenes_per_chapter: 3
dialogue_run_mean: 4.7
turn_len_median: 12
```
