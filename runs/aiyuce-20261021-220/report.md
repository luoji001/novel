# 电费单 生成报告

slug：`aiyuce-20261021-220`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12189
LLM 调用：57 次，累计 212.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电费单 | 2413 | normal | 94.4 | 0 |  | 1 |
| 2 | 核对折旧表 | 2410 | normal | 34.6 | 0 |  | 1 |
| 3 | 核对招聘JD | 1997 | normal | 90.2 | 0 |  | 0 |
| 4 | 核对交付周期 | 1774 | normal | 91.1 | 0 |  | 0 |
| 5 | 核对交付周期 | 2171 | normal | 91.7 | 0 |  | 3 |
| 6 | 核对电费单 | 1418 | short | 89.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 43.8 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 19.2 高于目标 18.0
  - narration_para_pct 31.2 低于目标 45.0
  - [observe] 标题重复：「核对交付周期」已存在
- 第 6 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×4
  - [observe] 标题重复：「核对电费单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11926
chapter_chars_mean: 1988
chapter_chars_median: 2040
chapter_chars_cv: 0.19
paragraphs_mean: 14.5
dialogue_chars_pct: 7.1
dialogue_para_pct: 26.7
interiority_para_pct: 20.5
narration_para_pct: 52.9
turn_under20_pct: 69.7
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 3.4
scenes_per_chapter: 1.5
dialogue_run_mean: 1.5
turn_len_median: 13
```
