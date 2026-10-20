# 账本的页数 生成报告

slug：`xuanyi-20261019-96`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14091
LLM 调用：68 次，累计 222.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 怀表里的刻痕 | 1763 | short | 97.6 | 0 |  | 0 |
| 2 | 报纸的霉味 | 3661 | normal | 93.5 | 0 |  | 2 |
| 3 | 翻阅账本的裂痕 | 3461 | normal | 92.7 | 0 |  | 3 |
| 4 | 手电筒的光 | 3272 | normal | 89.5 | 0 |  | 2 |
| 5 | 接煤油灯的光 | 1929 | short | 92.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「沈文远的」×6
  - attr_adv_pct 13.6 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「周素云点」×4、「沈文远的」×4、「“我不知道」×3
  - narration_para_pct 12.3 低于目标 20.0
  - [observe] attr_adv_pct 20.7 > 20.0（结构塌缩）
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3、「沈文远的」×3
- 第 5 章：
  - 单条套路句式超限：「周素云的」×6
  - narration_para_pct 5.7 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13365
chapter_chars_mean: 2673
chapter_chars_median: 3109
chapter_chars_cv: 0.32
paragraphs_mean: 65.2
dialogue_chars_pct: 31.8
dialogue_para_pct: 68.1
interiority_para_pct: 11.6
narration_para_pct: 20.3
turn_under20_pct: 84.7
turn_over200_pct: 0.0
attr_say_pct: 35.8
attr_adv_pct: 8.6
scenes_per_chapter: 3.8
dialogue_run_mean: 5.0
turn_len_median: 10
```
