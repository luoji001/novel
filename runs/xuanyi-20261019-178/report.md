# 绣线的痕迹 生成报告

slug：`xuanyi-20261019-178`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13957
LLM 调用：68 次，累计 239.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 绣针拨开线团 | 1777 | short | 96.2 | 0 |  | 2 |
| 2 | 绣架上的烛光 | 3820 | normal | 92.0 | 0 |  | 4 |
| 3 | 绣线的粗糙触感 | 3572 | normal | 90.1 | 0 |  | 2 |
| 4 | 红绸的粗粝触感 | 3241 | normal | 89.3 | 0 |  | 2 |
| 5 | 绣品上的名字 | 1542 | short | 90.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈怀瑾的」×4
  - narration_para_pct 8.0 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「苏绣坊」×28、「沈怀瑾的」×8
  - narration_para_pct 8.6 低于目标 20.0
  - attr_adv_pct 11.5 高于目标 10.0
  - dialogue_run_mean 10.3 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「顾清和的」×5、「沈怀瑾的」×4、「他知道这」×3
  - narration_para_pct 10.1 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「苏绣坊」×26、「沈怀瑾的」×6、「“我不知道」×3
  - narration_para_pct 15.4 低于目标 20.0
- 第 5 章：
  - narration_para_pct 10.0 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13341
chapter_chars_mean: 2668
chapter_chars_median: 3096
chapter_chars_cv: 0.38
paragraphs_mean: 54
dialogue_chars_pct: 41.2
dialogue_para_pct: 81.1
interiority_para_pct: 8.3
narration_para_pct: 10.6
turn_under20_pct: 67.6
turn_over200_pct: 0.0
attr_say_pct: 15.3
attr_adv_pct: 7.1
scenes_per_chapter: 1.8
dialogue_run_mean: 6.0
turn_len_median: 15
```
