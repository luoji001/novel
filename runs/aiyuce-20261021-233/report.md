# 铜铃 生成报告

slug：`aiyuce-20261021-233`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12291
LLM 调用：57 次，累计 224.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 查看质检评分数据 | 2008 | normal | 96.0 | 0 |  | 0 |
| 2 | 审视招聘JD细节 | 2625 | normal | 36.0 | 0 |  | 1 |
| 3 | 测试报告异常波动 | 1927 | normal | 33.8 | 0 |  | 1 |
| 4 | 查看质检评分数据 | 1988 | normal | 36.0 | 0 |  | 2 |
| 5 | 查看折旧表 | 2402 | normal | 33.9 | 0 |  | 1 |
| 6 | 查看质检评分数据 | 1335 | short | 33.1 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被实际发生的运维费用增长所推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「查看质检评分数据」已存在
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 64.0 高于目标 18.0
  - dialogue_run_mean 6.7 高于目标 4.0
  - narration_para_pct 9.1 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「查看质检评分数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11958
chapter_chars_mean: 1993
chapter_chars_median: 1950
chapter_chars_cv: 0.23
paragraphs_mean: 17.2
dialogue_chars_pct: 8.7
dialogue_para_pct: 16.7
interiority_para_pct: 10.1
narration_para_pct: 73.2
turn_under20_pct: 57.3
turn_over200_pct: 0.0
attr_say_pct: 13.0
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 3.0
turn_len_median: 21
```
