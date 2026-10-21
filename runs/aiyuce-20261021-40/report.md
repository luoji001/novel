# 电表 生成报告

slug：`aiyuce-20261021-40`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11252
LLM 调用：53 次，累计 203.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摊开电费单 | 2125 | normal | 37.6 | 0 |  | 1 |
| 2 | 折旧表上的折旧率 | 2056 | normal | 36.5 | 0 |  | 1 |
| 3 | 敲响警报的键盘声 | 2479 | normal | 35.7 | 0 |  | 2 |
| 4 | 通话中断的手机铃声 | 2107 | normal | 83.3 | 0 |  | 3 |
| 5 | 摊开电费单 | 1346 | normal | 89.5 | 0 |  | 1 |
| 6 | 电费单上的机房用电 | 1133 | short | 90.9 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被电力调度政策的重大调整推翻，例如如果…」）
- 第 4 章：
  - dialogue_chars_pct 44.6 高于目标 18.0
  - dialogue_run_mean 6.3 高于目标 4.0
  - narration_para_pct 9.1 低于目标 45.0
- 第 5 章：
  - [observe] 标题重复：「摊开电费单」已存在
- 第 6 章：
  - narration_para_pct 44.4 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 10986
chapter_chars_mean: 1831
chapter_chars_median: 2028
chapter_chars_cv: 0.28
paragraphs_mean: 14
dialogue_chars_pct: 13.4
dialogue_para_pct: 39.4
interiority_para_pct: 19.6
narration_para_pct: 41.0
turn_under20_pct: 57.8
turn_over200_pct: 0.0
attr_say_pct: 43.4
attr_adv_pct: 30.6
scenes_per_chapter: 1.2
dialogue_run_mean: 2.5
turn_len_median: 20
```
