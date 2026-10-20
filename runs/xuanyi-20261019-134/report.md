# 账本残页 生成报告

slug：`xuanyi-20261019-134`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13820
LLM 调用：68 次，累计 230.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙叩击木架 | 1607 | short | 86.7 | 0 |  | 2 |
| 2 | 算盘珠落 | 3371 | normal | 22.9 | 0 |  | 3 |
| 3 | 账本翻页 | 3247 | normal | 93.4 | 0 |  | 4 |
| 4 | 账页泛黄处 | 3485 | normal | 90.7 | 0 |  | 3 |
| 5 | 钥匙凹痕处 | 2105 | short | 91.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 14.0 低于目标 20.0
  - dialogue_run_mean 1.4 低于目标 1.5
- 第 2 章：
  - 单条套路句式超限：「他知道这」×4、「陈德昌的」×3
  - dialogue_chars_pct 9.2 低于目标 20.0
  - [observe] 章内自我复读 15 句（如「仓库里的空气潮湿而沉闷，棉布的气息混杂着霉味，让…」）
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「“我不知道」×3、「周素芬的」×3
  - narration_para_pct 10.6 低于目标 20.0
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「陈德昌的」×5、「周素芬的」×4
  - narration_para_pct 6.7 低于目标 20.0
  - dialogue_run_mean 10.8 高于目标 10.0
- 第 5 章：
  - attr_adv_pct 18.2 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13271
chapter_chars_mean: 2654
chapter_chars_median: 3103
chapter_chars_cv: 0.31
paragraphs_mean: 48
dialogue_chars_pct: 31.0
dialogue_para_pct: 68.7
interiority_para_pct: 8.5
narration_para_pct: 22.8
turn_under20_pct: 74.9
turn_over200_pct: 0.0
attr_say_pct: 32.8
attr_adv_pct: 11.4
scenes_per_chapter: 4.2
dialogue_run_mean: 4.9
turn_len_median: 11
```
