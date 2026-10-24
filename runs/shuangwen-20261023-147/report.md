# 旧账本 生成报告

slug：`shuangwen-20261023-147`
档位：爽文　闸门模式：observe
章数：10　总字数：17813
LLM 调用：97 次，累计 429.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 账本入怀 | 1687 | normal | 99.8 | 0 |  | 0 |
| 2 | 族谱翻页 | 1783 | normal | 37.3 | 0 |  | 2 |
| 3 | 账本入怀 | 1778 | normal | 92.8 | 0 |  | 2 |
| 4 | 账本摊开 | 1836 | normal | 93.5 | 0 |  | 1 |
| 5 | 账本摊开 | 1716 | normal | 93.9 | 0 |  | 2 |
| 6 | 账本摊开 | 1689 | normal | 37.2 | 0 |  | 4 |
| 7 | 账本摊开 | 1699 | normal | 93.7 | 0 |  | 3 |
| 8 | 账本摊开 | 1624 | normal | 93.6 | 0 |  | 3 |
| 9 | 账本摊开 | 1805 | normal | 94.4 | 0 |  | 2 |
| 10 | 账本摊开 | 2186 | long | 36.8 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「周德昌的」×6、「他知道这」×4
  - [observe] 章内自我复读 1 句（如「他知道，这场较量才刚刚开始…」）
- 第 3 章：
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「账本入怀」已存在
- 第 4 章：
  - 单条套路句式超限：「周德昌的」×8
- 第 5 章：
  - attr_adv_pct 23.1 高于目标 12.0
  - [observe] 标题重复：「账本摊开」已存在
- 第 6 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周德昌的」×6
  - [observe] attr_adv_pct 60.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「账本摊开」已存在
- 第 7 章：
  - 单条套路句式超限：「周怀远的」×3
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「账本摊开」已存在
- 第 8 章：
  - narration_para_pct 2.1 低于目标 5.0
  - dialogue_run_mean 14.7 高于目标 14.0
  - [observe] 标题重复：「账本摊开」已存在
- 第 9 章：
  - 单条套路句式超限：「微微一笑」×3
  - [observe] 标题重复：「账本摊开」已存在
- 第 10 章：
  - 单条套路句式超限：「周德昌的」×9、「周怀远的」×3
  - [observe] 章内自我复读 4 句（如「他说，“但我也希望你能明白，有些事情并不是那么简…」）
  - [observe] 标题重复：「账本摊开」已存在

## 整书结构指标

```
chapters: 10
total_chars: 16821
chapter_chars_mean: 1682
chapter_chars_median: 1644
chapter_chars_cv: 0.09
paragraphs_mean: 40.8
dialogue_chars_pct: 47.5
dialogue_para_pct: 82.3
interiority_para_pct: 6.6
narration_para_pct: 11.0
turn_under20_pct: 75.4
turn_over200_pct: 0.0
attr_say_pct: 17.2
attr_adv_pct: 14.8
scenes_per_chapter: 1.5
dialogue_run_mean: 7.4
turn_len_median: 12
```
