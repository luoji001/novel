# 合同审查量 生成报告

slug：`aiyuce-20261021-71`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11823
LLM 调用：57 次，累计 214.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 合同审查工作量统计表 | 2189 | normal | 37.8 | 0 |  | 1 |
| 2 | 合同审查量统计表 | 2398 | normal | 34.2 | 0 |  | 2 |
| 3 | 审阅报告的手指动作 | 1948 | normal | 89.6 | 0 |  | 1 |
| 4 | 手指滑动合同审查报告 | 1903 | normal | 82.6 | 0 |  | 3 |
| 5 | 翻阅财务报表 | 1952 | normal | 33.5 | 0 |  | 3 |
| 6 | 手指圈住准确率数字 | 1427 | short | 78.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《合同审查工作量统计表》近似 0.89 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - narration_para_pct 41.7 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 56.2 高于目标 18.0
  - dialogue_run_mean 5.7 高于目标 4.0
  - narration_para_pct 9.5 低于目标 45.0
- 第 5 章：
  - dialogue_chars_pct 56.2 高于目标 18.0
  - narration_para_pct 26.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 72.9 高于目标 18.0
  - dialogue_run_mean 12 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11539
chapter_chars_mean: 1923
chapter_chars_median: 1908
chapter_chars_cv: 0.17
paragraphs_mean: 14.8
dialogue_chars_pct: 27.4
dialogue_para_pct: 43.9
interiority_para_pct: 9.7
narration_para_pct: 46.4
turn_under20_pct: 52.9
turn_over200_pct: 0.0
attr_say_pct: 20.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 4.4
turn_len_median: 42
```
