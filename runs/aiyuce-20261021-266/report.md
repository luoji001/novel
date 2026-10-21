# 电表指针 生成报告

slug：`aiyuce-20261021-266`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13361
LLM 调用：57 次，累计 227.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲电费单 | 2305 | normal | 93.6 | 0 |  | 1 |
| 2 | 摩挲价格表 | 2509 | normal | 88.2 | 0 |  | 0 |
| 3 | 核对电费单 | 2208 | normal | 35.5 | 0 |  | 4 |
| 4 | 摩挲招聘JD | 2368 | normal | 91.4 | 0 |  | 0 |
| 5 | 摩挲招聘JD | 2321 | normal | 34.4 | 0 |  | 5 |
| 6 | 摩挲价格表 | 1644 | short | 87.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_run_mean 6 高于目标 4.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
  - narration_para_pct 41.2 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「如果某个意外事件使得所有竞争对手都暂时退出竞争圈…」）
  - [observe] 标题与《摩挲电费单》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「点了点头」×3
  - dialogue_chars_pct 29.3 高于目标 18.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「摩挲招聘JD」已存在
- 第 6 章：
  - interiority_para_pct 50.0 高于目标 40.0
  - narration_para_pct 30.0 低于目标 45.0
  - [observe] 标题重复：「摩挲价格表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 13055
chapter_chars_mean: 2176
chapter_chars_median: 2250
chapter_chars_cv: 0.14
paragraphs_mean: 17.8
dialogue_chars_pct: 9.5
dialogue_para_pct: 32.2
interiority_para_pct: 23.3
narration_para_pct: 44.5
turn_under20_pct: 70.9
turn_over200_pct: 0.0
attr_say_pct: 17.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.5
turn_len_median: 14
```
