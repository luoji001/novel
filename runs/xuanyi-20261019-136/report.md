# 怀表 生成报告

slug：`xuanyi-20261019-136`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14112
LLM 调用：68 次，累计 241.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本上的雨痕 | 1638 | short | 96.2 | 0 |  | 3 |
| 2 | 铁门缓缓开启 | 3995 | normal | 93.6 | 0 |  | 1 |
| 3 | 怀表里的刻痕 | 3521 | normal | 91.9 | 0 |  | 2 |
| 4 | 钥匙上的特殊标记 | 3142 | normal | 86.4 | 0 |  | 4 |
| 5 | 铜片上的未完句式 | 1811 | short | 88.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈德昌的」×5、「防空洞」×3
  - narration_para_pct 4.3 低于目标 20.0
  - dialogue_run_mean 14.7 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「防空洞」×13
- 第 3 章：
  - 单条套路句式超限：「陈德昌的」×6、「防空洞」×5
  - narration_para_pct 15.4 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「陈德昌的」×8、「防空洞」×6、「重庆警察局」×3
  - dialogue_chars_pct 63.6 高于目标 58.0
  - narration_para_pct 1.4 低于目标 20.0
  - dialogue_run_mean 33.5 高于目标 10.0
- 第 5 章：
  - dialogue_chars_pct 17.6 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13350
chapter_chars_mean: 2670
chapter_chars_median: 2988
chapter_chars_cv: 0.38
paragraphs_mean: 68.2
dialogue_chars_pct: 41.8
dialogue_para_pct: 76.3
interiority_para_pct: 6.6
narration_para_pct: 17.1
turn_under20_pct: 82.7
turn_over200_pct: 0.0
attr_say_pct: 20.6
attr_adv_pct: 5.0
scenes_per_chapter: 3.4
dialogue_run_mean: 11.5
turn_len_median: 11
```
