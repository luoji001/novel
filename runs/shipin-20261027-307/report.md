# 行李箱 生成报告

slug：`shipin-20261027-307`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7039
LLM 调用：57 次，累计 138.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 黑色行李箱的重量 | 777 | short | 96.3 | 0 |  | 3 |
| 2 | 红色保温杯的温度 | 1430 | normal | 94.8 | 0 |  | 0 |
| 3 | 充电器与保温杯 | 1491 | normal | 91.9 | 0 |  | 0 |
| 4 | 驾驶证的重量 | 1007 | normal | 91.9 | 0 |  | 0 |
| 5 | 行李箱坠入雪堆 | 1310 | normal | 93.1 | 0 |  | 1 |
| 6 | 行李箱坠入雪堆 | 1018 | normal | 93.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 47.5 高于目标 45.0
  - narration_para_pct 14.3 低于目标 35.0
  - dialogue_run_mean 6 高于目标 4.0
- 第 5 章：
  - narration_para_pct 31.4 低于目标 35.0
- 第 6 章：
  - [observe] 标题重复：「行李箱坠入雪堆」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6558
chapter_chars_mean: 1093
chapter_chars_median: 1084
chapter_chars_cv: 0.25
paragraphs_mean: 31.8
dialogue_chars_pct: 24.6
dialogue_para_pct: 51.8
interiority_para_pct: 2.4
narration_para_pct: 45.8
turn_under20_pct: 92.2
turn_over200_pct: 0.0
attr_say_pct: 44.0
attr_adv_pct: 2.2
scenes_per_chapter: 1.2
dialogue_run_mean: 2.6
turn_len_median: 9
```
