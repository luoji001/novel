# 红单 生成报告

slug：`xuanyi-20261019-77`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14305
LLM 调用：68 次，累计 213.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扫码枪的红色标签 | 1729 | short | 76.4 | 0 |  | 3 |
| 2 | 扫描记录的重影 | 3891 | normal | 90.7 | 0 |  | 3 |
| 3 | 扫码枪的红色标签 | 3658 | normal | 89.8 | 0 |  | 3 |
| 4 | 苍蝇停落的位置 | 3174 | normal | 90.9 | 0 |  | 1 |
| 5 | 重复扫描的面单 | 1848 | short | 89.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 7.4 低于目标 20.0
  - interiority_para_pct 22.2 高于目标 20.0
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「他知道这」×3、「陈志强的」×3、「为什么会」×3
  - narration_para_pct 11.3 低于目标 20.0
  - [observe] attr_adv_pct 21.7 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「周晓芸的」×4
  - narration_para_pct 12.2 低于目标 20.0
  - [observe] 标题重复：「扫码枪的红色标签」已存在
- 第 4 章：
  - 单条套路句式超限：「南方速递集团」×4
- 第 5 章：
  - dialogue_chars_pct 19.8 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13709
chapter_chars_mean: 2742
chapter_chars_median: 3053
chapter_chars_cv: 0.35
paragraphs_mean: 51.4
dialogue_chars_pct: 33.5
dialogue_para_pct: 70.1
interiority_para_pct: 10.5
narration_para_pct: 19.4
turn_under20_pct: 68.1
turn_over200_pct: 0.0
attr_say_pct: 35.4
attr_adv_pct: 11.0
scenes_per_chapter: 2
dialogue_run_mean: 4.6
turn_len_median: 13
```
