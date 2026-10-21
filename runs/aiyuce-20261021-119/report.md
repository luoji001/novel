# 服务器折旧表 生成报告

slug：`aiyuce-20261021-119`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11956
LLM 调用：57 次，累计 217.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 抚摸报价单 | 1783 | normal | 95.7 | 0 |  | 1 |
| 2 | 检查服务器性能测试报告 | 2499 | normal | 36.2 | 0 |  | 1 |
| 3 | 抚摸统计表 | 2228 | normal | 35.4 | 0 |  | 1 |
| 4 | 翻阅客户满意度调查表 | 1843 | normal | 23.9 | 0 |  | 1 |
| 5 | 敲击数据清单 | 2091 | normal | 34.7 | 0 |  | 3 |
| 6 | 翻阅报价单 | 1506 | short | 88.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 42.9 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的事实推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 50.2 高于目标 18.0
  - narration_para_pct 26.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 标题与《抚摸报价单》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11684
chapter_chars_mean: 1947
chapter_chars_median: 1916
chapter_chars_cv: 0.18
paragraphs_mean: 14.7
dialogue_chars_pct: 15.5
dialogue_para_pct: 37.9
interiority_para_pct: 14.8
narration_para_pct: 47.3
turn_under20_pct: 60.3
turn_over200_pct: 0.0
attr_say_pct: 14.2
attr_adv_pct: 8.1
scenes_per_chapter: 1.3
dialogue_run_mean: 2.0
turn_len_median: 16
```
