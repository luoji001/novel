# 红绸布 生成报告

slug：`xuanyi-20261019-21`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13681
LLM 调用：68 次，累计 223.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 照片背面的模糊字 | 1799 | short | 81.8 | 0 |  | 3 |
| 2 | 撕碎的登记簿边缘 | 3225 | normal | 42.9 | 0 |  | 3 |
| 3 | 火车票的模糊字迹 | 3711 | normal | 93.0 | 0 |  | 2 |
| 4 | 摩挲胶卷边缘 | 3551 | normal | 90.8 | 0 |  | 3 |
| 5 | 红绸布上的指痕 | 1390 | short | 43.9 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈秋实的」×4
  - dialogue_chars_pct 12.7 低于目标 20.0
  - interiority_para_pct 23.1 高于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「陈玉兰的」×6
  - dialogue_chars_pct 12.0 低于目标 20.0
  - interiority_para_pct 20.5 高于目标 20.0
- 第 3 章：
  - dialogue_chars_pct 59.3 高于目标 58.0
  - narration_para_pct 5.4 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「陈玉兰的」×5、「他知道这」×4、「带着一丝」×3
  - narration_para_pct 14.8 低于目标 20.0
  - attr_adv_pct 11.8 高于目标 10.0
- 第 5 章：
  - dialogue_chars_pct 9.3 低于目标 20.0
  - interiority_para_pct 29.2 高于目标 20.0
  - dialogue_run_mean 1.1 低于目标 1.5
  - [observe] 章内自我复读 15 句（如「突然，她的瞳孔微微收缩——那些看似随意垂下的布料…」）

## 整书结构指标

```
chapters: 5
total_chars: 13140
chapter_chars_mean: 2628
chapter_chars_median: 3121
chapter_chars_cv: 0.39
paragraphs_mean: 45.8
dialogue_chars_pct: 28.6
dialogue_para_pct: 65.3
interiority_para_pct: 15.7
narration_para_pct: 19.0
turn_under20_pct: 82.0
turn_over200_pct: 0.0
attr_say_pct: 43.6
attr_adv_pct: 4.7
scenes_per_chapter: 2.4
dialogue_run_mean: 3.4
turn_len_median: 12
```
