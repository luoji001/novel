# 电表转得更快 生成报告

slug：`aiyuce-20261021-86`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11282
LLM 调用：53 次，累计 209.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的用电量增幅 | 2049 | normal | 38.6 | 0 |  | 1 |
| 2 | 拨通电话 | 2115 | normal | 34.8 | 0 |  | 3 |
| 3 | 降低推理成本 | 2234 | normal | 36.0 | 0 |  | 2 |
| 4 | 摩挲纸页边缘 | 1914 | normal | 87.5 | 0 |  | 0 |
| 5 | 核对显卡标价涨幅 | 1470 | normal | 83.2 | 0 |  | 2 |
| 6 | 核对显卡标价涨幅 | 1494 | short | 84.2 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - dialogue_chars_pct 25.4 高于目标 18.0
  - narration_para_pct 35.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - 单条套路句式超限：「深圳华强北电子市场」×3
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - interiority_para_pct 57.1 高于目标 40.0
  - narration_para_pct 42.9 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 61.5 高于目标 18.0
  - dialogue_run_mean 6.5 高于目标 4.0
  - narration_para_pct 7.1 低于目标 45.0
  - [observe] 标题重复：「核对显卡标价涨幅」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11019
chapter_chars_mean: 1836
chapter_chars_median: 1936
chapter_chars_cv: 0.17
paragraphs_mean: 13.8
dialogue_chars_pct: 13.5
dialogue_para_pct: 26.9
interiority_para_pct: 15.8
narration_para_pct: 57.3
turn_under20_pct: 37.8
turn_over200_pct: 0.0
attr_say_pct: 49.9
attr_adv_pct: 2.9
scenes_per_chapter: 1.3
dialogue_run_mean: 2.6
turn_len_median: 26
```
