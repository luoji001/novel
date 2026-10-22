# 磅单 生成报告

slug：`shuangwen-20261022-27`
档位：爽文　闸门模式：observe
章数：10　总字数：20171
LLM 调用：97 次，累计 375.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 装货 | 1982 | normal | 39.9 | 0 |  | 1 |
| 2 | 一份磅单 | 2178 | normal | 92.7 | 0 |  | 2 |
| 3 | 一份旧卷宗 | 1957 | normal | 89.2 | 0 |  | 1 |
| 4 | 撕下滞纳金表 | 2101 | normal | 93.3 | 0 |  | 3 |
| 5 | 核对磅单数据 | 1953 | normal | 90.9 | 0 |  | 2 |
| 6 | 核对磅单数据 | 1945 | normal | 36.2 | 0 |  | 4 |
| 7 | 核对磅单数据 | 1582 | normal | 93.2 | 0 |  | 3 |
| 8 | 核对磅单数据 | 2045 | normal | 90.1 | 0 |  | 3 |
| 9 | 一枚戒指 | 2096 | normal | 92.2 | 0 |  | 4 |
| 10 | 核对磅单数据 | 2322 | long | 91.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] attr_adv_pct 60.0 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「李建国的」×4
  - attr_adv_pct 16.7 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「李建国的」×6
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
  - attr_adv_pct 13.0 高于目标 12.0
- 第 5 章：
  - narration_para_pct 2.3 低于目标 5.0
  - dialogue_run_mean 20.5 高于目标 14.0
- 第 6 章：
  - 单条套路句式超限：「李建国的」×3
  - narration_para_pct 4.9 低于目标 5.0
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「核对磅单数据」已存在
- 第 7 章：
  - 单条套路句式超限：「李建国的」×3
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「核对磅单数据」已存在
- 第 8 章：
  - 单条套路句式超限：「李建国的」×4、「他知道这」×4
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题重复：「核对磅单数据」已存在
- 第 9 章：
  - 单条套路句式超限：「李建国的」×4
  - narration_para_pct 2.1 低于目标 5.0
  - attr_adv_pct 13.6 高于目标 12.0
  - dialogue_run_mean 15.3 高于目标 14.0
- 第 10 章：
  - 单条套路句式超限：「李建国的」×3
  - [observe] 标题重复：「核对磅单数据」已存在

## 整书结构指标

```
chapters: 10
total_chars: 19106
chapter_chars_mean: 1911
chapter_chars_median: 1910
chapter_chars_cv: 0.1
paragraphs_mean: 46.2
dialogue_chars_pct: 50.1
dialogue_para_pct: 86.4
interiority_para_pct: 4.7
narration_para_pct: 8.9
turn_under20_pct: 72.5
turn_over200_pct: 0.0
attr_say_pct: 34.5
attr_adv_pct: 17.7
scenes_per_chapter: 2.3
dialogue_run_mean: 9.6
turn_len_median: 14
```
