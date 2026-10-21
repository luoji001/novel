# 数据镜 生成报告

slug：`aiyuce-20261021-65`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11878
LLM 调用：57 次，累计 217.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对名单 | 2037 | normal | 95.0 | 0 |  | 1 |
| 2 | 查看投诉记录表 | 2470 | normal | 37.2 | 0 |  | 2 |
| 3 | 核对投诉记录表 | 2346 | normal | 35.2 | 0 |  | 2 |
| 4 | 查看测试报告 | 1761 | normal | 90.2 | 0 |  | 1 |
| 5 | 检查投诉数据变化 | 2048 | normal | 35.7 | 0 |  | 1 |
| 6 | 翻阅预算分配表 | 1210 | short | 82.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 21.7 低于目标 45.0
- 第 2 章：
  - narration_para_pct 43.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《查看投诉记录表》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - narration_para_pct 28.6 低于目标 45.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 48.6 高于目标 18.0
  - narration_para_pct 20.0 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11601
chapter_chars_mean: 1934
chapter_chars_median: 1990
chapter_chars_cv: 0.23
paragraphs_mean: 15.3
dialogue_chars_pct: 12.7
dialogue_para_pct: 40.8
interiority_para_pct: 15.4
narration_para_pct: 43.8
turn_under20_pct: 63.1
turn_over200_pct: 0.0
attr_say_pct: 5.3
attr_adv_pct: 9.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.1
turn_len_median: 17
```
