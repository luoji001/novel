# 显影液的温度 生成报告

slug：`xuanyi-20261019-41`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13782
LLM 调用：68 次，累计 224.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 显影液中的双影 | 1557 | short | 77.8 | 0 |  | 2 |
| 2 | 账本的裂痕 | 3751 | normal | 93.5 | 0 |  | 2 |
| 3 | 铜钥匙与旧账本 | 3008 | normal | 92.5 | 0 |  | 2 |
| 4 | 胶卷与账本的相遇 | 3370 | normal | 89.6 | 0 |  | 3 |
| 5 | 显影中的双身影像 | 2091 | short | 92.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 8.9 低于目标 20.0
  - dialogue_run_mean 1.3 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「林婉如的」×5、「沈秋实的」×5、「”林婉如轻」×3
  - narration_para_pct 9.5 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「林婉如的」×3、「沈秋实的」×3
  - narration_para_pct 12.7 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「沈秋实的」×5、「”林婉如轻」×4、「林婉如的」×4
  - narration_para_pct 10.3 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「林婉如的」×4
  - narration_para_pct 8.9 低于目标 20.0
  - [observe] 标题与《显影液中的双影》近似 0.80 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13138
chapter_chars_mean: 2628
chapter_chars_median: 2867
chapter_chars_cv: 0.33
paragraphs_mean: 56.4
dialogue_chars_pct: 39.8
dialogue_para_pct: 76.1
interiority_para_pct: 10.0
narration_para_pct: 13.9
turn_under20_pct: 75.4
turn_over200_pct: 0.0
attr_say_pct: 24.8
attr_adv_pct: 7.7
scenes_per_chapter: 2.8
dialogue_run_mean: 4.8
turn_len_median: 11
```
