# 代码折旧表 生成报告

slug：`aiyuce-20261021-139`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12826
LLM 调用：57 次，累计 227.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻开电费单 | 2281 | normal | 38.8 | 0 |  | 3 |
| 2 | 翻看招聘JD | 1905 | normal | 36.5 | 0 |  | 2 |
| 3 | 摩挲纸边 | 2690 | normal | 35.4 | 0 |  | 4 |
| 4 | 敲击键盘 | 2571 | normal | 34.8 | 0 |  | 2 |
| 5 | 敲击键盘 | 2129 | normal | 35.8 | 0 |  | 4 |
| 6 | 敲击桌面 | 1244 | short | 34.4 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 23.5 高于目标 18.0
  - narration_para_pct 27.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 44.4 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「这条推论会被什么样的事实推翻呢…」）
- 第 3 章：
  - 单条套路句式超限：「点了点头」×3
  - dialogue_chars_pct 25.1 高于目标 18.0
  - narration_para_pct 40.6 低于目标 45.0
  - [observe] 章内自我复读 5 句（如「最终决定采取分阶段实施的方式，优先解决最紧迫的功…」）
- 第 4 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 18.8 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「敲击键盘」已存在
- 第 6 章：
  - dialogue_chars_pct 28.9 高于目标 18.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - narration_para_pct 35.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12455
chapter_chars_mean: 2076
chapter_chars_median: 2142
chapter_chars_cv: 0.25
paragraphs_mean: 24.2
dialogue_chars_pct: 19.7
dialogue_para_pct: 47.2
interiority_para_pct: 11.9
narration_para_pct: 40.8
turn_under20_pct: 50.0
turn_over200_pct: 0.0
attr_say_pct: 18.5
attr_adv_pct: 5.4
scenes_per_chapter: 3
dialogue_run_mean: 2.8
turn_len_median: 20
```
