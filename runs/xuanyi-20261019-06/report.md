# 钥匙牌 生成报告

slug：`xuanyi-20261019-06`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14770
LLM 调用：68 次，累计 243.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙牌的错位 | 1431 | short | 98.4 | 0 |  | 1 |
| 2 | 火车票的揭示 | 3713 | normal | 92.2 | 0 |  | 3 |
| 3 | 钥匙牌与房号牌的对峙 | 4172 | normal | 87.9 | 0 |  | 3 |
| 4 | 铁盒里的记事本 | 3560 | normal | 91.3 | 0 |  | 2 |
| 5 | 摩挲木钉 | 1889 | short | 93.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈国栋站在」×3
- 第 2 章：
  - 单条套路句式超限：「林秀兰的」×6、「陈国栋的」×6、「陈国栋站在」×4
  - narration_para_pct 6.4 低于目标 20.0
  - [observe] 章内自我复读 10 句（如「陈国栋压低声音说道，“他好像一直在找什么人…」）
- 第 3 章：
  - 单条套路句式超限：「陈国栋站在」×3、「“我不知道」×3、「陈国栋的」×3
  - narration_para_pct 16.1 低于目标 20.0
  - [observe] 章内自我复读 20 句（如「你知道我们这里的一切都是按规矩来的吗？如果你再胡…」）
- 第 4 章：
  - 单条套路句式超限：「陈国栋的」×6
  - narration_para_pct 19.4 低于目标 20.0
- 第 5 章：
  - narration_para_pct 14.3 低于目标 20.0
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 14079
chapter_chars_mean: 2816
chapter_chars_median: 3402
chapter_chars_cv: 0.41
paragraphs_mean: 57.6
dialogue_chars_pct: 41.2
dialogue_para_pct: 76.8
interiority_para_pct: 8.2
narration_para_pct: 15.0
turn_under20_pct: 72.5
turn_over200_pct: 0.0
attr_say_pct: 25.3
attr_adv_pct: 7.1
scenes_per_chapter: 2.2
dialogue_run_mean: 5.3
turn_len_median: 13
```
