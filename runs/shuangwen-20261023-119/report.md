# 磅单 生成报告

slug：`shuangwen-20261023-119`
档位：爽文　闸门模式：observe
章数：10　总字数：18870
LLM 调用：97 次，累计 417.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲纸角 | 1882 | normal | 98.6 | 0 |  | 2 |
| 2 | 签字对峙 | 2095 | normal | 37.2 | 0 |  | 1 |
| 3 | 磅单上的五吨差 | 1562 | normal | 94.0 | 0 |  | 0 |
| 4 | 核对磅单数据 | 1745 | normal | 94.6 | 0 |  | 2 |
| 5 | 敲打计算器 | 1786 | normal | 94.7 | 0 |  | 0 |
| 6 | 拼接磅单碎片 | 1888 | normal | 94.3 | 0 |  | 1 |
| 7 | 摊开旧纸页 | 1688 | normal | 35.6 | 0 |  | 4 |
| 8 | 核对磅单数据 | 1864 | normal | 92.4 | 0 |  | 2 |
| 9 | 校准证书更新 | 1853 | normal | 93.0 | 0 |  | 1 |
| 10 | 签字对峙 | 2497 | long | 85.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 3.2 低于目标 5.0
  - attr_adv_pct 18.2 高于目标 12.0
- 第 2 章：
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「过磅房」×3
  - narration_para_pct 3.6 低于目标 5.0
- 第 6 章：
  - attr_adv_pct 12.5 高于目标 12.0
- 第 7 章：
  - dialogue_chars_pct 74.3 高于目标 70.0
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 33 高于目标 14.0
  - [observe] attr_adv_pct 27.8 > 25.0（结构塌缩）
- 第 8 章：
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「核对磅单数据」已存在
- 第 9 章：
  - 单条套路句式超限：「过磅房」×5、「他知道这」×4
- 第 10 章：
  - 单条套路句式超限：「说道“你」×3
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 27.5 高于目标 14.0
  - [observe] 标题重复：「签字对峙」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17909
chapter_chars_mean: 1791
chapter_chars_median: 1762
chapter_chars_cv: 0.14
paragraphs_mean: 40.9
dialogue_chars_pct: 49.3
dialogue_para_pct: 84.6
interiority_para_pct: 6.0
narration_para_pct: 9.3
turn_under20_pct: 68.2
turn_over200_pct: 0.0
attr_say_pct: 30.7
attr_adv_pct: 14.5
scenes_per_chapter: 2.8
dialogue_run_mean: 11.2
turn_len_median: 14
```
