# 租卡 生成报告

slug：`aiyuce-20261021-194`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12283
LLM 调用：57 次，累计 232.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 显卡包装盒上的二维码 | 2208 | normal | 88.4 | 0 |  | 3 |
| 2 | 电费单上的数字 | 1985 | normal | 34.5 | 0 |  | 1 |
| 3 | 折旧表的计算 | 2113 | normal | 89.3 | 0 |  | 1 |
| 4 | 显卡租赁的定价策略 | 2077 | normal | 35.7 | 0 |  | 2 |
| 5 | 屏幕上的分配表 | 2214 | normal | 35.5 | 0 |  | 1 |
| 6 | CUDA编程的手势 | 1680 | short | 35.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 27.5 高于目标 18.0
  - dialogue_run_mean 5.7 高于目标 4.0
  - narration_para_pct 16.0 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 4 句（如「如果有数据显示店铺的实际电费支出低于2800元，…」）
- 第 3 章：
  - interiority_para_pct 41.2 高于目标 40.0
- 第 4 章：
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 11997
chapter_chars_mean: 2000
chapter_chars_median: 2048
chapter_chars_cv: 0.09
paragraphs_mean: 15.3
dialogue_chars_pct: 5.8
dialogue_para_pct: 22.3
interiority_para_pct: 28.2
narration_para_pct: 49.5
turn_under20_pct: 56.6
turn_over200_pct: 0.0
attr_say_pct: 27.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.9
turn_len_median: 14
```
