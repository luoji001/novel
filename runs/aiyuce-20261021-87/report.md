# 复核名单 生成报告

slug：`aiyuce-20261021-87`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11940
LLM 调用：57 次，累计 225.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 预算表上的AI开支 | 2350 | normal | 96.6 | 0 |  | 2 |
| 2 | 报价单上的数字 | 2098 | normal | 32.6 | 0 |  | 4 |
| 3 | 划线标注学历要求 | 2104 | normal | 35.0 | 0 |  | 1 |
| 4 | 鼠标划过屏幕上的数字 | 2209 | normal | 86.9 | 0 |  | 0 |
| 5 | 电话里的算法对话 | 2143 | normal | 35.6 | 0 |  | 2 |
| 6 | 目光停留统计数据 | 1030 | short | 86.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 19.4 高于目标 18.0
  - narration_para_pct 32.0 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 68.2 高于目标 18.0
  - dialogue_run_mean 8 高于目标 4.0
  - narration_para_pct 14.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被哪些事实推翻呢…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - interiority_para_pct 42.9 高于目标 40.0

## 整书结构指标

```
chapters: 6
total_chars: 11636
chapter_chars_mean: 1939
chapter_chars_median: 2078
chapter_chars_cv: 0.24
paragraphs_mean: 16.7
dialogue_chars_pct: 17.9
dialogue_para_pct: 44.5
interiority_para_pct: 14.0
narration_para_pct: 41.5
turn_under20_pct: 71.5
turn_over200_pct: 0.0
attr_say_pct: 28.8
attr_adv_pct: 3.0
scenes_per_chapter: 1.7
dialogue_run_mean: 3.2
turn_len_median: 14
```
