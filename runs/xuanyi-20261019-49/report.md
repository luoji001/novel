# 算珠失衡 生成报告

slug：`xuanyi-20261019-49`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13602
LLM 调用：68 次，累计 221.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 拨动算珠的人 | 1772 | short | 97.0 | 0 |  | 1 |
| 2 | 登记簿的新页 | 3415 | normal | 93.0 | 0 |  | 3 |
| 3 | 指纹覆盖的药瓶标签 | 3291 | normal | 91.4 | 0 |  | 2 |
| 4 | 解开布包的瞬间 | 3497 | normal | 89.8 | 0 |  | 3 |
| 5 | 解开布包的瞬间 | 1622 | short | 91.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 13.3 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周玉兰的」×4、「沈秋实的」×3
  - narration_para_pct 15.5 低于目标 20.0
  - [observe] attr_adv_pct 29.4 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「周玉兰的」×9、「沈秋实的」×6
  - narration_para_pct 14.1 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周玉兰的」×4、「”周玉兰轻」×3、「沈秋实的」×3
  - narration_para_pct 7.5 低于目标 20.0
  - attr_adv_pct 13.3 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「周玉兰的」×3、「沈秋实的」×3
  - narration_para_pct 10.7 低于目标 20.0
  - [observe] 标题重复：「解开布包的瞬间」已存在

## 整书结构指标

```
chapters: 5
total_chars: 12991
chapter_chars_mean: 2598
chapter_chars_median: 3132
chapter_chars_cv: 0.34
paragraphs_mean: 53.4
dialogue_chars_pct: 36.4
dialogue_para_pct: 76.5
interiority_para_pct: 11.3
narration_para_pct: 12.2
turn_under20_pct: 77.9
turn_over200_pct: 0.0
attr_say_pct: 30.5
attr_adv_pct: 12.2
scenes_per_chapter: 2.8
dialogue_run_mean: 4.9
turn_len_median: 12
```
