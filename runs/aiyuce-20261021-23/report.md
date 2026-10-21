# 页码 生成报告

slug：`aiyuce-20261021-23`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12204
LLM 调用：57 次，累计 224.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指划过预算表边缘 | 2291 | normal | 84.4 | 0 |  | 3 |
| 2 | 手指划过方案边缘 | 2146 | normal | 80.0 | 0 |  | 4 |
| 3 | 手指划过合同边缘 | 2218 | normal | 78.4 | 0 |  | 4 |
| 4 | 指节敲击桌面 | 2238 | normal | 79.0 | 0 |  | 3 |
| 5 | 手指划过方案边缘 | 2038 | normal | 83.0 | 0 |  | 4 |
| 6 | 手指划过合同边缘 | 1267 | short | 80.8 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 59.6 高于目标 18.0
  - dialogue_run_mean 10.5 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 61.2 高于目标 18.0
  - dialogue_run_mean 20 高于目标 4.0
  - narration_para_pct 8.7 低于目标 45.0
  - [observe] 标题与《手指划过预算表边缘》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - dialogue_chars_pct 59.0 高于目标 18.0
  - dialogue_run_mean 9 高于目标 4.0
  - narration_para_pct 3.4 低于目标 45.0
  - [observe] 标题与《手指划过方案边缘》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - dialogue_chars_pct 81.1 高于目标 18.0
  - dialogue_run_mean 27 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
- 第 5 章：
  - dialogue_chars_pct 45.8 高于目标 18.0
  - dialogue_run_mean 5.3 高于目标 4.0
  - narration_para_pct 27.3 低于目标 45.0
  - [observe] 标题重复：「手指划过方案边缘」已存在
- 第 6 章：
  - dialogue_chars_pct 68.5 高于目标 18.0
  - dialogue_run_mean 14 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题重复：「手指划过合同边缘」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11825
chapter_chars_mean: 1971
chapter_chars_median: 2114
chapter_chars_cv: 0.19
paragraphs_mean: 23.2
dialogue_chars_pct: 62.3
dialogue_para_pct: 89.6
interiority_para_pct: 3.7
narration_para_pct: 6.7
turn_under20_pct: 28.7
turn_over200_pct: 0.0
attr_say_pct: 14.2
attr_adv_pct: 0.8
scenes_per_chapter: 1.3
dialogue_run_mean: 14.3
turn_len_median: 32
```
