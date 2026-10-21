# 模型灯 生成报告

slug：`aiyuce-20261021-84`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11827
LLM 调用：57 次，累计 218.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 统计数据对比图 | 1837 | normal | 36.7 | 0 |  | 4 |
| 2 | 核对电费单 | 2135 | normal | 36.4 | 0 |  | 1 |
| 3 | 核对电费单 | 1947 | normal | 82.8 | 0 |  | 4 |
| 4 | 核对招聘JD | 2736 | normal | 35.5 | 0 |  | 1 |
| 5 | 核对电费单 | 1925 | normal | 32.6 | 0 |  | 5 |
| 6 | 核对成绩统计表 | 1241 | short | 88.7 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 46.3 高于目标 18.0
  - dialogue_run_mean 4.8 高于目标 4.0
  - narration_para_pct 29.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 53.3 高于目标 18.0
  - dialogue_run_mean 11.5 高于目标 4.0
  - narration_para_pct 7.7 低于目标 45.0
  - [observe] 标题重复：「核对电费单」已存在
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 39.4 高于目标 18.0
  - dialogue_run_mean 6 高于目标 4.0
  - narration_para_pct 13.3 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「如果最终的考试成绩仍然保持原来的分布模式，那么所…」）
  - [observe] 标题重复：「核对电费单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11528
chapter_chars_mean: 1921
chapter_chars_median: 1882
chapter_chars_cv: 0.25
paragraphs_mean: 17.5
dialogue_chars_pct: 24.1
dialogue_para_pct: 48.2
interiority_para_pct: 17.0
narration_para_pct: 34.7
turn_under20_pct: 52.1
turn_over200_pct: 0.0
attr_say_pct: 25.6
attr_adv_pct: 1.8
scenes_per_chapter: 1.5
dialogue_run_mean: 4.3
turn_len_median: 22
```
