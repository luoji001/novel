# 登录记录 生成报告

slug：`xuanyi-20261019-132`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15566
LLM 调用：68 次，累计 242.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账单上的名字 | 2053 | short | 99.8 | 0 |  | 3 |
| 2 | 07号电脑的登录记录 | 3793 | normal | 90.7 | 0 |  | 3 |
| 3 | 摩挲纸条边缘 | 3623 | normal | 87.4 | 0 |  | 2 |
| 4 | 摩挲账单边缘 | 3893 | normal | 88.4 | 0 |  | 4 |
| 5 | 摩挲电脑屏幕 | 2199 | short | 88.3 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林振东的」×5
  - narration_para_pct 8.2 低于目标 20.0
  - [observe] attr_adv_pct 30.8 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「苏婉如的」×6、「点了点头」×5、「”苏婉如轻」×4
  - narration_para_pct 3.7 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「”苏婉如轻」×3、「带着一丝」×3
  - [observe] 章内自我复读 21 句（如「你看，”她说，“在这段时间内，每一次‘异地登录’…」）
- 第 4 章：
  - 单条套路句式超限：「林振东的」×7、「他知道这」×4、「”苏婉如轻」×3
  - narration_para_pct 14.1 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 标题与《摩挲纸条边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「”苏婉如轻」×3
  - dialogue_chars_pct 64.3 高于目标 58.0
  - narration_para_pct 3.6 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - dialogue_run_mean 13 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 14817
chapter_chars_mean: 2963
chapter_chars_median: 3467
chapter_chars_cv: 0.3
paragraphs_mean: 67
dialogue_chars_pct: 39.4
dialogue_para_pct: 74.7
interiority_para_pct: 12.7
narration_para_pct: 12.6
turn_under20_pct: 78.1
turn_over200_pct: 0.0
attr_say_pct: 26.5
attr_adv_pct: 12.0
scenes_per_chapter: 3.2
dialogue_run_mean: 5.8
turn_len_median: 12
```
