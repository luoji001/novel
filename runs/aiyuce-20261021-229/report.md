# 代写员 生成报告

slug：`aiyuce-20261021-229`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11528
LLM 调用：57 次，累计 209.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的1800度 | 1948 | normal | 96.9 | 0 |  | 1 |
| 2 | 盯着电费单上的数字 | 2330 | normal | 36.1 | 0 |  | 2 |
| 3 | 盯住老式打印机 | 2488 | normal | 88.2 | 0 |  | 0 |
| 4 | 盯着折旧表上的数字 | 1642 | normal | 57.9 | 0 |  | 1 |
| 5 | 裁开申请表一角 | 1834 | normal | 92.0 | 0 |  | 1 |
| 6 | 盯住老式打印机 | 1280 | short | 90.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 31.2 低于目标 45.0
- 第 2 章：
  - narration_para_pct 31.2 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「如果客户普遍拒绝接受代写服务，或者竞争对手迅速采…」）
- 第 4 章：
  - [observe] 标题与《盯着电费单上的数字》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 14.3 低于目标 45.0
- 第 6 章：
  - [observe] 标题重复：「盯住老式打印机」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11265
chapter_chars_mean: 1878
chapter_chars_median: 1844
chapter_chars_cv: 0.23
paragraphs_mean: 13.3
dialogue_chars_pct: 8.0
dialogue_para_pct: 34.8
interiority_para_pct: 25.8
narration_para_pct: 39.4
turn_under20_pct: 64.8
turn_over200_pct: 0.0
attr_say_pct: 21.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.8
turn_len_median: 12
```
