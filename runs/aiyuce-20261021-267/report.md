# AI推理单 生成报告

slug：`aiyuce-20261021-267`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11723
LLM 调用：57 次，累计 218.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对设备兼容性 | 2100 | normal | 96.7 | 0 |  | 2 |
| 2 | 核对设备兼容性 | 2392 | normal | 35.7 | 0 |  | 2 |
| 3 | 核对设备兼容性 | 2285 | normal | 35.2 | 0 |  | 2 |
| 4 | 核对设备兼容性 | 1906 | normal | 34.9 | 0 |  | 4 |
| 5 | 核对设备兼容性 | 1678 | normal | 82.0 | 0 |  | 4 |
| 6 | 核对设备兼容性 | 1356 | short | 89.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 18.4 高于目标 18.0
  - narration_para_pct 36.8 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对设备兼容性」已存在
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对设备兼容性」已存在
- 第 4 章：
  - dialogue_chars_pct 31.9 高于目标 18.0
  - narration_para_pct 35.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对设备兼容性」已存在
- 第 5 章：
  - dialogue_chars_pct 63.5 高于目标 18.0
  - dialogue_run_mean 8 高于目标 4.0
  - narration_para_pct 5.9 低于目标 45.0
  - [observe] 标题重复：「核对设备兼容性」已存在
- 第 6 章：
  - [observe] 标题重复：「核对设备兼容性」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11441
chapter_chars_mean: 1907
chapter_chars_median: 1952
chapter_chars_cv: 0.2
paragraphs_mean: 15.5
dialogue_chars_pct: 18.7
dialogue_para_pct: 42.8
interiority_para_pct: 9.4
narration_para_pct: 47.8
turn_under20_pct: 51.4
turn_over200_pct: 0.0
attr_say_pct: 9.5
attr_adv_pct: 8.1
scenes_per_chapter: 1
dialogue_run_mean: 2.8
turn_len_median: 22
```
