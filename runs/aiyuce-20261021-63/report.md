# 肺结节识别 生成报告

slug：`aiyuce-20261021-63`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11494
LLM 调用：57 次，累计 219.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 手指滑过预算报表 | 2033 | normal | 95.3 | 0 |  | 1 |
| 2 | 手指滑过学历统计表 | 2010 | normal | 92.5 | 0 |  | 2 |
| 3 | 手指滑过测试报告 | 1903 | normal | 83.4 | 0 |  | 4 |
| 4 | 手指滑过预算报表 | 1992 | normal | 33.3 | 0 |  | 4 |
| 5 | 手指划过数据表格 | 2199 | normal | 34.0 | 0 |  | 3 |
| 6 | 手指划过测试报告 | 1351 | short | 34.2 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 42.1 低于目标 45.0
- 第 2 章：
  - interiority_para_pct 42.9 高于目标 40.0
  - narration_para_pct 42.9 低于目标 45.0
- 第 3 章：
  - dialogue_chars_pct 80.0 高于目标 18.0
  - dialogue_run_mean 29 高于目标 4.0
  - narration_para_pct 0.0 低于目标 45.0
  - [observe] 标题与《手指滑过预算报表》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - dialogue_chars_pct 37.5 高于目标 18.0
  - narration_para_pct 35.0 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「那就是如果出现一种全新的技术手段能够在保证服务质…」）
  - [observe] 标题重复：「手指滑过预算报表」已存在
- 第 5 章：
  - dialogue_chars_pct 28.2 高于目标 18.0
  - narration_para_pct 40.9 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 6 章：
  - dialogue_chars_pct 56.2 高于目标 18.0
  - narration_para_pct 29.4 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《手指滑过测试报告》近似 0.88 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11149
chapter_chars_mean: 1858
chapter_chars_median: 1950
chapter_chars_cv: 0.16
paragraphs_mean: 20.2
dialogue_chars_pct: 34.6
dialogue_para_pct: 58.2
interiority_para_pct: 9.4
narration_para_pct: 32.4
turn_under20_pct: 35.5
turn_over200_pct: 0.0
attr_say_pct: 7.5
attr_adv_pct: 3.2
scenes_per_chapter: 1.3
dialogue_run_mean: 6.6
turn_len_median: 31
```
