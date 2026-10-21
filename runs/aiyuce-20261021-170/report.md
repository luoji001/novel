# 电表 生成报告

slug：`aiyuce-20261021-170`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11859
LLM 调用：57 次，累计 236.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 报价单上的价格波动 | 1623 | normal | 38.8 | 0 |  | 2 |
| 2 | 核对库存清单 | 2425 | normal | 35.2 | 0 |  | 1 |
| 3 | 摩挲电费单边缘 | 2204 | normal | 36.6 | 0 |  | 1 |
| 4 | 摩挲租金合同边缘 | 2276 | normal | 35.4 | 0 |  | 1 |
| 5 | 摩挲采购订单边缘 | 1949 | normal | 36.4 | 0 |  | 2 |
| 6 | 核对库存清单 | 1376 | short | 35.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 26.7 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
  - [observe] 标题与《摩挲电费单边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - narration_para_pct 36.4 低于目标 45.0
  - [observe] 章内自我复读 5 句（如「就在这时，他的手机响了一声，是一条来自东莞市某A…」）
  - [observe] 标题重复：「核对库存清单」已存在

## 整书结构指标

```
chapters: 6
total_chars: 11564
chapter_chars_mean: 1927
chapter_chars_median: 2027
chapter_chars_cv: 0.21
paragraphs_mean: 15.7
dialogue_chars_pct: 7.7
dialogue_para_pct: 28.1
interiority_para_pct: 21.8
narration_para_pct: 50.1
turn_under20_pct: 75.2
turn_over200_pct: 0.0
attr_say_pct: 19.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 2.3
turn_len_median: 17
```
