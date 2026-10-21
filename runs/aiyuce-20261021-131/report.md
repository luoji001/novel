# 模型复核页数 生成报告

slug：`aiyuce-20261021-131`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12156
LLM 调用：57 次，累计 227.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻看案件处理清单 | 2252 | normal | 37.0 | 0 |  | 3 |
| 2 | 翻看案件处理清单 | 2186 | normal | 33.9 | 0 |  | 5 |
| 3 | 核对调查表数据 | 2061 | normal | 91.2 | 0 |  | 1 |
| 4 | 核对调查表数据 | 1975 | normal | 85.0 | 0 |  | 1 |
| 5 | 核对误判率数据 | 2450 | normal | 35.1 | 0 |  | 1 |
| 6 | 核对误判率数据 | 1226 | short | 85.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 41.7 高于目标 40.0
  - narration_para_pct 25.0 低于目标 45.0
  - [observe] 章内自我复读 4 句（如「就在他准备进一步查阅相关资料的时候，他的手机震动…」）
- 第 2 章：
  - dialogue_chars_pct 56.6 高于目标 18.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - narration_para_pct 14.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「翻看案件处理清单」已存在
- 第 3 章：
  - narration_para_pct 35.7 低于目标 45.0
- 第 4 章：
  - [observe] 标题重复：「核对调查表数据」已存在
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 42.4 高于目标 18.0
  - narration_para_pct 16.7 低于目标 45.0
  - [observe] 标题重复：「核对误判率数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11874
chapter_chars_mean: 1979
chapter_chars_median: 2073
chapter_chars_cv: 0.22
paragraphs_mean: 15.3
dialogue_chars_pct: 18.7
dialogue_para_pct: 40.7
interiority_para_pct: 19.9
narration_para_pct: 39.4
turn_under20_pct: 51.7
turn_over200_pct: 0.0
attr_say_pct: 11.2
attr_adv_pct: 2.1
scenes_per_chapter: 1.2
dialogue_run_mean: 2.4
turn_len_median: 20
```
