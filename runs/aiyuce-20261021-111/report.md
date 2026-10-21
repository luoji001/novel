# 影像初筛 生成报告

slug：`aiyuce-20261021-111`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12536
LLM 调用：57 次，累计 227.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅排班记录的焦虑 | 2471 | normal | 95.4 | 0 |  | 0 |
| 2 | 核对薪资明细表 | 2684 | normal | 34.5 | 0 |  | 1 |
| 3 | 翻阅AI报价单的博弈 | 1860 | normal | 81.9 | 0 |  | 3 |
| 4 | 展示数据图表 | 2078 | normal | 31.8 | 0 |  | 4 |
| 5 | 划破招聘JD的笔尖 | 2324 | normal | 35.3 | 0 |  | 1 |
| 6 | 翻阅影像处理报告 | 1113 | short | 89.1 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 52.3 高于目标 18.0
  - dialogue_run_mean 6 高于目标 4.0
  - narration_para_pct 6.7 低于目标 45.0
- 第 4 章：
  - dialogue_chars_pct 54.1 高于目标 18.0
  - dialogue_run_mean 9 高于目标 4.0
  - narration_para_pct 28.0 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 12245
chapter_chars_mean: 2041
chapter_chars_median: 2142
chapter_chars_cv: 0.27
paragraphs_mean: 15.7
dialogue_chars_pct: 18.7
dialogue_para_pct: 36.8
interiority_para_pct: 10.0
narration_para_pct: 53.2
turn_under20_pct: 62.4
turn_over200_pct: 0.0
attr_say_pct: 41.3
attr_adv_pct: 6.6
scenes_per_chapter: 1.2
dialogue_run_mean: 3.4
turn_len_median: 20
```
