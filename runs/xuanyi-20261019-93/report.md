# 铜锁 生成报告

slug：`xuanyi-20261019-93`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13044
LLM 调用：64 次，累计 214.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本最后一页的空白 | 1693 | short | 97.8 | 0 |  | 1 |
| 2 | 钥匙开启的秘密 | 3573 | normal | 44.2 | 0 |  | 3 |
| 3 | 怀表背面的刻痕 | 3548 | normal | 88.2 | 0 |  | 2 |
| 4 | 银镯子上的刻痕 | 3210 | normal | 92.7 | 0 |  | 3 |
| 5 | 账本缺口的疑问 | 1015 | short | 91.3 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 17.2 低于目标 20.0
- 第 2 章：
  - dialogue_chars_pct 15.3 低于目标 20.0
  - interiority_para_pct 26.7 高于目标 20.0
  - [observe] 章内自我复读 24 句（如「屋外的脚步声越来越近，伴随着夜风灌进来的寒气，他…」）
- 第 3 章：
  - 单条套路句式超限：「沈文远的」×7、「周慕云的」×5、「为什么会」×3
  - [observe] 章内自我复读 19 句（如「他想起之前在暗格里找到的那张泛黄纸条，纸上也写着…」）
- 第 4 章：
  - 单条套路句式超限：「沈文远的」×6
  - narration_para_pct 9.1 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「周慕云的」×3
  - narration_para_pct 13.6 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
  - [observe] 章节过短 956 < 1068（本章目标 1942 字的 55%）

## 整书结构指标

```
chapters: 5
total_chars: 12454
chapter_chars_mean: 2491
chapter_chars_median: 3063
chapter_chars_cv: 0.45
paragraphs_mean: 52.4
dialogue_chars_pct: 25.7
dialogue_para_pct: 62.2
interiority_para_pct: 16.6
narration_para_pct: 21.2
turn_under20_pct: 80.0
turn_over200_pct: 0.0
attr_say_pct: 10.4
attr_adv_pct: 5.1
scenes_per_chapter: 3.2
dialogue_run_mean: 3.3
turn_len_median: 13
```
