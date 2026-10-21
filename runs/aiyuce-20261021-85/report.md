# 笔锋 生成报告

slug：`aiyuce-20261021-85`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11711
LLM 调用：57 次，累计 209.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的数字 | 1775 | normal | 96.0 | 0 |  | 1 |
| 2 | 摩挲招聘JD复印件 | 2325 | normal | 95.7 | 0 |  | 1 |
| 3 | 摩挲报价单边缘 | 2261 | normal | 88.9 | 0 |  | 1 |
| 4 | 摩挲折旧表边缘 | 1911 | normal | 36.2 | 0 |  | 2 |
| 5 | 摩挲报价单边缘 | 2032 | normal | 36.8 | 0 |  | 3 |
| 6 | 摩挲电费单边缘 | 1401 | short | 90.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 40.0 低于目标 45.0
- 第 2 章：
  - narration_para_pct 16.7 低于目标 45.0
- 第 3 章：
  - narration_para_pct 33.3 低于目标 45.0
- 第 4 章：
  - narration_para_pct 31.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 26.7 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「你们是不是用了什么特殊的算法？会不会有什么隐藏的…」）
  - [observe] 标题重复：「摩挲报价单边缘」已存在
- 第 6 章：
  - narration_para_pct 21.4 低于目标 45.0
  - [observe] 标题与《摩挲报价单边缘》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11427
chapter_chars_mean: 1904
chapter_chars_median: 1926
chapter_chars_cv: 0.18
paragraphs_mean: 15.5
dialogue_chars_pct: 10.3
dialogue_para_pct: 46.2
interiority_para_pct: 25.7
narration_para_pct: 28.1
turn_under20_pct: 70.8
turn_over200_pct: 0.0
attr_say_pct: 12.5
attr_adv_pct: 0.0
scenes_per_chapter: 2.3
dialogue_run_mean: 1.8
turn_len_median: 10
```
