# 校对钟 生成报告

slug：`aiyuce-20261021-200`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12654
LLM 调用：57 次，累计 233.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对千字价格 | 2092 | normal | 95.8 | 0 |  | 1 |
| 2 | 折旧表的数字思索 | 2007 | normal | 36.3 | 0 |  | 1 |
| 3 | 校对能力的反复强调 | 2078 | normal | 36.7 | 0 |  | 1 |
| 4 | 电费账单的数字 | 2683 | normal | 34.6 | 0 |  | 1 |
| 5 | AI翻译测试报告 | 2354 | normal | 35.7 | 0 |  | 1 |
| 6 | 打印纸的摩擦声 | 1434 | short | 88.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 30.8 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 2 句（如「如果未来的AI技术发展出足以独立完成所有校对任务…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 20.6 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 12373
chapter_chars_mean: 2062
chapter_chars_median: 2038
chapter_chars_cv: 0.2
paragraphs_mean: 15.2
dialogue_chars_pct: 9.0
dialogue_para_pct: 32.5
interiority_para_pct: 10.9
narration_para_pct: 56.6
turn_under20_pct: 46.7
turn_over200_pct: 0.0
attr_say_pct: 4.8
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.9
turn_len_median: 22
```
