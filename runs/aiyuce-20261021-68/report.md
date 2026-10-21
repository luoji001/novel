# 校对钟 生成报告

slug：`aiyuce-20261021-68`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11407
LLM 调用：57 次，累计 215.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对报表的手指 | 1977 | normal | 94.1 | 0 |  | 1 |
| 2 | 校对表格上的数字 | 2005 | normal | 35.7 | 0 |  | 2 |
| 3 | 校对错误率的变化 | 2010 | normal | 35.4 | 0 |  | 1 |
| 4 | 手指划过合同条款 | 1954 | normal | 35.7 | 0 |  | 1 |
| 5 | 手机震动接收信息 | 2086 | normal | 37.0 | 0 |  | 2 |
| 6 | 手指划过校对表格 | 1369 | short | 35.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 26.3 低于目标 45.0
- 第 2 章：
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 60.9 高于目标 18.0
  - narration_para_pct 18.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）

## 整书结构指标

```
chapters: 6
total_chars: 11130
chapter_chars_mean: 1855
chapter_chars_median: 1940
chapter_chars_cv: 0.14
paragraphs_mean: 14.7
dialogue_chars_pct: 13.9
dialogue_para_pct: 41.8
interiority_para_pct: 18.5
narration_para_pct: 39.7
turn_under20_pct: 78.2
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.9
turn_len_median: 8
```
