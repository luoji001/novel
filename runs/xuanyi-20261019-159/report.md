# 铜印 生成报告

slug：`xuanyi-20261019-159`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13210
LLM 调用：68 次，累计 225.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲汇款单边缘 | 1466 | short | 83.8 | 0 |  | 2 |
| 2 | 铜印映照旧报纸 | 3358 | normal | 86.2 | 0 |  | 4 |
| 3 | 摩挲汇款单边缘 | 3538 | normal | 89.8 | 0 |  | 4 |
| 4 | 摩挲信纸边缘 | 3137 | normal | 91.6 | 0 |  | 4 |
| 5 | 抚摸木牌边缘 | 1706 | short | 92.6 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 29.6 高于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「林秀兰的」×4
  - dialogue_chars_pct 18.5 低于目标 20.0
  - interiority_para_pct 23.3 高于目标 20.0
  - narration_para_pct 18.6 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「林秀兰的」×7、「陈海山的」×5
  - narration_para_pct 10.7 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「1982年3月15日…」）
  - [observe] 标题重复：「摩挲汇款单边缘」已存在
- 第 4 章：
  - 单条套路句式超限：「林秀兰的」×10、「陈海山的」×4
  - narration_para_pct 13.3 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「你说得没错，我不该回来…」）
  - [observe] 标题与《摩挲汇款单边缘》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「林秀兰的」×5
  - narration_para_pct 11.8 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「1982年3月15日…」）
  - [observe] 与历史章节逐字重复 3 句（如「我发现了些奇怪的东西…」）

## 整书结构指标

```
chapters: 5
total_chars: 12654
chapter_chars_mean: 2531
chapter_chars_median: 3003
chapter_chars_cv: 0.37
paragraphs_mean: 47.8
dialogue_chars_pct: 31.4
dialogue_para_pct: 70.8
interiority_para_pct: 14.4
narration_para_pct: 14.8
turn_under20_pct: 79.3
turn_over200_pct: 0.0
attr_say_pct: 23.4
attr_adv_pct: 4.3
scenes_per_chapter: 3.2
dialogue_run_mean: 3.8
turn_len_median: 12
```
