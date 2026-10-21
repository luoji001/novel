# 校对小时 生成报告

slug：`aiyuce-20261021-248`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11861
LLM 调用：57 次，累计 220.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对电费单 | 1882 | normal | 94.9 | 0 |  | 0 |
| 2 | 敲击键盘 | 2314 | normal | 34.7 | 0 |  | 4 |
| 3 | 摩挲报价单边缘 | 1988 | normal | 33.7 | 0 |  | 4 |
| 4 | 摩挲报价单边缘 | 2298 | normal | 89.5 | 0 |  | 2 |
| 5 | 摩挲折旧表边缘 | 2096 | normal | 88.3 | 0 |  | 0 |
| 6 | 摩挲电费单边缘 | 1277 | short | 80.2 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - dialogue_chars_pct 27.2 高于目标 18.0
  - dialogue_run_mean 4.2 高于目标 4.0
  - narration_para_pct 24.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 59.4 高于目标 18.0
  - dialogue_run_mean 5.2 高于目标 4.0
  - narration_para_pct 11.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「我们必须尽快准备好新方案，不能再拖下去了…」）
- 第 4 章：
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 标题重复：「摩挲报价单边缘」已存在
- 第 6 章：
  - dialogue_chars_pct 37.3 高于目标 18.0
  - dialogue_run_mean 7 高于目标 4.0
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 标题与《摩挲报价单边缘》近似 0.71 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11557
chapter_chars_mean: 1926
chapter_chars_median: 1986
chapter_chars_cv: 0.19
paragraphs_mean: 17.7
dialogue_chars_pct: 20.3
dialogue_para_pct: 46.1
interiority_para_pct: 19.2
narration_para_pct: 34.7
turn_under20_pct: 67.0
turn_over200_pct: 0.0
attr_say_pct: 34.9
attr_adv_pct: 10.5
scenes_per_chapter: 1.3
dialogue_run_mean: 3.3
turn_len_median: 12
```
