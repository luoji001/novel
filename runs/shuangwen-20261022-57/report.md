# 旧凭牌 生成报告

slug：`shuangwen-20261022-57`
档位：爽文　闸门模式：observe
章数：10　总字数：19277
LLM 调用：97 次，累计 427.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 递出死亡证明 | 1984 | normal | 98.4 | 0 |  | 2 |
| 2 | 父亲的旧凭牌 | 1775 | normal | 91.1 | 0 |  | 1 |
| 3 | 递出死亡证明 | 1745 | normal | 92.5 | 0 |  | 2 |
| 4 | 递出死亡证明 | 1852 | normal | 91.6 | 0 |  | 2 |
| 5 | 递出旧凭牌 | 1873 | normal | 91.1 | 0 |  | 1 |
| 6 | 撕去登记册封面 | 1712 | normal | 92.7 | 0 |  | 2 |
| 7 | 递出旧凭牌 | 2463 | normal | 93.1 | 0 |  | 2 |
| 8 | 递出旧凭牌 | 1804 | normal | 89.6 | 0 |  | 2 |
| 9 | 旧凭牌轻叩桌面 | 1766 | normal | 90.6 | 0 |  | 2 |
| 10 | 旧凭牌轻叩桌面 | 2293 | long | 92.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「王铁山的」×6
  - dialogue_chars_pct 29.9 低于目标 30.0
- 第 2 章：
  - 单条套路句式超限：「王铁山的」×5
- 第 3 章：
  - 单条套路句式超限：「王铁山的」×6
  - [observe] 标题重复：「递出死亡证明」已存在
- 第 4 章：
  - 单条套路句式超限：「山门登记处」×7
  - [observe] 标题重复：「递出死亡证明」已存在
- 第 5 章：
  - 单条套路句式超限：「他知道这」×4
- 第 6 章：
  - 单条套路句式超限：「王铁山的」×6
  - attr_adv_pct 23.1 高于目标 12.0
- 第 7 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「递出旧凭牌」已存在
- 第 8 章：
  - 命中套话收尾句
  - [observe] 标题重复：「递出旧凭牌」已存在
- 第 9 章：
  - 单条套路句式超限：「王铁山的」×3
  - attr_adv_pct 22.2 高于目标 12.0
- 第 10 章：
  - 单条套路句式超限：「点了点头」×3
  - [observe] 标题重复：「旧凭牌轻叩桌面」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18335
chapter_chars_mean: 1834
chapter_chars_median: 1748
chapter_chars_cv: 0.13
paragraphs_mean: 39.5
dialogue_chars_pct: 43.3
dialogue_para_pct: 79.3
interiority_para_pct: 7.1
narration_para_pct: 13.6
turn_under20_pct: 66.6
turn_over200_pct: 0.0
attr_say_pct: 23.6
attr_adv_pct: 9.6
scenes_per_chapter: 1.7
dialogue_run_mean: 5.1
turn_len_median: 14
```
