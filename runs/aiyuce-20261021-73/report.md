# 纸笔 生成报告

slug：`aiyuce-20261021-73`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11646
LLM 调用：55 次，累计 211.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 分析客户订单记录 | 2156 | normal | 97.5 | 0 |  | 0 |
| 2 | 点击鼠标查看价格历史 | 2308 | normal | 36.8 | 0 |  | 1 |
| 3 | 翻阅订单记录 | 2105 | normal | 35.5 | 0 |  | 1 |
| 4 | 翻看设备折旧表 | 2001 | normal | 35.8 | 0 |  | 1 |
| 5 | 翻看问卷数据 | 2144 | normal | 35.4 | 0 |  | 3 |
| 6 | 停顿在价格数据点 | 926 | short | 92.3 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 4 章：
  - [observe] 章内自我复读 3 句（如「他知道，如果不能提高打印效率，那么到了学期末，当…」）
- 第 5 章：
  - 命中套话收尾句
  - narration_para_pct 43.8 低于目标 45.0
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 11385
chapter_chars_mean: 1898
chapter_chars_median: 2082
chapter_chars_cv: 0.26
paragraphs_mean: 13.5
dialogue_chars_pct: 4.8
dialogue_para_pct: 23.6
interiority_para_pct: 17.7
narration_para_pct: 58.8
turn_under20_pct: 80.1
turn_over200_pct: 0.0
attr_say_pct: 32.6
attr_adv_pct: 6.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.8
turn_len_median: 10
```
