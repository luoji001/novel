# 校对钟 生成报告

slug：`aiyuce-20261021-116`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11093
LLM 调用：57 次，累计 217.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 校对主管摩挲报价单 | 1835 | normal | 37.7 | 0 |  | 2 |
| 2 | 摩挲合同页边距 | 1894 | normal | 35.8 | 0 |  | 1 |
| 3 | 摩挲反馈表边缘 | 1939 | normal | 35.8 | 0 |  | 1 |
| 4 | 摩挲财务报表边缘 | 1981 | normal | 35.4 | 0 |  | 2 |
| 5 | 摩挲使用记录边缘 | 2042 | normal | 33.6 | 0 |  | 1 |
| 6 | 摩挲使用记录边缘 | 1396 | short | 33.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的事实推翻呢…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《摩挲反馈表边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「摩挲使用记录边缘」已存在

## 整书结构指标

```
chapters: 6
total_chars: 10832
chapter_chars_mean: 1805
chapter_chars_median: 1870
chapter_chars_cv: 0.13
paragraphs_mean: 13.3
dialogue_chars_pct: 3.0
dialogue_para_pct: 15.5
interiority_para_pct: 16.9
narration_para_pct: 67.6
turn_under20_pct: 73.0
turn_over200_pct: 0.0
attr_say_pct: 16.4
attr_adv_pct: 50.7
scenes_per_chapter: 1.3
dialogue_run_mean: 1.8
turn_len_median: 10
```
