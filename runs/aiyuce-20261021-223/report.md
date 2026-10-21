# 代码审核手册 生成报告

slug：`aiyuce-20261021-223`
档位：AI 推演　闸门模式：observe
章数：6　总字数：13039
LLM 调用：57 次，累计 232.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 填写入职表格 | 2320 | normal | 37.8 | 0 |  | 2 |
| 2 | 手册上的变量命名规则 | 2307 | normal | 88.6 | 0 |  | 0 |
| 3 | 敲击键盘 | 2901 | normal | 35.4 | 0 |  | 2 |
| 4 | 敲击键盘 | 2139 | normal | 31.8 | 0 |  | 5 |
| 5 | 标注冗余代码 | 2079 | normal | 33.5 | 0 |  | 3 |
| 6 | 敲击桌面 | 1287 | short | 35.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 42.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 41.9 高于目标 18.0
  - dialogue_run_mean 8.5 高于目标 4.0
  - narration_para_pct 10.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「敲击键盘」已存在
- 第 5 章：
  - dialogue_chars_pct 32.6 高于目标 18.0
  - narration_para_pct 31.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12703
chapter_chars_mean: 2117
chapter_chars_median: 2169
chapter_chars_cv: 0.24
paragraphs_mean: 20.7
dialogue_chars_pct: 19.5
dialogue_para_pct: 47.2
interiority_para_pct: 15.4
narration_para_pct: 37.4
turn_under20_pct: 46.0
turn_over200_pct: 0.0
attr_say_pct: 14.6
attr_adv_pct: 16.3
scenes_per_chapter: 3
dialogue_run_mean: 2.9
turn_len_median: 19
```
