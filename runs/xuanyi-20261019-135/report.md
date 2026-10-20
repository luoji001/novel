# 手表藏钞 生成报告

slug：`xuanyi-20261019-135`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14970
LLM 调用：68 次，累计 229.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手表里的钞票 | 1727 | short | 98.2 | 0 |  | 1 |
| 2 | 手表仍在走动 | 3634 | normal | 91.3 | 0 |  | 3 |
| 3 | 存折上的倒计时 | 3494 | normal | 90.8 | 0 |  | 2 |
| 4 | 快递单上的地址 | 4363 | normal | 87.4 | 0 |  | 3 |
| 5 | 钥匙下的报纸一角 | 1747 | short | 85.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 17.9 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈志远的」×9、「他知道这」×4、「“我不知道」×3
  - narration_para_pct 13.6 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「点了点头」×3、「林婉如的」×3
  - narration_para_pct 19.5 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「“我不知道」×6、「点了点头“」×3、「林婉如点」×3
  - narration_para_pct 8.2 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「我不记得我们在系统里录入过这个地址。而且，从地理…」）
- 第 5 章：
  - dialogue_chars_pct 17.7 低于目标 20.0
  - interiority_para_pct 21.9 高于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14203
chapter_chars_mean: 2841
chapter_chars_median: 3315
chapter_chars_cv: 0.4
paragraphs_mean: 68.8
dialogue_chars_pct: 41.1
dialogue_para_pct: 74.4
interiority_para_pct: 10.0
narration_para_pct: 15.6
turn_under20_pct: 74.8
turn_over200_pct: 0.0
attr_say_pct: 26.9
attr_adv_pct: 3.9
scenes_per_chapter: 3.4
dialogue_run_mean: 4.2
turn_len_median: 12
```
