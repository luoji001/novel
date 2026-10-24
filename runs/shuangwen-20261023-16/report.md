# 旧房产证 生成报告

slug：`shuangwen-20261023-16`
档位：爽文　闸门模式：observe
章数：10　总字数：18991
LLM 调用：97 次，累计 454.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕碎协议 | 1775 | normal | 100.0 | 0 |  | 1 |
| 2 | 递还证件 | 1456 | normal | 93.0 | 0 |  | 2 |
| 3 | 指尖抚过登记簿 | 1641 | normal | 92.7 | 0 |  | 1 |
| 4 | 摩挲补偿协议 | 1501 | normal | 36.4 | 0 |  | 3 |
| 5 | 指尖抚过房产证 | 2059 | normal | 94.1 | 0 |  | 1 |
| 6 | 指尖划过房产证 | 2092 | normal | 37.2 | 0 |  | 3 |
| 7 | 手指划过房产证 | 2120 | normal | 35.8 | 0 |  | 4 |
| 8 | 手指摩挲旧房产证 | 1888 | normal | 92.7 | 0 |  | 2 |
| 9 | 摩挲房产证 | 1871 | normal | 88.1 | 0 |  | 5 |
| 10 | 摩挲房产证 | 2578 | long | 89.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李建国的」×4
- 第 2 章：
  - 单条套路句式超限：「林小满的」×4、「李建国的」×3
  - narration_para_pct 4.5 低于目标 5.0
- 第 3 章：
  - 单条套路句式超限：「李建国的」×3
- 第 4 章：
  - 单条套路句式超限：「林小满的」×3
  - narration_para_pct 2.9 低于目标 5.0
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「李建国的」×3
- 第 6 章：
  - 单条套路句式超限：「李建国的」×6
  - [observe] attr_adv_pct 50.0 > 25.0（结构塌缩）
  - [observe] 标题与《指尖抚过房产证》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - 单条套路句式超限：「李建国的」×4
  - narration_para_pct 2.4 低于目标 5.0
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题与《指尖划过房产证》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「李建国的」×4
  - [observe] 标题与《手指划过房产证》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「李建国的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 12.5 高于目标 12.0
  - dialogue_run_mean 44 高于目标 14.0
  - [observe] 标题与《手指摩挲旧房产证》近似 0.77 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - 单条套路句式超限：「李建国的」×4
  - [observe] 标题重复：「摩挲房产证」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18067
chapter_chars_mean: 1807
chapter_chars_median: 1791
chapter_chars_cv: 0.18
paragraphs_mean: 38.8
dialogue_chars_pct: 50.8
dialogue_para_pct: 87.8
interiority_para_pct: 4.6
narration_para_pct: 7.5
turn_under20_pct: 69.0
turn_over200_pct: 0.0
attr_say_pct: 19.1
attr_adv_pct: 15.0
scenes_per_chapter: 1.3
dialogue_run_mean: 11.8
turn_len_median: 14
```
