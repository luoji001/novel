# AI病历 生成报告

slug：`aiyuce-20261021-15`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11568
LLM 调用：57 次，累计 211.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 查看折旧表 | 1919 | normal | 37.4 | 0 |  | 1 |
| 2 | 手指划过预算报表 | 2178 | normal | 36.0 | 0 |  | 1 |
| 3 | 目光停留报价单 | 1998 | normal | 90.1 | 0 |  | 0 |
| 4 | 手指划过工作日志 | 2039 | normal | 35.6 | 0 |  | 1 |
| 5 | 目光停留招聘JD | 1924 | normal | 35.9 | 0 |  | 2 |
| 6 | 目光停留工作日志 | 1504 | short | 36.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的证据推翻呢…」）
- 第 5 章：
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 11322
chapter_chars_mean: 1887
chapter_chars_median: 1922
chapter_chars_cv: 0.12
paragraphs_mean: 12.3
dialogue_chars_pct: 2.6
dialogue_para_pct: 24.6
interiority_para_pct: 22.8
narration_para_pct: 52.6
turn_under20_pct: 84.6
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.6
turn_len_median: 6
```
