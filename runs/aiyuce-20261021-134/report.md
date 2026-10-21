# 电表转数 生成报告

slug：`aiyuce-20261021-134`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11766
LLM 调用：57 次，累计 213.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对交易记录表 | 2151 | normal | 59.8 | 0 |  | 0 |
| 2 | 核对电费单数据 | 2057 | normal | 23.8 | 0 |  | 1 |
| 3 | 核对利润计算表 | 1795 | normal | 90.3 | 0 |  | 1 |
| 4 | 核对库存清单数据 | 2190 | normal | 36.4 | 0 |  | 2 |
| 5 | 核对库存清单数据 | 2170 | normal | 35.5 | 0 |  | 3 |
| 6 | 核对显卡交易记录 | 1397 | short | 91.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 3 句（如「一条可能推翻这条推论的情况是，如果市场上出现了更…」）
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《核对电费单数据》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 38.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对库存清单数据」已存在
- 第 6 章：
  - narration_para_pct 36.4 低于目标 45.0
  - [observe] 标题与《核对交易记录表》近似 0.80 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11484
chapter_chars_mean: 1914
chapter_chars_median: 2060
chapter_chars_cv: 0.16
paragraphs_mean: 14.8
dialogue_chars_pct: 5.5
dialogue_para_pct: 20.8
interiority_para_pct: 23.8
narration_para_pct: 55.4
turn_under20_pct: 69.8
turn_over200_pct: 0.0
attr_say_pct: 11.4
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.7
turn_len_median: 18
```
