# 锁芯 生成报告

slug：`xuanyi-20261019-31`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14091
LLM 调用：68 次，累计 234.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 锁芯的金粉 | 1825 | short | 75.7 | 0 |  | 2 |
| 2 | 便签纸的双面日期 | 3686 | normal | 92.1 | 0 |  | 2 |
| 3 | 锁芯的缺失环节 | 3651 | normal | 90.4 | 0 |  | 4 |
| 4 | 纸片飘入光斑 | 3156 | normal | 90.9 | 0 |  | 1 |
| 5 | 擦拭保险柜表面 | 1768 | short | 93.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 13.1 低于目标 20.0
  - interiority_para_pct 28.6 高于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林婉秋的」×4、「为什么会」×3
  - [observe] attr_adv_pct 27.8 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「林婉秋的」×3
  - narration_para_pct 6.0 低于目标 20.0
  - attr_adv_pct 10.2 高于目标 10.0
  - dialogue_run_mean 11 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「林婉秋的」×5、「带着一丝」×3、「周慕云的」×3
- 第 5 章：
  - 单条套路句式超限：「为什么会」×3
  - narration_para_pct 11.5 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13478
chapter_chars_mean: 2696
chapter_chars_median: 3019
chapter_chars_cv: 0.33
paragraphs_mean: 51.8
dialogue_chars_pct: 37.8
dialogue_para_pct: 73.3
interiority_para_pct: 7.4
narration_para_pct: 19.4
turn_under20_pct: 73.1
turn_over200_pct: 0.0
attr_say_pct: 23.9
attr_adv_pct: 13.5
scenes_per_chapter: 3.2
dialogue_run_mean: 4.9
turn_len_median: 14
```
