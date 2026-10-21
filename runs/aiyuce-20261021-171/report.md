# 铜铃 生成报告

slug：`aiyuce-20261021-171`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12896
LLM 调用：57 次，累计 220.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对预算表 | 2289 | normal | 38.0 | 0 |  | 1 |
| 2 | 核对日报表 | 2505 | normal | 35.4 | 0 |  | 2 |
| 3 | 招聘JD流转 | 2689 | normal | 90.1 | 0 |  | 0 |
| 4 | 核对预算表 | 1946 | normal | 87.1 | 0 |  | 3 |
| 5 | 核对日报表 | 2180 | normal | 90.9 | 0 |  | 1 |
| 6 | 核对报价单 | 1281 | short | 90.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《核对预算表》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - dialogue_chars_pct 32.8 高于目标 18.0
  - narration_para_pct 21.4 低于目标 45.0
  - [observe] 标题重复：「核对预算表」已存在
- 第 5 章：
  - [observe] 标题重复：「核对日报表」已存在
- 第 6 章：
  - dialogue_chars_pct 22.9 高于目标 18.0
  - narration_para_pct 38.5 低于目标 45.0
  - [observe] 标题与《核对日报表》近似 0.60 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 12611
chapter_chars_mean: 2102
chapter_chars_median: 2188
chapter_chars_cv: 0.23
paragraphs_mean: 16.7
dialogue_chars_pct: 10.5
dialogue_para_pct: 35.5
interiority_para_pct: 7.1
narration_para_pct: 57.4
turn_under20_pct: 65.9
turn_over200_pct: 0.0
attr_say_pct: 8.2
attr_adv_pct: 0.0
scenes_per_chapter: 2.2
dialogue_run_mean: 2.0
turn_len_median: 16
```
