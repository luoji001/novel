# 秤杆 生成报告

slug：`shuangwen-20261023-79`
档位：爽文　闸门模式：observe
章数：10　总字数：17746
LLM 调用：97 次，累计 387.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 电子秤的跳动 | 1590 | normal | 97.5 | 0 |  | 0 |
| 2 | 签字笔的裂痕 | 1988 | normal | 92.7 | 0 |  | 2 |
| 3 | 签字纸的签署 | 1973 | normal | 91.8 | 0 |  | 2 |
| 4 | 假磅单的真相 | 1799 | normal | 91.7 | 0 |  | 2 |
| 5 | 签字纸的签署 | 2124 | normal | 89.7 | 0 |  | 3 |
| 6 | 划线的监控录像 | 1277 | normal | 93.4 | 0 |  | 2 |
| 7 | 签字笔的裂痕 | 1552 | normal | 91.5 | 0 |  | 1 |
| 8 | 签字纸的签署 | 1574 | normal | 36.6 | 0 |  | 2 |
| 9 | 原始记录的较量 | 1703 | normal | 90.5 | 0 |  | 1 |
| 10 | 电子秤的跳动 | 2156 | long | 92.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「过磅房」×3
  - attr_adv_pct 25.0 高于目标 12.0
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×4
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「过磅房」×3
- 第 5 章：
  - 单条套路句式超限：「他知道自己」×3、「陈志远的」×3
  - attr_adv_pct 13.0 高于目标 12.0
  - [observe] 标题重复：「签字纸的签署」已存在
- 第 6 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
- 第 7 章：
  - [observe] 标题重复：「签字笔的裂痕」已存在
- 第 8 章：
  - [observe] attr_adv_pct 45.5 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字纸的签署」已存在
- 第 9 章：
  - attr_adv_pct 16.7 高于目标 12.0
- 第 10 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「电子秤的跳动」已存在

## 整书结构指标

```
chapters: 10
total_chars: 16745
chapter_chars_mean: 1674
chapter_chars_median: 1646
chapter_chars_cv: 0.17
paragraphs_mean: 42.4
dialogue_chars_pct: 45.0
dialogue_para_pct: 79.7
interiority_para_pct: 6.1
narration_para_pct: 14.2
turn_under20_pct: 77.0
turn_over200_pct: 0.0
attr_say_pct: 29.6
attr_adv_pct: 12.8
scenes_per_chapter: 1.9
dialogue_run_mean: 5.2
turn_len_median: 12
```
