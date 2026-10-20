# 红光 生成报告

slug：`xuanyi-20261019-197`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14829
LLM 调用：68 次，累计 234.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扫描仪的双倍记录 | 1914 | short | 99.2 | 0 |  | 2 |
| 2 | 扫描仪的计时器 | 3417 | normal | 91.8 | 0 |  | 2 |
| 3 | 扫描仪的双倍记录 | 3657 | normal | 90.1 | 0 |  | 3 |
| 4 | 扫描仪的异常脉冲 | 3772 | normal | 90.3 | 0 |  | 2 |
| 5 | 撕开的包裹封口 | 2064 | short | 88.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈雨桐的」×4
  - narration_para_pct 12.9 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周启明的」×5、「沈雨桐点」×3、「不仅仅是」×3
  - narration_para_pct 13.2 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「沈雨桐的」×5、「说道“我」×3、「周启明的」×3
  - narration_para_pct 18.7 低于目标 20.0
  - [observe] 标题重复：「扫描仪的双倍记录」已存在
- 第 4 章：
  - 单条套路句式超限：「沈雨桐点」×3、「沈雨桐的」×3、「周启明的」×3
  - narration_para_pct 15.8 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「“这是什么」×3、「周启明点点」×3、「这是什么？」×3
  - narration_para_pct 5.9 低于目标 20.0
  - [observe] 章内自我复读 20 句（如「我早上检查过扫描仪的时间参数，发现有些微差异。如…」）

## 整书结构指标

```
chapters: 5
total_chars: 14176
chapter_chars_mean: 2835
chapter_chars_median: 3296
chapter_chars_cv: 0.3
paragraphs_mean: 57
dialogue_chars_pct: 42.0
dialogue_para_pct: 80.0
interiority_para_pct: 5.9
narration_para_pct: 14.1
turn_under20_pct: 69.5
turn_over200_pct: 0.0
attr_say_pct: 27.7
attr_adv_pct: 3.0
scenes_per_chapter: 3.4
dialogue_run_mean: 6.5
turn_len_median: 14
```
