# 合规账单 生成报告

slug：`aiyuce-20261021-102`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12839
LLM 调用：57 次，累计 221.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 报价单上的三个数字 | 1983 | normal | 96.3 | 0 |  | 1 |
| 2 | 合规费用明细表 | 2171 | normal | 34.8 | 0 |  | 3 |
| 3 | 市场调研报告 | 2435 | normal | 36.1 | 0 |  | 1 |
| 4 | 核对报价单 | 2429 | normal | 35.5 | 0 |  | 3 |
| 5 | 核对报价单 | 2338 | normal | 35.8 | 0 |  | 2 |
| 6 | 核对合规费用明细表 | 1477 | short | 88.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 23.5 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 51.4 高于目标 18.0
  - narration_para_pct 16.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - 单条套路句式超限：「变得更加」×3
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的证据推翻呢…」）
  - [observe] 标题重复：「核对报价单」已存在
- 第 6 章：
  - [observe] 标题与《合规费用明细表》近似 0.88 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 12564
chapter_chars_mean: 2094
chapter_chars_median: 2206
chapter_chars_cv: 0.17
paragraphs_mean: 15
dialogue_chars_pct: 14.1
dialogue_para_pct: 37.1
interiority_para_pct: 18.0
narration_para_pct: 44.9
turn_under20_pct: 56.6
turn_over200_pct: 0.0
attr_say_pct: 18.9
attr_adv_pct: 2.1
scenes_per_chapter: 1.5
dialogue_run_mean: 2.1
turn_len_median: 18
```
