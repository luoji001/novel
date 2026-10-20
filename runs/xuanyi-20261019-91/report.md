# 铜锁 生成报告

slug：`xuanyi-20261019-91`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13978
LLM 调用：68 次，累计 230.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜锁与金属片 | 1700 | short | 92.8 | 0 |  | 1 |
| 2 | 摩挲账本封面 | 3169 | normal | 93.0 | 0 |  | 2 |
| 3 | 划痕藏玄机 | 4086 | normal | 91.3 | 0 |  | 2 |
| 4 | 摩挲怀表刻痕 | 3190 | normal | 90.5 | 0 |  | 2 |
| 5 | 摩挲登记簿边缘 | 1828 | short | 92.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 14 句（如「这里的每一道锁都应当有对应的钥匙。可现在，偏偏是…」）
- 第 2 章：
  - 单条套路句式超限：「周慕云的」×7、「沈佩兰的」×4、「微微一笑」×3
  - narration_para_pct 10.1 低于目标 20.0
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周慕云站在」×3、「周慕云点点」×3、「说道“我」×3
- 第 4 章：
  - 单条套路句式超限：「沈佩兰的」×7、「周慕云的」×6
  - narration_para_pct 5.9 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「周慕云站在」×3
  - 情节与已写章节重复 0.62 ≥ 0.62（撞上「周慕云在保险库发现死者手中握有第三道锁的钥匙，引发他对案…」）
  - narration_para_pct 12.5 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13295
chapter_chars_mean: 2659
chapter_chars_median: 3001
chapter_chars_cv: 0.37
paragraphs_mean: 57.2
dialogue_chars_pct: 38.9
dialogue_para_pct: 77.9
interiority_para_pct: 7.3
narration_para_pct: 14.8
turn_under20_pct: 72.6
turn_over200_pct: 0.0
attr_say_pct: 22.7
attr_adv_pct: 4.9
scenes_per_chapter: 2.2
dialogue_run_mean: 4.9
turn_len_median: 13
```
