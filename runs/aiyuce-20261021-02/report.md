# 显卡账本 生成报告

slug：`aiyuce-20261021-02`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12483
LLM 调用：57 次，累计 292.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对显卡销售清单 | 2034 | normal | 37.7 | 0 |  | 1 |
| 2 | 核对显卡销售清单 | 2205 | normal | 89.7 | 0 |  | 1 |
| 3 | 核对租金发票数据 | 2137 | normal | 35.4 | 0 |  | 1 |
| 4 | 核对显卡销售清单 | 2216 | normal | 89.9 | 0 |  | 2 |
| 5 | 核对显卡销售清单 | 2513 | normal | 35.4 | 0 |  | 3 |
| 6 | 核对显卡销售清单 | 1372 | short | 87.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 标题重复：「核对显卡销售清单」已存在
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 4 章：
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 标题重复：「核对显卡销售清单」已存在
- 第 5 章：
  - narration_para_pct 35.7 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「当实际发生的订单数量低于预期水平时，即可证明此前…」）
  - [observe] 标题重复：「核对显卡销售清单」已存在
- 第 6 章：
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 标题重复：「核对显卡销售清单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12225
chapter_chars_mean: 2038
chapter_chars_median: 2126
chapter_chars_cv: 0.19
paragraphs_mean: 13
dialogue_chars_pct: 3.6
dialogue_para_pct: 27.2
interiority_para_pct: 27.0
narration_para_pct: 45.8
turn_under20_pct: 78.3
turn_over200_pct: 0.0
attr_say_pct: 7.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.3
turn_len_median: 10
```
