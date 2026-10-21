# 排产员的笔 生成报告

slug：`aiyuce-20261021-184`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12685
LLM 调用：57 次，累计 224.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电费单数据 | 2246 | normal | 90.4 | 0 |  | 2 |
| 2 | 核对折旧表数据 | 2251 | normal | 36.1 | 0 |  | 1 |
| 3 | 核对报价单数据 | 1943 | normal | 36.2 | 0 |  | 2 |
| 4 | 核对招聘JD数据 | 2599 | normal | 89.7 | 0 |  | 2 |
| 5 | 核对电费单数据 | 2234 | normal | 91.1 | 0 |  | 1 |
| 6 | 核对电费单数据 | 1406 | short | 89.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 61.5 高于目标 40.0
  - narration_para_pct 30.8 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《核对电费单数据》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - dialogue_chars_pct 24.3 高于目标 18.0
  - narration_para_pct 21.7 低于目标 45.0
- 第 5 章：
  - [observe] 标题重复：「核对电费单数据」已存在
- 第 6 章：
  - [observe] 标题重复：「核对电费单数据」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12402
chapter_chars_mean: 2067
chapter_chars_median: 2195
chapter_chars_cv: 0.19
paragraphs_mean: 15.5
dialogue_chars_pct: 10.1
dialogue_para_pct: 29.3
interiority_para_pct: 23.1
narration_para_pct: 47.6
turn_under20_pct: 51.6
turn_over200_pct: 0.0
attr_say_pct: 18.4
attr_adv_pct: 2.6
scenes_per_chapter: 1.3
dialogue_run_mean: 1.5
turn_len_median: 22
```
