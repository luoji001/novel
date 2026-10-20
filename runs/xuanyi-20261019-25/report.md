# 药盒 生成报告

slug：`xuanyi-20261019-25`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14885
LLM 调用：68 次，累计 230.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 无人离场 | 1656 | short | 99.7 | 0 |  | 2 |
| 2 | 手机收到神秘短信 | 4060 | normal | 91.6 | 0 |  | 3 |
| 3 | 撕碎的值班表一角 | 3371 | normal | 88.9 | 0 |  | 3 |
| 4 | 指纹擦拭登记本 | 3825 | normal | 91.7 | 0 |  | 1 |
| 5 | 钥匙上的指纹痕迹 | 1968 | short | 89.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 10.3 低于目标 20.0
  - [observe] attr_adv_pct 28.6 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「林婉如的」×6、「沈墨站在」×3
  - narration_para_pct 9.3 低于目标 20.0
  - attr_adv_pct 15.8 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「林婉如的」×9、「“我不知道」×4、「”林婉如轻」×4
  - narration_para_pct 15.5 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「晨曦药业有限公司」×6
- 第 5 章：
  - 单条套路句式超限：「沈墨站在」×3

## 整书结构指标

```
chapters: 5
total_chars: 14208
chapter_chars_mean: 2842
chapter_chars_median: 3213
chapter_chars_cv: 0.37
paragraphs_mean: 56
dialogue_chars_pct: 35.3
dialogue_para_pct: 72.0
interiority_para_pct: 9.7
narration_para_pct: 18.4
turn_under20_pct: 66.5
turn_over200_pct: 0.0
attr_say_pct: 25.0
attr_adv_pct: 10.7
scenes_per_chapter: 3
dialogue_run_mean: 4.4
turn_len_median: 15
```
