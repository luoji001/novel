# 墨线 生成报告

slug：`aiyuce-20261021-145`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12357
LLM 调用：57 次，累计 211.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手机震动的声音 | 2079 | normal | 95.9 | 0 |  | 1 |
| 2 | 订单清单上的名字 | 2316 | normal | 90.4 | 0 |  | 0 |
| 3 | 成本曲线的倾斜 | 2138 | normal | 91.7 | 0 |  | 0 |
| 4 | 仔细阅读授权协议 | 2323 | normal | 89.5 | 0 |  | 1 |
| 5 | 电费单的数字对比 | 1864 | normal | 90.6 | 0 |  | 1 |
| 6 | 订单清单的更新 | 1631 | short | 36.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 33.3 低于目标 45.0
- 第 4 章：
  - narration_para_pct 43.8 低于目标 45.0
- 第 5 章：
  - narration_para_pct 35.7 低于目标 45.0
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《订单清单上的名字》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 12068
chapter_chars_mean: 2011
chapter_chars_median: 2058
chapter_chars_cv: 0.13
paragraphs_mean: 15.8
dialogue_chars_pct: 4.9
dialogue_para_pct: 26.6
interiority_para_pct: 25.4
narration_para_pct: 47.9
turn_under20_pct: 66.3
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 7.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.4
turn_len_median: 10
```
