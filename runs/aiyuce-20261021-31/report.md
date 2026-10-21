# 审查笔记 生成报告

slug：`aiyuce-20261021-31`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12485
LLM 调用：57 次，累计 223.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 代码审查日报的溢出 | 2279 | normal | 37.4 | 0 |  | 1 |
| 2 | AI工具的演示 | 2384 | normal | 91.8 | 0 |  | 0 |
| 3 | 手册的页码翻动 | 2477 | normal | 87.8 | 0 |  | 2 |
| 4 | 键盘上的指令输入 | 1946 | normal | 89.2 | 0 |  | 1 |
| 5 | 代码审查日报的溢出 | 2181 | normal | 35.6 | 0 |  | 3 |
| 6 | 代码审查日报的溢出 | 1212 | short | 35.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 5 句（如「这些做法可能会带来意想不到的好处，比如减少重复劳…」）
- 第 3 章：
  - dialogue_chars_pct 20.6 高于目标 18.0
  - narration_para_pct 15.4 低于目标 45.0
- 第 4 章：
  - 命中套话收尾句
- 第 5 章：
  - 命中套话收尾句
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「代码审查日报的溢出」已存在
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「代码审查日报的溢出」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12210
chapter_chars_mean: 2035
chapter_chars_median: 2179
chapter_chars_cv: 0.23
paragraphs_mean: 14.3
dialogue_chars_pct: 6.4
dialogue_para_pct: 24.1
interiority_para_pct: 17.0
narration_para_pct: 58.9
turn_under20_pct: 48.7
turn_over200_pct: 0.0
attr_say_pct: 4.6
attr_adv_pct: 4.6
scenes_per_chapter: 1.2
dialogue_run_mean: 1.6
turn_len_median: 18
```
