# 听评本的褶痕 生成报告

slug：`aiyuce-20261021-105`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12646
LLM 调用：57 次，累计 219.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 听课记录本的缺口 | 2092 | normal | 92.1 | 0 |  | 2 |
| 2 | 听课记录本的缺口 | 2169 | normal | 36.0 | 0 |  | 3 |
| 3 | 触摸屏幕的指尖 | 2604 | normal | 36.0 | 0 |  | 2 |
| 4 | 触摸屏幕的指尖 | 2072 | normal | 35.6 | 0 |  | 3 |
| 5 | 核对打印耗材用量 | 2389 | normal | 35.3 | 0 |  | 2 |
| 6 | 翻阅听课记录本 | 1314 | short | 90.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_run_mean 7 高于目标 4.0
  - narration_para_pct 35.7 低于目标 45.0
- 第 2 章：
  - narration_para_pct 28.6 低于目标 45.0
  - [observe] 章内自我复读 3 句（如「假如后续核实发现所有听评课资料都被完整保存于云端…」）
  - [observe] 标题重复：「听课记录本的缺口」已存在
- 第 3 章：
  - narration_para_pct 38.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - narration_para_pct 35.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「触摸屏幕的指尖」已存在
- 第 5 章：
  - narration_para_pct 23.1 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「一条推论会被什么推翻…」）
- 第 6 章：
  - narration_para_pct 12.5 低于目标 45.0
  - [observe] 标题与《听课记录本的缺口》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 12365
chapter_chars_mean: 2061
chapter_chars_median: 2080
chapter_chars_cv: 0.21
paragraphs_mean: 15.2
dialogue_chars_pct: 12.8
dialogue_para_pct: 46.1
interiority_para_pct: 23.6
narration_para_pct: 30.3
turn_under20_pct: 45.0
turn_over200_pct: 0.0
attr_say_pct: 3.2
attr_adv_pct: 3.4
scenes_per_chapter: 1.7
dialogue_run_mean: 2.5
turn_len_median: 19
```
