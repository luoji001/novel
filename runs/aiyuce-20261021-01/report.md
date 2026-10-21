# 纸钱 生成报告

slug：`aiyuce-20261021-01`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12020
LLM 调用：57 次，累计 275.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 计算器上的数字 | 2110 | normal | 89.5 | 0 |  | 3 |
| 2 | 报价单上的单价 | 2379 | normal | 88.1 | 0 |  | 2 |
| 3 | 客户群体统计表 | 2154 | normal | 89.4 | 0 |  | 0 |
| 4 | 计算器上的数字 | 1949 | normal | 35.7 | 0 |  | 2 |
| 5 | 维修费明细 | 2166 | normal | 35.7 | 0 |  | 2 |
| 6 | 报表上的数字 | 1256 | short | 36.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 34.6 高于目标 18.0
  - dialogue_run_mean 5.2 高于目标 4.0
  - narration_para_pct 18.5 低于目标 45.0
- 第 2 章：
  - interiority_para_pct 52.9 高于目标 40.0
  - narration_para_pct 23.5 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「如果最终证明这套设备的确提高了工作效率并带动了额…」）
  - [observe] 标题重复：「计算器上的数字」已存在
- 第 5 章：
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《计算器上的数字》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11729
chapter_chars_mean: 1955
chapter_chars_median: 2076
chapter_chars_cv: 0.2
paragraphs_mean: 16.3
dialogue_chars_pct: 7.8
dialogue_para_pct: 33.4
interiority_para_pct: 28.8
narration_para_pct: 37.8
turn_under20_pct: 82.0
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 2.0
turn_len_median: 4
```
