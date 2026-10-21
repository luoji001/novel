# 听评 生成报告

slug：`aiyuce-20261021-177`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12431
LLM 调用：57 次，累计 218.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 计算公式 | 2378 | normal | 37.5 | 0 |  | 2 |
| 2 | AI作文批改系统演示 | 2160 | normal | 85.2 | 0 |  | 3 |
| 3 | 计算公式 | 2244 | normal | 36.0 | 0 |  | 2 |
| 4 | 听课记录统计表 | 2208 | normal | 35.5 | 0 |  | 1 |
| 5 | 屏幕上的数据表 | 2133 | normal | 78.5 | 0 |  | 3 |
| 6 | 敲打桌面的手指 | 1302 | short | 85.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 章内自我复读 5 句（如「如果在未来某个季度突然增加了额外的听课任务或者调…」）
- 第 2 章：
  - dialogue_chars_pct 39.8 高于目标 18.0
  - dialogue_run_mean 6 高于目标 4.0
  - narration_para_pct 23.5 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「计算公式」已存在
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 76.9 高于目标 18.0
  - dialogue_run_mean 13.5 高于目标 4.0
  - narration_para_pct 3.6 低于目标 45.0
- 第 6 章：
  - interiority_para_pct 44.4 高于目标 40.0
  - narration_para_pct 33.3 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 12119
chapter_chars_mean: 2020
chapter_chars_median: 2134
chapter_chars_cv: 0.19
paragraphs_mean: 17.5
dialogue_chars_pct: 23.9
dialogue_para_pct: 46.7
interiority_para_pct: 15.2
narration_para_pct: 38.2
turn_under20_pct: 48.4
turn_over200_pct: 0.0
attr_say_pct: 21.1
attr_adv_pct: 24.4
scenes_per_chapter: 1.3
dialogue_run_mean: 4.0
turn_len_median: 22
```
