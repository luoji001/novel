# 标尺 生成报告

slug：`aiyuce-20261021-221`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12006
LLM 调用：57 次，累计 220.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指摩挲纸边 | 2025 | normal | 38.2 | 0 |  | 2 |
| 2 | 摩挲考核表边缘 | 2253 | normal | 35.6 | 0 |  | 1 |
| 3 | 屏幕上的数字 | 2118 | normal | 83.4 | 0 |  | 2 |
| 4 | 摩挲财务报表边缘 | 1990 | normal | 82.7 | 0 |  | 4 |
| 5 | 摩挲日志边缘 | 2181 | normal | 88.4 | 0 |  | 2 |
| 6 | 摩挲测试报告边缘 | 1433 | short | 32.3 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 43.8 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「如果AI质检系统在未来一年内成功提升其识别准确率…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 50.4 高于目标 18.0
  - narration_para_pct 17.6 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 49.4 高于目标 18.0
  - dialogue_run_mean 9.5 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题与《摩挲考核表边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - narration_para_pct 30.8 低于目标 45.0
  - [observe] 标题与《摩挲考核表边缘》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 62.8 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「如果最终的自动标注覆盖率没有达到预期效果，那么质…」）
  - [observe] 标题与《摩挲财务报表边缘》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11719
chapter_chars_mean: 1953
chapter_chars_median: 2024
chapter_chars_cv: 0.15
paragraphs_mean: 15.8
dialogue_chars_pct: 30.4
dialogue_para_pct: 58.6
interiority_para_pct: 10.6
narration_para_pct: 30.8
turn_under20_pct: 36.8
turn_over200_pct: 0.0
attr_say_pct: 18.3
attr_adv_pct: 4.6
scenes_per_chapter: 1.3
dialogue_run_mean: 3.3
turn_len_median: 30
```
