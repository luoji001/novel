# 绣花针 生成报告

slug：`xuanyi-20261019-138`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13869
LLM 调用：68 次，累计 238.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 绣线藏匿于麻绳中 | 1847 | short | 99.6 | 0 |  | 0 |
| 2 | 解锁雕花木箱 | 3193 | normal | 93.7 | 0 |  | 3 |
| 3 | 擦拭账本的褐色污渍 | 3775 | normal | 91.4 | 0 |  | 2 |
| 4 | 摩挲绣品的指尖 | 3112 | normal | 93.1 | 0 |  | 3 |
| 5 | 绣品边缘的深蓝色块 | 1937 | short | 93.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「沈文渊的」×9、「陆青梧点」×3
  - narration_para_pct 14.3 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「陆青梧点」×3、「沈文渊的」×3
  - narration_para_pct 15.1 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「陆青梧点」×3
  - narration_para_pct 15.2 低于目标 20.0
  - attr_adv_pct 16.0 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「”陆青梧低」×3、「沈文渊的」×3
  - narration_para_pct 7.1 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13181
chapter_chars_mean: 2636
chapter_chars_median: 2965
chapter_chars_cv: 0.31
paragraphs_mean: 60.4
dialogue_chars_pct: 45.8
dialogue_para_pct: 79.7
interiority_para_pct: 5.7
narration_para_pct: 14.6
turn_under20_pct: 71.2
turn_over200_pct: 0.0
attr_say_pct: 21.4
attr_adv_pct: 8.4
scenes_per_chapter: 1.6
dialogue_run_mean: 5.4
turn_len_median: 14
```
