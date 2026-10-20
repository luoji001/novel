# 火车票 生成报告

slug：`xuanyi-20261019-83`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14720
LLM 调用：68 次，累计 232.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 箱子的秘密 | 1948 | short | 97.9 | 0 |  | 1 |
| 2 | 纸条的遗失 | 3758 | normal | 91.1 | 0 |  | 2 |
| 3 | 钥匙的低语 | 3801 | normal | 85.8 | 0 |  | 3 |
| 4 | 火车票的褶痕 | 3181 | normal | 89.9 | 0 |  | 2 |
| 5 | 凹陷木板的低语 | 2027 | short | 89.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林志远的」×4
- 第 2 章：
  - 单条套路句式超限：「林志远的」×7、「陈雪梅的」×5、「林志远站在」×3
  - narration_para_pct 16.0 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「陈雪梅的」×9、「“我不知道」×5、「点了点头」×3
  - narration_para_pct 11.8 低于目标 20.0
  - [observe] 章内自我复读 39 句（如「陈雪梅轻声说道，目光落在账本的最后一页，那里有一…」）
- 第 4 章：
  - 单条套路句式超限：「“我不知道」×6、「林志远的」×4
  - narration_para_pct 8.6 低于目标 20.0
- 第 5 章：
  - narration_para_pct 12.2 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「他蹲下来仔细查看，灰尘下面隐约能看到一些细小的刮…」）

## 整书结构指标

```
chapters: 5
total_chars: 13944
chapter_chars_mean: 2789
chapter_chars_median: 3005
chapter_chars_cv: 0.31
paragraphs_mean: 70.2
dialogue_chars_pct: 37.1
dialogue_para_pct: 79.7
interiority_para_pct: 6.7
narration_para_pct: 13.6
turn_under20_pct: 86.8
turn_over200_pct: 0.0
attr_say_pct: 21.2
attr_adv_pct: 4.0
scenes_per_chapter: 5.6
dialogue_run_mean: 5.2
turn_len_median: 11
```
