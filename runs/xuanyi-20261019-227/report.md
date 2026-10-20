# 铜匣 生成报告

slug：`xuanyi-20261019-227`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13906
LLM 调用：68 次，累计 235.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 砚台铭文之谜 | 1611 | short | 100.0 | 0 |  | 2 |
| 2 | 砚台上的铭文异变 | 3672 | normal | 87.9 | 0 |  | 3 |
| 3 | 钥匙开启的刹那 | 3437 | normal | 87.8 | 0 |  | 3 |
| 4 | 玉牌与砚台对话 | 3510 | normal | 87.7 | 0 |  | 2 |
| 5 | 砚台上的旧信笺 | 1671 | short | 90.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈子安的」×4
  - narration_para_pct 5.0 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「点了点头“」×3、「沈子安点点」×3
  - narration_para_pct 5.6 低于目标 20.0
  - dialogue_run_mean 11.7 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「沈子安的」×5
  - narration_para_pct 15.8 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「沈子安的笑容更深了些…」）
- 第 4 章：
  - 单条套路句式超限：「陆怀远的」×7、「点了点头」×5
  - narration_para_pct 16.0 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「他知道这」×4
  - narration_para_pct 11.8 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13202
chapter_chars_mean: 2640
chapter_chars_median: 3290
chapter_chars_cv: 0.38
paragraphs_mean: 60.2
dialogue_chars_pct: 43.6
dialogue_para_pct: 80.1
interiority_para_pct: 8.4
narration_para_pct: 11.4
turn_under20_pct: 69.7
turn_over200_pct: 0.0
attr_say_pct: 23.0
attr_adv_pct: 3.4
scenes_per_chapter: 2
dialogue_run_mean: 6.8
turn_len_median: 13
```
