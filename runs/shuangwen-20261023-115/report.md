# 验收单 生成报告

slug：`shuangwen-20261023-115`
档位：爽文　闸门模式：observe
章数：10　总字数：18130
LLM 调用：97 次，累计 404.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧版清单被丢弃 | 1577 | normal | 98.3 | 0 |  | 1 |
| 2 | 递回旧版设备清单 | 1830 | normal | 93.4 | 0 |  | 2 |
| 3 | 递回旧版设备清单 | 1996 | normal | 93.7 | 0 |  | 4 |
| 4 | 递回旧版设备清单 | 1440 | normal | 93.7 | 0 |  | 4 |
| 5 | 清单与报告的对峙 | 1700 | normal | 92.5 | 0 |  | 0 |
| 6 | 旧版清单被紧握 | 1823 | normal | 92.2 | 0 |  | 1 |
| 7 | 撕角验收单 | 1870 | normal | 93.3 | 0 |  | 1 |
| 8 | 递回旧版设备清单 | 1540 | normal | 94.4 | 0 |  | 1 |
| 9 | 递回旧版设备清单 | 1928 | normal | 91.0 | 0 |  | 3 |
| 10 | 旧版清单被紧握 | 2416 | long | 93.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林晓阳的」×6
- 第 2 章：
  - narration_para_pct 2.6 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 22.2 高于目标 12.0
  - [observe] 标题重复：「递回旧版设备清单」已存在
- 第 4 章：
  - 单条套路句式超限：「周振国的」×3
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题重复：「递回旧版设备清单」已存在
- 第 6 章：
  - [observe] 标题与《旧版清单被丢弃》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - narration_para_pct 2.8 低于目标 5.0
- 第 8 章：
  - [observe] 标题重复：「递回旧版设备清单」已存在
- 第 9 章：
  - 单条套路句式超限：「周振国的」×4、「林晓阳的」×4
  - narration_para_pct 3.2 低于目标 5.0
  - [observe] 标题重复：「递回旧版设备清单」已存在
- 第 10 章：
  - 命中套话收尾句
  - [observe] 标题重复：「旧版清单被紧握」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17286
chapter_chars_mean: 1729
chapter_chars_median: 1748
chapter_chars_cv: 0.16
paragraphs_mean: 34
dialogue_chars_pct: 49.9
dialogue_para_pct: 86.2
interiority_para_pct: 5.9
narration_para_pct: 8.0
turn_under20_pct: 63.0
turn_over200_pct: 0.0
attr_say_pct: 16.4
attr_adv_pct: 7.1
scenes_per_chapter: 1.4
dialogue_run_mean: 7.5
turn_len_median: 14
```
