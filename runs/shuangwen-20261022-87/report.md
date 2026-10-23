# 磅单 生成报告

slug：`shuangwen-20261022-87`
档位：爽文　闸门模式：observe
章数：10　总字数：19636
LLM 调用：97 次，累计 433.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 工牌上的凹陷痕迹 | 1999 | normal | 98.1 | 0 |  | 1 |
| 2 | 敲打桌面的手指 | 1857 | normal | 92.5 | 0 |  | 0 |
| 3 | 敲打桌面的手指 | 1817 | normal | 92.7 | 0 |  | 3 |
| 4 | 敲打桌面的手指 | 1860 | normal | 93.9 | 0 |  | 1 |
| 5 | 敲打桌面的手指 | 1947 | normal | 93.0 | 0 |  | 3 |
| 6 | 拍桌反驳 | 2122 | normal | 36.6 | 0 |  | 3 |
| 7 | 拍桌反驳 | 1995 | normal | 36.4 | 0 |  | 3 |
| 8 | 敲打桌面的手指 | 2030 | normal | 92.5 | 0 |  | 2 |
| 9 | 敲打桌面的手指 | 1802 | normal | 37.0 | 0 |  | 3 |
| 10 | 拍桌反驳 | 2197 | long | 92.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 25.0 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「李国强的」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「敲打桌面的手指」已存在
- 第 4 章：
  - [observe] 标题重复：「敲打桌面的手指」已存在
- 第 5 章：
  - 单条套路句式超限：「李国强的」×4
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「敲打桌面的手指」已存在
- 第 6 章：
  - narration_para_pct 3.6 低于目标 5.0
  - dialogue_run_mean 17.7 高于目标 14.0
  - [observe] attr_adv_pct 29.2 > 25.0（结构塌缩）
- 第 7 章：
  - 单条套路句式超限：「李国强的」×6
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
  - [observe] 标题重复：「拍桌反驳」已存在
- 第 8 章：
  - narration_para_pct 2.8 低于目标 5.0
  - [observe] 标题重复：「敲打桌面的手指」已存在
- 第 9 章：
  - 单条套路句式超限：「李国强的」×9
  - [observe] attr_adv_pct 27.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「敲打桌面的手指」已存在
- 第 10 章：
  - 单条套路句式超限：「李国强的」×5
  - [observe] 标题重复：「拍桌反驳」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18649
chapter_chars_mean: 1865
chapter_chars_median: 1853
chapter_chars_cv: 0.07
paragraphs_mean: 41.7
dialogue_chars_pct: 49.2
dialogue_para_pct: 85.6
interiority_para_pct: 4.3
narration_para_pct: 10.1
turn_under20_pct: 64.0
turn_over200_pct: 0.0
attr_say_pct: 29.6
attr_adv_pct: 16.7
scenes_per_chapter: 1.7
dialogue_run_mean: 7.7
turn_len_median: 15
```
