# 副本 生成报告

slug：`shuangwen-20261023-94`
档位：爽文　闸门模式：observe
章数：10　总字数：18811
LLM 调用：97 次，累计 421.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 合同副本的折痕 | 1869 | normal | 98.3 | 0 |  | 2 |
| 2 | 合同副本的折痕 | 1991 | normal | 36.6 | 0 |  | 2 |
| 3 | 展开旧合同 | 1833 | normal | 90.9 | 0 |  | 3 |
| 4 | 合同副本的折痕 | 1698 | normal | 90.2 | 0 |  | 1 |
| 5 | 合同副本的折痕 | 1671 | normal | 90.7 | 0 |  | 2 |
| 6 | 签协议的手势 | 1573 | normal | 93.6 | 0 |  | 1 |
| 7 | 签字时的红印 | 1762 | normal | 92.0 | 0 |  | 1 |
| 8 | 合同副本的折痕 | 1821 | normal | 37.4 | 0 |  | 3 |
| 9 | 碎纸机吞文件 | 2004 | normal | 94.3 | 0 |  | 2 |
| 10 | 证件摊开的瞬间 | 2579 | long | 92.9 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李振国的」×8
  - attr_adv_pct 20.0 高于目标 12.0
- 第 2 章：
  - [observe] 章内自我复读 6 句（如「就在这一刻，走廊尽头的门被推开了一条缝，一道瘦长…」）
  - [observe] 标题重复：「合同副本的折痕」已存在
- 第 3 章：
  - narration_para_pct 2.2 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
  - dialogue_run_mean 22.5 高于目标 14.0
- 第 4 章：
  - [observe] 标题重复：「合同副本的折痕」已存在
- 第 5 章：
  - 单条套路句式超限：「李振国的」×4
  - [observe] 标题重复：「合同副本的折痕」已存在
- 第 6 章：
  - 单条套路句式超限：「李振国的」×3
- 第 7 章：
  - 单条套路句式超限：「李振国的」×3
- 第 8 章：
  - narration_para_pct 4.7 低于目标 5.0
  - [observe] attr_adv_pct 38.5 > 25.0（结构塌缩）
  - [observe] 标题重复：「合同副本的折痕」已存在
- 第 9 章：
  - 单条套路句式超限：「李振国的」×5
  - attr_adv_pct 13.3 高于目标 12.0

## 整书结构指标

```
chapters: 10
total_chars: 17878
chapter_chars_mean: 1788
chapter_chars_median: 1724
chapter_chars_cv: 0.15
paragraphs_mean: 38.9
dialogue_chars_pct: 51.8
dialogue_para_pct: 85.8
interiority_para_pct: 3.5
narration_para_pct: 10.7
turn_under20_pct: 63.4
turn_over200_pct: 0.0
attr_say_pct: 19.0
attr_adv_pct: 10.6
scenes_per_chapter: 1.7
dialogue_run_mean: 8.5
turn_len_median: 14
```
