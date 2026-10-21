# 算盘珠 生成报告

slug：`aiyuce-20261021-230`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11237
LLM 调用：57 次，累计 223.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 红笔圈出的日均交易量 | 1436 | normal | 90.7 | 0 |  | 2 |
| 2 | 核对租金账单 | 2013 | normal | 59.0 | 0 |  | 2 |
| 3 | 手指划过价格清单 | 2335 | normal | 89.8 | 0 |  | 0 |
| 4 | 手指划过发布日历 | 2116 | normal | 35.8 | 0 |  | 1 |
| 5 | 核对价格清单 | 1856 | normal | 35.2 | 0 |  | 1 |
| 6 | 核对价格清单 | 1475 | short | 35.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 32.9 高于目标 18.0
  - narration_para_pct 41.7 低于目标 45.0
- 第 2 章：
  - interiority_para_pct 41.7 高于目标 40.0
  - narration_para_pct 41.7 低于目标 45.0
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对价格清单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 10975
chapter_chars_mean: 1829
chapter_chars_median: 1892
chapter_chars_cv: 0.2
paragraphs_mean: 13
dialogue_chars_pct: 6.2
dialogue_para_pct: 19.1
interiority_para_pct: 22.7
narration_para_pct: 58.2
turn_under20_pct: 56.2
turn_over200_pct: 0.0
attr_say_pct: 64.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.3
turn_len_median: 16
```
