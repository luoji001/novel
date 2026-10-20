# 砚台 生成报告

slug：`xuanyi-20261019-167`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14241
LLM 调用：68 次，累计 232.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 砚台的刻痕 | 1758 | short | 95.0 | 0 |  | 2 |
| 2 | 铜钱与砚台对话 | 3577 | normal | 93.0 | 0 |  | 2 |
| 3 | 触摸残缺的云纹 | 3679 | normal | 90.3 | 0 |  | 2 |
| 4 | 墨色凝于砚台之上 | 3387 | normal | 88.8 | 0 |  | 2 |
| 5 | 抚摸砚台的凹陷 | 1835 | short | 91.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陆知远的」×4、「沈怀瑾的」×3
  - narration_para_pct 15.4 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「沈怀瑾的」×6、「陆知远的」×5
  - narration_para_pct 14.1 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「陆知远的」×4、「沈怀瑾的」×3
  - narration_para_pct 18.7 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「陆知远的」×5、「沈怀瑾的」×5、「”陆知远低」×3
  - narration_para_pct 7.2 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「陆知远的」×4
  - narration_para_pct 2.7 低于目标 20.0
  - dialogue_run_mean 11 高于目标 10.0

## 整书结构指标

```
chapters: 5
total_chars: 13560
chapter_chars_mean: 2712
chapter_chars_median: 3231
chapter_chars_cv: 0.34
paragraphs_mean: 60
dialogue_chars_pct: 38.4
dialogue_para_pct: 75.9
interiority_para_pct: 11.8
narration_para_pct: 12.3
turn_under20_pct: 72.9
turn_over200_pct: 0.0
attr_say_pct: 11.2
attr_adv_pct: 7.2
scenes_per_chapter: 2
dialogue_run_mean: 5.2
turn_len_median: 13
```
