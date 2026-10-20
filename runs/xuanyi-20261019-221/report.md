# 显影液滴落 生成报告

slug：`xuanyi-20261019-221`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15189
LLM 调用：68 次，累计 235.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 显影液中的旧身影 | 1352 | short | 92.4 | 0 |  | 1 |
| 2 | 登记簿里的死亡日期 | 4297 | normal | 92.2 | 0 |  | 3 |
| 3 | 显影液中的旧身影 | 3521 | normal | 88.4 | 0 |  | 3 |
| 4 | 表格右下角的日期 | 4147 | normal | 87.7 | 0 |  | 3 |
| 5 | 照片后的裂痕 | 1867 | short | 90.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 18.0 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周婉秋的」×7、「沈国强的」×7、「带着一丝」×3
  - narration_para_pct 11.2 低于目标 20.0
  - [observe] attr_adv_pct 27.3 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「周婉秋的」×4、「沈国强的」×4
  - dialogue_chars_pct 18.9 低于目标 20.0
  - [observe] 标题重复：「显影液中的旧身影」已存在
- 第 4 章：
  - 单条套路句式超限：「沈国强的」×8、「沈国强站在」×4、「点了点头」×3
  - narration_para_pct 10.2 低于目标 20.0
  - [observe] 章内自我复读 19 句（如「他想起那天在暗房里看到的照片，照片上的人正是李素…」）
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周婉秋的」×4
  - attr_adv_pct 14.3 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 14475
chapter_chars_mean: 2895
chapter_chars_median: 3377
chapter_chars_cv: 0.44
paragraphs_mean: 63
dialogue_chars_pct: 34.3
dialogue_para_pct: 72.5
interiority_para_pct: 9.6
narration_para_pct: 17.8
turn_under20_pct: 79.6
turn_over200_pct: 0.0
attr_say_pct: 32.2
attr_adv_pct: 12.2
scenes_per_chapter: 3
dialogue_run_mean: 4.0
turn_len_median: 11
```
