# 成本表 生成报告

slug：`aiyuce-20261021-41`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11669
LLM 调用：57 次，累计 223.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对质检成本明细表 | 2157 | normal | 37.6 | 0 |  | 1 |
| 2 | 核对质检成本明细表 | 1955 | normal | 34.9 | 0 |  | 3 |
| 3 | 核对质检成本明细表 | 2179 | normal | 88.9 | 0 |  | 1 |
| 4 | 翻看误判率数据 | 1947 | normal | 87.5 | 0 |  | 1 |
| 5 | 翻看考勤记录 | 2223 | normal | 34.5 | 0 |  | 1 |
| 6 | 翻看质检成本明细表 | 1202 | short | 35.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 30.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对质检成本明细表」已存在
- 第 3 章：
  - [observe] 标题重复：「核对质检成本明细表」已存在
- 第 4 章：
  - narration_para_pct 41.2 低于目标 45.0
- 第 5 章：
  - [observe] 章内自我复读 3 句（如「如果有新的数据显示，公司在2023年内并未有意缩…」）
- 第 6 章：
  - dialogue_chars_pct 19.1 高于目标 18.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《核对质检成本明细表》近似 0.78 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11406
chapter_chars_mean: 1901
chapter_chars_median: 2011
chapter_chars_cv: 0.2
paragraphs_mean: 13.3
dialogue_chars_pct: 5.4
dialogue_para_pct: 27.8
interiority_para_pct: 20.2
narration_para_pct: 52.0
turn_under20_pct: 78.1
turn_over200_pct: 0.0
attr_say_pct: 15.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.5
turn_len_median: 8
```
