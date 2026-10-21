# 电表指针 生成报告

slug：`aiyuce-20261021-06`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11233
LLM 调用：57 次，累计 205.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对报价单 | 1878 | normal | 97.1 | 0 |  | 0 |
| 2 | 电费单的对比分析 | 2106 | normal | 36.1 | 0 |  | 1 |
| 3 | 核对折旧明细 | 2107 | normal | 91.5 | 0 |  | 0 |
| 4 | 核对电费单 | 2142 | normal | 35.5 | 0 |  | 2 |
| 5 | 核对报价单 | 1852 | normal | 90.0 | 0 |  | 2 |
| 6 | 核对电费单 | 1142 | short | 34.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《核对报价单》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 标题重复：「核对报价单」已存在
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对电费单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 10965
chapter_chars_mean: 1828
chapter_chars_median: 1940
chapter_chars_cv: 0.2
paragraphs_mean: 15
dialogue_chars_pct: 6.5
dialogue_para_pct: 20.0
interiority_para_pct: 11.8
narration_para_pct: 68.3
turn_under20_pct: 43.3
turn_over200_pct: 0.0
attr_say_pct: 4.7
attr_adv_pct: 4.7
scenes_per_chapter: 2
dialogue_run_mean: 1.4
turn_len_median: 18
```
