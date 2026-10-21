# 模型教学法 生成报告

slug：`aiyuce-20261021-216`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11534
LLM 调用：57 次，累计 208.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲成绩统计表 | 2461 | normal | 38.0 | 0 |  | 2 |
| 2 | 核对报销凭证 | 2369 | normal | 35.8 | 0 |  | 2 |
| 3 | 核对报销凭证 | 1749 | normal | 89.6 | 0 |  | 1 |
| 4 | 核对报销凭证 | 1942 | normal | 34.6 | 0 |  | 2 |
| 5 | 核对评分表数据 | 1929 | normal | 35.6 | 0 |  | 1 |
| 6 | 核对评分表数据 | 1078 | short | 35.6 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 38.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 标题重复：「核对报销凭证」已存在
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对报销凭证」已存在
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - interiority_para_pct 50.0 高于目标 40.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对评分表数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11275
chapter_chars_mean: 1879
chapter_chars_median: 1892
chapter_chars_cv: 0.26
paragraphs_mean: 13.8
dialogue_chars_pct: 6.6
dialogue_para_pct: 27.3
interiority_para_pct: 27.9
narration_para_pct: 44.8
turn_under20_pct: 72.6
turn_over200_pct: 0.0
attr_say_pct: 24.0
attr_adv_pct: 12.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.4
turn_len_median: 12
```
