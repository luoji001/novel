# 铜铃 生成报告

slug：`aiyuce-20261021-231`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12342
LLM 调用：57 次，累计 222.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 统计表上的数字 | 2065 | normal | 38.1 | 0 |  | 1 |
| 2 | 错误率对比图表 | 2459 | normal | 35.9 | 0 |  | 1 |
| 3 | 红笔圈住“AI初筛 | 2155 | normal | 92.3 | 0 |  | 2 |
| 4 | 绩效考核记录 | 2573 | normal | 36.2 | 0 |  | 1 |
| 5 | 摩挲纸张边缘 | 1754 | normal | 87.0 | 0 |  | 3 |
| 6 | 摩挲预算报告边缘 | 1330 | short | 37.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的证据所驳斥呢…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - 单条套路句式超限：「智影科技的」×3
  - narration_para_pct 20.0 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - 单条套路句式超限：「智影科技的」×3
  - dialogue_chars_pct 38.3 高于目标 18.0
  - narration_para_pct 12.5 低于目标 45.0
- 第 6 章：
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12041
chapter_chars_mean: 2007
chapter_chars_median: 2064
chapter_chars_cv: 0.23
paragraphs_mean: 17
dialogue_chars_pct: 12.8
dialogue_para_pct: 38.2
interiority_para_pct: 16.3
narration_para_pct: 45.5
turn_under20_pct: 50.4
turn_over200_pct: 0.0
attr_say_pct: 1.4
attr_adv_pct: 0.0
scenes_per_chapter: 2.8
dialogue_run_mean: 1.8
turn_len_median: 20
```
