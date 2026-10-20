# 绣线颜色 生成报告

slug：`xuanyi-20261019-238`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14196
LLM 调用：68 次，累计 234.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 掀开账本一角 | 1834 | short | 94.1 | 0 |  | 3 |
| 2 | 账本上的暗格 | 3994 | normal | 92.6 | 0 |  | 3 |
| 3 | 绣线上的陌生商标 | 2915 | normal | 88.0 | 0 |  | 2 |
| 4 | 掀开绣绷一角 | 3667 | normal | 89.6 | 0 |  | 3 |
| 5 | 掀开绣绷一角 | 1781 | short | 93.1 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈砚秋的」×4
  - interiority_para_pct 22.2 高于目标 20.0
  - narration_para_pct 11.1 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「沈砚秋的」×8、「顾云舟的」×4、「顾云舟点了点头」×3
  - narration_para_pct 11.1 低于目标 20.0
  - attr_adv_pct 17.9 高于目标 10.0
- 第 3 章：
  - narration_para_pct 15.9 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「他记得张师傅最后一次来坊时曾说过，最近市面上有些…」）
- 第 4 章：
  - 单条套路句式超限：「沈砚秋的」×3
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 标题与《掀开账本一角》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - dialogue_chars_pct 60.2 高于目标 58.0
  - narration_para_pct 0.0 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
  - [observe] 标题重复：「掀开绣绷一角」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13512
chapter_chars_mean: 2702
chapter_chars_median: 2810
chapter_chars_cv: 0.35
paragraphs_mean: 56.8
dialogue_chars_pct: 35.6
dialogue_para_pct: 71.8
interiority_para_pct: 11.8
narration_para_pct: 16.4
turn_under20_pct: 72.1
turn_over200_pct: 0.0
attr_say_pct: 15.3
attr_adv_pct: 10.5
scenes_per_chapter: 2.8
dialogue_run_mean: 5.1
turn_len_median: 14
```
