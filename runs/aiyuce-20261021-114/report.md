# 报价单 生成报告

slug：`aiyuce-20261021-114`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12074
LLM 调用：57 次，累计 214.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 放大镜下的表格 | 1894 | normal | 38.6 | 0 |  | 1 |
| 2 | 数字的反复跳跃 | 2230 | normal | 36.3 | 0 |  | 1 |
| 3 | 行业分析报告的解读 | 2321 | normal | 34.8 | 0 |  | 3 |
| 4 | 毛利率数据的对比 | 2032 | normal | 87.1 | 0 |  | 0 |
| 5 | 报价调整的博弈 | 2134 | normal | 33.8 | 0 |  | 1 |
| 6 | 使用率与竞品动态 | 1457 | short | 34.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 1 句（如「他又看了一眼报价单，心中不禁产生疑问：这份文件到…」）
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - dialogue_chars_pct 28.2 高于目标 18.0
  - narration_para_pct 32.1 低于目标 45.0
  - [observe] 章内自我复读 2 句（如「与此同时，他也意识到自己正处于一种微妙的位置：既…」）
- 第 5 章：
  - [observe] 章内自我复读 5 句（如「而且在这个过程中还存在着其他变量干扰因子例如法律…」）
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 11756
chapter_chars_mean: 1959
chapter_chars_median: 2038
chapter_chars_cv: 0.15
paragraphs_mean: 17
dialogue_chars_pct: 7.8
dialogue_para_pct: 22.4
interiority_para_pct: 12.7
narration_para_pct: 64.9
turn_under20_pct: 46.5
turn_over200_pct: 0.0
attr_say_pct: 36.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 2.8
turn_len_median: 17
```
