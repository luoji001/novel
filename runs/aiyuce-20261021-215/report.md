# 复核页 生成报告

slug：`aiyuce-20261021-215`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11747
LLM 调用：57 次，累计 215.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻动财务报表 | 2073 | normal | 94.4 | 0 |  | 0 |
| 2 | 翻动财务报表 | 1965 | normal | 81.0 | 0 |  | 4 |
| 3 | 指尖划过调查表 | 2570 | normal | 32.7 | 0 |  | 4 |
| 4 | 指尖划过记录表 | 2049 | normal | 80.2 | 0 |  | 4 |
| 5 | 手指滑过错误率报告 | 1968 | normal | 86.1 | 0 |  | 2 |
| 6 | 红标警示 | 1116 | short | 34.6 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - dialogue_chars_pct 57.7 高于目标 18.0
  - dialogue_run_mean 9 高于目标 4.0
  - narration_para_pct 5.0 低于目标 45.0
  - [observe] 标题重复：「翻动财务报表」已存在
- 第 3 章：
  - dialogue_chars_pct 68.6 高于目标 18.0
  - dialogue_run_mean 6.5 高于目标 4.0
  - narration_para_pct 13.3 低于目标 45.0
  - [observe] 章内自我复读 4 句（如「我觉得这就是根本的问题所在，”陈文远说道，“如果…」）
- 第 4 章：
  - dialogue_chars_pct 55.1 高于目标 18.0
  - dialogue_run_mean 10.5 高于目标 4.0
  - narration_para_pct 12.0 低于目标 45.0
  - [observe] 标题与《指尖划过调查表》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - dialogue_chars_pct 50.3 高于目标 18.0
  - narration_para_pct 10.0 低于目标 45.0
- 第 6 章：
  - dialogue_chars_pct 66.5 高于目标 18.0
  - dialogue_run_mean 4.5 高于目标 4.0
  - narration_para_pct 18.2 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 11403
chapter_chars_mean: 1900
chapter_chars_median: 1944
chapter_chars_cv: 0.24
paragraphs_mean: 20.2
dialogue_chars_pct: 49.4
dialogue_para_pct: 74.5
interiority_para_pct: 6.8
narration_para_pct: 18.7
turn_under20_pct: 38.6
turn_over200_pct: 0.0
attr_say_pct: 21.3
attr_adv_pct: 6.4
scenes_per_chapter: 1.7
dialogue_run_mean: 6.1
turn_len_median: 29
```
