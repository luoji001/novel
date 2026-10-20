# 硬币密码 生成报告

slug：`xuanyi-20261019-11`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13728
LLM 调用：68 次，累计 226.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 指纹与铜锈痕迹 | 1482 | short | 88.5 | 0 |  | 1 |
| 2 | 摩挲硬币边缘 | 3789 | normal | 93.0 | 0 |  | 2 |
| 3 | 摩挲钥匙表面 | 3579 | normal | 90.9 | 0 |  | 3 |
| 4 | 摩挲信纸边缘 | 3257 | normal | 91.1 | 0 |  | 2 |
| 5 | 钥匙开启第二道锁 | 1616 | short | 85.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 13.5 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「周文远的」×4、「为什么会」×4、「周文远点了点头」×3
  - narration_para_pct 11.9 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「沈慕云的」×5、「他知道这」×4、「泰华洋行」×4
  - narration_para_pct 18.2 低于目标 20.0
  - attr_adv_pct 12.9 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「沈慕云的」×8、「沈慕云站在」×3、「他知道这」×3
  - [observe] 标题与《摩挲硬币边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - dialogue_chars_pct 19.1 低于目标 20.0
  - interiority_para_pct 22.7 高于目标 20.0
  - narration_para_pct 18.2 低于目标 20.0
  - [observe] attr_adv_pct 28.6 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 13133
chapter_chars_mean: 2627
chapter_chars_median: 3119
chapter_chars_cv: 0.4
paragraphs_mean: 49.8
dialogue_chars_pct: 31.6
dialogue_para_pct: 66.6
interiority_para_pct: 13.5
narration_para_pct: 19.9
turn_under20_pct: 70.9
turn_over200_pct: 0.0
attr_say_pct: 23.8
attr_adv_pct: 8.3
scenes_per_chapter: 3.2
dialogue_run_mean: 2.9
turn_len_median: 13
```
