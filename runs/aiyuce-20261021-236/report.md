# 校对小时 生成报告

slug：`aiyuce-20261021-236`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11298
LLM 调用：57 次，累计 208.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的电量增幅 | 2073 | normal | 39.0 | 0 |  | 3 |
| 2 | 翻看七月的报价单 | 1919 | normal | 36.1 | 0 |  | 2 |
| 3 | 查看招聘JD | 2031 | normal | 92.0 | 0 |  | 1 |
| 4 | 核对客户反馈报告 | 2076 | normal | 88.0 | 0 |  | 0 |
| 5 | 核对折旧表数据 | 2120 | normal | 35.4 | 0 |  | 3 |
| 6 | 翻看报价单边缘 | 1073 | short | 81.5 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - narration_para_pct 31.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 36.4 低于目标 45.0
- 第 5 章：
  - dialogue_chars_pct 33.6 高于目标 18.0
  - narration_para_pct 22.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 69.4 高于目标 18.0
  - dialogue_run_mean 11 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题与《翻看七月的报价单》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 10993
chapter_chars_mean: 1832
chapter_chars_median: 1998
chapter_chars_cv: 0.22
paragraphs_mean: 17.2
dialogue_chars_pct: 18.2
dialogue_para_pct: 45.1
interiority_para_pct: 15.5
narration_para_pct: 39.4
turn_under20_pct: 59.6
turn_over200_pct: 0.0
attr_say_pct: 13.3
attr_adv_pct: 7.8
scenes_per_chapter: 1.2
dialogue_run_mean: 3.6
turn_len_median: 16
```
