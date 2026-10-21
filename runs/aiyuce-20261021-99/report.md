# 筛影 生成报告

slug：`aiyuce-20261021-99`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11139
LLM 调用：53 次，累计 203.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指轻敲桌面 | 2247 | normal | 94.2 | 0 |  | 0 |
| 2 | 手指轻敲桌面 | 2247 | normal | 89.0 | 0 |  | 3 |
| 3 | 手指划过数字 | 1869 | normal | 90.5 | 0 |  | 1 |
| 4 | 手指划过数字 | 2014 | normal | 90.2 | 0 |  | 2 |
| 5 | 手指轻敲桌面 | 1342 | normal | 89.4 | 0 |  | 1 |
| 6 | 手指轻敲键盘 | 1414 | short | 88.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - dialogue_chars_pct 27.5 高于目标 18.0
  - narration_para_pct 15.4 低于目标 45.0
  - [observe] 标题重复：「手指轻敲桌面」已存在
- 第 3 章：
  - narration_para_pct 26.7 低于目标 45.0
- 第 4 章：
  - narration_para_pct 35.7 低于目标 45.0
  - [observe] 标题重复：「手指划过数字」已存在
- 第 5 章：
  - [observe] 标题重复：「手指轻敲桌面」已存在
- 第 6 章：
  - dialogue_chars_pct 27.6 高于目标 18.0
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 标题与《手指轻敲桌面》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 10881
chapter_chars_mean: 1814
chapter_chars_median: 1898
chapter_chars_cv: 0.22
paragraphs_mean: 14
dialogue_chars_pct: 14.3
dialogue_para_pct: 44.2
interiority_para_pct: 18.5
narration_para_pct: 37.3
turn_under20_pct: 40.2
turn_over200_pct: 0.0
attr_say_pct: 20.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.8
turn_len_median: 20
```
