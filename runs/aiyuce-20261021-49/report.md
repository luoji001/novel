# 电耗计 生成报告

slug：`aiyuce-20261021-49`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11619
LLM 调用：57 次，累计 218.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 查看代写服务报价单 | 2293 | normal | 39.4 | 0 |  | 2 |
| 2 | 核对电费单数据 | 2285 | normal | 36.6 | 0 |  | 1 |
| 3 | 贴JD的剪刀动作 | 2431 | normal | 90.1 | 0 |  | 0 |
| 4 | 打印店老板看报价单 | 1837 | normal | 36.2 | 0 |  | 1 |
| 5 | 核对折旧表数据 | 1606 | normal | 89.2 | 0 |  | 2 |
| 6 | 盯着代写报价单 | 1161 | short | 92.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 37.5 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 28.3 高于目标 18.0
  - narration_para_pct 35.3 低于目标 45.0
- 第 6 章：
  - narration_para_pct 22.2 低于目标 45.0
  - [observe] 标题与《查看代写服务报价单》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 6
total_chars: 11306
chapter_chars_mean: 1884
chapter_chars_median: 2009
chapter_chars_cv: 0.26
paragraphs_mean: 17.7
dialogue_chars_pct: 11.4
dialogue_para_pct: 41.2
interiority_para_pct: 15.9
narration_para_pct: 42.9
turn_under20_pct: 65.2
turn_over200_pct: 0.0
attr_say_pct: 4.7
attr_adv_pct: 3.9
scenes_per_chapter: 2.7
dialogue_run_mean: 1.7
turn_len_median: 15
```
