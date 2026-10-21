# 电表 生成报告

slug：`aiyuce-20261021-196`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13403
LLM 调用：57 次，累计 235.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单的负载率核查 | 2228 | normal | 37.8 | 0 |  | 1 |
| 2 | 手机屏幕亮起 | 2501 | normal | 89.9 | 0 |  | 1 |
| 3 | 指认负载率数据 | 2505 | normal | 35.7 | 0 |  | 1 |
| 4 | 核对折旧表数据 | 2369 | normal | 88.7 | 0 |  | 0 |
| 5 | 手指点在数字上 | 2533 | normal | 87.2 | 0 |  | 2 |
| 6 | 手指划过负载率曲线 | 1261 | short | 85.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 33.3 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 24.6 高于目标 18.0
  - narration_para_pct 34.8 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 25.6 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 13108
chapter_chars_mean: 2185
chapter_chars_median: 2388
chapter_chars_cv: 0.22
paragraphs_mean: 16.3
dialogue_chars_pct: 12.8
dialogue_para_pct: 34.3
interiority_para_pct: 16.3
narration_para_pct: 49.3
turn_under20_pct: 34.6
turn_over200_pct: 0.0
attr_say_pct: 17.7
attr_adv_pct: 2.8
scenes_per_chapter: 1.2
dialogue_run_mean: 2.6
turn_len_median: 26
```
