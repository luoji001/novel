# 模型 生成报告

slug：`aiyuce-20261021-156`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12785
LLM 调用：57 次，累计 227.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的12度增长 | 2065 | normal | 94.2 | 0 |  | 2 |
| 2 | 自制模型的教学实践 | 2850 | normal | 23.0 | 0 |  | 1 |
| 3 | 核对成绩统计表 | 2149 | normal | 90.0 | 0 |  | 0 |
| 4 | 设备折旧表的摩挲 | 2381 | normal | 36.9 | 0 |  | 2 |
| 5 | 折旧表上的磨损痕迹 | 2060 | normal | 82.4 | 0 |  | 4 |
| 6 | 摩挲纸边的张伟 | 1274 | short | 89.3 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 41.2 高于目标 40.0
  - narration_para_pct 41.2 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 2 句（如「具备自制物理模型的能力…」）
- 第 4 章：
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么呢推翻…」）
- 第 5 章：
  - 命中套话收尾句
  - dialogue_chars_pct 62.6 高于目标 18.0
  - dialogue_run_mean 15 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 12471
chapter_chars_mean: 2078
chapter_chars_median: 2060
chapter_chars_cv: 0.25
paragraphs_mean: 17.5
dialogue_chars_pct: 12.6
dialogue_para_pct: 32.4
interiority_para_pct: 26.5
narration_para_pct: 41.0
turn_under20_pct: 72.7
turn_over200_pct: 0.0
attr_say_pct: 26.2
attr_adv_pct: 16.0
scenes_per_chapter: 1.7
dialogue_run_mean: 4.1
turn_len_median: 13
```
