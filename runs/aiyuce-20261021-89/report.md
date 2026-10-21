# 质检录音 生成报告

slug：`aiyuce-20261021-89`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11953
LLM 调用：53 次，累计 224.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击键盘 | 2376 | normal | 37.8 | 0 |  | 1 |
| 2 | 调取排班表核对数据 | 2626 | normal | 88.1 | 0 |  | 1 |
| 3 | 审核时间统计表 | 2168 | normal | 35.5 | 0 |  | 2 |
| 4 | 敲击桌面边缘 | 2019 | normal | 35.0 | 0 |  | 1 |
| 5 | 敲击屏幕分析数据 | 1146 | normal | 89.9 | 0 |  | 1 |
| 6 | 敲击屏幕分析数据 | 1612 | short | 83.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 3 句（如「那里既有新来的实习生正跟着导师学习基础操作步骤，…」）
- 第 2 章：
  - narration_para_pct 33.3 低于目标 45.0
- 第 3 章：
  - narration_para_pct 38.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 37.5 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 30.5 高于目标 18.0
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 标题重复：「敲击屏幕分析数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11687
chapter_chars_mean: 1948
chapter_chars_median: 2046
chapter_chars_cv: 0.27
paragraphs_mean: 14.2
dialogue_chars_pct: 12.4
dialogue_para_pct: 34.3
interiority_para_pct: 17.4
narration_para_pct: 48.3
turn_under20_pct: 41.8
turn_over200_pct: 0.0
attr_say_pct: 34.5
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 1.7
turn_len_median: 20
```
