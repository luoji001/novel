# 账簿 生成报告

slug：`shuangwen-20261022-91`
档位：爽文　闸门模式：observe
章数：10　总字数：19168
LLM 调用：97 次，累计 433.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账簿上的丹药痕迹 | 1811 | normal | 97.5 | 0 |  | 2 |
| 2 | 账簿上的两枚灵石 | 2009 | normal | 93.1 | 0 |  | 1 |
| 3 | 签字未落的账簿 | 1838 | normal | 92.4 | 0 |  | 0 |
| 4 | 补全三份账簿 | 1676 | normal | 93.2 | 0 |  | 0 |
| 5 | 摩挲账簿边缘 | 1902 | normal | 92.1 | 0 |  | 3 |
| 6 | 攥紧账簿的指尖 | 1814 | normal | 93.0 | 0 |  | 1 |
| 7 | 摩挲账簿边缘 | 1661 | normal | 92.5 | 0 |  | 1 |
| 8 | 攥紧账簿的指尖 | 1891 | normal | 94.5 | 0 |  | 3 |
| 9 | 攥紧账簿的指尖 | 1991 | normal | 94.2 | 0 |  | 2 |
| 10 | 摩挲账簿边缘 | 2565 | long | 94.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3、「林远站在」×3
  - attr_adv_pct 12.5 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「他知道这」×3
- 第 5 章：
  - narration_para_pct 4.9 低于目标 5.0
  - attr_adv_pct 20.8 高于目标 12.0
  - dialogue_run_mean 19 高于目标 14.0
- 第 6 章：
  - 单条套路句式超限：「他知道这」×3
- 第 7 章：
  - [observe] 标题重复：「摩挲账簿边缘」已存在
- 第 8 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「攥紧账簿的指尖」已存在
- 第 9 章：
  - 单条套路句式超限：「林远站在」×3、「了自己的」×3
  - [observe] 标题重复：「攥紧账簿的指尖」已存在
- 第 10 章：
  - 单条套路句式超限：「林远站在」×3
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「摩挲账簿边缘」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18200
chapter_chars_mean: 1820
chapter_chars_median: 1780
chapter_chars_cv: 0.13
paragraphs_mean: 40.5
dialogue_chars_pct: 47.8
dialogue_para_pct: 79.4
interiority_para_pct: 7.4
narration_para_pct: 13.1
turn_under20_pct: 67.1
turn_over200_pct: 0.0
attr_say_pct: 21.3
attr_adv_pct: 10.4
scenes_per_chapter: 3.4
dialogue_run_mean: 7.0
turn_len_median: 14
```
