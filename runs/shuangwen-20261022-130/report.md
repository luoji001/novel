# 签笔 生成报告

slug：`shuangwen-20261022-130`
档位：爽文　闸门模式：observe
章数：10　总字数：18734
LLM 调用：97 次，累计 413.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 合同副本在手 | 1813 | normal | 98.2 | 0 |  | 0 |
| 2 | 签字笔敲桌面 | 2073 | normal | 36.2 | 0 |  | 1 |
| 3 | 签字笔敲桌面 | 1919 | normal | 92.0 | 0 |  | 1 |
| 4 | 签字笔敲桌面 | 1961 | normal | 92.8 | 0 |  | 1 |
| 5 | 指纹在纸上 | 1590 | normal | 96.5 | 0 |  | 2 |
| 6 | 签字笔敲桌面 | 1578 | normal | 90.5 | 0 |  | 2 |
| 7 | 职级证书递过去 | 1627 | normal | 93.7 | 0 |  | 2 |
| 8 | 签字笔敲桌面 | 2267 | normal | 94.2 | 0 |  | 2 |
| 9 | 承诺书在手 | 1597 | normal | 95.4 | 0 |  | 1 |
| 10 | 签字笔敲桌面 | 2299 | long | 37.3 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - [observe] 章内自我复读 1 句（如「他相信，只要继续努力下去，总有一天能够彻底打破眼…」）
- 第 3 章：
  - [observe] 标题重复：「签字笔敲桌面」已存在
- 第 4 章：
  - [observe] 标题重复：「签字笔敲桌面」已存在
- 第 5 章：
  - 单条套路句式超限：「张国强的」×4
  - narration_para_pct 3.1 低于目标 5.0
- 第 6 章：
  - 单条套路句式超限：「张国强的」×5
  - [observe] 标题重复：「签字笔敲桌面」已存在
- 第 7 章：
  - 单条套路句式超限：「张国强的」×3
  - attr_adv_pct 22.2 高于目标 12.0
- 第 8 章：
  - 单条套路句式超限：「“李建军你」×5
  - [observe] 标题重复：「签字笔敲桌面」已存在
- 第 9 章：
  - 单条套路句式超限：「他知道这」×3
- 第 10 章：
  - narration_para_pct 3.8 低于目标 5.0
  - [observe] attr_adv_pct 29.4 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔敲桌面」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17841
chapter_chars_mean: 1784
chapter_chars_median: 1790
chapter_chars_cv: 0.15
paragraphs_mean: 37.1
dialogue_chars_pct: 46.8
dialogue_para_pct: 82.1
interiority_para_pct: 6.7
narration_para_pct: 11.2
turn_under20_pct: 60.0
turn_over200_pct: 0.0
attr_say_pct: 26.7
attr_adv_pct: 8.0
scenes_per_chapter: 2.3
dialogue_run_mean: 6.4
turn_len_median: 16
```
