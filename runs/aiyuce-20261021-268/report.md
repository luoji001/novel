# 电表 生成报告

slug：`aiyuce-20261021-268`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13957
LLM 调用：57 次，累计 235.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 敲击键盘的手指 | 2307 | normal | 97.5 | 0 |  | 1 |
| 2 | 敲击键盘的手指 | 2480 | normal | 35.9 | 0 |  | 2 |
| 3 | 阅读招聘JD | 2858 | normal | 35.7 | 0 |  | 1 |
| 4 | 服务器折旧表 | 2202 | normal | 37.3 | 0 |  | 2 |
| 5 | 电价调整记录 | 2702 | normal | 35.7 | 0 |  | 1 |
| 6 | 服务器折旧表 | 1402 | short | 34.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 38.5 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「敲击键盘的手指」已存在
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 44.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「服务器折旧表」已存在

## 整书结构指标

```
chapters: 6
total_chars: 13681
chapter_chars_mean: 2280
chapter_chars_median: 2350
chapter_chars_cv: 0.22
paragraphs_mean: 15.3
dialogue_chars_pct: 3.7
dialogue_para_pct: 19.9
interiority_para_pct: 16.9
narration_para_pct: 63.1
turn_under20_pct: 79.6
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.1
turn_len_median: 15
```
