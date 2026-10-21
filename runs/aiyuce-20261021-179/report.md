# 索引 生成报告

slug：`aiyuce-20261021-179`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12397
LLM 调用：57 次，累计 223.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对账目 | 1975 | normal | 94.5 | 0 |  | 1 |
| 2 | 核对账目 | 2396 | normal | 36.0 | 0 |  | 4 |
| 3 | 核对错误案例 | 1995 | normal | 36.0 | 0 |  | 2 |
| 4 | 核对问卷 | 2308 | normal | 35.0 | 0 |  | 2 |
| 5 | 核对合伙人表格 | 2359 | normal | 36.4 | 0 |  | 1 |
| 6 | 核对合伙人表格 | 1358 | short | 90.0 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 33.3 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 20.1 高于目标 18.0
  - narration_para_pct 38.9 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「这条推论会被什么样的数据驳斥呢…」）
  - [observe] 标题重复：「核对账目」已存在
- 第 3 章：
  - narration_para_pct 43.8 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「如果有足够的数据显示错误率显著下降，并且客户反馈…」）
- 第 4 章：
  - 命中套话收尾句
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么数据反驳吗…」）
- 第 6 章：
  - [observe] 标题重复：「核对合伙人表格」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12135
chapter_chars_mean: 2022
chapter_chars_median: 2104
chapter_chars_cv: 0.19
paragraphs_mean: 14.7
dialogue_chars_pct: 8.4
dialogue_para_pct: 32.7
interiority_para_pct: 13.0
narration_para_pct: 54.4
turn_under20_pct: 66.2
turn_over200_pct: 0.0
attr_say_pct: 8.3
attr_adv_pct: 7.6
scenes_per_chapter: 1.5
dialogue_run_mean: 1.2
turn_len_median: 14
```
