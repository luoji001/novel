# 铜铃 生成报告

slug：`aiyuce-20261021-66`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11736
LLM 调用：57 次，累计 215.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对协议副本条款 | 1870 | normal | 94.7 | 0 |  | 0 |
| 2 | 核对协议副本条款 | 2325 | normal | 35.9 | 0 |  | 4 |
| 3 | 核对成本分析表 | 2269 | normal | 34.5 | 0 |  | 1 |
| 4 | 核对成本分析表 | 2101 | normal | 34.6 | 0 |  | 2 |
| 5 | 发送法律咨询函 | 1896 | normal | 36.0 | 0 |  | 1 |
| 6 | 核对成本分析表 | 1269 | short | 35.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「不仅仅是」×3
  - narration_para_pct 44.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对协议副本条款」已存在
- 第 3 章：
  - [observe] 章内自我复读 4 句（如「如果有权威性的审计报告能够证明该公司确实是在某个…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
  - [observe] 标题重复：「核对成本分析表」已存在
- 第 5 章：
  - [observe] 章内自我复读 4 句（如「如果这家律所最终认定第7条不具备足够的法律基础，…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对成本分析表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11472
chapter_chars_mean: 1912
chapter_chars_median: 1956
chapter_chars_cv: 0.2
paragraphs_mean: 13.8
dialogue_chars_pct: 3.1
dialogue_para_pct: 21.6
interiority_para_pct: 18.1
narration_para_pct: 60.4
turn_under20_pct: 95.0
turn_over200_pct: 0.0
attr_say_pct: 26.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.6
turn_len_median: 13
```
