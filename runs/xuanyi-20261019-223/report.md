# 行李箱 生成报告

slug：`xuanyi-20261019-223`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14122
LLM 调用：68 次，累计 224.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 身份证被触碰 | 1737 | short | 99.8 | 0 |  | 1 |
| 2 | 指纹触碰身份证 | 3835 | normal | 89.8 | 0 |  | 4 |
| 3 | 汇款单被撕碎 | 3369 | normal | 91.7 | 0 |  | 3 |
| 4 | 钥匙藏身枕头底 | 3433 | normal | 91.4 | 0 |  | 2 |
| 5 | 指纹触碰火车票 | 1743 | short | 91.0 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 16.7 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「为什么会」×4、「“我不知道」×3、「林志远的」×3
  - narration_para_pct 2.5 低于目标 20.0
  - dialogue_run_mean 14.8 高于目标 10.0
  - [observe] attr_adv_pct 25.9 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「”苏婉清轻」×4
  - narration_para_pct 7.4 低于目标 20.0
  - [observe] attr_adv_pct 20.8 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「苏婉清的」×4、「不仅仅是」×3、「林志远的」×3
  - narration_para_pct 13.3 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13419
chapter_chars_mean: 2684
chapter_chars_median: 3219
chapter_chars_cv: 0.36
paragraphs_mean: 62.4
dialogue_chars_pct: 40.7
dialogue_para_pct: 81.3
interiority_para_pct: 6.7
narration_para_pct: 12.0
turn_under20_pct: 80.6
turn_over200_pct: 0.0
attr_say_pct: 38.4
attr_adv_pct: 15.6
scenes_per_chapter: 3
dialogue_run_mean: 6.5
turn_len_median: 11
```
