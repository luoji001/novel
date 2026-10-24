# 老客户名单 生成报告

slug：`shuangwen-20261023-142`
档位：爽文　闸门模式：observe
章数：10　总字数：19331
LLM 调用：97 次，累计 410.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 翻阅客户名单 | 2001 | normal | 95.6 | 0 |  | 1 |
| 2 | 翻阅客户名单 | 1770 | normal | 90.9 | 0 |  | 4 |
| 3 | 签署新合同 | 1956 | normal | 93.5 | 0 |  | 2 |
| 4 | 翻阅客户名单 | 1994 | normal | 92.6 | 0 |  | 2 |
| 5 | 抚摸印章边缘 | 1971 | normal | 92.2 | 0 |  | 0 |
| 6 | 抚摸印章边缘 | 1673 | normal | 92.9 | 0 |  | 3 |
| 7 | 翻阅客户名单 | 1685 | normal | 91.9 | 0 |  | 2 |
| 8 | 翻阅客户名单 | 2141 | normal | 93.8 | 0 |  | 1 |
| 9 | 抚摸账本边缘 | 1880 | normal | 90.2 | 0 |  | 1 |
| 10 | 翻阅客户名单 | 2250 | long | 92.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「他知道这」×3
- 第 2 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
  - dialogue_run_mean 20 高于目标 14.0
  - [observe] 标题重复：「翻阅客户名单」已存在
- 第 3 章：
  - 单条套路句式超限：「说道“我」×3、「李建平的」×3
  - attr_adv_pct 14.3 高于目标 12.0
- 第 4 章：
  - narration_para_pct 0.0 低于目标 5.0
  - [observe] 标题重复：「翻阅客户名单」已存在
- 第 6 章：
  - narration_para_pct 2.9 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「抚摸印章边缘」已存在
- 第 7 章：
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「翻阅客户名单」已存在
- 第 8 章：
  - [observe] 标题重复：「翻阅客户名单」已存在
- 第 9 章：
  - [observe] 标题与《抚摸印章边缘》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 10 章：
  - attr_adv_pct 13.6 高于目标 12.0
  - [observe] 标题重复：「翻阅客户名单」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18396
chapter_chars_mean: 1840
chapter_chars_median: 1858
chapter_chars_cv: 0.1
paragraphs_mean: 39.3
dialogue_chars_pct: 50.9
dialogue_para_pct: 86.8
interiority_para_pct: 5.5
narration_para_pct: 7.7
turn_under20_pct: 61.4
turn_over200_pct: 0.0
attr_say_pct: 14.1
attr_adv_pct: 11.2
scenes_per_chapter: 1.8
dialogue_run_mean: 9.4
turn_len_median: 16
```
