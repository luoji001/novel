# 计费器 生成报告

slug：`aiyuce-20261021-270`
档位：AI 推演　闸门模式：observe
章数：6　总字数：12299
LLM 调用：57 次，累计 219.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 计算报价单上的数字 | 2343 | normal | 95.2 | 0 |  | 1 |
| 2 | 核对电费单与数据 | 2052 | normal | 36.0 | 0 |  | 1 |
| 3 | 核对招聘JD内容 | 2063 | normal | 35.8 | 0 |  | 1 |
| 4 | 核对合同修订内容 | 1914 | normal | 35.9 | 0 |  | 1 |
| 5 | 核对服务器折旧数据 | 2522 | normal | 85.0 | 0 |  | 1 |
| 6 | 核对报价单与电费单 | 1399 | short | 34.8 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 44.4 低于目标 45.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 2 句（如「如果某位技术人员能够在短时间内研发出自研模型并且…」）
- 第 5 章：
  - interiority_para_pct 53.3 高于目标 40.0
- 第 6 章：
  - [observe] 章内自我复读 3 句（如「毕竟没有任何一项投资能够真正脱离其背后的财务结构…」）

## 整书结构指标

```
chapters: 6
total_chars: 12038
chapter_chars_mean: 2006
chapter_chars_median: 2014
chapter_chars_cv: 0.19
paragraphs_mean: 13
dialogue_chars_pct: 3.3
dialogue_para_pct: 19.6
interiority_para_pct: 29.8
narration_para_pct: 50.6
turn_under20_pct: 71.0
turn_over200_pct: 0.0
attr_say_pct: 8.0
attr_adv_pct: 0.0
scenes_per_chapter: 1
dialogue_run_mean: 1.3
turn_len_median: 12
```
