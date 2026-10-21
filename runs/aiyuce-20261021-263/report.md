# 错判 生成报告

slug：`aiyuce-20261021-263`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12732
LLM 调用：57 次，累计 217.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 结算单边缘卷曲 | 2246 | normal | 94.3 | 0 |  | 1 |
| 2 | 报价单边缘卷曲 | 2203 | normal | 34.2 | 0 |  | 4 |
| 3 | 检查AI分析结果 | 2165 | normal | 36.0 | 0 |  | 1 |
| 4 | 签署附加协议 | 2589 | normal | 35.0 | 0 |  | 1 |
| 5 | 检查AI分析结果 | 2285 | normal | 34.8 | 0 |  | 2 |
| 6 | 检查AI分析结果 | 1238 | short | 87.3 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 31.2 低于目标 45.0
- 第 2 章：
  - dialogue_chars_pct 44.1 高于目标 18.0
  - narration_para_pct 20.0 低于目标 45.0
  - [observe] 章内自我复读 4 句（如「那为什么昨天客户投诉说检索过程中出现了两次错误？…」）
  - [observe] 标题与《结算单边缘卷曲》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻呢…」）
  - [observe] 标题重复：「检查AI分析结果」已存在
- 第 6 章：
  - [observe] 标题重复：「检查AI分析结果」已存在

## 整书结构指标

```
chapters: 6
total_chars: 12444
chapter_chars_mean: 2074
chapter_chars_median: 2174
chapter_chars_cv: 0.22
paragraphs_mean: 15.8
dialogue_chars_pct: 11.0
dialogue_para_pct: 31.8
interiority_para_pct: 15.3
narration_para_pct: 52.9
turn_under20_pct: 48.0
turn_over200_pct: 0.0
attr_say_pct: 31.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.8
turn_len_median: 18
```
