# 质检灯 生成报告

slug：`aiyuce-20261021-17`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12799
LLM 调用：57 次，累计 222.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 分析质检报表 | 2077 | normal | 37.2 | 0 |  | 2 |
| 2 | 核对投诉统计表 | 2735 | normal | 35.8 | 0 |  | 1 |
| 3 | 核对坐席名单 | 2112 | normal | 36.3 | 0 |  | 2 |
| 4 | 翻阅质检岗招聘JD | 2201 | normal | 89.7 | 0 |  | 1 |
| 5 | 测试报告数据滑动 | 2195 | normal | 36.4 | 0 |  | 2 |
| 6 | 核对误差率数据 | 1473 | short | 90.1 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 42.1 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 41.2 低于目标 45.0
- 第 5 章：
  - narration_para_pct 41.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）

## 整书结构指标

```
chapters: 6
total_chars: 12512
chapter_chars_mean: 2085
chapter_chars_median: 2102
chapter_chars_cv: 0.19
paragraphs_mean: 15.8
dialogue_chars_pct: 10.3
dialogue_para_pct: 40.9
interiority_para_pct: 13.5
narration_para_pct: 45.7
turn_under20_pct: 70.4
turn_over200_pct: 0.0
attr_say_pct: 4.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.9
turn_len_median: 15
```
