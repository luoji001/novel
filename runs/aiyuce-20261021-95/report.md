# 检索表 生成报告

slug：`aiyuce-20261021-95`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12220
LLM 调用：57 次，累计 222.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对人工检索小时数 | 2301 | normal | 96.1 | 0 |  | 0 |
| 2 | 核对人工检索小时数 | 1856 | normal | 35.4 | 0 |  | 3 |
| 3 | 核对服务器折旧表 | 1803 | normal | 34.7 | 0 |  | 3 |
| 4 | 核对测试报告细节 | 2430 | normal | 36.1 | 0 |  | 2 |
| 5 | 核对人工检索小时数 | 2297 | normal | 90.8 | 0 |  | 2 |
| 6 | 核对满意度问卷 | 1527 | short | 80.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对人工检索小时数」已存在
- 第 3 章：
  - dialogue_chars_pct 32.0 高于目标 18.0
  - narration_para_pct 33.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 40.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - narration_para_pct 11.8 低于目标 45.0
  - [observe] 标题重复：「核对人工检索小时数」已存在
- 第 6 章：
  - dialogue_chars_pct 49.1 高于目标 18.0
  - dialogue_run_mean 6.5 高于目标 4.0
  - narration_para_pct 12.5 低于目标 45.0

## 整书结构指标

```
chapters: 6
total_chars: 11928
chapter_chars_mean: 1988
chapter_chars_median: 2030
chapter_chars_cv: 0.18
paragraphs_mean: 15.7
dialogue_chars_pct: 16.8
dialogue_para_pct: 45.1
interiority_para_pct: 21.0
narration_para_pct: 33.8
turn_under20_pct: 56.8
turn_over200_pct: 0.0
attr_say_pct: 23.1
attr_adv_pct: 12.3
scenes_per_chapter: 1.5
dialogue_run_mean: 2.4
turn_len_median: 16
```
