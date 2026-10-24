# 旧名单 生成报告

slug：`shuangwen-20261023-02`
档位：爽文　闸门模式：observe
章数：10　总字数：18689
LLM 调用：97 次，累计 409.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 折痕里的名字 | 2133 | normal | 97.0 | 0 |  | 2 |
| 2 | 摩挲纸边的重量 | 2193 | normal | 93.3 | 0 |  | 0 |
| 3 | 撕碎证书的瞬间 | 1484 | normal | 37.7 | 0 |  | 1 |
| 4 | 画线的违约金条款 | 1768 | normal | 92.7 | 0 |  | 2 |
| 5 | 摩挲纸边的重量 | 1806 | normal | 94.4 | 0 |  | 1 |
| 6 | 摩挲纸边的重量 | 1737 | normal | 93.1 | 0 |  | 2 |
| 7 | 摩挲纸边的重量 | 1647 | normal | 92.9 | 0 |  | 1 |
| 8 | 握手的承诺 | 1810 | normal | 90.9 | 0 |  | 4 |
| 9 | 摩挲纸边的重量 | 1704 | normal | 94.4 | 0 |  | 1 |
| 10 | 摩挲纸边的重量 | 2397 | long | 93.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - narration_para_pct 4.8 低于目标 5.0
- 第 3 章：
  - [observe] attr_adv_pct 57.1 > 25.0（结构塌缩）
- 第 4 章：
  - attr_adv_pct 19.4 高于目标 12.0
  - dialogue_run_mean 17.7 高于目标 14.0
- 第 5 章：
  - [observe] 标题重复：「摩挲纸边的重量」已存在
- 第 6 章：
  - 单条套路句式超限：「市文化局」×3
  - [observe] 标题重复：「摩挲纸边的重量」已存在
- 第 7 章：
  - [observe] 标题重复：「摩挲纸边的重量」已存在
- 第 8 章：
  - dialogue_chars_pct 72.9 高于目标 70.0
  - narration_para_pct 4.5 低于目标 5.0
  - attr_adv_pct 21.9 高于目标 12.0
  - dialogue_run_mean 21 高于目标 14.0
- 第 9 章：
  - [observe] 标题重复：「摩挲纸边的重量」已存在
- 第 10 章：
  - [observe] 标题重复：「摩挲纸边的重量」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17649
chapter_chars_mean: 1765
chapter_chars_median: 1674
chapter_chars_cv: 0.15
paragraphs_mean: 44.1
dialogue_chars_pct: 52.4
dialogue_para_pct: 85.0
interiority_para_pct: 4.7
narration_para_pct: 10.4
turn_under20_pct: 72.1
turn_over200_pct: 0.0
attr_say_pct: 35.5
attr_adv_pct: 11.6
scenes_per_chapter: 1.9
dialogue_run_mean: 10.0
turn_len_median: 14
```
