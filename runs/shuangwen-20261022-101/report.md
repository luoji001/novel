# 旧账本 生成报告

slug：`shuangwen-20261022-101`
档位：爽文　闸门模式：observe
章数：10　总字数：19646
LLM 调用：97 次，累计 442.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 签字笔的重量 | 2147 | normal | 100.0 | 0 |  | 0 |
| 2 | 计算器的数字 | 2188 | normal | 94.6 | 0 |  | 1 |
| 3 | 账本摊开的瞬间 | 1866 | normal | 90.5 | 0 |  | 1 |
| 4 | 账本摊开的瞬间 | 1741 | normal | 91.6 | 0 |  | 3 |
| 5 | 账本摊开的瞬间 | 1682 | normal | 87.5 | 0 |  | 3 |
| 6 | 账本摊开的瞬间 | 1903 | normal | 93.7 | 0 |  | 1 |
| 7 | 账本摊开的瞬间 | 1838 | normal | 92.5 | 0 |  | 2 |
| 8 | 账本摊开的瞬间 | 1769 | normal | 36.7 | 0 |  | 5 |
| 9 | 账本摊开的瞬间 | 2006 | normal | 93.7 | 0 |  | 2 |
| 10 | 账本摊开的瞬间 | 2496 | long | 92.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - attr_adv_pct 18.8 高于目标 12.0
- 第 3 章：
  - dialogue_run_mean 21 高于目标 14.0
- 第 4 章：
  - 单条套路句式超限：「陈志远的」×3
  - dialogue_run_mean 14.7 高于目标 14.0
  - [observe] 标题重复：「账本摊开的瞬间」已存在
- 第 5 章：
  - narration_para_pct 0.0 低于目标 5.0
  - dialogue_run_mean 28 高于目标 14.0
  - [observe] 标题重复：「账本摊开的瞬间」已存在
- 第 6 章：
  - [observe] 标题重复：「账本摊开的瞬间」已存在
- 第 7 章：
  - attr_adv_pct 15.4 高于目标 12.0
  - [observe] 标题重复：「账本摊开的瞬间」已存在
- 第 8 章：
  - 单条套路句式超限：「带着一丝」×3
  - attr_adv_pct 13.3 高于目标 12.0
  - dialogue_run_mean 17.5 高于目标 14.0
  - [observe] 章内自我复读 2 句（如「陈老板，你是不是有什么事瞒着我们？…」）
  - [observe] 标题重复：「账本摊开的瞬间」已存在
- 第 9 章：
  - 单条套路句式超限：「周海峰的」×3、「陈志远的」×3
  - [observe] 标题重复：「账本摊开的瞬间」已存在
- 第 10 章：
  - narration_para_pct 4.8 低于目标 5.0
  - attr_adv_pct 19.0 高于目标 12.0
  - [observe] 标题重复：「账本摊开的瞬间」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18548
chapter_chars_mean: 1855
chapter_chars_median: 1768
chapter_chars_cv: 0.13
paragraphs_mean: 45.8
dialogue_chars_pct: 53.7
dialogue_para_pct: 89.4
interiority_para_pct: 4.0
narration_para_pct: 6.6
turn_under20_pct: 71.9
turn_over200_pct: 0.0
attr_say_pct: 27.1
attr_adv_pct: 11.2
scenes_per_chapter: 1.7
dialogue_run_mean: 12.9
turn_len_median: 14
```
