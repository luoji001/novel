# 听评课笔记 生成报告

slug：`aiyuce-20261021-201`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12361
LLM 调用：57 次，累计 218.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击桌面的钢笔 | 2039 | normal | 38.3 | 0 |  | 1 |
| 2 | 教师输入范文体验 | 2450 | normal | 34.5 | 0 |  | 3 |
| 3 | 周工作时间统计表 | 2104 | normal | 90.5 | 0 |  | 0 |
| 4 | AI批改作文系统上线 | 2632 | normal | 33.7 | 0 |  | 1 |
| 5 | 查看成本效益分析报告 | 1903 | normal | 85.8 | 0 |  | 2 |
| 6 | 听课记录表核对 | 1227 | short | 88.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - dialogue_chars_pct 26.4 高于目标 18.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么样的事实所推翻呢…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 33.5 高于目标 18.0
  - narration_para_pct 20.0 低于目标 45.0
- 第 6 章：
  - 命中套话收尾句
  - dialogue_chars_pct 20.7 高于目标 18.0
  - narration_para_pct 16.7 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 12099
chapter_chars_mean: 2016
chapter_chars_median: 2030
chapter_chars_cv: 0.24
paragraphs_mean: 13.2
dialogue_chars_pct: 13.9
dialogue_para_pct: 36.9
interiority_para_pct: 11.4
narration_para_pct: 51.7
turn_under20_pct: 44.4
turn_over200_pct: 0.0
attr_say_pct: 10.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.8
turn_len_median: 22
```
