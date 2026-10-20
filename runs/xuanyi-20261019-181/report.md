# 显影液的倒影 生成报告

slug：`xuanyi-20261019-181`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13631
LLM 调用：68 次，累计 226.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 显影盘的涟漪 | 1846 | short | 68.7 | 0 |  | 3 |
| 2 | 照片上的蓝裙子 | 3339 | normal | 91.2 | 0 |  | 3 |
| 3 | 触摸账本的指尖 | 3449 | normal | 87.9 | 0 |  | 3 |
| 4 | 抚摸结婚照的指尖 | 3269 | normal | 88.8 | 0 |  | 2 |
| 5 | 搅动显影液的指尖 | 1723 | short | 90.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 8.6 低于目标 20.0
  - interiority_para_pct 24.0 高于目标 20.0
  - dialogue_run_mean 1.2 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「苏婉秋的」×6、「“我不知道」×3、「”苏婉秋轻」×3
  - narration_para_pct 7.0 低于目标 20.0
  - attr_adv_pct 17.6 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「苏婉秋的」×6、「不仅仅是」×3、「林永年的」×3
  - interiority_para_pct 21.7 高于目标 20.0
  - attr_adv_pct 18.2 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「苏婉秋点」×4、「苏婉秋的」×4
  - narration_para_pct 12.1 低于目标 20.0
- 第 5 章：
  - narration_para_pct 16.7 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13046
chapter_chars_mean: 2609
chapter_chars_median: 3121
chapter_chars_cv: 0.31
paragraphs_mean: 50.4
dialogue_chars_pct: 30.3
dialogue_para_pct: 67.4
interiority_para_pct: 15.1
narration_para_pct: 17.5
turn_under20_pct: 79.7
turn_over200_pct: 0.0
attr_say_pct: 29.7
attr_adv_pct: 8.9
scenes_per_chapter: 3.2
dialogue_run_mean: 4.0
turn_len_median: 11
```
