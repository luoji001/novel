# 空页 生成报告

slug：`xuanyi-20261019-169`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14643
LLM 调用：68 次，累计 232.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 空白纸页的低语 | 1780 | short | 94.5 | 0 |  | 1 |
| 2 | 算盘与登记本的错位 | 3934 | normal | 92.2 | 0 |  | 3 |
| 3 | 钢笔的双重印记 | 3600 | normal | 90.2 | 0 |  | 2 |
| 4 | 指纹的微光 | 3357 | normal | 92.3 | 0 |  | 3 |
| 5 | 钥匙上的陌生指纹 | 1967 | short | 81.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 17.2 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「“我不知道」×4、「林素华的」×4、「陈国栋点」×3
  - narration_para_pct 15.6 低于目标 20.0
  - [observe] attr_adv_pct 40.0 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「林素华的」×4
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「为什么会」×4
  - narration_para_pct 11.6 低于目标 20.0
  - [observe] attr_adv_pct 44.4 > 20.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「陈国栋的」×5
  - interiority_para_pct 28.1 高于目标 20.0
  - narration_para_pct 15.6 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13916
chapter_chars_mean: 2783
chapter_chars_median: 3206
chapter_chars_cv: 0.33
paragraphs_mean: 64.6
dialogue_chars_pct: 36.7
dialogue_para_pct: 70.6
interiority_para_pct: 10.5
narration_para_pct: 18.9
turn_under20_pct: 76.7
turn_over200_pct: 0.0
attr_say_pct: 23.4
attr_adv_pct: 26.3
scenes_per_chapter: 5.4
dialogue_run_mean: 4.5
turn_len_median: 12
```
