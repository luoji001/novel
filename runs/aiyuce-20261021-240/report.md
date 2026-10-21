# 电表 生成报告

slug：`aiyuce-20261021-240`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13269
LLM 调用：57 次，累计 230.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 成绩统计表 | 2265 | normal | 38.0 | 0 |  | 3 |
| 2 | 检查老旧设备使用情况 | 2271 | normal | 36.0 | 0 |  | 2 |
| 3 | 敲击木桌的手指 | 2629 | normal | 36.7 | 0 |  | 2 |
| 4 | 敲击木桌的手指 | 2454 | normal | 35.2 | 0 |  | 2 |
| 5 | 翻阅泛黄备课笔记 | 2161 | normal | 88.5 | 0 |  | 0 |
| 6 | 翻阅泛黄备课笔记 | 1483 | short | 90.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 42.9 高于目标 40.0
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 4 句（如「她看着桌上的实验器材清单，心里明白了一个道理：如…」）
- 第 2 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 43.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「敲击木桌的手指」已存在
- 第 6 章：
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 标题重复：「翻阅泛黄备课笔记」已存在

## 整书结构指标

```
chapters: 6
total_chars: 13004
chapter_chars_mean: 2167
chapter_chars_median: 2224
chapter_chars_cv: 0.18
paragraphs_mean: 13.8
dialogue_chars_pct: 5.4
dialogue_para_pct: 33.8
interiority_para_pct: 19.9
narration_para_pct: 46.4
turn_under20_pct: 74.2
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 8.4
scenes_per_chapter: 1.5
dialogue_run_mean: 1.5
turn_len_median: 12
```
