# 纸条的真相 生成报告

slug：`xuanyi-20261019-196`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14748
LLM 调用：68 次，累计 241.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 登记簿的末页 | 1757 | short | 95.9 | 0 |  | 4 |
| 2 | 登记簿的空白处 | 3339 | normal | 93.2 | 0 |  | 4 |
| 3 | 怀表的错位时光 | 3794 | normal | 90.2 | 0 |  | 4 |
| 4 | 木牌上的日期 | 4032 | normal | 90.1 | 0 |  | 6 |
| 5 | 纸条的灰烬 | 1821 | short | 90.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈文远的」×5、「为什么会」×4
  - narration_para_pct 8.3 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 10.0
  - [observe] 章内自我复读 9 句（如「周婉秋站在原地，看着他的背影消失在黑暗之中，心中…」）
- 第 2 章：
  - 单条套路句式超限：「沈文远的」×4、「沈文远站在」×3
  - narration_para_pct 12.5 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 标题与《登记簿的末页》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「周婉秋的」×3、「为什么会」×3
  - narration_para_pct 16.1 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「1943年5月20日…」）
- 第 4 章：
  - 单条套路句式超限：「点了点头“」×4、「重庆防空洞管理处」×4、「“我不知道」×3
  - dialogue_chars_pct 59.1 高于目标 58.0
  - narration_para_pct 7.5 低于目标 20.0
  - attr_adv_pct 18.4 高于目标 10.0
  - dialogue_run_mean 11.8 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「1943年5月20日…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「1943年5月20日…」）

## 整书结构指标

```
chapters: 5
total_chars: 14070
chapter_chars_mean: 2814
chapter_chars_median: 3196
chapter_chars_cv: 0.37
paragraphs_mean: 59.6
dialogue_chars_pct: 39.5
dialogue_para_pct: 78.9
interiority_para_pct: 7.8
narration_para_pct: 13.4
turn_under20_pct: 72.9
turn_over200_pct: 0.0
attr_say_pct: 13.1
attr_adv_pct: 12.7
scenes_per_chapter: 3.8
dialogue_run_mean: 6.6
turn_len_median: 11
```
