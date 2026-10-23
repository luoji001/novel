# 副本 生成报告

slug：`shuangwen-20261022-143`
档位：爽文　闸门模式：observe
章数：10　总字数：19170
LLM 调用：97 次，累计 411.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 一张空白印章 | 1676 | normal | 38.6 | 0 |  | 2 |
| 2 | 签字笔上的墨迹 | 1796 | normal | 92.5 | 0 |  | 1 |
| 3 | 一叠文件被拍响 | 1998 | normal | 94.1 | 0 |  | 1 |
| 4 | 一张撕裂的纸张 | 2084 | normal | 37.5 | 0 |  | 1 |
| 5 | 一张泛黄的副本 | 2022 | normal | 91.7 | 0 |  | 2 |
| 6 | 一份泛黄的副本 | 1761 | normal | 92.1 | 0 |  | 3 |
| 7 | 一份泛黄的副本 | 1854 | normal | 92.9 | 0 |  | 1 |
| 8 | 签字笔上的墨迹 | 1591 | normal | 37.7 | 0 |  | 2 |
| 9 | 一份完整备案 | 2055 | normal | 93.7 | 0 |  | 1 |
| 10 | 一份泛黄的副本 | 2323 | long | 93.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李国强的」×3
  - [observe] attr_adv_pct 42.9 > 25.0（结构塌缩）
- 第 2 章：
  - 命中套话收尾句
- 第 3 章：
  - attr_adv_pct 19.0 高于目标 12.0
- 第 4 章：
  - [observe] attr_adv_pct 60.0 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「李国强的」×6、「点了点头」×3
  - attr_adv_pct 20.0 高于目标 12.0
- 第 6 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 19 高于目标 14.0
  - [observe] 标题与《一张泛黄的副本》近似 0.86 ≥ 0.6（换个角度，别只换一个词）
- 第 7 章：
  - [observe] 标题重复：「一份泛黄的副本」已存在
- 第 8 章：
  - [observe] attr_adv_pct 26.7 > 25.0（结构塌缩）
  - [observe] 标题重复：「签字笔上的墨迹」已存在
- 第 9 章：
  - attr_adv_pct 15.0 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「点了点头“」×4
  - [observe] 标题重复：「一份泛黄的副本」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18218
chapter_chars_mean: 1822
chapter_chars_median: 1838
chapter_chars_cv: 0.12
paragraphs_mean: 39.7
dialogue_chars_pct: 52.1
dialogue_para_pct: 87.3
interiority_para_pct: 4.8
narration_para_pct: 7.9
turn_under20_pct: 64.6
turn_over200_pct: 0.0
attr_say_pct: 26.8
attr_adv_pct: 20.2
scenes_per_chapter: 1.7
dialogue_run_mean: 8.6
turn_len_median: 14
```
