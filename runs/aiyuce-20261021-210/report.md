# 电价飙升 生成报告

slug：`aiyuce-20261021-210`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12155
LLM 调用：57 次，累计 229.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的红色标记 | 2015 | normal | 38.5 | 0 |  | 1 |
| 2 | 检查折旧表数据 | 2315 | normal | 36.2 | 0 |  | 1 |
| 3 | 核对服务器负载数据 | 2305 | normal | 35.4 | 0 |  | 3 |
| 4 | 核对报价单页边数据 | 2107 | normal | 35.7 | 0 |  | 1 |
| 5 | 敲击键盘 | 2183 | normal | 35.5 | 0 |  | 1 |
| 6 | 核对服务器负载数据 | 1224 | short | 89.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 27.2 高于目标 18.0
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「如果在接下来的一个月中没有任何显著的客户流失迹象…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 标题重复：「核对服务器负载数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11866
chapter_chars_mean: 1978
chapter_chars_median: 2098
chapter_chars_cv: 0.2
paragraphs_mean: 15.3
dialogue_chars_pct: 8.7
dialogue_para_pct: 35.1
interiority_para_pct: 9.0
narration_para_pct: 55.9
turn_under20_pct: 56.6
turn_over200_pct: 0.0
attr_say_pct: 3.8
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.7
turn_len_median: 12
```
