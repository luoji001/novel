# 红绸布 生成报告

slug：`xuanyi-20261019-213`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14201
LLM 调用：68 次，累计 241.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 刻痕深处的秘密 | 1458 | short | 62.5 | 0 |  | 3 |
| 2 | 铜钱盒的裂痕 | 3585 | normal | 89.3 | 0 |  | 3 |
| 3 | 掀开红绸布一角 | 3628 | normal | 91.4 | 0 |  | 2 |
| 4 | 铜秤上的刻度消失 | 3654 | normal | 93.3 | 0 |  | 3 |
| 5 | 铜钱盒中的凹痕 | 1871 | short | 92.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 4.8 低于目标 20.0
  - dialogue_run_mean 1 低于目标 1.5
  - [observe] 章内自我复读 14 句（如「他蹲下身，仔细端详着铜钱边缘的划痕，又抬眼看向账…」）
- 第 2 章：
  - 单条套路句式超限：「沈九安的」×3
  - attr_adv_pct 18.2 高于目标 10.0
  - [observe] 章内自我复读 19 句（如「打开最底层的一个小匣子，取出一本泛黄的笔记本，翻…」）
- 第 3 章：
  - 单条套路句式超限：「周玉兰的」×4、「为什么会」×3
  - attr_adv_pct 12.5 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「沈九安的」×4、「”周玉兰低」×3
  - narration_para_pct 11.1 低于目标 20.0
  - attr_adv_pct 15.2 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「沈九安的」×8
  - narration_para_pct 11.1 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
  - [observe] 标题与《铜钱盒的裂痕》近似 0.77 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 13547
chapter_chars_mean: 2709
chapter_chars_median: 3431
chapter_chars_cv: 0.38
paragraphs_mean: 57.4
dialogue_chars_pct: 30.5
dialogue_para_pct: 71.6
interiority_para_pct: 7.7
narration_para_pct: 20.7
turn_under20_pct: 85.1
turn_over200_pct: 0.0
attr_say_pct: 28.1
attr_adv_pct: 16.0
scenes_per_chapter: 3.6
dialogue_run_mean: 3.9
turn_len_median: 10
```
