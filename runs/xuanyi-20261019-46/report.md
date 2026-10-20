# 铜铃 生成报告

slug：`xuanyi-20261019-46`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14174
LLM 调用：68 次，累计 218.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙牌移位 | 1585 | short | 98.2 | 0 |  | 2 |
| 2 | 翻开日期的瞬间 | 3812 | normal | 48.3 | 0 |  | 3 |
| 3 | 箱子上的红标签 | 3273 | normal | 90.9 | 0 |  | 3 |
| 4 | 钟摆上的倒影 | 3713 | normal | 90.1 | 0 |  | 2 |
| 5 | 钥匙牌移位 | 1786 | short | 84.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林雪梅的」×5、「”林雪梅低」×3
  - narration_para_pct 6.9 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周正国的」×7
  - interiority_para_pct 26.2 高于目标 20.0
  - narration_para_pct 19.7 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「周正国的」×5
  - narration_para_pct 10.4 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「周正国的」×11、「林雪梅的」×6、「周正国感到」×3
  - narration_para_pct 13.8 低于目标 20.0
- 第 5 章：
  - dialogue_chars_pct 14.9 低于目标 20.0
  - [observe] 标题重复：「钥匙牌移位」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13565
chapter_chars_mean: 2713
chapter_chars_median: 3124
chapter_chars_cv: 0.38
paragraphs_mean: 53.4
dialogue_chars_pct: 33.9
dialogue_para_pct: 68.3
interiority_para_pct: 15.9
narration_para_pct: 15.9
turn_under20_pct: 76.2
turn_over200_pct: 0.0
attr_say_pct: 29.2
attr_adv_pct: 6.6
scenes_per_chapter: 4
dialogue_run_mean: 3.7
turn_len_median: 11
```
