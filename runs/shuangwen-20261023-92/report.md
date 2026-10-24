# 旧借书卡 生成报告

slug：`shuangwen-20261023-92`
档位：爽文　闸门模式：observe
章数：10　总字数：19360
LLM 调用：97 次，累计 444.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧借书卡的复生 | 1773 | normal | 99.7 | 0 |  | 1 |
| 2 | 借书卡的签名差异 | 2067 | normal | 92.6 | 0 |  | 1 |
| 3 | 借书卡的摩挲 | 2094 | normal | 91.0 | 0 |  | 5 |
| 4 | 撕开借书卡后背 | 2125 | normal | 86.8 | 0 |  | 2 |
| 5 | 手令与旧卡对峙 | 1536 | normal | 36.7 | 0 |  | 3 |
| 6 | 摩挲借书卡边缘 | 1999 | normal | 92.2 | 0 |  | 1 |
| 7 | 摩挲借书卡边缘 | 1867 | normal | 91.8 | 0 |  | 2 |
| 8 | 摩挲借书卡边缘 | 1792 | normal | 86.5 | 0 |  | 3 |
| 9 | 摩挲借书卡边缘 | 1719 | normal | 36.6 | 0 |  | 3 |
| 10 | 摩挲借书卡边缘 | 2378 | long | 92.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李怀远的」×3
- 第 2 章：
  - 单条套路句式超限：「李怀远的」×4
- 第 3 章：
  - 单条套路句式超限：「带着一丝」×3、「李怀远的」×3
  - narration_para_pct 2.0 低于目标 5.0
  - attr_adv_pct 15.8 高于目标 12.0
  - dialogue_run_mean 15 高于目标 14.0
  - [observe] 标题与《旧借书卡的复生》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - narration_para_pct 3.6 低于目标 5.0
  - dialogue_run_mean 15.8 高于目标 14.0
- 第 5 章：
  - 单条套路句式超限：「李怀远的」×4
  - narration_para_pct 2.8 低于目标 5.0
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「李怀远的」×4
- 第 7 章：
  - narration_para_pct 3.2 低于目标 5.0
  - [observe] 标题重复：「摩挲借书卡边缘」已存在
- 第 8 章：
  - narration_para_pct 2.9 低于目标 5.0
  - dialogue_run_mean 34 高于目标 14.0
  - [observe] 标题重复：「摩挲借书卡边缘」已存在
- 第 9 章：
  - 单条套路句式超限：「李怀远的」×6
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「摩挲借书卡边缘」已存在
- 第 10 章：
  - 单条套路句式超限：「李怀远的」×5
  - [observe] 标题重复：「摩挲借书卡边缘」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18280
chapter_chars_mean: 1828
chapter_chars_median: 1843
chapter_chars_cv: 0.12
paragraphs_mean: 45.9
dialogue_chars_pct: 51.0
dialogue_para_pct: 88.0
interiority_para_pct: 4.9
narration_para_pct: 7.2
turn_under20_pct: 75.2
turn_over200_pct: 0.0
attr_say_pct: 34.2
attr_adv_pct: 12.1
scenes_per_chapter: 1.2
dialogue_run_mean: 11.3
turn_len_median: 12
```
