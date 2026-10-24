# 旧账本 生成报告

slug：`shuangwen-20261023-01`
档位：爽文　闸门模式：observe
章数：10　总字数：19538
LLM 调用：97 次，累计 456.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 计算器上的数字 | 1855 | normal | 39.2 | 0 |  | 3 |
| 2 | 计算器上的数字 | 1642 | normal | 92.3 | 0 |  | 2 |
| 3 | 旧账本的修改痕迹 | 1947 | normal | 37.2 | 0 |  | 3 |
| 4 | 签字笔的使用权 | 1733 | normal | 35.2 | 0 |  | 4 |
| 5 | 计算器上的数字 | 2164 | normal | 93.8 | 0 |  | 1 |
| 6 | 旧账本的修改痕迹 | 2113 | normal | 37.0 | 0 |  | 4 |
| 7 | 账本上的签名疑云 | 1955 | normal | 91.1 | 0 |  | 2 |
| 8 | 碎纸机的嗡鸣声 | 1843 | normal | 93.1 | 0 |  | 2 |
| 9 | 旧账本的修改痕迹 | 1852 | normal | 91.3 | 0 |  | 2 |
| 10 | 账本上的签名疑云 | 2424 | long | 91.1 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - 单条套路句式超限：「张国强的」×3
  - [observe] attr_adv_pct 36.4 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「张国强的」×3
  - [observe] 标题重复：「计算器上的数字」已存在
- 第 3 章：
  - 单条套路句式超限：「张国强的」×4
  - narration_para_pct 3.4 低于目标 5.0
  - [observe] attr_adv_pct 36.8 > 25.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「张国强的」×6、「带着一丝」×3
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 32 高于目标 14.0
  - [observe] attr_adv_pct 150.0 > 25.0（结构塌缩）
- 第 5 章：
  - [observe] 标题重复：「计算器上的数字」已存在
- 第 6 章：
  - 单条套路句式超限：「张国强的」×8
  - dialogue_run_mean 14.8 高于目标 14.0
  - [observe] attr_adv_pct 63.2 > 25.0（结构塌缩）
  - [observe] 标题重复：「旧账本的修改痕迹」已存在
- 第 7 章：
  - 单条套路句式超限：「张国强的」×6、「结账窗口」×3
  - attr_adv_pct 15.4 高于目标 12.0
- 第 8 章：
  - 单条套路句式超限：「张国强的」×3
  - attr_adv_pct 22.2 高于目标 12.0
- 第 9 章：
  - 单条套路句式超限：「张国强的」×4
  - [observe] 标题重复：「旧账本的修改痕迹」已存在
- 第 10 章：
  - 单条套路句式超限：「张国强的」×3
  - [observe] 标题重复：「账本上的签名疑云」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18413
chapter_chars_mean: 1841
chapter_chars_median: 1788
chapter_chars_cv: 0.12
paragraphs_mean: 47
dialogue_chars_pct: 47.6
dialogue_para_pct: 84.9
interiority_para_pct: 5.4
narration_para_pct: 9.7
turn_under20_pct: 78.1
turn_over200_pct: 0.0
attr_say_pct: 25.2
attr_adv_pct: 32.6
scenes_per_chapter: 1.3
dialogue_run_mean: 10.1
turn_len_median: 12
```
