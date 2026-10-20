# 行李箱 生成报告

slug：`xuanyi-20261019-163`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13063
LLM 调用：68 次，累计 218.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲纸张的指尖 | 1599 | short | 97.8 | 0 |  | 2 |
| 2 | 揭开行李箱的秘密 | 3480 | normal | 90.8 | 0 |  | 5 |
| 3 | 摩挲纸张的指尖 | 3043 | normal | 91.6 | 0 |  | 4 |
| 4 | 摩挲车票的指尖 | 3080 | normal | 26.4 | 0 |  | 5 |
| 5 | 摩挲车票的指尖 | 1856 | short | 91.4 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - 单条套路句式超限：「“我不知道」×3、「苏婉如的」×3
- 第 2 章：
  - 单条套路句式超限：「苏婉如点」×3、「为什么会」×3
  - narration_para_pct 13.6 低于目标 20.0
  - attr_adv_pct 17.6 高于目标 10.0
  - dialogue_run_mean 13.2 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「林秋实接过纸张，眯着眼睛看了片刻，然后抬起头看向…」）
- 第 3 章：
  - 单条套路句式超限：「林秋实点了点头」×3、「为什么会」×3
  - narration_para_pct 6.6 低于目标 20.0
  - dialogue_run_mean 11.3 高于目标 10.0
  - [observe] 标题重复：「摩挲纸张的指尖」已存在
- 第 4 章：
  - 单条套路句式超限：「林秋实站在」×3、「林秋实的」×3
  - dialogue_chars_pct 9.7 低于目标 20.0
  - interiority_para_pct 22.6 高于目标 20.0
  - dialogue_run_mean 1.1 低于目标 1.5
  - [observe] 标题与《摩挲纸张的指尖》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「林秋实的」×4
  - narration_para_pct 6.1 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 标题重复：「摩挲车票的指尖」已存在

## 整书结构指标

```
chapters: 5
total_chars: 12468
chapter_chars_mean: 2494
chapter_chars_median: 2876
chapter_chars_cv: 0.32
paragraphs_mean: 51.4
dialogue_chars_pct: 35.4
dialogue_para_pct: 69.9
interiority_para_pct: 11.7
narration_para_pct: 18.4
turn_under20_pct: 82.1
turn_over200_pct: 0.0
attr_say_pct: 19.3
attr_adv_pct: 7.8
scenes_per_chapter: 3
dialogue_run_mean: 7.1
turn_len_median: 13
```
