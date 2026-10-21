# 页数统计表 生成报告

slug：`aiyuce-20261021-143`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11912
LLM 调用：57 次，累计 217.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对预算报表 | 2177 | normal | 93.8 | 0 |  | 0 |
| 2 | 电话中的AI提案 | 1797 | normal | 90.7 | 0 |  | 1 |
| 3 | 核对页数统计表 | 2431 | normal | 35.4 | 0 |  | 1 |
| 4 | 核对准确率数据 | 2201 | normal | 35.7 | 0 |  | 1 |
| 5 | 问卷回收的敲击声 | 2023 | normal | 36.0 | 0 |  | 3 |
| 6 | 红色数字的警示 | 1277 | short | 80.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 42.9 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 18.3 高于目标 18.0
  - narration_para_pct 29.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 59.9 高于目标 18.0
  - dialogue_run_mean 14 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11633
chapter_chars_mean: 1939
chapter_chars_median: 2051
chapter_chars_cv: 0.21
paragraphs_mean: 15.2
dialogue_chars_pct: 13.1
dialogue_para_pct: 39.0
interiority_para_pct: 7.7
narration_para_pct: 53.2
turn_under20_pct: 63.2
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 3.9
turn_len_median: 18
```
