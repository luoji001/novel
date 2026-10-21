# 算力账单 生成报告

slug：`aiyuce-20261021-126`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12476
LLM 调用：57 次，累计 213.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对折旧表数据 | 2168 | normal | 95.5 | 0 |  | 0 |
| 2 | 核对电费账单数据 | 2148 | normal | 35.0 | 0 |  | 1 |
| 3 | 核对招聘JD数据 | 1960 | normal | 36.2 | 0 |  | 2 |
| 4 | 核对电费账单数据 | 2522 | normal | 35.6 | 0 |  | 4 |
| 5 | 核对许可证条款 | 2190 | normal | 35.5 | 0 |  | 1 |
| 6 | 核对报价单数据 | 1482 | short | 91.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - narration_para_pct 43.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - dialogue_chars_pct 24.4 高于目标 18.0
  - narration_para_pct 38.1 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「与此同时，在杭州的某个角落里，一位CTO正仔细核…」）
  - [observe] 标题重复：「核对电费账单数据」已存在
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - narration_para_pct 27.3 低于目标 45.0
  - [observe] 标题与《核对电费账单数据》近似 0.67 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 12174
chapter_chars_mean: 2029
chapter_chars_median: 2110
chapter_chars_cv: 0.17
paragraphs_mean: 16.7
dialogue_chars_pct: 9.9
dialogue_para_pct: 32.2
interiority_para_pct: 14.9
narration_para_pct: 52.9
turn_under20_pct: 65.0
turn_over200_pct: 0.0
attr_say_pct: 26.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.5
turn_len_median: 14
```
