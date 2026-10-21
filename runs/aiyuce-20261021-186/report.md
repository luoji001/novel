# 涨价单 生成报告

slug：`aiyuce-20261021-186`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12721
LLM 调用：57 次，累计 206.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对报价单 | 2141 | normal | 37.3 | 0 |  | 1 |
| 2 | 核对报价单 | 2398 | normal | 34.7 | 0 |  | 2 |
| 3 | 核对财务报表 | 2358 | normal | 88.7 | 0 |  | 0 |
| 4 | 核对合同修改记录 | 2317 | normal | 87.0 | 0 |  | 0 |
| 5 | 核对许可证变更 | 2145 | normal | 35.0 | 0 |  | 1 |
| 6 | 核对报价单数据 | 1356 | short | 87.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「他点开查看后，却发现其中提及的新条款内容也未能体…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题重复：「核对报价单」已存在
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被哪些数据所反驳呢…」）
- 第 6 章：
  - narration_para_pct 44.4 低于目标 45.0
  - [observe] 标题与《核对报价单》近似 0.83 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 12459
chapter_chars_mean: 2076
chapter_chars_median: 2186
chapter_chars_cv: 0.19
paragraphs_mean: 14.2
dialogue_chars_pct: 2.7
dialogue_para_pct: 16.8
interiority_para_pct: 16.1
narration_para_pct: 67.1
turn_under20_pct: 70.3
turn_over200_pct: 0.0
attr_say_pct: 31.8
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 1.3
turn_len_median: 8
```
