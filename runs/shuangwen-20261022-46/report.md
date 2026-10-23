# 旧车票 生成报告

slug：`shuangwen-20261022-46`
档位：爽文　闸门模式：observe
章数：10　总字数：19731
LLM 调用：97 次，累计 374.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕开欠条 | 1735 | normal | 100.0 | 0 |  | 1 |
| 2 | 撕开旧车票 | 2023 | normal | 37.6 | 0 |  | 3 |
| 3 | 摩挲账本 | 2256 | normal | 92.5 | 0 |  | 2 |
| 4 | 摩挲纸边 | 2099 | normal | 37.9 | 0 |  | 2 |
| 5 | 摩挲纸边 | 1842 | normal | 93.3 | 0 |  | 2 |
| 6 | 摩挲纸边 | 1622 | normal | 92.7 | 0 |  | 4 |
| 7 | 摩挲纸边 | 2001 | normal | 92.4 | 0 |  | 3 |
| 8 | 摩挲袖口褶皱 | 1763 | normal | 36.7 | 0 |  | 1 |
| 9 | 摩挲纸边 | 1877 | normal | 93.4 | 0 |  | 4 |
| 10 | 摩挲纸边 | 2503 | long | 92.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈志远的」×9
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「李浩站在」×3
  - [observe] 章内自我复读 1 句（如「你知道这意味着什么吗？…」）
- 第 3 章：
  - 单条套路句式超限：「他知道这」×4
  - attr_adv_pct 25.0 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「陈志远的」×7
  - [observe] attr_adv_pct 37.5 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「他知道这」×3
  - [observe] 标题重复：「摩挲纸边」已存在
- 第 6 章：
  - 命中套话收尾句
  - 单条套路句式超限：「陈志远的」×7、「他知道这」×3
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 标题重复：「摩挲纸边」已存在
- 第 7 章：
  - 单条套路句式超限：「陈志远的」×5、「他知道这」×3
  - attr_adv_pct 15.4 高于目标 12.0
  - [observe] 标题重复：「摩挲纸边」已存在
- 第 8 章：
  - [observe] attr_adv_pct 45.5 > 25.0（结构塌缩）
- 第 9 章：
  - 单条套路句式超限：「陈志远的」×5
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「摩挲纸边」已存在
- 第 10 章：
  - 单条套路句式超限：「他知道这」×5、「陈志远的」×4
  - attr_adv_pct 13.0 高于目标 12.0
  - [observe] 标题重复：「摩挲纸边」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18674
chapter_chars_mean: 1867
chapter_chars_median: 1846
chapter_chars_cv: 0.14
paragraphs_mean: 46.2
dialogue_chars_pct: 45.2
dialogue_para_pct: 81.6
interiority_para_pct: 6.4
narration_para_pct: 12.0
turn_under20_pct: 76.1
turn_over200_pct: 0.0
attr_say_pct: 32.0
attr_adv_pct: 19.0
scenes_per_chapter: 1.9
dialogue_run_mean: 6.1
turn_len_median: 12
```
