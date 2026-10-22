# 玉简 生成报告

slug：`shuangwen-20261022-31`
档位：爽文　闸门模式：observe
章数：10　总字数：19028
LLM 调用：97 次，累计 378.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 玉简微光初现 | 1665 | normal | 99.0 | 0 |  | 1 |
| 2 | 玉简与玉筒相触 | 1787 | normal | 91.4 | 0 |  | 2 |
| 3 | 玉简微光初现 | 2499 | normal | 37.0 | 0 |  | 2 |
| 4 | 灵石入账 | 1546 | normal | 93.1 | 0 |  | 0 |
| 5 | 玉简入匣 | 1656 | normal | 92.3 | 0 |  | 2 |
| 6 | 玉简轻触账簿边沿 | 1701 | normal | 87.8 | 0 |  | 3 |
| 7 | 玉简盖上印章 | 2141 | normal | 93.9 | 0 |  | 0 |
| 8 | 玉简轻触账簿边沿 | 1940 | normal | 93.8 | 0 |  | 2 |
| 9 | 玉简入匣 | 1654 | normal | 93.9 | 0 |  | 1 |
| 10 | 玉简轻触账簿边沿 | 2429 | long | 93.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李长风的」×6
- 第 2 章：
  - 单条套路句式超限：「点了点头」×4、「他知道这」×3
  - attr_adv_pct 20.0 高于目标 12.0
- 第 3 章：
  - [observe] attr_adv_pct 29.2 > 25.0（结构塌缩）
  - [observe] 标题重复：「玉简微光初现」已存在
- 第 5 章：
  - narration_para_pct 3.2 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
- 第 6 章：
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 25.0 高于目标 12.0
  - dialogue_run_mean 33 高于目标 14.0
- 第 8 章：
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「玉简轻触账簿边沿」已存在
- 第 9 章：
  - [observe] 标题重复：「玉简入匣」已存在
- 第 10 章：
  - [observe] 标题重复：「玉简轻触账簿边沿」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17953
chapter_chars_mean: 1795
chapter_chars_median: 1658
chapter_chars_cv: 0.18
paragraphs_mean: 46.2
dialogue_chars_pct: 51.6
dialogue_para_pct: 84.5
interiority_para_pct: 6.1
narration_para_pct: 9.4
turn_under20_pct: 69.6
turn_over200_pct: 0.0
attr_say_pct: 21.5
attr_adv_pct: 13.2
scenes_per_chapter: 1.9
dialogue_run_mean: 9.5
turn_len_median: 14
```
