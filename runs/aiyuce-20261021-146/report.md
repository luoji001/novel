# 显卡折旧 生成报告

slug：`aiyuce-20261021-146`
档位：AI 推演　闸门模式：observe
章数：6　总字数：11980
LLM 调用：57 次，累计 217.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 核对租金账单 | 2631 | normal | 38.2 | 0 |  | 2 |
| 2 | 核对税务申报表 | 1910 | normal | 92.2 | 0 |  | 1 |
| 3 | 核对招聘JD | 1707 | normal | 36.6 | 0 |  | 1 |
| 4 | 核对推理报价单 | 2561 | normal | 36.6 | 0 |  | 1 |
| 5 | 核对电费单 | 1743 | normal | 91.2 | 0 |  | 1 |
| 6 | 核对折旧表 | 1422 | short | 35.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 36.8 低于目标 45.0
  - [observe] 章内自我复读 6 句（如「他知道要想在这个竞争激烈的市场里站稳脚跟，就必须…」）
- 第 2 章：
  - narration_para_pct 25.0 低于目标 45.0
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「他深知，如果没有足够的人力支持，店铺的运转效率会…」）
- 第 4 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）
- 第 5 章：
  - dialogue_chars_pct 19.1 高于目标 18.0
- 第 6 章：
  - [observe] 章内自我复读 1 句（如「这条推论会被什么推翻…」）

## 整书结构指标

```
chapters: 6
total_chars: 11704
chapter_chars_mean: 1951
chapter_chars_median: 1782
chapter_chars_cv: 0.25
paragraphs_mean: 15.5
dialogue_chars_pct: 9.9
dialogue_para_pct: 33.8
interiority_para_pct: 16.4
narration_para_pct: 49.8
turn_under20_pct: 50.4
turn_over200_pct: 0.0
attr_say_pct: 14.6
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.9
turn_len_median: 22
```
