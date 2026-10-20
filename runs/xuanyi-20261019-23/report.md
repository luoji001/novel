# 行李箱 生成报告

slug：`xuanyi-20261019-23`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14017
LLM 调用：68 次，累计 227.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 箱子的秘密 | 1811 | short | 98.6 | 0 |  | 2 |
| 2 | 窗帘掀开 | 3513 | normal | 92.7 | 0 |  | 2 |
| 3 | 汇款单被摩挲 | 3221 | normal | 91.3 | 0 |  | 2 |
| 4 | 钥匙的低语 | 3915 | normal | 89.9 | 0 |  | 3 |
| 5 | 箱子的秘密 | 1552 | short | 93.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「“我不知道」×3
  - narration_para_pct 18.2 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×6、「”苏婉儿轻」×4、「苏婉儿的」×3
  - narration_para_pct 9.0 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
  - narration_para_pct 11.4 低于目标 20.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「“我不知道」×8、「苏婉儿点」×5、「林志远的」×4
  - narration_para_pct 8.6 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「他知道这」×4
  - narration_para_pct 14.7 低于目标 20.0
  - [observe] 标题重复：「箱子的秘密」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13271
chapter_chars_mean: 2654
chapter_chars_median: 3067
chapter_chars_cv: 0.38
paragraphs_mean: 66.2
dialogue_chars_pct: 41.5
dialogue_para_pct: 82.8
interiority_para_pct: 5.9
narration_para_pct: 11.3
turn_under20_pct: 82.5
turn_over200_pct: 0.0
attr_say_pct: 25.9
attr_adv_pct: 3.6
scenes_per_chapter: 5.6
dialogue_run_mean: 7.4
turn_len_median: 10
```
