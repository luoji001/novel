# 智影入场 生成报告

slug：`aiyuce-20261021-159`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11869
LLM 调用：57 次，累计 218.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对影像统计表 | 1977 | normal | 98.8 | 0 |  | 1 |
| 2 | 核对预算报表数据 | 2371 | normal | 37.4 | 0 |  | 2 |
| 3 | 核对AI报价单 | 2207 | normal | 36.9 | 0 |  | 1 |
| 4 | 设备维护记录更新 | 2033 | normal | 36.0 | 0 |  | 2 |
| 5 | 核对AI报价单 | 2044 | normal | 35.4 | 0 |  | 2 |
| 6 | 核对预算报表数据 | 1231 | short | 35.3 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 42.9 低于目标 45.0
- 第 2 章：
  - narration_para_pct 31.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - 单条套路句式超限：「智影科技的」×3
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 4 句（如「比如说，如果AI系统的误诊率高于现有的平均水平，…」）
  - [observe] 标题重复：「核对AI报价单」已存在
- 第 6 章：
  - 单条套路句式超限：「智影科技的」×3
  - dialogue_chars_pct 33.3 高于目标 18.0
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对预算报表数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11596
chapter_chars_mean: 1933
chapter_chars_median: 1993
chapter_chars_cv: 0.2
paragraphs_mean: 14.5
dialogue_chars_pct: 7.1
dialogue_para_pct: 31.1
interiority_para_pct: 15.5
narration_para_pct: 53.4
turn_under20_pct: 70.3
turn_over200_pct: 0.0
attr_say_pct: 5.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 1.8
turn_len_median: 16
```
