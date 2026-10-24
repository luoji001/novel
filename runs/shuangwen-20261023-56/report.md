# 旧户籍档案 生成报告

slug：`shuangwen-20261023-56`
档位：爽文　闸门模式：observe
章数：10　总字数：19341
LLM 调用：97 次，累计 442.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一张房产证 | 1890 | normal | 98.5 | 0 |  | 1 |
| 2 | 签字笔洇开的墨迹 | 1485 | normal | 37.6 | 0 |  | 1 |
| 3 | 一张老照片 | 1719 | normal | 93.4 | 0 |  | 0 |
| 4 | 指纹压痕 | 2463 | normal | 90.9 | 0 |  | 2 |
| 5 | 墨迹消散 | 1835 | normal | 91.1 | 0 |  | 3 |
| 6 | 签字笔洇开的墨迹 | 2037 | normal | 91.5 | 0 |  | 3 |
| 7 | 指纹压痕 | 1854 | normal | 36.7 | 0 |  | 3 |
| 8 | 户籍档案风波 | 1918 | normal | 93.3 | 0 |  | 2 |
| 9 | 摩挲房产证边缘 | 1669 | normal | 93.5 | 0 |  | 2 |
| 10 | 户籍档案风波 | 2461 | long | 37.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 16.0 高于目标 12.0
- 第 2 章：
  - [observe] 章内自我复读 1 句（如「如果按照现有的人名登记的话，那么这份房产证是否还…」）
- 第 4 章：
  - 单条套路句式超限：「王振国的」×4
  - dialogue_run_mean 17 高于目标 14.0
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「王振国的」×3、「李国强的」×3
  - attr_adv_pct 16.7 高于目标 12.0
- 第 6 章：
  - 单条套路句式超限：「李国强的」×4
  - narration_para_pct 4.7 低于目标 5.0
  - [observe] 标题重复：「签字笔洇开的墨迹」已存在
- 第 7 章：
  - dialogue_run_mean 17.5 高于目标 14.0
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
  - [observe] 标题重复：「指纹压痕」已存在
- 第 8 章：
  - 单条套路句式超限：「李国强的」×4
  - narration_para_pct 2.6 低于目标 5.0
- 第 9 章：
  - narration_para_pct 3.3 低于目标 5.0
  - dialogue_run_mean 14.5 高于目标 14.0
- 第 10 章：
  - narration_para_pct 2.2 低于目标 5.0
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「户籍档案风波」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18383
chapter_chars_mean: 1838
chapter_chars_median: 1776
chapter_chars_cv: 0.17
paragraphs_mean: 39.3
dialogue_chars_pct: 50.2
dialogue_para_pct: 87.9
interiority_para_pct: 3.0
narration_para_pct: 9.1
turn_under20_pct: 65.9
turn_over200_pct: 0.0
attr_say_pct: 24.8
attr_adv_pct: 12.0
scenes_per_chapter: 1.7
dialogue_run_mean: 9.8
turn_len_median: 16
```
