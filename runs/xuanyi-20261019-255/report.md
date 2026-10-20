# 手表密码 生成报告

slug：`xuanyi-20261019-255`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14341
LLM 调用：68 次，累计 220.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 表盘映出冰柜阴影 | 1657 | short | 97.8 | 0 |  | 1 |
| 2 | 登记簿上的模糊字迹 | 3735 | normal | 35.7 | 0 |  | 4 |
| 3 | 触摸冰柜的手表 | 3601 | normal | 89.6 | 0 |  | 3 |
| 4 | 触摸手册的边缘 | 3605 | normal | 85.6 | 0 |  | 3 |
| 5 | 登记簿边缘的指纹 | 1738 | short | 89.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 18.8 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「他知道这」×3
  - dialogue_chars_pct 11.0 低于目标 20.0
  - interiority_para_pct 23.1 高于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈婉如的」×3
  - [observe] attr_adv_pct 21.4 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「沈婉如的」×6、「“我不知道」×3
  - narration_para_pct 9.0 低于目标 20.0
  - [observe] 章内自我复读 31 句（如「那么，你能不能告诉我，在你的技术手册里有没有提到…」）
- 第 5 章：
  - narration_para_pct 18.2 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13725
chapter_chars_mean: 2745
chapter_chars_median: 3434
chapter_chars_cv: 0.38
paragraphs_mean: 53.2
dialogue_chars_pct: 26.4
dialogue_para_pct: 63.3
interiority_para_pct: 12.9
narration_para_pct: 23.8
turn_under20_pct: 71.1
turn_over200_pct: 0.0
attr_say_pct: 22.6
attr_adv_pct: 9.1
scenes_per_chapter: 5
dialogue_run_mean: 4.0
turn_len_median: 12
```
