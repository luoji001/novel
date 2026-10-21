# 听课笔记 生成报告

slug：`aiyuce-20261021-141`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11026
LLM 调用：53 次，累计 203.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 计算器与标签的对峙 | 1920 | normal | 37.0 | 0 |  | 4 |
| 2 | 听课记录本使用统计表 | 2684 | normal | 35.6 | 0 |  | 1 |
| 3 | 听课记录本使用统计表 | 1204 | normal | 89.5 | 0 |  | 1 |
| 4 | 听课记录本使用统计表 | 2086 | normal | 35.5 | 0 |  | 3 |
| 5 | 翻开听课记录本 | 1930 | normal | 89.2 | 0 |  | 2 |
| 6 | 翻开听课记录本 | 1196 | short | 35.4 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 43.4 高于目标 18.0
  - dialogue_run_mean 4.3 高于目标 4.0
  - narration_para_pct 35.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被哪些具体的证据反驳吗…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 标题重复：「听课记录本使用统计表」已存在
- 第 4 章：
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「听课记录本使用统计表」已存在
- 第 5 章：
  - dialogue_chars_pct 21.6 高于目标 18.0
  - narration_para_pct 40.9 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 20.7 高于目标 18.0
  - dialogue_run_mean 5 高于目标 4.0
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「翻开听课记录本」已存在

## 整书结构指标

```
chapters: 6
total_chars: 10733
chapter_chars_mean: 1789
chapter_chars_median: 1868
chapter_chars_cv: 0.31
paragraphs_mean: 15.2
dialogue_chars_pct: 19.0
dialogue_para_pct: 41.8
interiority_para_pct: 14.1
narration_para_pct: 44.1
turn_under20_pct: 46.7
turn_over200_pct: 0.0
attr_say_pct: 30.4
attr_adv_pct: 2.4
scenes_per_chapter: 1.7
dialogue_run_mean: 2.8
turn_len_median: 31
```
