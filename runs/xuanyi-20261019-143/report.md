# 指纹印 生成报告

slug：`xuanyi-20261019-143`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14362
LLM 调用：68 次，累计 234.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 陌生指纹印 | 1702 | short | 97.0 | 0 |  | 4 |
| 2 | 指纹印的秘密 | 3841 | normal | 91.1 | 0 |  | 2 |
| 3 | 晾衣绳被拉弯的瞬间 | 3481 | normal | 89.9 | 0 |  | 2 |
| 4 | 行李箱的去向 | 3292 | normal | 89.2 | 0 |  | 2 |
| 5 | 行李箱消失的时刻 | 2041 | short | 91.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「“我不知道」×3、「苏婉秋的」×3
  - narration_para_pct 4.3 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
  - dialogue_run_mean 13.7 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×4、「林永年站在」×3
  - narration_para_pct 16.8 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「苏婉秋的」×7、「”苏婉秋低」×3、「带着一丝」×3
  - narration_para_pct 10.3 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「苏婉秋的」×5、「“我不知道」×4、「林永年的」×4
  - narration_para_pct 12.8 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「他知道这」×4
  - narration_para_pct 14.8 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13553
chapter_chars_mean: 2711
chapter_chars_median: 3122
chapter_chars_cv: 0.33
paragraphs_mean: 73
dialogue_chars_pct: 47.0
dialogue_para_pct: 81.9
interiority_para_pct: 5.6
narration_para_pct: 12.5
turn_under20_pct: 79.4
turn_over200_pct: 0.0
attr_say_pct: 26.8
attr_adv_pct: 5.3
scenes_per_chapter: 4.4
dialogue_run_mean: 8.1
turn_len_median: 10
```
