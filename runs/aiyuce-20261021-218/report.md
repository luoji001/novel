# 价差 生成报告

slug：`aiyuce-20261021-218`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11537
LLM 调用：57 次，累计 210.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 检查LED灯泡电压 | 1903 | normal | 94.0 | 0 |  | 0 |
| 2 | 更新招聘JD的内容 | 2249 | normal | 36.2 | 0 |  | 2 |
| 3 | 修改报价单 | 1939 | normal | 35.8 | 0 |  | 1 |
| 4 | 整理库存与客户互动 | 2290 | normal | 35.1 | 0 |  | 1 |
| 5 | 查看显卡报价单 | 1924 | normal | 34.7 | 0 |  | 1 |
| 6 | 修改显卡标价 | 1226 | short | 86.0 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 31.6 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 6 句（如「如果有新的产品发布引起市场价格大幅下跌，那么即使…」）
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 11262
chapter_chars_mean: 1877
chapter_chars_median: 1892
chapter_chars_cv: 0.2
paragraphs_mean: 14.7
dialogue_chars_pct: 4.4
dialogue_para_pct: 14.2
interiority_para_pct: 20.7
narration_para_pct: 65.1
turn_under20_pct: 25.9
turn_over200_pct: 0.0
attr_say_pct: 60.3
attr_adv_pct: 100.8
scenes_per_chapter: 1.7
dialogue_run_mean: 2.3
turn_len_median: 34
```
