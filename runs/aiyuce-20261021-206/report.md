# 电闸 生成报告

slug：`aiyuce-20261021-206`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11500
LLM 调用：57 次，累计 225.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对显卡标价数据 | 2259 | normal | 97.1 | 0 |  | 0 |
| 2 | 核对电费单数据 | 2276 | normal | 91.4 | 0 |  | 0 |
| 3 | 核对折旧表数据 | 1746 | normal | 89.7 | 0 |  | 1 |
| 4 | 调整显卡标价策略 | 1939 | normal | 36.0 | 0 |  | 1 |
| 5 | 核对显卡标价数据 | 1987 | normal | 34.9 | 0 |  | 2 |
| 6 | 核对库存清单数据 | 1287 | short | 87.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - narration_para_pct 36.4 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 4 句（如「如果某天所有的显卡型号在同一时间点出现价格反弹，…」）
  - [observe] 标题重复：「核对显卡标价数据」已存在
- 第 6 章：
  - [observe] 标题与《核对电费单数据》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11236
chapter_chars_mean: 1873
chapter_chars_median: 1919
chapter_chars_cv: 0.19
paragraphs_mean: 13.7
dialogue_chars_pct: 5.1
dialogue_para_pct: 20.4
interiority_para_pct: 19.5
narration_para_pct: 60.0
turn_under20_pct: 47.7
turn_over200_pct: 0.0
attr_say_pct: 20.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.6
turn_len_median: 21
```
