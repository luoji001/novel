# 校对钟 生成报告

slug：`aiyuce-20261021-44`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11929
LLM 调用：57 次，累计 216.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铅笔痕迹下的价格分歧 | 1856 | normal | 95.5 | 0 |  | 1 |
| 2 | 折叠的报价单 | 2519 | normal | 34.0 | 0 |  | 3 |
| 3 | 手指摩挲文件夹边缘 | 1879 | normal | 33.1 | 0 |  | 3 |
| 4 | 手指摩挲文件夹边缘 | 2072 | normal | 88.1 | 0 |  | 3 |
| 5 | 手指摩挲文件边缘 | 2080 | normal | 79.4 | 0 |  | 4 |
| 6 | 手指摩挲文件边缘 | 1517 | short | 84.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现。

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 41.7 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 33.8 高于目标 18.0
  - narration_para_pct 40.9 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「假如经过一个月的实际应用之后，发现员工的整体工作…」）
- 第 3 章：
  - dialogue_chars_pct 39.2 高于目标 18.0
  - narration_para_pct 30.0 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「如果后续数据显示客户的错误率并没有进一步降低，那…」）
- 第 4 章：
  - dialogue_chars_pct 21.1 高于目标 18.0
  - narration_para_pct 43.8 低于目标 45.0
  - [observe] 标题重复：「手指摩挲文件夹边缘」已存在
- 第 5 章：
  - dialogue_chars_pct 38.0 高于目标 18.0
  - dialogue_run_mean 6 高于目标 4.0
  - narration_para_pct 38.1 低于目标 45.0
  - [observe] 标题与《手指摩挲文件夹边缘》近似 0.94 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 27.2 高于目标 18.0
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 标题重复：「手指摩挲文件边缘」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11617
chapter_chars_mean: 1936
chapter_chars_median: 1922
chapter_chars_cv: 0.17
paragraphs_mean: 17.3
dialogue_chars_pct: 28.5
dialogue_para_pct: 57.5
interiority_para_pct: 3.4
narration_para_pct: 39.0
turn_under20_pct: 40.0
turn_over200_pct: 0.0
attr_say_pct: 16.3
attr_adv_pct: 3.2
scenes_per_chapter: 1.5
dialogue_run_mean: 2.8
turn_len_median: 26
```
