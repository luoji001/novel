# 显卡折旧表 生成报告

slug：`aiyuce-20261021-182`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13015
LLM 调用：57 次，累计 235.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单上的显卡用量 | 2318 | normal | 95.5 | 0 |  | 0 |
| 2 | 敲击键盘的指节 | 2395 | normal | 91.0 | 0 |  | 2 |
| 3 | 手机支付确认信息 | 2379 | normal | 36.3 | 0 |  | 2 |
| 4 | 折旧表上的损耗曲线 | 2337 | normal | 35.5 | 0 |  | 1 |
| 5 | 核对销售数据表 | 2106 | normal | 58.7 | 0 |  | 0 |
| 6 | 核对库存报表 | 1474 | short | 36.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - dialogue_chars_pct 20.9 高于目标 18.0
  - narration_para_pct 13.3 低于目标 45.0
- 第 3 章：
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「如果这条推论会被什么推翻呢…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12721
chapter_chars_mean: 2120
chapter_chars_median: 2274
chapter_chars_cv: 0.16
paragraphs_mean: 16.2
dialogue_chars_pct: 8.8
dialogue_para_pct: 39.4
interiority_para_pct: 13.2
narration_para_pct: 47.3
turn_under20_pct: 80.7
turn_over200_pct: 0.0
attr_say_pct: 43.7
attr_adv_pct: 7.2
scenes_per_chapter: 1.7
dialogue_run_mean: 1.9
turn_len_median: 10
```
