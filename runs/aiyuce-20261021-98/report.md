# 显卡库存 生成报告

slug：`aiyuce-20261021-98`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12052
LLM 调用：57 次，累计 228.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 调整显卡陈列位置 | 2260 | normal | 38.4 | 0 |  | 1 |
| 2 | 核对电费单 | 2173 | normal | 36.4 | 0 |  | 2 |
| 3 | 核对显卡成交金额 | 2237 | normal | 23.2 | 0 |  | 1 |
| 4 | 调价显卡库存 | 1869 | normal | 89.1 | 0 |  | 0 |
| 5 | 核对显卡折旧表 | 2052 | normal | 35.3 | 0 |  | 1 |
| 6 | 核对显卡折旧表 | 1455 | short | 86.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 41.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_run_mean 5 高于目标 4.0
  - narration_para_pct 30.0 低于目标 45.0
  - [observe] 标题重复：「核对显卡折旧表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11785
chapter_chars_mean: 1964
chapter_chars_median: 2066
chapter_chars_cv: 0.15
paragraphs_mean: 14.3
dialogue_chars_pct: 4.8
dialogue_para_pct: 23.3
interiority_para_pct: 22.9
narration_para_pct: 53.8
turn_under20_pct: 79.2
turn_over200_pct: 0.0
attr_say_pct: 15.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.9
turn_len_median: 14
```
