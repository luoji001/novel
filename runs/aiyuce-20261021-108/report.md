# 实验课 生成报告

slug：`aiyuce-20261021-108`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11260
LLM 调用：57 次，累计 211.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 灯光闪烁 | 1754 | normal | 90.4 | 0 |  | 3 |
| 2 | 模型演示与实验操作 | 1884 | normal | 33.7 | 0 |  | 4 |
| 3 | 模型演示与实验操作 | 2261 | normal | 34.9 | 0 |  | 2 |
| 4 | 模型演示与实验操作 | 2293 | normal | 78.6 | 0 |  | 5 |
| 5 | 教学模型使用情况统计表 | 1840 | normal | 87.2 | 0 |  | 0 |
| 6 | 模型演示与实验操作 | 1222 | short | 85.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 28.8 高于目标 18.0
  - dialogue_run_mean 5.5 高于目标 4.0
  - narration_para_pct 6.7 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 65.5 高于目标 18.0
  - dialogue_run_mean 6 高于目标 4.0
  - narration_para_pct 14.3 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「2024年6月物理统考试卷分析报告…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「模型演示与实验操作」已存在
- 第 4 章：
  - 命中套话收尾句
  - dialogue_chars_pct 40.6 高于目标 18.0
  - dialogue_run_mean 7 高于目标 4.0
  - narration_para_pct 16.7 低于目标 45.0
  - [observe] 标题重复：「模型演示与实验操作」已存在
- 第 6 章：
  - dialogue_chars_pct 34.2 高于目标 18.0
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 标题重复：「模型演示与实验操作」已存在

## 整书结构指标

```
chapters: 6
total_chars: 10961
chapter_chars_mean: 1827
chapter_chars_median: 1809
chapter_chars_cv: 0.21
paragraphs_mean: 16.2
dialogue_chars_pct: 28.6
dialogue_para_pct: 52.4
interiority_para_pct: 7.5
narration_para_pct: 40.1
turn_under20_pct: 46.3
turn_over200_pct: 0.0
attr_say_pct: 12.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 4.1
turn_len_median: 30
```
