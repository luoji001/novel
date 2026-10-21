# 代码验证 生成报告

slug：`aiyuce-20261021-19`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11461
LLM 调用：57 次，累计 214.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电费单 | 2198 | normal | 37.4 | 0 |  | 2 |
| 2 | 核对权限管理代码 | 1803 | normal | 37.5 | 0 |  | 2 |
| 3 | 核对权限管理代码 | 2017 | normal | 35.7 | 0 |  | 3 |
| 4 | 核对折旧表 | 2239 | normal | 36.4 | 0 |  | 1 |
| 5 | 核对代码验证报告 | 1973 | normal | 35.8 | 0 |  | 3 |
| 6 | 核对代码验证报告 | 1225 | short | 87.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - narration_para_pct 41.7 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「如果这些逻辑漏洞根本不会影响实际运行，那么他的所…」）
- 第 3 章：
  - narration_para_pct 40.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对权限管理代码」已存在
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 5 章：
  - dialogue_chars_pct 23.5 高于目标 18.0
  - narration_para_pct 34.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
- 第 6 章：
  - dialogue_chars_pct 23.3 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 标题重复：「核对代码验证报告」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11163
chapter_chars_mean: 1860
chapter_chars_median: 1934
chapter_chars_cv: 0.2
paragraphs_mean: 16.3
dialogue_chars_pct: 14.5
dialogue_para_pct: 40.8
interiority_para_pct: 19.2
narration_para_pct: 40.0
turn_under20_pct: 57.0
turn_over200_pct: 0.0
attr_say_pct: 14.5
attr_adv_pct: 10.9
scenes_per_chapter: 1.8
dialogue_run_mean: 2.1
turn_len_median: 19
```
