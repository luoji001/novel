# 涨工时费 生成报告

slug：`aiyuce-20261021-166`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11647
LLM 调用：53 次，累计 205.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 盯屏细数执业证书 | 2051 | normal | 95.3 | 0 |  | 1 |
| 2 | 用电量增幅 | 2263 | normal | 87.0 | 0 |  | 2 |
| 3 | 盯报价单算成本增 | 2383 | normal | 36.1 | 0 |  | 2 |
| 4 | 盯折旧表看使用年限 | 1447 | normal | 90.0 | 0 |  | 0 |
| 5 | 盯屏幕看执业证书 | 2297 | normal | 36.6 | 0 |  | 2 |
| 6 | 盯报价单算成本增 | 1200 | short | 34.4 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 28.6 低于目标 45.0
- 第 2 章：
  - interiority_para_pct 57.1 高于目标 40.0
  - narration_para_pct 35.7 低于目标 45.0
- 第 3 章：
  - narration_para_pct 35.3 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这让人事主管感到一丝希望，但也更加坚定了他对未来…」）
  - [observe] 标题与《盯屏细数执业证书》近似 0.75 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - [observe] 章内自我复读 4 句（如「如果市场需求真的如某些人所说那样并不见明显上升趋…」）
  - [observe] 标题重复：「盯报价单算成本增」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11386
chapter_chars_mean: 1898
chapter_chars_median: 2114
chapter_chars_cv: 0.26
paragraphs_mean: 13.5
dialogue_chars_pct: 3.8
dialogue_para_pct: 25.6
interiority_para_pct: 29.3
narration_para_pct: 45.1
turn_under20_pct: 85.6
turn_over200_pct: 0.0
attr_say_pct: 0.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.4
turn_len_median: 12
```
