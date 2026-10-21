# 算法修正 生成报告

slug：`aiyuce-20261021-259`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12205
LLM 调用：57 次，累计 214.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电费单核对 | 2186 | normal | 95.8 | 0 |  | 1 |
| 2 | 核对旧文件细节 | 2233 | normal | 90.0 | 0 |  | 3 |
| 3 | 审核员接过报价单 | 1963 | normal | 35.0 | 0 |  | 3 |
| 4 | 核对折旧表细节 | 2114 | normal | 35.8 | 0 |  | 2 |
| 5 | 核对数据字段格式 | 2098 | normal | 88.0 | 0 |  | 1 |
| 6 | 核对数据字段格式 | 1605 | short | 35.2 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 21.1 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 27.6 高于目标 18.0
  - dialogue_run_mean 5 高于目标 4.0
  - narration_para_pct 10.7 低于目标 45.0
- 第 3 章：
  - dialogue_chars_pct 39.7 高于目标 18.0
  - narration_para_pct 24.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《核对旧文件细节》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3
- 第 6 章：
  - dialogue_chars_pct 26.8 高于目标 18.0
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对数据字段格式」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11864
chapter_chars_mean: 1977
chapter_chars_median: 2054
chapter_chars_cv: 0.11
paragraphs_mean: 20.3
dialogue_chars_pct: 20.5
dialogue_para_pct: 50.1
interiority_para_pct: 18.3
narration_para_pct: 31.5
turn_under20_pct: 47.8
turn_over200_pct: 0.0
attr_say_pct: 15.4
attr_adv_pct: 4.6
scenes_per_chapter: 2.3
dialogue_run_mean: 2.8
turn_len_median: 23
```
