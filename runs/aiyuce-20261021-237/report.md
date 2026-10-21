# 批改纸条 生成报告

slug：`aiyuce-20261021-237`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11918
LLM 调用：57 次，累计 222.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 批改表数据波动 | 2261 | normal | 36.6 | 0 |  | 3 |
| 2 | 翻看对比分析报告 | 2009 | normal | 85.5 | 0 |  | 2 |
| 3 | 系统断开瞬间 | 2073 | normal | 34.2 | 0 |  | 4 |
| 4 | 翻看预算明细表 | 2050 | normal | 35.2 | 0 |  | 3 |
| 5 | 翻看满意度调查问卷 | 2277 | normal | 33.8 | 0 |  | 3 |
| 6 | 翻看工作量统计表 | 1242 | short | 34.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现。

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 33.0 高于目标 18.0
  - narration_para_pct 26.1 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 2 章：
  - dialogue_chars_pct 31.2 高于目标 18.0
  - narration_para_pct 27.8 低于目标 45.0
- 第 3 章：
  - dialogue_chars_pct 38.2 高于目标 18.0
  - dialogue_run_mean 4.8 高于目标 4.0
  - narration_para_pct 17.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「一条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 21.1 高于目标 18.0
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「这条推论会被什么推翻？…」）
- 第 5 章：
  - dialogue_chars_pct 29.6 高于目标 18.0
  - narration_para_pct 29.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 37.4 高于目标 18.0
  - narration_para_pct 14.3 低于目标 45.0
  - [observe] 章内自我复读 4 句（如「如果未来AI系统能够自动学习并整合教师常用的个性…」）

## 整书结构指标

```
chapters: 6
total_chars: 11589
chapter_chars_mean: 1932
chapter_chars_median: 2004
chapter_chars_cv: 0.19
paragraphs_mean: 19.2
dialogue_chars_pct: 31.4
dialogue_para_pct: 68.0
interiority_para_pct: 8.8
narration_para_pct: 23.2
turn_under20_pct: 38.4
turn_over200_pct: 0.0
attr_say_pct: 18.6
attr_adv_pct: 12.4
scenes_per_chapter: 1.8
dialogue_run_mean: 3.2
turn_len_median: 30
```
