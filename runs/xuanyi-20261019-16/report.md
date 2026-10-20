# 火车票 生成报告

slug：`xuanyi-20261019-16`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14445
LLM 调用：68 次，累计 229.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜壶嘶鸣 | 2211 | short | 100.0 | 0 |  | 2 |
| 2 | 钥匙的重量 | 3714 | normal | 91.6 | 0 |  | 3 |
| 3 | 钥匙的凹痕 | 3305 | normal | 90.8 | 0 |  | 3 |
| 4 | 钥匙的裂痕 | 3449 | normal | 91.3 | 0 |  | 3 |
| 5 | 摩挲火车票 | 1761 | short | 91.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周素云的」×4、「”周素云轻」×3
  - narration_para_pct 16.9 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×3、「”周素云轻」×3、「沈文远点点」×3
  - narration_para_pct 10.9 低于目标 20.0
  - attr_adv_pct 14.6 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「沈文远的」×5、「周素云的」×4、「“我不知道」×3
  - narration_para_pct 9.1 低于目标 20.0
  - [observe] 标题与《钥匙的重量》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「沈文远的」×14
  - narration_para_pct 4.2 低于目标 20.0
  - [observe] 标题与《钥匙的凹痕》近似 0.80 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「沈文远的」×3
  - attr_adv_pct 20.0 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13684
chapter_chars_mean: 2737
chapter_chars_median: 3138
chapter_chars_cv: 0.3
paragraphs_mean: 69.2
dialogue_chars_pct: 37.2
dialogue_para_pct: 79.1
interiority_para_pct: 9.8
narration_para_pct: 11.1
turn_under20_pct: 88.2
turn_over200_pct: 0.0
attr_say_pct: 41.3
attr_adv_pct: 9.7
scenes_per_chapter: 3
dialogue_run_mean: 4.9
turn_len_median: 11
```
