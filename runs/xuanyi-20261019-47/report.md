# 铜钱 生成报告

slug：`xuanyi-20261019-47`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13715
LLM 调用：68 次，累计 228.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 砚台的交易记录 | 1718 | short | 83.3 | 0 |  | 4 |
| 2 | 钥匙与落叶的对话 | 3591 | normal | 89.8 | 0 |  | 4 |
| 3 | 砚台边缘的摩挲 | 3141 | normal | 92.4 | 0 |  | 2 |
| 4 | 匾额边缘的刻痕 | 3500 | normal | 92.2 | 0 |  | 2 |
| 5 | 铜钱与账本对谈 | 1760 | short | 92.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 15.9 低于目标 20.0
  - interiority_para_pct 21.7 高于目标 20.0
  - narration_para_pct 17.4 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「几年前，有个自称是文物专家的人来店里看过那方砚台…」）
- 第 2 章：
  - 单条套路句式超限：「点了点头」×3、「陆知行点」×3、「沈怀远的」×3
  - narration_para_pct 10.4 低于目标 20.0
  - attr_adv_pct 15.0 高于目标 10.0
  - [observe] 章内自我复读 19 句（如「陆知行看着他，似是明白了什么，点了点头，随后又回…」）
- 第 3 章：
  - 单条套路句式超限：「陆知行点」×4、「沈怀远的」×4
  - narration_para_pct 1.6 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3
  - narration_para_pct 12.7 低于目标 20.0
- 第 5 章：
  - narration_para_pct 17.5 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13041
chapter_chars_mean: 2608
chapter_chars_median: 3002
chapter_chars_cv: 0.34
paragraphs_mean: 59.2
dialogue_chars_pct: 38.0
dialogue_para_pct: 79.3
interiority_para_pct: 10.0
narration_para_pct: 10.7
turn_under20_pct: 75.7
turn_over200_pct: 0.0
attr_say_pct: 13.2
attr_adv_pct: 6.0
scenes_per_chapter: 2.2
dialogue_run_mean: 5.5
turn_len_median: 11
```
