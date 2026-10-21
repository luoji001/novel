# 审查表 生成报告

slug：`aiyuce-20261021-79`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11771
LLM 调用：57 次，累计 218.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 代码审查任务分配表 | 2287 | normal | 37.5 | 0 |  | 1 |
| 2 | 代码审查工具采购预算 | 2218 | normal | 35.3 | 0 |  | 1 |
| 3 | 代码审查任务分配表 | 1896 | normal | 87.5 | 0 |  | 1 |
| 4 | 代码审查工具使用报告 | 2081 | normal | 91.5 | 0 |  | 1 |
| 5 | 代码审查工具使用报告 | 1898 | normal | 91.2 | 0 |  | 1 |
| 6 | 代码审查工具使用报告 | 1385 | short | 33.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 2 句（如「具备至少半年的代码审查经验…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 标题重复：「代码审查任务分配表」已存在
- 第 4 章：
  - [observe] 标题与《代码审查工具采购预算》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 标题重复：「代码审查工具使用报告」已存在
- 第 6 章：
  - dialogue_chars_pct 30.3 高于目标 18.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「代码审查工具使用报告」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11503
chapter_chars_mean: 1917
chapter_chars_median: 1948
chapter_chars_cv: 0.17
paragraphs_mean: 13
dialogue_chars_pct: 7.9
dialogue_para_pct: 26.5
interiority_para_pct: 15.6
narration_para_pct: 57.9
turn_under20_pct: 57.6
turn_over200_pct: 0.0
attr_say_pct: 16.9
attr_adv_pct: 59.8
scenes_per_chapter: 1.3
dialogue_run_mean: 1.9
turn_len_median: 14
```
