# 成绩曲线 生成报告

slug：`aiyuce-20261021-144`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11951
LLM 调用：57 次，累计 220.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字的犹豫时刻 | 2039 | normal | 35.1 | 0 |  | 4 |
| 2 | 材料清单的核对 | 2161 | normal | 35.3 | 0 |  | 3 |
| 3 | 核对成绩统计表 | 2199 | normal | 37.0 | 0 |  | 1 |
| 4 | 工资发放明细的对比 | 2186 | normal | 35.8 | 0 |  | 2 |
| 5 | 核对成绩统计表 | 2085 | normal | 35.1 | 0 |  | 4 |
| 6 | 备课记录表的滑动指触 | 1275 | short | 84.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 38.3 高于目标 18.0
  - dialogue_run_mean 4.2 高于目标 4.0
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 章内自我复读 5 句（如「这时，张伟注意到了一个细节，那就是这份记录表中的…」）
- 第 2 章：
  - dialogue_chars_pct 28.4 高于目标 18.0
  - narration_para_pct 36.8 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「如果未来发现这些物料的成本远高于预期，则可能会影…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「不过他也清楚，要想彻底证明这一点，还需要更多的时…」）
- 第 5 章：
  - dialogue_chars_pct 20.8 高于目标 18.0
  - narration_para_pct 29.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对成绩统计表」已存在
- 第 6 章：
  - dialogue_chars_pct 36.8 高于目标 18.0
  - narration_para_pct 25.0 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11626
chapter_chars_mean: 1938
chapter_chars_median: 2072
chapter_chars_cv: 0.18
paragraphs_mean: 18.7
dialogue_chars_pct: 25.0
dialogue_para_pct: 52.0
interiority_para_pct: 12.0
narration_para_pct: 36.0
turn_under20_pct: 42.5
turn_over200_pct: 0.0
attr_say_pct: 18.3
attr_adv_pct: 6.1
scenes_per_chapter: 1.7
dialogue_run_mean: 2.7
turn_len_median: 25
```
