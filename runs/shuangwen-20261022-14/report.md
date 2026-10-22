# 账页风波 生成报告

slug：`shuangwen-20261022-14`
档位：爽文　闸门模式：observe
章数：10　总字数：18208
LLM 调用：97 次，累计 376.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜灯照族谱 | 1659 | normal | 39.8 | 0 |  | 1 |
| 2 | 墨迹拂案 | 1947 | normal | 93.6 | 0 |  | 2 |
| 3 | 拂墨辨真伪 | 1672 | normal | 94.0 | 0 |  | 1 |
| 4 | 残页展真相 | 1693 | normal | 92.5 | 0 |  | 0 |
| 5 | 账册掀开一角 | 1442 | normal | 91.4 | 0 |  | 3 |
| 6 | 拂墨辨真伪 | 1892 | normal | 91.9 | 0 |  | 3 |
| 7 | 拂墨辨真伪 | 1667 | normal | 90.7 | 0 |  | 4 |
| 8 | 拂墨辨真伪 | 2116 | normal | 91.0 | 0 |  | 2 |
| 9 | 拂墨辨真伪 | 1801 | normal | 37.5 | 0 |  | 3 |
| 10 | 拂墨辨真伪 | 2309 | long | 36.3 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「周守仁的」×7
  - attr_adv_pct 16.7 高于目标 12.0
- 第 3 章：
  - attr_adv_pct 12.5 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「周守仁的」×5
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「周守仁的」×6
  - attr_adv_pct 21.4 高于目标 12.0
  - [observe] 标题重复：「拂墨辨真伪」已存在
- 第 7 章：
  - 单条套路句式超限：「周守仁的」×6
  - 情节与已写章节重复 0.71 ≥ 0.7（撞上「周文清发现族谱与账册记载不符，质疑家族历史的真实性，引发…」）
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「拂墨辨真伪」已存在
- 第 8 章：
  - 单条套路句式超限：「周守仁的」×4
  - [observe] 标题重复：「拂墨辨真伪」已存在
- 第 9 章：
  - 情节与已写章节重复 0.80 ≥ 0.7（撞上「周怀远出示父亲留下的账本残页，揭露族谱中被抹去的名字，引…」）
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
  - [observe] 标题重复：「拂墨辨真伪」已存在
- 第 10 章：
  - 单条套路句式超限：「周守仁的」×6
  - narration_para_pct 2.6 低于目标 5.0
  - dialogue_run_mean 19 高于目标 14.0
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「拂墨辨真伪」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17294
chapter_chars_mean: 1729
chapter_chars_median: 1642
chapter_chars_cv: 0.14
paragraphs_mean: 38.7
dialogue_chars_pct: 48.5
dialogue_para_pct: 86.0
interiority_para_pct: 4.5
narration_para_pct: 9.6
turn_under20_pct: 72.2
turn_over200_pct: 0.0
attr_say_pct: 17.2
attr_adv_pct: 18.6
scenes_per_chapter: 1.7
dialogue_run_mean: 8.3
turn_len_median: 12
```
