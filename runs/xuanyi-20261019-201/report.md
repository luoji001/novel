# 显影液 生成报告

slug：`xuanyi-20261019-201`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13314
LLM 调用：68 次，累计 214.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 显影液中的身影 | 1463 | short | 56.4 | 0 |  | 4 |
| 2 | 账本上的陌生名字 | 3715 | normal | 85.1 | 0 |  | 4 |
| 3 | 照片中的男人 | 3270 | normal | 91.0 | 0 |  | 3 |
| 4 | 钥匙的锈痕 | 3208 | normal | 90.7 | 0 |  | 1 |
| 5 | 显影液的异常配方 | 1653 | short | 95.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈国强的」×3
  - dialogue_chars_pct 4.4 低于目标 20.0
  - interiority_para_pct 28.6 高于目标 20.0
  - dialogue_run_mean 1 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「沈国强的」×5、「周婉秋的」×4、「他知道这」×4
  - dialogue_chars_pct 17.5 低于目标 20.0
  - interiority_para_pct 21.4 高于目标 20.0
  - [observe] 章内自我复读 19 句（如「然而，每当他快要接近真相的时候，总有一些东西让他…」）
- 第 3 章：
  - 单条套路句式超限：「周婉秋的」×9、「“我不知道」×3、「沈国强的」×3
  - narration_para_pct 12.2 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「你是不是知道些什么？…」）
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3
- 第 5 章：
  - narration_para_pct 11.6 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 12749
chapter_chars_mean: 2550
chapter_chars_median: 3083
chapter_chars_cv: 0.39
paragraphs_mean: 48.6
dialogue_chars_pct: 26.2
dialogue_para_pct: 59.2
interiority_para_pct: 17.3
narration_para_pct: 23.4
turn_under20_pct: 75.2
turn_over200_pct: 0.0
attr_say_pct: 21.8
attr_adv_pct: 3.5
scenes_per_chapter: 2.8
dialogue_run_mean: 3.5
turn_len_median: 12
```
