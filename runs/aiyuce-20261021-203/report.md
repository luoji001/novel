# 页码之争 生成报告

slug：`aiyuce-20261021-203`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11937
LLM 调用：57 次，累计 231.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 文件上的数字 | 2319 | normal | 96.2 | 0 |  | 0 |
| 2 | 文件上的数字 | 2212 | normal | 90.1 | 0 |  | 3 |
| 3 | 翻阅财务报表 | 1847 | normal | 33.5 | 0 |  | 4 |
| 4 | 翻阅误判报告 | 2306 | normal | 34.0 | 0 |  | 3 |
| 5 | 红色警告框 | 1865 | normal | 90.1 | 0 |  | 0 |
| 6 | 敲击报告 | 1382 | short | 33.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - dialogue_chars_pct 27.8 高于目标 18.0
  - narration_para_pct 29.6 低于目标 45.0
  - [observe] 标题重复：「文件上的数字」已存在
- 第 3 章：
  - dialogue_chars_pct 58.5 高于目标 18.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - narration_para_pct 9.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「比如说，当某个重要判决依据仅仅依靠一页纸就可以决…」）
- 第 4 章：
  - dialogue_chars_pct 52.1 高于目标 18.0
  - narration_para_pct 20.5 低于目标 45.0
  - [observe] 章内自我复读 4 句（如「我知道这个问题很重要，所以我正在努力改进模型…」）
- 第 6 章：
  - dialogue_chars_pct 46.4 高于目标 18.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 11580
chapter_chars_mean: 1930
chapter_chars_median: 1984
chapter_chars_cv: 0.18
paragraphs_mean: 21.7
dialogue_chars_pct: 31.6
dialogue_para_pct: 58.3
interiority_para_pct: 10.2
narration_para_pct: 31.5
turn_under20_pct: 34.1
turn_over200_pct: 0.0
attr_say_pct: 12.7
attr_adv_pct: 2.7
scenes_per_chapter: 1
dialogue_run_mean: 2.8
turn_len_median: 25
```
