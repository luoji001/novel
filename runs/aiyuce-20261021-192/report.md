# 电表 生成报告

slug：`aiyuce-20261021-192`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12077
LLM 调用：57 次，累计 229.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 划动预算明细指针 | 1769 | normal | 39.1 | 0 |  | 2 |
| 2 | 核对电费单 | 2228 | normal | 34.6 | 0 |  | 1 |
| 3 | 模型教学与成绩变化 | 2224 | normal | 34.7 | 0 |  | 1 |
| 4 | 模型清单更新对比 | 2180 | normal | 34.6 | 0 |  | 1 |
| 5 | 核对预算明细 | 2158 | normal | 89.1 | 0 |  | 0 |
| 6 | 核对电费单 | 1512 | short | 33.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 41.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 3 句（如「斜面滑动摩擦系数测定仪…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对电费单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11784
chapter_chars_mean: 1964
chapter_chars_median: 2121
chapter_chars_cv: 0.15
paragraphs_mean: 16.5
dialogue_chars_pct: 3.0
dialogue_para_pct: 14.2
interiority_para_pct: 12.7
narration_para_pct: 73.1
turn_under20_pct: 93.3
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.9
turn_len_median: 11
```
