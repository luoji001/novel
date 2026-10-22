# 旧发票 生成报告

slug：`shuangwen-20261022-08`
档位：爽文　闸门模式：observe
章数：10　总字数：18490
LLM 调用：97 次，累计 351.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧发票对决 | 1566 | normal | 100.0 | 0 |  | 0 |
| 2 | 墨迹晕开 | 1962 | normal | 93.8 | 0 |  | 1 |
| 3 | 账本摊开 | 2063 | normal | 94.6 | 0 |  | 2 |
| 4 | 发票摊开 | 1902 | normal | 92.4 | 0 |  | 1 |
| 5 | 签字摊开 | 1686 | normal | 93.1 | 0 |  | 0 |
| 6 | 摊开账本 | 1991 | normal | 93.4 | 0 |  | 2 |
| 7 | 发票摊开 | 1992 | normal | 91.3 | 0 |  | 1 |
| 8 | 发票摊开 | 1438 | normal | 37.4 | 0 |  | 2 |
| 9 | 摊开账本 | 1612 | normal | 94.3 | 0 |  | 2 |
| 10 | 发票摊开 | 2268 | long | 92.0 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - attr_adv_pct 12.5 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 20.0 高于目标 12.0
- 第 4 章：
  - attr_adv_pct 18.8 高于目标 12.0
- 第 6 章：
  - narration_para_pct 4.5 低于目标 5.0
  - attr_adv_pct 16.0 高于目标 12.0
- 第 7 章：
  - [observe] 标题重复：「发票摊开」已存在
- 第 8 章：
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
  - [observe] 标题重复：「发票摊开」已存在
- 第 9 章：
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 标题重复：「摊开账本」已存在
- 第 10 章：
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「发票摊开」已存在

## 整书结构指标

```
chapters: 10
total_chars: 17643
chapter_chars_mean: 1764
chapter_chars_median: 1849
chapter_chars_cv: 0.14
paragraphs_mean: 35.8
dialogue_chars_pct: 47.3
dialogue_para_pct: 82.6
interiority_para_pct: 6.0
narration_para_pct: 11.4
turn_under20_pct: 66.9
turn_over200_pct: 0.0
attr_say_pct: 34.3
attr_adv_pct: 12.8
scenes_per_chapter: 1.8
dialogue_run_mean: 7.1
turn_len_median: 15
```
