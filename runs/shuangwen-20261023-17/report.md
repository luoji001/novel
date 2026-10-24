# 聘书 生成报告

slug：`shuangwen-20261023-17`
档位：爽文　闸门模式：observe
章数：10　总字数：18868
LLM 调用：97 次，累计 436.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 按手印 | 1733 | normal | 39.0 | 0 |  | 2 |
| 2 | 按手印 | 1781 | normal | 94.6 | 0 |  | 2 |
| 3 | 按手印 | 1681 | normal | 92.1 | 0 |  | 3 |
| 4 | 按手印 | 1871 | normal | 93.2 | 0 |  | 2 |
| 5 | 按手印 | 1892 | normal | 92.7 | 0 |  | 3 |
| 6 | 按手印 | 1700 | normal | 93.1 | 0 |  | 2 |
| 7 | 拍聘书 | 1943 | normal | 91.4 | 0 |  | 2 |
| 8 | 撕碎的工龄证明 | 1945 | normal | 89.8 | 0 |  | 4 |
| 9 | 按手印 | 1691 | normal | 94.0 | 0 |  | 3 |
| 10 | 拍聘书 | 2621 | long | 90.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「王小红站在」×3
  - [observe] attr_adv_pct 50.0 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「王小红的」×3
  - [observe] 标题重复：「按手印」已存在
- 第 3 章：
  - 命中套话收尾句
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「按手印」已存在
- 第 4 章：
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「按手印」已存在
- 第 5 章：
  - 单条套路句式超限：「王小红的」×3
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 标题重复：「按手印」已存在
- 第 6 章：
  - 单条套路句式超限：「王小红的」×4、「知道自己」×3
  - [observe] 标题重复：「按手印」已存在
- 第 7 章：
  - attr_adv_pct 18.2 高于目标 12.0
  - dialogue_run_mean 18.5 高于目标 14.0
- 第 8 章：
  - 命中套话收尾句
  - 单条套路句式超限：「王小红站在」×3
  - dialogue_chars_pct 28.8 低于目标 30.0
  - attr_adv_pct 20.0 高于目标 12.0
- 第 9 章：
  - narration_para_pct 4.9 低于目标 5.0
  - attr_adv_pct 23.8 高于目标 12.0
  - [observe] 标题重复：「按手印」已存在
- 第 10 章：
  - [observe] 标题重复：「拍聘书」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17948
chapter_chars_mean: 1795
chapter_chars_median: 1736
chapter_chars_cv: 0.15
paragraphs_mean: 39.8
dialogue_chars_pct: 46.3
dialogue_para_pct: 82.2
interiority_para_pct: 6.1
narration_para_pct: 11.6
turn_under20_pct: 71.4
turn_over200_pct: 0.0
attr_say_pct: 20.0
attr_adv_pct: 15.1
scenes_per_chapter: 1.7
dialogue_run_mean: 8.4
turn_len_median: 13
```
