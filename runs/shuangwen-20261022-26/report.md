# 旧账本 生成报告

slug：`shuangwen-20261022-26`
档位：爽文　闸门模式：observe
章数：10　总字数：18782
LLM 调用：97 次，累计 373.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扳手拨动螺丝 | 1384 | normal | 97.8 | 0 |  | 1 |
| 2 | 账本翻页的瞬间 | 1920 | normal | 94.6 | 0 |  | 1 |
| 3 | 账本翻页的瞬间 | 2074 | normal | 92.2 | 0 |  | 3 |
| 4 | 签字的手伸出来 | 1668 | normal | 90.8 | 0 |  | 2 |
| 5 | 签字的手伸出来 | 2054 | normal | 93.0 | 0 |  | 2 |
| 6 | 账本翻页的瞬间 | 2015 | normal | 93.0 | 0 |  | 4 |
| 7 | 账本翻页的瞬间 | 2137 | normal | 92.8 | 0 |  | 2 |
| 8 | 钢笔递出的时刻 | 1962 | normal | 93.9 | 0 |  | 1 |
| 9 | 账本翻页的瞬间 | 1608 | normal | 37.2 | 0 |  | 3 |
| 10 | 账本翻页的瞬间 | 1950 | long | 36.7 | 0 |  | 6 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 3.8 低于目标 5.0
- 第 2 章：
  - attr_adv_pct 23.5 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「陈志远的」×9
  - attr_adv_pct 25.0 高于目标 12.0
  - [observe] 标题重复：「账本翻页的瞬间」已存在
- 第 4 章：
  - 单条套路句式超限：「林小满的」×3
  - attr_adv_pct 18.2 高于目标 12.0
- 第 5 章：
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题重复：「签字的手伸出来」已存在
- 第 6 章：
  - 单条套路句式超限：「陈志远的」×7
  - narration_para_pct 4.7 低于目标 5.0
  - attr_adv_pct 18.2 高于目标 12.0
  - [observe] 标题重复：「账本翻页的瞬间」已存在
- 第 7 章：
  - 单条套路句式超限：「陈志远的」×6、「办公室」×3
  - [observe] 标题重复：「账本翻页的瞬间」已存在
- 第 8 章：
  - attr_adv_pct 14.3 高于目标 12.0
- 第 9 章：
  - 命中套话收尾句
  - [observe] attr_adv_pct 125.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「账本翻页的瞬间」已存在
- 第 10 章：
  - 单条套路句式超限：「陈志远的」×4
  - narration_para_pct 0.0 低于目标 5.0
  - attr_adv_pct 18.2 高于目标 12.0
  - dialogue_run_mean 17 高于目标 14.0
  - [observe] 章内自我复读 3 句（如「陈志远说着，拿出了一份结账单，上面写着“年底前完…」）
  - [observe] 标题重复：「账本翻页的瞬间」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17789
chapter_chars_mean: 1779
chapter_chars_median: 1848
chapter_chars_cv: 0.13
paragraphs_mean: 41.7
dialogue_chars_pct: 50.2
dialogue_para_pct: 84.6
interiority_para_pct: 5.7
narration_para_pct: 9.6
turn_under20_pct: 74.8
turn_over200_pct: 0.0
attr_say_pct: 35.6
attr_adv_pct: 25.6
scenes_per_chapter: 2.3
dialogue_run_mean: 7.9
turn_len_median: 14
```
