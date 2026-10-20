# 存折补款 生成报告

slug：`xuanyi-20261019-44`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15507
LLM 调用：68 次，累计 242.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本上的缺口 | 1692 | short | 98.1 | 0 |  | 1 |
| 2 | 黑布包里的秘密 | 4407 | normal | 86.2 | 0 |  | 4 |
| 3 | 账本上的凹痕 | 3684 | normal | 90.3 | 0 |  | 3 |
| 4 | 饭盒里的秘密 | 3899 | normal | 91.3 | 0 |  | 4 |
| 5 | 铁皮盒的锁芯 | 1820 | short | 88.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 16.1 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「他知道这」×5、「点了点头」×4
  - narration_para_pct 16.5 低于目标 20.0
  - attr_adv_pct 15.0 高于目标 10.0
  - [observe] 章内自我复读 14 句（如「他知道，这场谈话还没有结束，真正的较量还在后面…」）
- 第 3 章：
  - 单条套路句式超限：「赵德昌的」×4、「孙美兰点了点头」×3、「赵德昌站在」×3
  - narration_para_pct 8.5 低于目标 20.0
  - [observe] 标题与《账本上的缺口》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「赵德昌的」×3
  - narration_para_pct 16.2 低于目标 20.0
  - attr_adv_pct 16.0 高于目标 10.0
  - [observe] 标题与《黑布包里的秘密》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 10.5 低于目标 20.0
  - [observe] attr_adv_pct 50.0 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 14807
chapter_chars_mean: 2961
chapter_chars_median: 3506
chapter_chars_cv: 0.41
paragraphs_mean: 62
dialogue_chars_pct: 35.7
dialogue_para_pct: 75.3
interiority_para_pct: 10.9
narration_para_pct: 13.8
turn_under20_pct: 75.7
turn_over200_pct: 0.0
attr_say_pct: 7.3
attr_adv_pct: 16.3
scenes_per_chapter: 7.2
dialogue_run_mean: 5.3
turn_len_median: 13
```
